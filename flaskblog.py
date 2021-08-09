from flask import Flask, render_template

app = Flask(__name__)

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

if __name__ == '__main__':
    app.run(debug=True)