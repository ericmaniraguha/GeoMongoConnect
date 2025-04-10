# Setting Up a Django Project

This guide walks you through the process of setting up a Django project using Windows PowerShell. Follow these steps to get started quickly with Django development.

## Prerequisites

- Python 3.8+ should be installed on your system.
- PowerShell should be available on your Windows machine.
- `pip` should be installed with Python (it usually is by default).

---

## Step 1: Create a Virtual Environment

Start by creating a virtual environment to isolate your project dependencies.

```powershell
python -m venv geo_env

```
## Step 2: Activate the Virtual Environment
Activate the virtual environment to start using it for installing dependencies.

```powershell
geo_env\Scripts\activate

```
Your prompt will change to indicate that you're now inside the virtual environment` (e.g., (geo_env))`.

## Step 3: Install Django
With the virtual environment activated, install Django by running: `pip install Django
`
Django will be downloaded and installed along with its dependencies.

## Step 4: Start a New Django Project
Now that Django is installed, you can create a new Django project. In this example, we’ll name it `geo_data_pipeline`.

```powershell
django-admin startproject geo_data_pipeline
```
This command creates a directory called `geo_data_pipeline` with the necessary files for the project.

## Step 5: Navigate to the Project Directory
Change into the project directory:
```powershell
cd .\geo_data_pipeline\
```

## Step 6: Run the Development Server
Start the Django development server to ensure everything is set up correctly:

```powershell

python .\manage.py runserver
```
The server will start, and you should see output like this:


```pgsql
Starting development server at `http://127.0.0.1:8000/`
Quit the `server with` CTRL-BREAK.

```

Open a browser and visit `http://127.0.0.1:8000/ `to view the default Django welcome page.

## Step 7: Apply Migrations
You might see a warning about unapplied migrations. To apply them, run:
```powershell
python manage.py migrate
```
This ensures your database schema is up to date with the default Django apps (like `admin`, `auth`, `etc`.).

## Step 8: Start a New Django App
You can now start creating Django apps inside your project. For example, to create an app named `app`, run:

```powershell
python .\manage.py startapp app
```
This creates an `app` directory where you can define models, views, templates, and other components for your Django application.

## Additional Notes
- Development Server: The Django development server is only suitable for development and debugging. For production, consider using a WSGI or ASGI server (e.g., Gunicorn, Daphne).

- Favicon Warning: You might encounter a 404 error for `favicon.ico` in the browser, which is normal and can be ignored.


## Conclusion
You’ve successfully set up a Django project and started a development server. You can now begin building your web application by adding models, views, and templates within your app directory.

```vbnet

This `README.md` provides step-by-step instructions to set up a Django project on Windows using PowerShell. Let me know if you need further clarification!

```