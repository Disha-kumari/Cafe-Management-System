from flask import Flask, render_template, request, redirect, session, jsonify
import pyodbc

app = Flask(__name__)
app.secret_key = "cafe_secret_key"


def get_connection():
    conn = pyodbc.connect(
        "Driver={SQL Server};"
        "Server=DESKTOP-5OUD1G3;"
        "Database=cafe_database;"
        "Trusted_Connection=yes;"
    )
    return conn


# LOGIN PAGE
@app.route("/")
def login():
    return render_template("login.html")


# LOGIN USER
@app.route("/login_user", methods=["POST"])
def login_user():

    username = request.form["username"]
    password = request.form["password"]

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM Customer WHERE username=? AND password=?",
        username, password
    )

    user = cursor.fetchone()

    if user:
        session["user"] = username
        return redirect("/menu_page")

    return "Invalid Login"


# REGISTER PAGE
@app.route("/register")
def register():
    return render_template("register.html")


# REGISTER USER
@app.route("/register_user", methods=["POST"])
def register_user():

    username = request.form["username"]
    password = request.form["password"]

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO Customer(username,password) VALUES (?,?)",
        username, password
    )

    conn.commit()

    return redirect("/")


# MENU PAGE
@app.route("/menu_page")
def menu_page():

    if "user" not in session:
        return redirect("/")

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT item_id,item_name,price,image_url FROM Menu")

    rows = cursor.fetchall()

    items = []

    for r in rows:
        items.append({
            "id": r[0],
            "name": r[1],
            "price": r[2],
            "image": r[3]
        })

    return render_template("menu.html", items=items)


# PLACE ORDER
@app.route("/place_order", methods=["POST"])
def place_order():

    data = request.json

    items = data["items"]
    payment = data["payment"]
    total = data["total"]

    conn = get_connection()
    cursor = conn.cursor()

    customer_id = 1

    cursor.execute(
        "INSERT INTO Orders(customer_id,order_date,total_amount) VALUES (?,GETDATE(),?)",
        customer_id, total
    )

    conn.commit()

    cursor.execute("SELECT MAX(order_id) FROM Orders")
    order_id = cursor.fetchone()[0]

    for item in items:

        cursor.execute(
            "INSERT INTO Order_Details(order_id,item_id,quantity) VALUES (?,?,?)",
            order_id, item["id"], item["qty"]
        )

    cursor.execute(
        "INSERT INTO Payment(order_id,payment_mode,payment_status) VALUES (?,?,?)",
        order_id, payment, "Paid"
    )

    conn.commit()

    return jsonify({"status": "success"})


# LOGOUT
@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)