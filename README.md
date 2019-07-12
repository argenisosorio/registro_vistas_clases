# Registro de Usuarios - Vistas basadas en clases

Creado por dM

## Versiones
```
Django==1.8.8
Python==2.7
```

## (Registrar Persona)

Aplicación que sirve para registrar
personas, almacenar los registros en
una base de datos y luego consultar
los mismos. Se veran ejemplos sencillos
de creación de modelos, vistas basadas
en clases y la utilización de etiquetas
con codigo python en las plantillas.

## Tip

La base de datos es sqlite3, al
migrar se creara, así como
creara la tabla y campos descritos
en el modelo.

## Comandos usados en secuencia para probar el proyecto

$ python manage.py makemigrations registro

$ python manage.py migrate

$ python manage.py createsuperuser

$ python manage.py runserver

## Rama messages

El proyecto contiene una rama messages que muestra
como se envian mensajes usando los métodos de las clases
genéricas de Django.

## Rama bitacora

El proyecto contiene una rama bitacora que muestra
como podemos crear un modelo para guardar logs
de las acciones ejecutadas por un usuario
y mostrarlas en una plantilla.

## Rama upload

En la rama upload hay un ejemplo
de como subir archivos al servidor usando
un formulario.

## Rama upload_model

En esta rama encontraremos un ejemplo
de como subir ficheros al servidor usando
los modelos y formularios de django, e
instanciaremos los ficheros subidos con un objeto en
la base de datos.

## Rama auth

En esta rama encontraremos un ejemplo
de autenticación de usuarios, cierre de
sesión y creación de cuentas de usuarios
del sistema con modelo perfil asociado.

## Rama selects

En esta rama encontraremos un ejemplo
de campos de selección de formularios que se cargan de datos
dependiente de otros campos.

## Rama create_acount

En esta rama encontraremos un ejemplo
de creación de cuentas de usuarios
del sistema.

## Rama type_users

En esta rama encontraremos un ejemplo
de creación de cuentas de usuarios
del sistema y jugamos con los tipos
de usuarios y el last_name.

## Rama profile_photo

En esta rama encontraremos un ejemplo
de creación de como subir y mostrar
una imagen de perfil de una persona
que se registre en el sistema.