from flask import Flask, render_template, request, redirect, url_for

from db import db
from Estudiante import Estudiante

class Programa:  
    def __init__(self):

        self.app = Flask(__name__)
        self.app.config['SQLALCHEMY_DATABASE_URI']="sqlite:///estudiantes.sqlite3"

    #Agregar la Database a nuestra aplicación
        db.init_app(self.app)

        self.app.add_url_rule('/nuevo', view_func=self.agregar, methods=["GET", "POST"])  

        #Iniciar servidor

        with self.app.app_context():
            db.create_all()
        self.app.run(debug=True)
        
    def buscarTodos(self):
        
        return "TO DO: Tengo que buscar los registros de la tabla"
    def agregar(self):

        #Verificar si debe enviar el formulario o procesar los datos

        if request.method=="POST":

            #crear un objeto de la clase estudiante con los valores del formulario
            nombre=request.form['nombre']
            email=request.form['email']
            codigo=request.form['codigo']

            miEstudiante=Estudiante(nombre, email, codigo)

            #Guardar el objeto en la base de datos

            db.session.add(miEstudiante)
            db.session.commit()

            return redirect(url_for('buscar todos'))
        return render_template('nuevoEstudiante.html')


miPrograma = Programa()  # Create an instance of the class
