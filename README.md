# Menu app
Send text messages to users containing menus of Chase and Lenoir dining halls
Utilizes React and Django frameworks

## How to run:
### 1: Activate virtual environment:
venv/Scripts/activate (Windows)
source bin/activate (Mac)
### 2: Install libraries:
python -m pip install -r requirements.txt  
npm install axios
### 3: Run Django project:
python manage.py runserver
### 4: Run React project:
npm start

The React application sends an HTTP POST request to the Django application with the inputted phone number as the request data. The Django application, using a REST API, receives the request and uses the data to create a new phone number record in the database.

The Django application uses the Django REST framework to handle the incoming HTTP requests and to serialize and deserialize data between JSON format (used in the HTTP requests and responses) and Python objects (used in the Django code). The PhoneNumberSerializer class is used to validate and deserialize the incoming data, and to serialize the outgoing data. The PhoneNumberViewSet class is used to handle the incoming HTTP requests and to perform the appropriate actions, such as creating a new phone number record in the database.

Superuser PW: 1152

Future:
Maybe make scrape a sub-function of main, so it doesn't open a new driver 6 times
Add CSS
Verify input to be phone number format