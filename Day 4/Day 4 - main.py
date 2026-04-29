import csv
import utility
billing = __import__("Day 2 - billing")

def run():
    path = "python/customers.csv"
    
    if not utility.check_file(path):
        print("File not found!")
        return
    
    with open(path, "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            try:
                name = row["name"]
                units = float(row["units"])
                
                bill = billing.calculate_bill(units)
                
                print(f"{name} → ₹{bill}")
            except Exception as e:
                print(f"Error in data for {row.get('name', 'Unknown')}")

if __name__ == "__main__":
    run()