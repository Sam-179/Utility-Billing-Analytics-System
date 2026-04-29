# Utility Billing System 

A professional-grade Python application designed to automate the calculation, management, and visualization of electricity billing data. This system transforms raw consumer usage statistics into structured financial reports and actionable data insights.

##  System Capabilities
*   **Tiered Pricing Engine:** Implements a slab-based calculation model with rates set at ₹5, ₹7, and ₹10 per unit based on consumption thresholds.
*   **Automated Batch Processing:** Facilitates multi-customer support by reading customer profiles and usage data directly from CSV files.
*   **Dynamic Business Logic:** Automatically applies conditional financial rules, including a 10% discount for energy conservation and a 10% penalty for late payments.
*   **Data Persistence:** Ensures all billing records are exported to structured output files, allowing for historical tracking and future auditing.
*   **Analytical Visualization:** Utilizes **Pandas** and **Seaborn** to generate graphical reports, such as "Units vs. Bill Amount" charts, to identify consumption trends.

##  Technical Architecture
*   **Modular Design:** The codebase is organized into specialized modules (e.g., `billing.py`, `main.py`) to ensure high readability and ease of maintenance.
*   **Input Validation:** Features robust error handling to prevent incorrect data entry and ensure mathematical accuracy.
*   **Version Control:** Developed using a structured Git workflow, with daily milestones tracked via GitHub to maintain project integrity.

##  Tech Stack
*   **Primary Language:** Python
*   **Data Libraries:** Pandas, Matplotlib, Seaborn
*   **Environment:** VS Code, Git, GitHub

##  Project Summary
The Utility Billing System serves as an efficient bridge between mathematical logic and real-world data management. By integrating file I/O operations with advanced Python libraries, the project demonstrates a scalable approach to utility administration and automated financial reporting.
