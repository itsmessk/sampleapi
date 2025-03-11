import os
from flask import Flask, jsonify

app = Flask(__name__)

# Sample author data
author_data = {
    "author": {
        "name": "John Doe",
        "bio": "Your detailed biography here..."
    }
}

@app.route('/author', methods=['GET'])
def get_author():
    return jsonify(author_data)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))  # Railway assigns a dynamic port
    app.run(host="0.0.0.0", port=port)
