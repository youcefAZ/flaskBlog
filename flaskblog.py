from flask import Flask, render_template, url_for, flash
from werkzeug.utils import redirect
from forms import RegistrationForm, LoginForm

app = Flask(__name__)
app.config['SECRET_KEY']='414033ecf232af8b271e0d72677196cb'

games=[
    {
        'name': 'Half-life',
        'devloper': 'Valve',
        'year': '1998'
    },
    {
        'name': 'The witcher 3',
        'devloper': 'CD projekt RED',
        'year': '2015'
    }
]

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html',games=games)

@app.route("/about")
def about():
    return render_template('about.html',title='about')

@app.route("/register", methods=['GET','POST'])
def register():
    form=RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created! welcome {form.username.data}!')
        return redirect(url_for('home'))
    
    return render_template('register.html',title='Register',form=form)

@app.route("/Login")
def login():
    form=LoginForm()
    return render_template('login.html',title='Login',form=form)




if __name__ == '__main__':
    app.run(debug=True)