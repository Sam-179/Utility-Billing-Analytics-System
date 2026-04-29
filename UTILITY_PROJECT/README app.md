# ⚡ Smart Utility Billing System

A modern, **full-stack web application** built with **Python (Flask)** that calculates electricity and water bills with dynamic currency conversion and usage insights.

---

##  Key Features

*   **Dual Service Support:** Toggle between **Electricity ⚡** and **Water 💧** billing modes.
*   **Intelligent Warnings:** A dynamic feedback system that alerts users of **"High Usage"** or rewards **"Eco-Warriors"** based on consumption levels.
*   **Multi-Currency Toggle:** Real-time conversion between **INR (₹)**, **USD ($)**, and **EUR (€)**.
*   **Responsive UI:** A sleek, mobile-friendly design featuring **CSS3 gradients** and **glassmorphism-inspired** cards.
*   **Automatic Adjustments:** 
    *   **10% Discount** for low energy usage (< 100 units).
    *   **10% Late Fee** penalty for overdue payments.

---

##  Smart Math Logic

The system uses specific algorithms to ensure fair and tiered pricing:

### **Electricity Calculation ⚡**
The bill is calculated using a **Slab System**:
1.  **First 100 units:** ₹5 per unit
2.  **101 to 300 units:** ₹7 per unit
3.  **Above 300 units:** ₹10 per unit

> **Formula Example:** If you use **350 units**, the math is:  
> `(100 × 5) + (200 × 7) + (50 × 10) = ₹2,400`

### **Water Calculation 💧**
*   **Flat Tier 1 (Up to 50 units):** ₹2 per unit
*   **Flat Tier 2 (Above 50 units):** ₹5 per unit for the remaining units.

---

## 🤖 Built with AI Collaboration
This project was developed using a **"Pair Programming"** approach with **Gemini (AI)** to bridge the gap between logic and design.

*   **Logic Optimization:** Worked with AI to refine the tiered pricing algorithms and handle edge-case mathematical accuracy.
*   **UI/UX Design:** Assisted in generating the modern CSS layout, gradient backgrounds, and handling the dynamic color-switching for usage warnings.
*   **Debugging:** Used AI as a real-time debugging partner to resolve VS Code CSS validation errors and directory pathing issues.

---

## 🛠️ Tech Stack

*   **Backend:** Python 3, Flask
*   **Frontend:** HTML5, CSS3 (Flexbox & Dynamic Jinja2 Templates)
*   **Tools:** VS Code, Git/GitHub, Gemini AI
