## Proyecto 2

Sistemas y Tecnologias Web

El proyecto fue realizado tomando como base un proyecto de Base de Datos

--------------------------------------------

## Componentes del proyecto
El proyecto contiene algunos componentes como lo es la barra de navegacion.

## Programa principal

Este proyecto, al estar utilizando una base de datos, se trato de conectar con python por lo que el mejor software a utilizar es Flask. Para este se debe tener un programa principal, que en este caso se llama Proyecto.py, en el que se llevan los cambios de las paginas (como las rutas de estas) y se adjunta la informacion escencial de la base de datos, asi como alimenta las paginas HTML que se encuentran el la carpeta de templates. La parte a destacar de este programa es el uso de un puntero para conectar el programa con la base de datos. El puntero se puede ver así: 

```bash
import psycopg2
conn= psycopg2.connect(database="Proyecto2",
    user='postgres',
    password='Hola!',
    host='localhost')
conn.autocommit=True
cursor=conn.cursor()
```
Y ya con esto, el programa de python puede correr diferentes querys dentro de la base de datos. Los datos que se escriben en la contraseña y en el usuario dependeran de lo que cada persona desee utilizar, en este caso, esta contraseña es demostrativa.

Para iniciar el proyecto de Python de manera local, se puede hacer de diferentes maneras. Si se utiliza Visual Studio Code, se puede empezar dandole a la flecha de inicio en la parte superior derecha, aunque si no se utiliza o se quisiera iniciar desde la linea de comando (terminal de la computadora) se puede iniciar usando el comando: 
```bash
pyhton Proyecto.py
```
Y con esto deberia generar el servidor local para visualizar el proyecto

## Forms

Dentro de este programa se pueden ver los formularios del Log in y del Sign In que son manejados por una extension de Flask que crea automaticamente estos formularios. De estos se puede sacar la informacion que se inserta en la base de datos, como tambien se puede comprobar si es que se necesita para tener un log in. Luego en las respectivas paginas del inicio de sesion como en el de registro se deben personalizar los campos ya que son los que muestran el HTML.

Algunas cosas que podemos resaltar de este archivo es que hay que tomar en cuenta los Validators que se escriben en cada campo ya que estos pueden generar un error en la escritura en la base de datos. 

### Templates
La carpeta de Templates crea las diferentes paginas en HTML que se utiliza en el proyecto. Ya que el proyecto esta basado en Flask, en el que se utiliza Python, este se tiene que adjuntar aparte en el programa principal. En estas templates se pueden ver algunos archivos que utilizan la herencia para poder funcionar de manera mas optima.

Los mas importantes de esta carpeta son los archivos de layout1.html y layout2.html que son los padres para todos los demas archivos.

---------------------------------------------------------------------------------------------------------------------------------------------------

Las tecnologias que se utilizaron en este proyecto fueron:

### Flask
Esta es la tecnologia base de mi pagina web, maneja todas las funciones entre los HTML y el archivo de Python que controla la Base de Datos
### PostgreSQL
Esta es el lenguaje de la base del proyecto ya que todo se contruye en base a esto. El objetivo era hacer una pagina web funcional que conectara con la base de datos y se pudieran realizar las diferentes actividades sin que hubiera errores de lectura y escritura
### PGAdmin
Este es el gestor de Base de Datos que se utilizo para tener un control en lo que pasaba dentro de la misma. 
### Python
Se utiliza Python ya que Flask lo necesita para funcionar, aunque este solo es utilizado en muy contadas ocaciones ya que python solo es utilizadon en el "MAIN" y en los formularios de inicio de sesion como tambien en el de Registro. 
### CSS
El CSS de este proyecto se conecta con las paginas y los layouts para darle diferente personalizacion a cada componente si es que se le quiere dar.
