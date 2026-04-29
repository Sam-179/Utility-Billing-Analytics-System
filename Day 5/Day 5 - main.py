import csv
import utility
billing = __import__("Day 2 - billing")

def run():
    path = "python/customers.csv"
    
    if not utility.check_file(path):
        return

    count = 0
    total_money = 0

    with open(path, "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            name = row["name"]
            units = float(row["units"])
            bill = billing.calculate_bills(units)
            
            count += 1
            total_money += bill
            
            print(f"{name}: {bill}")

    print("Total Customers:", count)
    print("Total Revenue:", total_money)
    if count > 0:
        print("Average Bill:", total_money / count)

if __name__ == "__main__":
    run()