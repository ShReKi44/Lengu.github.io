from flask import Flask , render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__, template_folder='templates', static_folder='static')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///lgu.db'
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
db = SQLAlchemy(app)


class User(db.Model):
    username = db.Column(db.String(20), primary_key=True, nullable=False)
    password = db.Column(db.String, nullable=False)
    email = db.Column(db.String, primary_key=True, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.id



@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html")


@app.route('/login')
def login_page():
    return render_template("login_page.html")


@app.route('/register', methods=['POST','GET'])
def register_page():
    if request.method == "POST":
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']

        user = User(username=username,password=password,email=email)

        try:
            db.session.add(user)
            db.session.commit()
            return redirect('/index')
        except:
            return "Error"
    else:
        return render_template("register_page.html")


if __name__ == "__main__":
    app.run(debug=True) 
