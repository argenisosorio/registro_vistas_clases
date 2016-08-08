#Registro de Usuarios - Vistas basadas en clases

Creado por dM

##Versiones
```
Django==1.8.8
Python==2.7
```

##(Registrar Persona)

Aplicación que sirve para registrar
personas, almacenar los registros en
una base de datos y luego consultar
los mismos. Se veran ejemplos sencillos
de creación de modelos, vistas basadas
en clases y la utilización de etiquetas
con codigo python en las plantillas.

##Tip

La base de datos es sqlite3, al
migrar se creara, así como
creara la tabla y campos descritos
en el modelo.

##Comandos usados en secuencia para probar el proyecto

$ python manage.py migrate

$ python manage.py makemigrations

$ python manage.py migrate

$ python manage.py createsuperuser

$ python manage.py runserver