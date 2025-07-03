import os
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Read PostgreSQL details from environment variables
DB_USER = os.getenv("POSTGRES_USER", "postgres")
DB_PASSWORD = os.getenv("POSTGRES_PASSWORD", "password")
DB_NAME = os.getenv("POSTGRES_DB", "mydatabase")
DB_HOST = os.getenv("POSTGRES_HOST", "backend-service")
DB_PORT = os.getenv("POSTGRES_PORT", "5432")

app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# User Model
class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False, unique=True)
    email = db.Column(db.String(100), nullable=False, unique=True)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']

        # Prevent duplicates
        existing_user = User.query.filter((User.name == name) | (User.email == email)).first()
        if existing_user:
            return "User with this name or email already exists!"

        new_user = User(name=name, email=email)
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('index'))

    users = User.query.all()
    return render_template('index.html', users=users)

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(host='0.0.0.0', port=5000)

