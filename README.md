# ⚡ Utility Billing & Analytics System

A professional-grade Python ecosystem designed to automate the calculation, management, and visualization of utility data. This project features both a **high-performance data processing engine** for batch analysis and an **interactive Flask web application** for real-time consumer billing.

---

## 🌐 Web Application Features
The web-based interface allows for manual entry and immediate bill generation with a modern user experience:
*   **Dual Service Support:** Toggle between **Electricity ⚡** and **Water 💧** billing modes.
*   **Intelligent Warnings:** Dynamic feedback alerts users of **"High Usage"** or rewards **"Eco-Warriors"** based on consumption levels.
*   **Multi-Currency Toggle:** Real-time conversion between **INR (₹)**, **USD ($)**, and **EUR (€)**.
*   **Responsive UI:** A sleek design featuring **CSS3 gradients** and **glassmorphism-inspired** cards.

## ⚙️ Core System Capabilities
*   **Tiered Pricing Engine:** Implements a slab-based calculation model (₹5, ₹7, and ₹10/unit) based on consumption thresholds.
*   **Automated Batch Processing:** Facilitates multi-customer support by reading customer profiles directly from **CSV files**.
*   **Dynamic Business Logic:** Applies conditional rules, including a **10% discount** for conservation and a **10% penalty** for late payments.
*   **Analytical Visualization:** Utilizes **Pandas** and **Seaborn** to generate graphical reports, identifying consumption trends through data.

---

## 🧮 Calculation Logic
The system ensures fair pricing through tiered algorithms:

### **Electricity (Slab System)**
1.  **First 100 units:** ₹5 / unit
2.  **101 to 300 units:** ₹7 / unit
3.  **Above 300 units:** ₹10 / unit

> **Formula Example:** `(100 × 5) + (200 × 7) + (Remaining × 10)`

### **Water (Tiered System)**
*   **Tier 1 (Up to 50 units):** ₹2 / unit
*   **Tier 2 (Above 50 units):** ₹5 / unit

---

## 🤖 Built with AI Collaboration
This project was developed using a **"Pair Programming"** approach with **Gemini (AI)** to bridge the gap between backend logic and frontend design.
*   **Logic Optimization:** Refined the tiered pricing algorithms for mathematical edge-cases.
*   **UI/UX Design:** Assisted in generating the modern CSS layout and dynamic color-switching warnings.
*   **Debugging:** Used AI as a real-time partner to resolve VS Code validation and Flask routing issues.

## 🛠️ Tech Stack
*   **Backend:** Python (Flask), Pandas
*   **Frontend:** HTML5, CSS3 (Jinja2 Templates)
*   **Visualization:** Matplotlib, Seaborn
*   **Environment:** VS Code, Git, GitHub

---
