# FootBall Tournament

This is a simple web-based foot ball tournament managing application using Django and HTML.


## Installation Instructions

To install the application on your system follow these steps:

1. Clone this repository
2. Create a virtualenv using `virtualenv -p python3 envname` and install the requirements using `pip install -r requirements.txt`
3. Execute `python manage.py makemigrations` and `python manage.py migrate` to reflect database model instances.
4. Finally execute `python manage.py runserver` to start the server.
5. Navigate to *http://127.0.0.1:8000* on your web browser. And create superuser using register and then login to the platform 
    for further operations such as add teams, team members, assigning match schedules.

