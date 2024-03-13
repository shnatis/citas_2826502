from . import app, db
from .models import *
from flask import render_template, request, flash, redirect 


#crear ruta para ver los medicos 
@app.route("/medicos")
def get_all_medicos():
    medicos = Medico.query.all()
    return render_template("medicos.html" , medicos=medicos )

#crear ruta para ver los pacientes
@app.route("/pacientes")
def get_all_pacientes():
    pacientes = Paciente.query.all()
    return render_template("pacientes.html" , pacientes=pacientes )

#crear ruta para ver los consultorios
@app.route("/consultorios")
def get_all_consultorios():
    consultorios = Consultorio.query.all()
    return render_template("pacientes.html" , consultorios=consultorios )

#crear ruta traer el medico por id (get)
@app.route("/medicos/<int:id>")
def get_medico_by_id(id):
    medico = Medico.query.get(id)
    return render_template("medico.html",
                           med = medico)

@app.route("/pacientes/<int:id>")
def get_paciente_by_id(id):
    paciente = Paciente.query.get(id)
    return render_template("paciente.html",
                           pac = paciente)

#crear ruta para crear nuevo medico
@app.route("/medicos/create" , methods = [ 'GET' , 'POST'] )
def create_medico():
    if( request.method == 'GET' ):
        especialidades = [
            "Cardiologia",
            "Pediatria", 
            "Oncologia"
        ]
    medico_update = Medico.query.get(id)
    if(request.method == "GET"):  
        return render_template('medico_update.html',
                            medico_update = medico_update,
                            especialidades = especialidades)
    
    ####
    ## Cuando el usuario presiona el boton guardar  
    ## los datos del formulario viajan al servidor
    ## utilizando el metodo POST

    elif(request.method == 'POST'):
        #cuando se presiona 'guardar'
        new_medico = Medico(nombre = request.form["nombre"], 
                            apellidos = request.form["apellidos"],
                            tipo_identificacion = request.form["ti"],
                            numero_identificacion = request.form["ni"],
                            registro_medico = request.form["rm"],
                            especialidad = request.form["es"]
                            )
        
        db.session.add(new_medico)
        db.session.commit()
        flash("Medico registrado correctamente")
        return redirect("/medicos")
    
@app.route("/medicos/update/<int:id>", methods= ["POST" , "GET"])
def update_medico(id):
    especialidades = [
            "Cardiologia" ,
            "Pediatria" ,
            "Oncologia"

        ]
    medico_update = Medico.query.get(id)
    if(request.method == "GET"):
        return render_template("medico_update.html" ,
                           medico_update = medico_update ,
                           especialidades = especialidades)
    elif(request.method == "POST"):
        medico_update.nombre = request.form["nombre"]
        medico_update.apellidos = request.form["apellidos"]
        medico_update.tipo_identificacion = request.form["ti"]
        medico_update.numero_identificacion = request.form["ni"]
        medico_update.registro_medico = request.form["rm"]
        medico_update.especialiad = request.form["es"]
        db.session.commit()
        return "medico actualizado"
    
@app.route("/medicos/delete/<int:id>")
def delete_medico(id):
    medico_delete = Medico.query.get(id)
    db.session.delete(medico_delete)
    db.session.commit()
    return redirect("/medicos")