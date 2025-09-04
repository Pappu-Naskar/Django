# Django Tutorial 

## 🚀 Getting Started

## First, download the `Django` extension in your code editor

## Step 1:

*Create a virtual environment to install Django packages and more. Let's create a virtual environment...*

**Open your code editor terminal**

```bash
python -m venv .venv
```  

**Another way to create a virtual environment using the uv package**

- **uv Package**: An extremely fast Python package and project manager, written in Rust.

  **1. Install the uv package:**

   Open your code editor terminal

    ```bash
    pip install uv
    ```
  **2. To create a virtual environment:**
    ```bash
    uv venv
    ```

**Activate the venv environment:**

  - **Open your code editor terminal**
      - *For Windows* 

       ```bash
       source .venv/Scripts/activate
       ```
       - For Linux/mac:

       ```bash
       source .venv/bin/activate
       ```


**To deactivate a virtual environment, type:**

```bash
deactivate
```
## Step 2:

**Install django packages**
[Django](https://www.djangoproject.com/)
- **Open code editor terminal**

  ```bash
  uv pip install django
  ```

## Step 3:

**Create python project using Django**

- **Open code editor terminal**
  
  ```bash
  django-admin starproject projectDjango
  ```
- **Run Django Project**
  ```bash
  cd projectDjango
  ```
- **Next you can show manage.py fille and then we use this file for run Python poject .**

  ```bash
  python manage.py runserver
  ```

**Know about manage.py file**: This file is your stating point file . This file set environment variabls and many more . And when you go production work invoke your system by this file . First time run only this file .

**sqlite3 file** : this file is defult **Data Base** using in Django

## Step 4

**Go under project folder**

**Know about pycache folder:** When you have multiple moduls in python then its create this folder .

**Main file of project settings.py file:** Hear you see configeration of Django .(for example: BASE_DIR ,SECRET_KEY , DEBUG = True : YOU SHOW WEB PAGE) and many more conf settings .

**Url.py:** This file is routing file.You visit many link pages.




## Step 5

# Templates in Django
**Django flow Structure**
![]()

**Next Create views.py file in Project folder.**

**Views.py** : This file define all views.This file deal business logic.

**Write some code in views.py**
```python
from django.http import HttpResponse
 
def home(requst):
    return HttpResponse("Hello, world . you are at chai aur Django home page")
     
def about(requst):
    return HttpResponse("Hello, world . you are at chai aur Django about page")

def contact(requst):
    return HttpResponse("Hello, world . you are at chai aur Django contact page")
```  

## Handel Urls

**Open urls.py files**

**Lets add routs in urls.py from views.py file.**

```python
from django.contrib import admin
from django.urls import path 
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('',views.Route,nam='route_name')
    # for example:
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
]
```

### **Open Terminal and Run this Project**

```bash
cd projectDjango
projectDjango> python manage.py runserver
``` 

**Open website in your system defult browser there you view all routing pages**

#### **How to Use Templetes in Django ?**

**Lets Start:**

**_where create templets depands how you see fils or how you do settings._**

**Right click on `Project Root Folder` and click new folder and create folder and name it `templates`.**

**Right click on `Project Root Folder` and click new folder and create folder and name it `static`.**

**Create `Css and JavaScript` files in this `static` folder .**

**And create `HTML` fils in this `templates` folder.**

### **Next**

**Right click on `templates` folder and create new file `index.html `.**

**lets write codes in `index.html`.**

**Hear not sugations is not givien in html file**

**When open `html`  html emmet is not working, fix this problem prces `Ctrl + , > search emmet > Go to Emmet:include Languages > Add item >Key:'django-html' or value:'html'` .**
 

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Chai aur Django</title>
</head>
<body>
    <h1>Chai aur Django</h1>
</body>
</html>
```

**Lode this templates and Return back**

**Open `views.py` and Render using import `from django.shortcuts import render` a templates.**

```python
from django.http import HttpResponse
from django.shortcuts import render

def home(requst):
    # return HttpResponse("Hello, world . you are at chai aur Django home page")
    return render(requst,'website/index.html')
def about(requst):
    return HttpResponse("Hello, world . you are at chai aur Django about page")
def contact(requst):
    return HttpResponse("Hello, world . you are at chai aur Django contact page")
```  

**When run this code its return Error `TemplateDoesNotExist at /index.html`**

#### **Ok Resolve this Error**

### **Why this Error Exist ?**
### Ans: **Becouse you forget to set main project from where load templates**

**Click `settings.py` file -**
**Go `TEMPLATES` section and there this settings**

```python
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'], #Hear write 'templates'
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
```
### Now fixed Error
**Project work Perfactly**

### **Add some `CSS` in website pages**

## Lets Start

**Right click on `static` folder and create `style.css `file**

```Css
body{
  background-color: #031d5d;
  color: white;
}
h1{
  text-align: center;
  font-size: 2em;
}
```

**Now how to load css file in this projects ?**

**Open `templates/index.html` and add `Css`**

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Chai aur Django</title>
    <!-- <link rel='stylesheet' href="../../static/style.css"> -->
    <!-- this code give Error -->

    <!-- use template Engin -->
    <link rel='stylesheet' href="{% static 'style.css' %}">
    <!-- this code give Error -->
    </head>
<body>
    <h1>Chai aur Django</h1>
</body>
</html>
```

**This code give Eroor like `invalid block tag on : 'static'. Did you forget to register or load this tag?`**

### **Why this Error Exist ?**
**Ans: When you use static acid and static keyword then set template engin 
load static acid.** 

**Lets resolve it**

```html
{% load static %}
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Chai aur Django</title>
    <!-- <link rel='stylesheet' href="../../static/style.css"> -->
    <!-- this code give Error -->

    <!-- use template Engin -->
    <link rel='stylesheet' href="{% static 'style.css' %}">
    <!-- this code give Error -->
    </head>
<body>
    <h1>Chai aur Django</h1>
</body>
</html>
```

**this code run perfectly but you can see css is not empliment on this project**

**Lets resolve it**

**Open `settings.py` file-**

```python
import os
# import os libery
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.2/howto/static-files/
STATIC_URL = 'static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR,'static')]
```

### **Now fix all problems and css work perfectly**

***`Same process you can use javaScript in this projects just like css file use`***


# ***Step 6***

## **Jinja2 and django apps**

### ***How to create Apps in Django Projects***

## 🚀 Getting Started

[Learn about Jinja2, visit jinja2](https://jinja.palletsprojects.com/en/stable/api/#high-level-api)

[Visit Django Templets Layer](https://docs.djangoproject.com/en/5.2/topics/templates/) **in this link when you go there you see how to use `variables` by using `{{variables}}`** 


**`{% csrf_token %}` This definition is deliberately vague. For example, a tag can output content, serve as a control structure e.g. an “if” statement or a “for” loop, grab content from a database, or even enable access to other template tags.** 

**Filtes -transform the values of veriables and tag arguments `{{django|title}}`**

## Lets create apps

**Open terminal**
```bash
cd projectDjango
```
```bash
python manage.py startapp <Appname>
```
**Then you see `app`folder under root folder**.

**Next step**

**set app to main project**

**Open `settings.py` in main project folder.**

```python
# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'appName',
] 
```
**Now properliy install and configer app**

**Main project deal by using `App`.**

**How to deal with main project?**

**Right click app folder and create `new folder` name `templates` hit Enter.**

**Next right click on `templates` folder and Create fouther Folder name `appName`. And next right click `appName` folder and create file `all_project.html`**

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>All Chai</title>
</head>
<body>
    <h1>All types of available chai</h1>
</body>
</html>
```

**Next open `appName/views.py` file for render templates**

```python
from django.shortcuts import render
# Create your views here
def all_project(request):
  return render(request,'appName/all_projects.html')
```

**Go main project click `urls.py` and copy all code**

**Then go `appName` and right click create file `urls.py` and hit Enter**

```python
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    
]
```
**First pass control**

**Go main project click `urls.py` . Transfar control 
```python
from django.contrib import admin
from django.urls import path, include 
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
   path('appName',include('appName.urls')),   
]
```
**Then go `appName` and right click create file `urls.py` and hit Enter**

```python
# Remove admin
# from django.contrib import admin
from django.urls import path
from . import views

#localhost:8000/chai

urlpatterns = [     
 path('', views.all_project, name='all_project'),  
   
]
```

**Run project**
```bash
cd projectDjango
projectDjango > python manage.py runserver
```

**Show home page when reload project then type search bar localhost:8000/appname**

## **Lets know about jinja2**

**Right click on main templates create file `layout.html` and hit enter.**

```html
{% load static tailwind_tags %}
{% load static %}
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title> 
      <!-- for using defferent title using block_unnamed -->
        {% block title %}
        Default value
        {% endblock %}
    </title>
    <link rel="stylesheet" href="{% static 'style.css'%}">
     {% tailwind_css %}
</head>
<body>
  <nav>This is our navbar</nav>
    {% block content %}{% endblock %}
</body>
</html>
```

## ***How to use `layout.html`***

**Go `projectDjango > templates > index.html` and hit enter**

```html
<!-- which file use as a templates -->
{% extends "layout.html" %}

{% block title %}
Home Page
{% endblock %}

{% block content %}

<h1 class='bg-green-400 p-4 text-2xl'>Chai aur code  | Home page</h1> 
 
{% endblock %} 
```

**This layout templates use in app templates folder**
***`all_project.html` hit Enter***
```html
<!-- which file use as a templates -->
{% extends "layout.html" %}

{% block title %}
All Projects 
{% endblock %}

{% block content %}

<h1>All projects for you</h1>
 
{% endblock %} 
```
**Show home page when reload project then type search bar localhost:8000/appname/**

# ***Step 7***
## 🚀 Getting Started

***How to set Tailwind Css with our projects***

**To download tailwind css [Click me](https://pypi.org/project/django-tailwind/)**

***Next Open Terminal***
**Hear we not use uv . We use pip.** 

**At first activate `.venv` folder .**
```bash
source .venv/Scripts/activate
```
**How to install pip in .venv**
- **first commend**
  ```bash
  python -m ensurepip --upgrade
  ```
- **second commendd**
  ```bash
  python -m pip install --upgrade pip
  ```
**Finaly install pip**

**Next install tailwind css using pip .**
***We set hot-reload when changes any file server is automticaliy reloaded***
**OK install hot-reload**
```bash
pip install 'django-tailwind[reload]'
```

**Set Tailwind with main app/projects**
**`projectDjango>settings.py` open and go INTSTALL_APPS seaction and conf the settings.**

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'chai',
    'tailwind',
]
```
***Save it***

**And run a simple Commend in terminal**
```bash
python manage.py tailwind init
```
**After some time later when tailwind fullfil installed then ask `app_name` you also set any name of `app_name` and hit enter.**

***After you see theme folder in main project folder.***

**Ok install one more app in main projects `setting.py`.**
**Open `setting.py` file and go INTSTALL_APPS seaction and conf the settings.**

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'chai',
    'tailwind',
    'theme',
]
```
## **Next**
 
**Open `setting.py` file and go to under INTSTALL_APPS seaction and conf the settings.**

```python
TAILWIND_APP_NAME = 'theme'
 
INTERNAL_IPS = ['127.0.0.1']
```

**Finaly install tailwind by using `manage.py`**
```bash
python manage.py tailwind install
```
**Next you open `projectDjango>theme>base.html`**
**Copy tailwind templates Engins from base.html file.**

**Then open our `layout.html` which we create .Open that file and paste hear.** 

```html
{% load static tailwind_tags %}
{% load static %}
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title> 
        {% block title %}
        Default value
        {% endblock %}
    </title>
    <link rel="stylesheet" href="{% static 'style.css'%}">
     {% tailwind_css %}
</head>
<body>
    <nav>This is our navbar</nav>
    {% block content %}{% endblock %}
</body>
</html>
```

***Now run server***

**Write tailwind class in `index.html` open `projectDjango>templates>index.html` click.**
```html
{% extends "layout.html" %}

{% block title %}
Home page
{% endblock %}
{% block content%}
 <h1 class='bg-green-400 p-4 text-2xl'>Chai aur code  | Home page</h1> 
{% endblock %}
```
**this tailwind classes isn't working because tailwind is not genrate.**

**Ok Fix that Error**

**Open new terminal and activate .venv and rename the terminal name tailwind**
```bash
python manage.py tailwind start
```
**Now relode web page but tailwind is not working because npm bin path is not set with main project settings.**

**Open main `projectDjango>settings.py`.
```python
TAILWIND_APP_NAME = 'theme'
#install tailwindcss 
# open cmd and commend where npm hit enter show two path where show npm.cmd copy and paste hear

NPM_BIN_PATH =  r"C:\Program Files\nodejs\npm.cmd"

INTERNAL_IPS = ['127.0.0.1']
```
**Now start tailwind**
```bash
python manage.py tailwind start
```
**IN production you can not use defferent Terminal you use same terminal where your main app run.**

```bash
python manage.py tailwind build
```
***Ok conf Auto reloding browser\hot-reloding settings***
**Open `setting.py` file and go INTSTALL_APPS seaction and conf the settings.**
```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'chai',
    'tailwind',
    'theme',
    'django_browser_reload',
]
```
**Open `projectDjango>settings.py`click go `MIDDLEWARE` section**
```python
MIDDLEWARE = [
    "django_browser_reload.middleware.BrowserReloadMiddleware",
]
```

***And final setting open `projectsDjango>urls.py` click**
```python
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('chai/',include('chai.urls')),
  
     

    path("__reload__/",include("django_browser_reload.urls"))
] + static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)
```
**Restart Tailwind app and project**

**Now perfectly work hot-relode**

## ***Start admin panel***
```bash
python manage.py migrate
```
***now run server there is no error showing***

***click broser search bar localhost\8000\admin now admin panel is show where from admin panel rendering go `projectDjango>projectDjango>urls.py`click you can see admin user is rendering.**

**add you chai veritys**

**conf Chaiveritys Object**

**Open `models.py` file**

```python
from django.db import models
from django.utils import timezone

# Create your models here.
class ChaiVarity(models.Model):
    CHAI_TYPE_CHOICE = [
        ('ML','MASALA'),
        ('GR','GINGER'),
        ('KL','KIWI'),
        ('PL','PLAIN'),
        ('EL','ELACHI'),
    ]
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='chais/')
    #hear you face a error [HINT: gET PILLOW AT......... or run command "python -m pip install pillow".]
    date_added = models.DateTimeField(default=timezone.now)
    type =models.CharField(max_length=2,choices = CHAI_TYPE_CHOICE)
    description = models.TextField(default='')
    price = models.DecimalField(max_digits=5, decimal_places=2,default=0.00)
 
```

**Install Pillow**
```bash
python -m pip install Pillow
```
**settings you need where you save images `main projects>settings.py` open it.**

```python
#paste it Static section
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR,'media')
```
**settings for urls for images `main projects>urls.py` open it.**
```python
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('chai/',include('chai.urls')),
  
     

    path("__reload__/",include("django_browser_reload.urls"))
] + static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)
```

**Next tolk to database what chages in models open terminal**

```bash
python manage.py makemigration
python manage.py migrate
```
**Now how to use attact any models an see in admin panel**

**Lets Start**

**Open app `admin.py` files--**
```python
from django.contrib import admin
from .models import ChaiVarity 

# Register your models here.
admin.site.register(ChaiVarity)
```
**Now start your server again and go `localhost:8000/admin` there you show Class which you Createted in models.py file.**

**add you chai veritys**

**conf Chaiveritys Object**

**Open `models.py` file**

```python
from django.db import models
from django.utils import timezone

# Create your models here.
class ChaiVarity(models.Model):
    CHAI_TYPE_CHOICE = [
        ('ML','MASALA'),
        ('GR','GINGER'),
        ('KL','KIWI'),
        ('PL','PLAIN'),
        ('EL','ELACHI'),
    ]
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='chais/')
    date_added = models.DateTimeField(default=timezone.now)
    type =models.CharField(max_length=2,choices = CHAI_TYPE_CHOICE)
    description = models.TextField(default='')
   
    def __str__(self):
        return f'{self.name}'
```

### **Next steps**

#### How to show object in our webpage ? 
**Lets Begin**

**Open `app>views.py` files**

```python
from django.shortcuts import render
from .models import ChaiVarity
 
# Create your views here.

def all_chai(request):
    chais = ChaiVarity.objects.all()
    return render(request,'chai/all_chai.html',{'chais':chais})
```

**Handel frontend value**

**Open `app>templates>chai>all_chai.html`

```html
{% extends "layout.html" %}

{% block title %}
Cahi Page
{% endblock %}
{% block content%}
<h1>All Chai for you</h1>
<div class="grid grid-cols-3 gap-4 m-4 ">
    <!-- using for-block for handel frontend value -->
    {% for chai in chais %} 
    <div class = "bg-blue-900 p-5 rounded">
        <img class='rounded shadow-lg' src="{{chai.image.url}}" alt="">
        <h3 class='text-2xl font-bold '>{{chai.name}}</h3>
        <h6>{{chai.price}}</h6>
        <a href="{% url 'chai_detail' chai.id %}">
            <button 
            type="button"
            class="inline-fles items-center w-[100%] mt-2 justify-center px-4 py-2 border border-transparent text-sm font-medium rounded-md text-white bg-orange-600 hover:bg-orange-700 focus:outline-none focus:rign-2 focus:ring-offset-2 focus:ring-orange-500"
            >
                {{chai.type}} - {{chai.id}}
            </button>
        </a>
    </div>    
    {% endfor %}
</div>
{% endblock %}
```
***After add Description***

**Open `models.py` file**

```python
from django.db import models
from django.utils import timezone

# Create your models here.
class ChaiVarity(models.Model):
    CHAI_TYPE_CHOICE = [
        ('ML','MASALA'),
        ('GR','GINGER'),
        ('KL','KIWI'),
        ('PL','PLAIN'),
        ('EL','ELACHI'),
    ]
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='chais/')
    date_added = models.DateTimeField(default=timezone.now)
    type =models.CharField(max_length=2,choices = CHAI_TYPE_CHOICE)
    description = models.TextField(default='')
   
    def __str__(self):
        return f'{self.name}'
```  
**Next tolk to database what chages in models open terminal**

```bash
python manage.py makemigration <app>
python manage.py migrate
```

***Now run server***

***How to detils page***

**Create `chai_details.html file under app>templates/chai folder`**

**Open `app>views.py` files** 

```python
from django.shortcuts import render
from .models import ChaiVarity
 
from django.shortcuts import get_object_or_404

# Create your views here.

def all_chai(request):
    chais = ChaiVarity.objects.all()
    return render(request,'chai/all_chai.html',{'chais':chais})

def chai_detail(request,chai_id):
    chai = get_object_or_404(ChaiVarity , pk=chai_id)
    return render(request ,'chai/chai_details.html',{'chai':chai})
 
```

## ***Next rendering chai_detail page***

**Open `app>urls.py`

```python
 
from django.urls import path
from . import views

urlpatterns = [    
    path('', views.all_chai, name='all_chai'),
    path('<int:chai_id>/', views.chai_detail, name='chai_detail'),   
]  
```
**Create `chai_details.html file under app>templates/chai folder`**

```html
{% extends "layout.html" %} {% block title %} Cahi Detail Page {% endblock %} 
{%block content%}
<h1>Chai Detail Page</h1>
 
{% endblock %}
```

**Open `all_chai.html file under app>templates/chai folder` for handel all_chai id when open chai_details page then show id what user click to show chai details**
```html
{% extends "layout.html" %}

{% block title %}
Cahi Page
{% endblock %}
{% block content%}
<h1>All Chai for you</h1>
<div class="grid grid-cols-3 gap-4 m-4 ">

    {% for chai in chais %}
    <div class = "bg-blue-900 p-5 rounded">
        <img class='rounded shadow-lg' src="{{chai.image.url}}" alt="">
        <h3 class='text-2xl font-bold '>{{chai.name}}</h3>
        <h6>{{chai.price}}</h6>
        <a href="{% url 'chai_detail' chai.id %}">
            <button 
            type="button"
            class="inline-fles items-center w-[100%] mt-2 justify-center px-4 py-2 border border-transparent text-sm font-medium rounded-md text-white bg-orange-600 hover:bg-orange-700 focus:outline-none focus:rign-2 focus:ring-offset-2 focus:ring-orange-500"
            >
                {{chai.type}} - {{chai.id}}
            </button>
        </a>
    </div>
    
    {% endfor %}
</div>
{% endblock %}

```

**Now we add Chai_details pages**

**Open `chai_details.html file under app>templates/chai folder`**
```html
{% extends "layout.html" %} {% block title %} Cahi Detail Page {% endblock %} 
{%block content%}
<h1>Chai Detail Page</h1>
<h3>{{chai.name}}</h3>
<p>{{chai.description}}</p>
<div class="flex items-center justify-center mt-56">
   <a href="{% url 'all_chai' %}">
            <button 
            type="button"
            class="inline-fles items-center mt-2 justify-center px-4 py-2 border border-transparent text-sm font-medium rounded-md text-white bg-orange-600 hover:bg-orange-700 focus:outline-none focus:rign-2 focus:ring-offset-2 focus:ring-orange-500"
            >
               Back
            </button>
        </a>
</div>
{% endblock %}
```

# ***Step 7***
## 🚀 Getting Started

## Relationships and Forms in Django

**Django has a number of built-in relationships that you can use to connect your models to each other. These relationships are used to create a more complex and powerful database.**

**The most common relationships are:**
- **One-to-many**
- **Many-to-many**
- **One-to-one**

## **One-to-many**

**One-to-many relationships are used when you have a model that has a foreign key to another model. In a One-to-Many relationship, each instance of the parent model can be associated with multiple instances of the child model. For example, a Chai variety can have multiple reviews.**

**In the existing `chai` app, open `models.py` and add the following code:**

```models.py
class ChaiReview(models.Model):
  chai = models.ForeignKey(ChaiVariety, on_delete=models.CASCADE, related_name='reviews')
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  rating = models.IntegerField()
  comment = models.TextField()
  date_added = models.DateTimeField(default=timezone.now)

  def __str__(self):
    return f'{self.user.username} review for {self.chai.name}'
```

**This code creates a new model called `ChaiReview` that has a foreign key to the `ChaiVariety` model. The `user `field is a foreign key to the` User `model, and the `rating `and `comment` fields are integers and text fields respectively.**

## **Many-to-many**

**Many-to-many relationships are used when you have a model that has a many-to-many relationship with another model. In a Many-to-Many relationship, each instance of one model can be associated with multiple instances of another model, and vice versa. For example, a Chai variety can be featured in multiple stores, and each store can feature multiple chai varieties.**

**In the existing `chai` app, open `models.py` and add the following code:**

```python
class Store(models.Model):
  name = models.CharField(max_length=100)
  location = models.CharField(max_length=100)
  chai_varieties = models.ManyToManyField(ChaiVariety, related_name='stores')

  def __str__(self):
    return self.name
```    

## **One-to-one**

**One-to-one relationships are used when you have a model that has a one-to-one relationship with another model. In a One-to-One relationship, each instance of one model is associated with one and only one instance of another model. For example, each Chai variety can have a unique certificate.**

**In the existing `chai `app, open `models.py` and add the following code:**

```python
class ChaiCertificate(models.Model):
  chai = models.OneToOneField(ChaiVariety, on_delete=models.CASCADE, related_name='certificate')
  certificate_number = models.CharField(max_length=100)
  issued_date = models.DateTimeField(default=timezone.now)
  valid_until = models.DateTimeField()

  def __str__(self):
   return f'Certificate for {self.chai.name}'
```

## **Update the admin**

**In the existing `chai` app, open `admin.py` and add the following code:**

```python
from django.contrib import admin
from .models import ChaiVariety, ChaiReview, Store, ChaiCertificate

class ChaiReviewInline(admin.TabularInline):
  model = ChaiReview
  extra = 1

class ChaiVarietyAdmin(admin.ModelAdmin):
  list_display = ('name', 'type', 'date_added')
  inlines = [ChaiReviewInline]

class StoreAdmin(admin.ModelAdmin):
  list_display = ('name', 'location')
  filter_horizontal = ('chai_varieties',)

class ChaiCertificateAdmin(admin.ModelAdmin):
  list_display = ('chai', 'certificate_number', 'issued_date', 'valid_until')

admin.site.register(ChaiVariety, ChaiVarietyAdmin)
admin.site.register(Store, StoreAdmin)
admin.site.register(ChaiCertificate, ChaiCertificateAdmin)
```
## **Adding a form on frontend**

**In the existing `chai` app, create a new file called `forms.py` in the `chai` app directory. In this file, add the following code:**

```python
from django import forms
from .models import ChaiVariety

class ChaiVarietyForm(forms.Form):
  chai_variety = forms.ModelChoiceField(queryset=ChaiVariety.objects.all(), label="Select Chai Variety")
```
## **Handle the view for the form**
**In the existing `chai` app, open `views.py` and add the following code:**  

```python
from .models import ChaiVariety, Store
from .forms import ChaiVarietyForm

def chai_store_view(request):
  stores = None
  if request.method == 'POST':
    form = ChaiVarietyForm(request.POST)
    if form.is_valid():
      chai_variety = form.cleaned_data['chai_variety']
      stores = Store.objects.filter(chai_varieties=chai_variety)
  else:
    form = ChaiVarietyForm()

  return render(request, 'chai/chai_stores.html', {'form': form, 'stores': stores})
```
## **Add the template**
**In the existing chai `app`, create a new file called `chai_stores.html `in the` chai `app directory. In this file, add the following code:**

```python
{% extends 'layout.html' %}

{% block content %}
  <h1>Chai Stores</h1>
  <form method="post">
    {% csrf_token %}
      {{ form.as_p }}
    <button type="submit">Search Stores</button>
  </form>
  {% if stores %}
    <h2>Stores with selected Chai Variety</h2>
    <ul>
      {% for store in stores %}
      <li>{{ store.name }} - {{ store.location }}</li>
      {% endfor %}
    </ul>
  {% endif %}
{% endblock %}
```
## **Update the urls**
**In the `urls.py` file, add the following code to the urlpatterns list:**

```python
path('chai_stores/', views.chai_store_view, name='chai_stores'),
```
## **Run the server**
**In the terminal, navigate to the `chai `directory and run the following command:

```bash
python manage.py runserver
```
**That’s it! You have successfully created a form that allows users to search for stores that have a specific chai variety. You can now add more functionality to the form and the view to make it more useful.**

# **I learn Django from chai aur code . [Chai aur code](https://youtu.be/j6szNSzw4BU?si=1r25o2IC7mwRtb3y)**






























































































