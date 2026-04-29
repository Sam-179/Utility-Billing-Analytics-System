from flask import Flask, render_template, request

app = Flask(__name__)

def calc_electricity(units):
    if units <= 100: amount = units * 5
    elif units <= 300: amount = (100 * 5) + ((units - 100) * 7)
    else: amount = (100 * 5) + (200 * 7) + ((units - 300) * 10)
    return amount

def calc_water(units):
    if units <= 50: return units * 2
    return (50 * 2) + ((units - 50) * 5)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    service = request.form.get('service')
    units = int(request.form.get('units'))
    status = request.form.get('status')
    currency = request.form.get('currency')
    
    # 1. Calculation Logic
    if service == 'Electricity':
        base_inr = calc_electricity(units)
    else:
        base_inr = calc_water(units)

    # 2. Adjustments
    discount = (base_inr * 0.10) if units < 100 else 0
    penalty = (base_inr * 0.10) if status == "Late" else 0
    final_inr = base_inr - discount + penalty

    # 3. Usage Warning Logic
    if units > 500:
        warning, color = "⚠️ High Usage! Consider saving energy.", "#dc3545"
    elif units < 100:
        warning, color = "🌱 Eco-Warrior! Great job saving power.", "#28a745"
    else:
        warning, color = "👍 Standard Usage. Well managed!", "#764ba2"

    # 4. Currency Conversion
    symbol = "₹"
    final_total = final_inr
    if currency == "USD":
        final_total, symbol = final_inr / 83, "$"
    elif currency == "EUR":
        final_total, symbol = final_inr / 90, "€"

    return render_template('result.html', units=units, status=status, service=service,
                           total=round(final_total, 2), symbol=symbol, 
                           warning=warning, warning_color=color)

if __name__ == "__main__":
    app.run(debug=True)