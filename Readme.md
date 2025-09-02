      Django Project and File Structure


# Django Tutorial 

## 🚀 Getting Started
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
       - For Linex/mac:

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














    
       
    







