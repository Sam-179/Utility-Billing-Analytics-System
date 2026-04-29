import importlib
import utility

billing_mod = importlib.import_module("Day 2 - billing")

def run_day_7_report():
    print("--- Day 7: Enhanced Billing Report ---")
    
    units = 200
    status = "Late"
    
    bill_amount = billing_mod.calculate_bills(units)
    
    if units < 100:
        bill_amount *= 0.90
        print(f"Applied 10% Discount.")

    if status == "Late":
        bill_amount *= 1.10
        print(f"Applied 10% Late Payment Penalty.")
    
    print(f"Final Amount to Pay: ₹{bill_amount:.2f}")

if __name__ == "__main__":
    run_day_7_report()