from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm
app = Flask(__name__)
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'
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
@app.route("/about")
def about():
    return render_template('about.html', title='About')

@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        cursor.execute("INSERT INTO usuario (nombre, apellido, edad, altura, calorias, peso_act, contra, acc_type) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)", (form.Nombre.data, form.Apellido.data, form.Edad.data, form.Altura.data, form.Calorias.data, form.Peso_act.data, form.password.data, form.Miembro.data))
        cursor.execute("SELECT user_id FROM usuario WHERE nombre = %s AND apellido = %s", (form.Nombre.data, form.Apellido.data))
        user_id = cursor.fetchone()[0]
        flash(f'Creada la cuenta! Su número de usuario es: {user_id}. ¡Guárdelo muy bien, por favor!')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)



@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        cursor.execute("select nombre from usuario where user_id = %s and contra = %s", (form.User.data, form.password.data))
        existe=cursor.rowcount
        if existe == 1:
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Inicio de sesión erroneo. Por favor revise los datos ingresados')
    return render_template('login.html', title='Login', form=form)

@app.route("/home")
def home():
    return render_template('home.html', posts=posts)

@app.route("/configuration")
def configuration():
    return render_template('configuration.html', posts=posts)

if __name__ == '__main__':
    app.run(debug=True)