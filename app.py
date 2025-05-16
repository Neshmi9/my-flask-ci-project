from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)


@app.route('/')
def home():
    return 'Hello from Flask CI/CD App!'


@app.route('/add', methods=['POST'])
def add_data():
    name = request.json.get('name')
    conn = sqlite3.connect('data.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO users (name) VALUES (?)', (name,))
    conn.commit()
    conn.close()
    return jsonify({'message': 'User added'}), 201


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
