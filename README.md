# Buenas a todos por aqui os pongo una guia a seguir para poder inicializar el projecto

# Primero: Debeis ejectuar las virtualizacion 
  - py -3 -m venv venv
  - venv\Scripts\activate
# Sefundo: Mirar a donde guardareis la base de datos NYSQL, POGRESQL, SQLITE... 
  - En mi caso use MYSQL. 
  - Por defecto Django mtiene SQLITE
  - pip install mysqlclient
  
    (DATOS PARA QUE FUNCIONE LA CONFIGURACION DE MYSQL)

    'default': 
    {
      'ENGINE': 'django.db.backends.mysql',
      'NAME': '',
      'USER': '',
      'PASSWORD': '',
      'HOST': '',
      'PORT': '',
    }

    (Subir a la base de datos)
    py manage.py migrate 

    (Cuando hay cambio en el modelos)
    py manage.py makemigrations
    
# Tercero: Crear un superusuario
  - py manage.py createsuperuser

# Cuarto: Crear la app y añadirla al settings
  - django-admin startapp "catalog" (Ir al settings del proyecto y añadir la nueva app em "INSTALLED_APPS")

# Quinto: Añadir la Ruta de la APP 

  * from django.urls import include
  urlpatterns =+ [
    *  path('catalog/', include("catalog.urls")),
  ]
  
# Extra: 

ARRANCAR: manage.py runserver <-- Recordar debeis estar en la principal carpeta donde esta el "manage.py"
Para poner las rutas estaticas:

  * from django.conf import settings
  * from django.conf.urls.static import static
  urlpatterns =+ [

  ] * + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
