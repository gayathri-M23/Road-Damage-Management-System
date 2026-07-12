import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="gayathri@2008.",
    database="road_damage_db"
)

cursor = db.cursor(buffered=True)

print("Database Connected Successfully!")
