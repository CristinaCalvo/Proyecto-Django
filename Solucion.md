<h1>Django Task</h1>
<h2>Creamos el repositorio</h2>
<p>Una vez creado el repositorio lo copiamos a nuestra máquina local con el siguiente comando:</p>

``` bash
git clone https://github.com/CristinaCalvo/Proyecto-Django.git
```

<h2>Instalación de entorno virtual</h2>
<p>Antes de instalar Django lo primero que haremos es instalar un entorno virtual, entonces lo activamos</p>

``` bash
source /usr/local/bin/virtualenvwrapper.sh
```
<p>Y una vez activado lo creamos</p>

``` bash
mkvirtualenv django
```
<p>Una vez que hayas creado el entorno virtual, verás que tu terminal muestra el prefijo del entorno virtual (django).</p>
<p>Si ya lo tienes creado de antes o quieres reutilizar uno</p>

``` bash
workon nombre
```

<h2>Instalación de Django</h2>
<p>Con el entorno virtual activado, estás listo para instalar Django. Antes de hacerlo, asegúrate de tener la última versión de pip ejecutando el siguiente comando:</p>

``` bash
python -m pip install --upgrade pip
```

<p>Ahora, crea un archivo llamado <code>requirements.txt</code> en el directorio de tu proyecto con el contenido <code>Django~=3.2.10</code></p>

``` bash
echo Django~=3.2.10 > requirements.txt
```
<p>Instalamos todos los paquetes necesarios</p>

``` bash
pip install -r requirements.txt
```

<p>¡Listo! Django está instalado en tu entorno virtual, y estás preparado para comenzar tu desarrollo.</p>

<h2>Iniciamos Proyecto</h2>
<p>Vamos a crear un proyecto de Task que nos deje subir tareas con su nombre, descripción y marcarlas como realizadas</p>

<p>Antes de ejecutar estos comandos, asegúrate de estar en tu entorno virtual </p>

``` bash
django-admin startproject mysite .
```
<p>Con esto crearíamos la estructura del directorio inicial, <code>mysite</code> y <code>manage.py</code></p>

<p>Lo siguiente que hacemos es crear el archivo <code>.gitignore</code> para que contemple archivos que no queremos subir</p>

``` bash
touch .gitignore
```

<p>Lo que contendría .gitignore</p>

``` bash
*.pyc
*~
__pycache__
myvenv
db.sqlite3
/static
.DS_Store
```

<p>Recuerda que este archivo está oculto, si quieres verlo tienes que hacerlo con <code>ls -la</code></p>

<p>A continuación editamos los datos básicos en <code>mysite/settings.py</code></p>

<p>Edita <code>LANGUAGE_CODE</code> y <code>TIME_ZONE</code></p>

``` bash
LANGUAGE_CODE = ‘es-es’
```
``` bash
TIME_ZONE = ‘Europe/Madrid’
```

<p>Comprueba que esta <code>STATIC_URL</code> correctamente</p>

``` bash
STATIC_URL = '/static/'
```
<p>Después añade <code>STATIC_ROOT</code></p>

``` bash
STATIC_ROOT = BASE_DIR / 'static'
```
<p>Añade <code>'127.0.0.1', '.pythonanywhere.com'</code> en <code>ALLOWED_HOSTS</code> </p>

``` bash
ALLOWED_HOSTS = ['127.0.0.1', '.pythonanywhere.com']
```

<p>Comprueba que la base de datos está bien enlazada</p>

``` bash
DATABASES = {

      'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
                  }
            }
```

<p>Y por último crea e inicializa la base de datos</p>

``` bash
python manage.py migrate
```

<p>Ahora lo que vamos hacer es arrancar el servidor</p>

``` bash
python manage.py runserver
```

<p>Abre tu navegador y verifica si tu sitio web se está ejecutando ingresando la siguiente dirección:</p>

``` bash
http://127.0.0.1:8000/
```

<p>¡Enhorabuena! Has iniciado con un servidor web. Ahora estás listo para empezar a crear contenido para tu proyecto.</p>

<h2>Creamos la aplicación</h2>

<p>Para crear la aplicación</p>

``` bash
python manage.py startapp task
```

<p>Después registraríamos nuestra aplicación recien hecha en <code>mysite/settings.py</code></p>

``` bash
      INSTALLED_APPS = [
            'django.contrib.admin',
            'django.contrib.auth',
            'django.contrib.contenttypes',
            'django.contrib.sessions',
            'django.contrib.messages',
            'django.contrib.staticfiles',
            'task',
]
```
<h2>Creamos modelo</h2>
<p>Definimos el modelo Task en el archivo <code>blog/models.py</code>. Este modelo tiene propiedades como título, texto, autor, una casilla para marcar que está hecho, fechas y un método publicar.</p>


``` bash
from django.db import models
from django.conf import settings
from django.utils import timezone

class Task(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    validacion = models.BooleanField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

def publish(self):
    self.published_date = timezone.now()
    self.save()

def __str__(self):
    return self.title
```

<p>Luego, creamos un archivo de migración y aplicamos la migración para agregar el modelo Task a la base de datos SQLite que utilizamos. </p>

<p>Preparamos un fichero de migración</p>

``` bash
python manage.py makemigrations task
```

<p>Aplicamos un fichero de migración</p>

``` bash
python manage.py migrate task
```

<h2>Aministrador de Django</h2>
<p>Con el administrador de Django podremos editar y publicar nuestras Tasks</p>
<p>Abre el archivo <code>task/admin.py</code> en tu editor y reemplaza su contenido con el siguiente código:</p>

``` bash
from django.contrib import admin
from .models import Task

admin.site.register(Task)
```

<p>En este código, estamos importando el modelo Task que definimos anteriormente y lo registramos con el administrador mediante <code>admin.site.register(Task)</code>.</p>

<p>Creamos un administrador desde la carpeta principal</p>

``` bash
python manage.py createsuperuser
```

<p>Recuerda iniciar el servidor web para ver los cambios</p>

``` bash
python manage.py runserver
```
<p>En el navegador:</p>

``` bash
http://127.0.0.1:8000/admin/
```

<h2>URL de Task</h2>
<p>Modificamos <code>mysite/urls.py</code> y añadimos la importación de task.urls</p>

``` bash
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('task.urls')),
]
```

<p>Luego, en un nuevo archivo llamado <code>task/urls.py</code>, definimos las URLs específicas de la aplicación de task:</p>

``` bash
from django.urls import path
from . import views

urlpatterns = [
	path('', views.task_list, name='task_list'),
]
```

<h2>Vistas de Task</h2>

<p>Si has intentado iniciar el servidor y te da error es por que primero tenemos que configurar la vista de Task</p>
<p>Abre el archivo <code>task/views.py</code> y agrega esta vista</p>

``` bash
from django.shortcuts import render
from django.utils import timezone
from .models import Task

      def task_list(request):
      tasks = Task.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
      return render(request, 'task/task_list.html', {'tasks': tasks})
```

<p>Hemos creado una vista llamada task_list que utiliza la función render para construir la plantilla task/task_list.html.

Guarda el archivo y visita http://127.0.0.1:8000/ para ver el resultado.

Si encuentras un error, no te preocupes. A continuación vamos a crear plantillas.</p>

<h2>Nuestra plantilla html</h2>
<p>Crea un archivo llamado task_list.html en el directorio <code>task/templates/task</code>.</p>

<p>Dentro de la carpeta task</p>

``` bash
mkdir templates
```

<p>Dentro de la carpeta task/templates</p>

``` bash
mkdir task
```

<p>Dentro de la carpeta task/templates/task</p>

``` bash
touch task_list.html
```

<p>Por último en <code>task_list.html</code></p>

``` bash
<div>
    <h1><a href="/">Tareas</a></h1> 
</div>
    {% for task in tasks %}
    <div>
        <p> publicado: {{ task.published_date }}</p>
        <h2><a href="">{{ task.title }}</a></h2>
        <p>{{task.text|linebreaksbr}}</p> 
        <p>Estado: {{task.validacion}}</p>
    </div>
    {% endfor %}
```

<p>Ahora cuando iniciemos el servidor deberiámos ver como todo sale correctamente</p>

<p>Gracias por ver :)</p>

