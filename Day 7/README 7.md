Overview
This day focused on adding real-world financial logic to the billing system. I implemented conditional rewards for efficiency and penalties for late payments.

New Features
Low-Usage Discount: 10% reduction for consumption < 100 units.

Late Penalty: 10% increase for "Late" payment status.

Fixed Charge: ₹100 added to every base bill.

Test Case: 200 Units (Late)
Base Slabs:

100 units @ ₹5 = ₹500

100 units @ ₹7 = ₹700

Fixed Charge: ₹1200 + ₹100 = ₹1300

Adjustments:

Discount: None (Usage > 100).

Penalty: ₹1300 + 10% = ₹1430

Final Total: ₹1430.00