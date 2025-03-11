from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Author data
authors = [
    {"name": "J.K. Rowling", "bio": "British author, best known for the Harry Potter series."},
    {"name": "George R.R. Martin", "bio": "Famous for 'A Song of Ice and Fire', which inspired 'Game of Thrones'."},
    {"name": "Agatha Christie", "bio": "English writer known for her detective novels featuring Poirot and Miss Marple."},
    {"name": "Stephen King", "bio": "American author of horror, supernatural fiction, and suspense novels."},
    {"name": "Jane Austen", "bio": "Known for 'Pride and Prejudice' and 'Sense and Sensibility'."},
    {"name": "Mark Twain", "bio": "Famous for 'Huckleberry Finn' and 'Tom Sawyer'."},
    {"name": "Leo Tolstoy", "bio": "Russian author known for 'War and Peace' and 'Anna Karenina'."},
    {"name": "Charles Dickens", "bio": "Writer of 'Oliver Twist' and 'A Tale of Two Cities'."},
    {"name": "Ernest Hemingway", "bio": "Known for 'The Old Man and the Sea' and 'A Farewell to Arms'."},
    {"name": "Gabriel García Márquez", "bio": "Colombian novelist famous for 'One Hundred Years of Solitude'."}
]

# Route to get all authors
@app.route('/authors', methods=['GET'])
def get_authors():
    return jsonify({"authors": authors})

# Route to get an author by name
@app.route('/authors/<name>', methods=['GET'])
def get_author(name):
    author = next((a for a in authors if a["name"].lower() == name.lower()), None)
    if author:
        return jsonify(author)
    return jsonify({"error": "Author not found"}), 404

# Route to add a new author
@app.route('/authors', methods=['POST'])
def add_author():
    new_author = request.json
    if "name" in new_author and "bio" in new_author:
        authors.append(new_author)
        return jsonify({"message": "Author added successfully"}), 201
    return jsonify({"error": "Invalid data"}), 400

if __name__ == '__main__':
    app.run(debug=True)
