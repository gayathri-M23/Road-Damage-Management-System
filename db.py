import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="**************",
    database="road_damage_db"
)

cursor = db.cursor(buffered=True)

print("Database Connected Successfully!")
