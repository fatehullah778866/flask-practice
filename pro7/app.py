from flask import Flask, render_template,request,redirect,url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

#database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///books.db'
app.config['SQLALCHEMY_TRACK_MODIFICATION'] = False

db = SQLAlchemy(app)

#model (book table)
class Book(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(100), nullable = False)
    author = db.Column(db.String(50), nullable = False)
    
    def __repr__(self):
        return f"<Book {self.title}>"
    

with app.app_context():
    db.create_all()

#crud routes
@app.route('/')
def index():
    books = Book.query.all()
    return render_template('index.html', books=books)

@app.route('/add', methods = ['GET','POST'])
def add_book():
    if request.method == 'POST':
        title = request.form['title']
        author = request.form['author']
        new_book = Book(title=title, author=author)
        db.session.add(new_book)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('add.html')

@app.route('/update/<int:id>', methods=['GET','POST'])
def update(id):
    book = Book.query.get_or_404(id)
    if request.method == 'POST':
        book.title = request.form['title']
        book.author = request.form['author']
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('update.html', book=book)

@app.route('/delete/<int:id>')
def delete(id):
    book = Book.query.get_or_404(id)
    db.session.delete(book)
    db.session.commit()
    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(debug=True)