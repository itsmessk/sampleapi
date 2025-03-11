import os
from flask import Flask, jsonify

app = Flask(__name__)

# Sample author data
author_data = {
  "authors": [
    {
      "name": "J.K. Rowling",
      "bio": "J.K. Rowling is a British author, best known for writing the Harry Potter series, which has become one of the best-selling book series in history. Her works include novels, screenplays, and various charity publications."
    },
    {
      "name": "George R.R. Martin",
      "bio": "George R.R. Martin is an American novelist and short story writer, famous for his epic fantasy series 'A Song of Ice and Fire', which inspired the television series 'Game of Thrones'."
    },
    {
      "name": "Agatha Christie",
      "bio": "Agatha Christie was an English writer known for her 66 detective novels and 14 short story collections, particularly those revolving around fictional detectives Hercule Poirot and Miss Marple."
    },
    {
      "name": "Stephen King",
      "bio": "Stephen King is an American author of horror, supernatural fiction, suspense, and fantasy novels. His books have sold over 350 million copies, with many adapted into films, television series, and miniseries."
    },
    {
      "name": "Jane Austen",
      "bio": "Jane Austen was an English novelist known for her six major novels, including 'Pride and Prejudice' and 'Sense and Sensibility', which explore themes of love, class, and social status."
    },
    {
      "name": "Mark Twain",
      "bio": "Mark Twain was an American writer, humorist, and lecturer, best known for his novels 'Adventures of Huckleberry Finn' and 'The Adventures of Tom Sawyer'."
    },
    {
      "name": "Leo Tolstoy",
      "bio": "Leo Tolstoy was a Russian author considered one of the greatest novelists of all time, known for his masterpieces 'War and Peace' and 'Anna Karenina'."
    },
    {
      "name": "Charles Dickens",
      "bio": "Charles Dickens was an English writer and social critic, famous for creating some of the world's best-known fictional characters and novels, including 'Oliver Twist', 'A Christmas Carol', and 'Great Expectations'."
    },
    {
      "name": "Harper Lee",
      "bio": "Harper Lee was an American novelist widely known for her novel 'To Kill a Mockingbird', which won the Pulitzer Prize and is considered a classic of modern American literature."
    },
    {
      "name": "F. Scott Fitzgerald",
      "bio": "F. Scott Fitzgerald was an American novelist and short story writer, famous for his novel 'The Great Gatsby', which is widely regarded as a literary classic and a contender for the title 'Great American Novel'."
    }
    ]
  }

@app.route('/author', methods=['GET'])
def get_author():
    return jsonify(author_data)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))  # Railway assigns a dynamic port
    app.run(host="0.0.0.0", port=port)
