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
            'blog',
]
```




