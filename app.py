from flask import (
    Flask,
    render_template,
    redirect,
    flash,
    url_for,
)

from flask_sqlalchemy import SQLAlchemy
from wtforms import StringField
from flask_wtf import FlaskForm
from flask_migrate import Migrate
from wtforms.validators import InputRequired,Length,Email
from wtforms import validators
from sqlalchemy.exc import (
    IntegrityError,
    DataError,
    DatabaseError,
    InterfaceError,
    InvalidRequestError,
)


app = Flask(__name__)

app.secret_key = 'secret-key'
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///database.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db = SQLAlchemy(app)
migrate = Migrate(app,db)



class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username


class UserForm(FlaskForm):
    username = StringField(validators=[InputRequired(), Length(1, 64)])
    email = StringField(validators=[InputRequired(),Email(), Length(1, 64)])



@app.route("/", methods=("GET", "POST"))
def index():
    form = UserForm()
    if form.validate_on_submit():
        try:
            username = form.username.data
            email = form.email.data
            
            user = User(
                username=username,
                email=email
            )
    
            db.session.add(user)
            db.session.commit()
            flash(f"Record Saved!", "success")

            return redirect(url_for("index"))
        except InvalidRequestError:
            db.session.rollback()
            flash(f"Something went wrong!", "danger")
        except IntegrityError:
            db.session.rollback()
            flash(f"Record already exists!.", "warning")
        except DataError:
            db.session.rollback()
            flash(f"Invalid Entry", "warning")
        except InterfaceError:
            db.session.rollback()
            flash(f"Error connecting to the database", "danger")
        except DatabaseError:
            db.session.rollback()
            flash(f"Error connecting to the database", "danger")
        except BuildError:
            db.session.rollback()
            flash(f"An error occured !", "danger")

    return render_template("index.html",form=form)

if __name__ == "__main__":
    app.run(debug=True)
