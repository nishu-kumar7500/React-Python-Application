from flask import Flask, jsonify
from flask_cors import CORS
import random

app = Flask(__name__)
CORS(app)

facts = [
    "India is the world's largest democracy.",
    "The game of chess originated in India.",
    "India has the world's largest postal network.",
    "Yoga originated in India over 5,000 years ago."
]

@app.route('/fact')
def fact():
    return jsonify({"fact": random.choice(facts)})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
