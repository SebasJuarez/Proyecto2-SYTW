from flask import Flask, render_template, url_for
app = Flask(__name__)
import psycopg2
conn= psycopg2.connect(database="Proyecto2",
    user='postgres',
    password='Fac3viche',
    host='localhost')
conn.autocommit=True
cursor=conn.cursor()
cursor.execute("SELECT nombre, apellido FROM usuario WHERE user_id = 20")
result = cursor.fetchone()

if result is not None:
    Hol11 = result[0]
    Hol12 = result[1]
    Hol1 = Hol11 + " " + Hol12
else:
    # Handle the case where no results are found
    Hol1 = result[0]  # or assign a default value

cursor.execute("SELECT nombre, apellido FROM usuario WHERE user_id = 18")
result = cursor.fetchone()

if result is not None:
    Hol21 = result[0]
    Hol22 = result[1]
    Hol2 = Hol21 + " " + Hol22
else:
    # Handle the case where no results are found
    Hol2 = result[0]  # or assign a default valu

posts = [
    {
        'author': Hol1,
        'title': 'Como ser mono en la ciudad',
        'content': 'First post content',
        'date_posted': 'April 20, 2018'
    },
    {
        'author': Hol2,
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'April 21, 2018'
    }
]


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)


@app.route("/about")
def about():
    return render_template('about.html', title='About')


if __name__ == '__main__':
    app.run(debug=True)