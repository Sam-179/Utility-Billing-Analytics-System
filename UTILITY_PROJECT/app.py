import os
import sqlite3
import calendar
from datetime import datetime, timedelta
from flask import Flask, render_template, request, redirect, url_for, session, flash
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.secret_key = 'smartbill_secret_key'

# --- DATABASE INITIALIZATION ---
def init_db():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL,
            role TEXT DEFAULT 'customer'
        )
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS records (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL,
            units REAL NOT NULL,
            base_amount REAL NOT NULL,
            late_fee REAL NOT NULL,
            total REAL NOT NULL,
            due_date TEXT NOT NULL,
            date_calculated TEXT NOT NULL
        )
    ''')
    # Default Master Admin (admin / admin123)
    admin_pass = generate_password_hash('admin123', method='pbkdf2:sha256')
    cursor.execute("INSERT OR IGNORE INTO users (username, password, role) VALUES (?, ?, ?)", 
                   ('admin', admin_pass, 'master'))
    conn.commit()
    conn.close()

init_db()

# --- HELPERS ---
def get_system_dates():
    """Sets due date to the 1st of the NEXT month."""
    now = datetime.now()
    today_str = now.strftime('%Y-%m-%d')
    
    # Logic to find the 1st of the next month
    if now.month == 12:
        next_month = 1
        next_year = now.year + 1
    else:
        next_month = now.month + 1
        next_year = now.year
        
    due_date_str = f"{next_year}-{next_month:02d}-01"
    return today_str, due_date_str

def calculate_slab_bill(units):
    if units <= 100:
        s1 = units * 5
        return s1, [s1, 0, 0]
    elif units <= 200:
        s1 = 100 * 5
        s2 = (units - 100) * 7
        return s1 + s2, [s1, s2, 0]
    else:
        s1 = 100 * 5
        s2 = 100 * 7
        s3 = (units - 200) * 10
        return s1 + s2 + s3, [s1, s2, s3]

# --- ROUTES ---
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE username = ?", (username,))
        user = cursor.fetchone()
        conn.close()
        if user and check_password_hash(user[2], password):
            session['username'] = user[1]
            session['role'] = user[3]
            return redirect(url_for('dashboard'))
        flash('Invalid username or password!')
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = generate_password_hash(request.form['password'], method='pbkdf2:sha256')
        try:
            conn = sqlite3.connect('database.db')
            cursor = conn.cursor()
            cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
            conn.commit()
            conn.close()
            return redirect(url_for('login'))
        except:
            flash('Username already exists!')
    return render_template('register.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    if 'username' not in session:
        return redirect(url_for('login'))
    
    units = float(request.form['units'])
    today_str, auto_due_date = get_system_dates()
    
    # 1. Slab Calculation
    base_total, slabs = calculate_slab_bill(units)
    
    # 2. Apply 10% Discount if units < 100
    discount = 0.0
    if units < 100:
        discount = round(base_total * 0.10, 2)
        base_total -= discount
    
    # 3. Late Fee Check (If today is strictly AFTER the 1st of next month)
    late_fee = 0.0
    due_datetime = datetime.strptime(auto_due_date, '%Y-%m-%d')
    if datetime.now() >= (due_datetime + timedelta(days=1)):
        late_fee = round(base_total * 0.10, 2)
    
    final_total = base_total + late_fee
    
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('''INSERT INTO records 
        (username, units, base_amount, late_fee, total, due_date, date_calculated) 
        VALUES (?, ?, ?, ?, ?, ?, ?)''', 
        (session['username'], units, base_total, late_fee, final_total, auto_due_date, today_str))
    conn.commit()
    conn.close()
    
    return render_template('result.html', units=units, base=base_total, late=late_fee, total=final_total, slabs=slabs, discount=discount)

@app.route('/dashboard')
def dashboard():
    if 'username' not in session:
        return redirect(url_for('login'))
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    if session['role'] == 'master':
        cursor.execute("SELECT * FROM records ORDER BY date_calculated DESC")
    else:
        cursor.execute("SELECT * FROM records WHERE username = ? ORDER BY date_calculated DESC", (session['username'],))
    history = cursor.fetchall()
    conn.close()
    return render_template('dashboard.html', history=history)

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)