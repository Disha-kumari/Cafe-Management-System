# ☕ Cafe Management System

A simple web-based Cafe Management System developed using **Python Flask, HTML, CSS, JavaScript, and Microsoft SQL Server**.

The system allows users to register, log in, view the cafe menu, add food items to a cart, place orders, and select a payment method. Customer and order details are stored in a SQL Server database.

## ✨ Features

- 👤 User Registration and Login
- 🍴 View Cafe Menu
- 🛒 Add Items to Cart
- 💰 Automatic Total Calculation
- 📦 Place Orders
- 💳 Select Payment Method
- 🗄️ SQL Server Database
- 🚪 Logout

## 🛠️ Technologies Used

| Technology | Purpose |
|------------|---------|
| Python | Backend |
| Flask | Web Framework |
| HTML | Page Structure |
| CSS | Styling |
| JavaScript | Cart Functionality |
| SQL Server | Database |
| PyODBC | Database Connection |

## 📂 Project Structure

```text
Cafe-Management-System/
│
├── app.py
├── db_config.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── static/
│   ├── images/
│   ├── script.js
│   └── style.css
│
└── templates/
    ├── admin.html
    ├── forgot.html
    ├── login.html
    ├── menu.html
    └── register.html
🔄 Workflow
Register / Login
       ↓
   View Menu
       ↓
   Add to Cart
       ↓
 Calculate Total
       ↓
Select Payment
       ↓
  Place Order
       ↓
 Store in SQL Server
🗄️ Database

The project uses Microsoft SQL Server.

Main tables:

Customer
Menu
Orders
Order_Details
Payment
⚙️ How to Run
1. Clone the Repository
git clone https://github.com/Disha-kumari/Cafe-Management-System.git
2. Open the Project
cd Cafe-Management-System
3. Install Dependencies
pip install -r requirements.txt
4. Configure Database

Make sure SQL Server is running and update the connection details in db_config.py.

5. Run the Application
python app.py

Open:

http://127.0.0.1:5000
🎯 Project Objective

The main objective of this project is to provide a simple digital system for managing cafe customers, menu items, orders, and payments using a web application and database.

👩‍💻 Technologies

Python | Flask | HTML | CSS | JavaScript | SQL Server


This is much closer to the **simple, not-overdone** style you usually want for your college projects.