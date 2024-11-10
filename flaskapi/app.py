from flask import Flask,request,jsonify
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/kimomay"
mongo = PyMongo(app)

@app.route('/',methods=["GET"])
def sayHi():
    return jsonify({"message":"Default Route"})

@app.route('/books',methods=["GET"])
def get_books():
    books = mongo.db.books
    result = []
    for book in books.find():
        result.append({
            "_id": str(book["_id"]),
            "author": book["author"],
            "imageLink":book["imageLink"],
            "language": book["language"],
            "link":book["link"],
            "pages":book["pages"],
            "title":book["title"],
            "year":book["year"]
        })
    return jsonify({"data":result})

@app.route('/book/<name>',methods=['GET'])
def book_authors(name):
    books = mongo.db.books
    result = []
    for book in books.find({"author":name}):
        result.append({
            "_id": str(book["_id"]),
            "author": book["author"],
            "imageLink":book["imageLink"],
            "language": book["language"],
            "link":book["link"],
            "pages":book["pages"],
            "title":book["title"],
            "year":book["year"]
        })
    return jsonify({"data":result})

@app.route('/bookq',methods=['GET'])
def book_authors_query():
    name = request.args.get('name')
    books = mongo.db.books
    if name:
        query = {"author":name}
    else:
        query = {}
    result = []
    
    for book in  books.find(query):
        result.append({
            "_id": str(book["_id"]),
            "author": book["author"],
            "imageLink":book["imageLink"],
            "language": book["language"],
            "link":book["link"],
            "pages":book["pages"],
            "title":book["title"],
            "year":book["year"]
        })
    return jsonify({"data":result})


@app.route('/addBook',methods=["POST"])
def add_books():
    data = request.get_json()
    books = mongo.db.books
    books.insert_one(data)
    return jsonify({"data":"Book Inserted"})

@app.route('/addBook',methods=["PUT"])
def add_books():
    data = request.get_json()
    books = mongo.db.books
    books.update_one({"_id":ObjectId(id)},{"$set":data})
    return jsonify({"data":"Book updated"})




if __name__ == "__main__":
    app.run(port=8000)