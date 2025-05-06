from flask import Flask, render_template, request
import sqlite3
import serial

app = Flask(__name__)
arduino = serial.Serial('COM3', 9600)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/search", methods=["POST"])
def search():
    keyword = request.form["keyword"]
    conn = sqlite3.connect("parts.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Parts WHERE Description LIKE ?", (f"%{keyword}%",))
    results = cursor.fetchall()
    conn.close()
    return render_template("index.html", results=results)

@app.route("/light_up", methods=["POST"])
def light_up():
    bin = request.form["bin"]
    arduino.write(f"{bin}\n".encode())
    return "OK"

if __name__ == "__main__":
    app.run(debug=True)
