import csv
import os

billing = __import__("Day 2 - billing")

def run():
    path = 'python/customers.csv'
    
    if not os.path.exists(path):
        print("File not found!")
        return

    with open(path, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            try:
                name = row['name']
                units = float(row['units'])
                total = billing.calculate_bill(units)
                print(f"Customer: {name} | Bill: ₹{total}")
            except:
                print(f"Skipping {name} - Invalid units data!")

if __name__ == "__main__":
    run()