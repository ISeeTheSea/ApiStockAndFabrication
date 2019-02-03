import time
import mysql.connector

from flask import Flask
from flask import jsonify


app = Flask(__name__)
def get_hit_count():
    return 10

def check_db():
    connection = mysql.connector.connect(host="240411f0d3e7",
        user="dbwdev",
        passwd="dbwdevpass", 
        database='apisf_stock')
    return connection

@app.route('/')
def hello():
    connection = mysql.connector.connect(host="269376b19436",
        user="dbwdev",
        passwd="dbwdevpass", 
        database='apisf_db')
    cursor = connection.cursor()
    
    query = ("SELECT email from apisf_db.admin")
    
    cursor.execute(query, ())
    
    #count = get_hit_count()
    return jsonify(data=cursor.fetchall())

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
