# RED_SOCIAL_DJANGO
 RED SOCIAL

 # Objetivo Principal

 Crear una aplicación con el framework django,para entregar a los usuarios un espacio donde poder compartir sus ideas
a través de esta red social.

# Para ver la aplicación vea los siguientes pasos

Para crear un repositorio local $ git init

Clonas el repositorio en tu repositorio local $ git clone

Para agregar archivos al área de trabajo $ git add

Luego, navegas a la carpeta clonada Se ejecuta el entorno virtual, se debe navegar hasta la carpeta que contenga el entorno virtual call venvGrupal_3/Scripts/activate

Se navega a la carpeta que contenga el archivo manage.py en esta carpeta se ejecuta el siguiente comando python manage.py runserver

Se realizan las migraciones correspondientes python manage.py makemigrations python manage.py migrate

Se crea el superusuraio administrador python manage.py createsuperuser

Se vuelce a ejecutar el proyecto python manage.py runserver

¡¡¡¡ A DISFRUTAR DE ESTA RED SOCIAL ¡¡¡¡¡

# Desarrollo

Principales librerias que se ocupan en la aplicación
asgiref==3.4.1
Django==3.2.9
Pillow==8.4.0
psycopg2==2.9.2
psycopg2-binary==2.9.2
pytz==2021.3
sqlparse==0.4.2

# Bases de datos

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='batman.png')}

Almacenamos los perfiles de la aplicación.

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    timestamp = models.DateTimeField(default=timezone.now)
    content = models.TextField()
    image = models.ImageField(upload_to='media/images')

Almacenamos los post que hacen cada uno de los usuarios

class Relationship(models.Model):
    from_user = models.ForeignKey(User,related_name='relationships', on_delete=models.CASCADE)
    to_user = models.ForeignKey(User,related_name='related_to', on_delete=models.CASCADE)

Almacenamos las relaciones que se pueden dar entre los distintos usuarios de la aplicación

# Formularios

class UserRegisterForm(UserCreationForm):
    username = forms.CharField()
    email = forms.EmailField()
    password1 = forms.CharField(label='Contraseña',widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirma Contraseña',widget=forms.PasswordInput) 

    class Meta:
        model = User
        fields = ['username','email','password1','password2']
        help_text = { k:"" for k in fields }

Se crea este formulario para que cada usuario se pueda registrar en nuestra  red social


Creamos la parte donde el usuario puede dejar un post 
class PostForm(forms.ModelForm):
    content = forms.CharField(label='', widget=forms.Textarea(attrs={'rows':2, 'placeholder':'¿Qué estas pensando hoy?'}), required=True)  
    class Meta:
        model = Post
        fields = ['content','image']

Se crea este formulario para recibir los post de cada usuario