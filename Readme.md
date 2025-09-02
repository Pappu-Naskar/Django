                    
# Django Tutorial 

## 🚀 Getting Started

## First download `Django` Extention in your Code editor
## Step 1:

*Create virtual environment for install Django packages an many more. Lets Create virtual environment.....*

**Open code editor terminal**

```bash
python -m venv .venv
```  

**Another Way to Create virtual environment useing uv  package**

- **uv Package**: An extremely fast Python package and project manager, written in Rust.

  **1. Install uv package:**

   Open code editor terminal

    ```bash
    pip install uv
    ```
  **2. To create a virtual environment:**
    ```bash
    uv venv
    ```

**Activate venv environment:**

  - **Open code editor terminal**
      - *For window* 

       ```bash
       source .venv/Scripts/activate
       ```
       - *For Linex/mac:

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

**Go main project folder and click `urls.py` and copy all code**

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

<h1>This is Home Page</h1>
 
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










 




































    
       
    







