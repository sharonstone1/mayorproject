# Application description  

The website is divided in two parts: 
- [`frontend`](frontend): The frontend of the application built in Javascript, HTML and CSS. It should be compile with [npm](https://nodejs.org/en/). 
- `backend`: It is the REST API of the restaurant service, it is coded in python around Django and Django rest framework. It also serves the frontend to the user. 

## Setup the backend 

The backend is built around the Django web framework in the python language. To setup it, follow these steps: 
- Install [Python](https://www.python.org/downloads/)
- Create a folder for the virtual environment at the root folder: `mkdir venv`
- Setup the python virtual environment: `python -m venv venv`
- Load the virtual environment: `source venv/Scripts/activate`
- Install requirements: `pip install -r requirements.txt`
- Make database migrations:  `python manage.py makemigrations api`
- Create the database: `python manage.py migrate`
- Load the database fixtures: `python manage.py loaddata db.json`

## Compile the frontend 

The backend is constructed with [Vue.js](https://vuejs.org/) and built with [npm](https://nodejs.org/en/). 
To compile it follow these steps: 
- Install [npm](https://nodejs.org/en/)
- Go into the frontend folder: `cd frontend`
- Install Javascript packages: `npm install`
- Build the application: `npm run build` 

## Start the application 

In the root folder execute the command: `python manage.py runserver`. The Web application is now accessible at 
[http://127.0.0.1:8000/](http://127.0.0.1:8000/).
