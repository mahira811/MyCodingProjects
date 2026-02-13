import sqlite3
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/api/words', methods=['GET'])
def get_words():
    conn = sqlite3.connect('dictionary.db')
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM Words')
    rows = cursor.fetchall()
    output = []
    for row in rows:
        word_data = {
         	"Word": str(row[0]), 
                	"Meaning": str(row[1]),
                	"Sentence": str(row[2])
        }
        output.append(word_data)
    conn.close()
    return jsonify(output)
         
if __name__ == '__main__':
    app.run(debug=True, port=5000)




