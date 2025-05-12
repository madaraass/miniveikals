
from flask import Flask, render_template, request, redirect, url_for
import sqlite3
import os

app = Flask(__name__)

DATABASE = 'database/cars.sqlite'

def get_db_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    if not os.path.exists(DATABASE):
        os.makedirs('database', exist_ok=True)
        conn = get_db_connection()
        with open('schema.sql', 'r', encoding='utf-8') as f:
            conn.executescript(f.read())
        conn.commit()
        conn.close()
        print("✅ Datubāze izveidota no schema.sql")
    else:
        print("ℹ️ Datubāze jau eksistē.")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/cars')
def cars():
    conn = get_db_connection()
    cars = conn.execute('SELECT * FROM Cars').fetchall()
    conn.close()
    return render_template('cars.html', cars=cars)

@app.route('/add', methods=('GET', 'POST'))
def add_car():
    if request.method == 'POST':
        name = request.form['name']
        brand = request.form['brand']
        year = request.form['year']
        image_url = request.form['image_url']
        conn = get_db_connection()
        conn.execute('INSERT INTO Cars (name, brand, year, image_url) VALUES (?, ?, ?, ?)', 
                     (name, brand, year, image_url))
        conn.commit()
        conn.close()
        return redirect(url_for('cars'))
    return render_template('add_car.html')

@app.route('/edit/<int:id>', methods=('GET', 'POST'))
def edit_car(id):
    conn = get_db_connection()
    car = conn.execute('SELECT * FROM Cars WHERE id = ?', (id,)).fetchone()
    if request.method == 'POST':
        name = request.form['name']
        brand = request.form['brand']
        year = request.form['year']
        image_url = request.form['image_url']
        conn.execute('UPDATE Cars SET name = ?, brand = ?, year = ?, image_url = ? WHERE id = ?',
                     (name, brand, year, image_url, id))
        conn.commit()
        conn.close()
        return redirect(url_for('cars'))
    conn.close()
    return render_template('edit_car.html', car=car)

@app.route('/delete/<int:id>', methods=['POST'])
def delete_car(id):
    conn = get_db_connection()
    conn.execute('DELETE FROM Cars WHERE id = ?', (id,))
    conn.commit()
    conn.close()
    return redirect(url_for('cars'))

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
