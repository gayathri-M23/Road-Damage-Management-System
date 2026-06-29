from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = "rdms_secret_key"
from db import db, cursor

@app.route("/", methods=["GET", "POST"])
def home():

    if request.method == "POST":

        email = request.form["email"]
        password = request.form["password"]

        sql = "SELECT * FROM users WHERE email=%s AND password=%s"
        values = (email, password)

        cursor.execute(sql, values)

        user = cursor.fetchone()

        if user:
            session["user_id"] = user[0]
            return redirect(url_for("dashboard"))
        else:
            return "Invalid Email or Password!"

    return render_template("01_login_board.html")
    
@app.route("/register", methods=["GET", "POST"])
def register():

    if request.method == "POST":

        fullname = request.form["fullname"]
        email = request.form["email"]
        phone = request.form["phone"]
        location = request.form["location"]
        password = request.form["password"]

        sql = """
        INSERT INTO users(fullname, email, phone, location, password)
        VALUES(%s, %s, %s, %s, %s)
        """

        values = (fullname, email, phone, location, password)

        cursor.execute(sql, values)
        db.commit()

        return "Registration Successful!"

    return render_template("02_register_page.html")

@app.route("/dashboard")
def dashboard():
    return render_template("03_dashboard.html")

@app.route("/report", methods=["GET", "POST"])
def report():

    if request.method == "POST":

        location = request.form["location"]
        damage_type = request.form["damage_type"]
        description = request.form["description"]

        sql = """
        INSERT INTO complaints(user_id, location, damage_type, description, status)
        VALUES(%s, %s, %s, %s, %s)
        """

        values = (session["user_id"], location, damage_type, description, "Pending")

        cursor.execute(sql, values)
        db.commit()

        return "Report Submitted Successfully!"

    return render_template("04_report_damage.html")

@app.route("/myreports")
def myreports():

    sql = "SELECT * FROM complaints"

    cursor.execute(sql)

    reports = cursor.fetchall()

    return render_template("05_my_reports.html", reports=reports)

@app.route("/profile")
def profile():

    user_id = session.get("user_id")

    sql = "SELECT * FROM users WHERE id=%s"
    cursor.execute(sql, (user_id,))

    user = cursor.fetchone()

    return render_template("06_profile.html", user=user)

@app.route("/admin", methods=["GET", "POST"])
def admin():

    if request.method == "POST":

        username = request.form["username"]
        password = request.form["password"]

        if username == "admin" and password == "admin123":
            return redirect(url_for("admin_dashboard"))

        return "Invalid Admin Login!"

    return render_template("07_admin_login.html")

@app.route("/admin_dashboard")
def admin_dashboard():
    return render_template("08_admin_dashboard.html")

@app.route("/all_complaints")
def all_complaints():

    sql = "SELECT * FROM complaints"

    cursor.execute(sql)

    complaints = cursor.fetchall()

    return render_template("09_all_complaints.html", complaints=complaints)

@app.route("/update_status/<int:id>", methods=["GET", "POST"])
def update_status(id):

    if request.method == "POST":
        status = request.form["status"]

        sql = "UPDATE complaints SET status=%s WHERE complaint_id=%s"

        cursor.execute(sql, (status, id))
        db.commit()

    return redirect(url_for("all_complaints"))

@app.route("/logout")
def logout():

    session.clear()

    return redirect(url_for("home"))

if __name__ == "__main__":
    app.run(debug=True)
