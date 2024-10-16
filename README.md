pip install opencv-python
pip install Pillow
https://github.com/mushfiq1998/video-stream-with-django-opencv/tree/main
pytho -m pip freeze > requirements.txt

http://127.0.0.1:8000/swagger/

bash
```
    pip install -r requirements.txt
    python3 -m venv venvpip
    python manage.py startapp task
    pip freeze > requirement.txt
    python manage.py makemigrations
```

bash
```
    python manage.py migrate
    python manage.py showmigrations
    
```

- https://github.com/ageitgey/face_recognition
- https://github.com/Vampboy/Face-Recognition-Login-System
- https://dev.to/unic/add-text-to-your-certificate-image-in-seconds-with-django-and-opencv-5f37
- https://pyimagesearch.com/2015/05/11/creating-a-face-detection-api-with-python-and-opencv-in-just-5-minutes/
- https://github.com/pyplane/django-faceid/blob/main/profiles/views.py

- REF PERWEEK
    - https://github.com/reasonable-productivity/web-back-end
    - https://github.com/reasonable-productivity/web-front-end
    - https://github.com/jaingaurav126?tab=repositories
    - https://github.com/sawardekar/face_recognition_django
    - https://github.com/YaseenMunowwar/Presence.git
    - https://github.com/Divyansh6799/Face-recognition-in-python-django
    - https://www.geeksforgeeks.org/how-to-install-face-recognition-in-python-on-windows/
    - https://gist.github.com/dotja/6da4783e3f1f1e1dd569a116660e9c42
    - https://github.com/RekhuGopal/PythonHacks/blob/main/Django_REST_API/cloudquicklabs/cars/models.py

    

# Reasonable Productivity Back-end

This is an api for the Reasonable Productivity system built with the Django REST Framework.

## Running Locally

1. Clone this repo
1. cd into this repo
1. Create a python virtual environment: `python -m venv venv`
1. Activate virutal environment: `source venv/bin/activate`
1. `pip install -r requirements.txt`
1. `python manage.py runserver`

## Schema

**Task**

* user_id: ForeinKey
* title: required
* description: default=''
* completed: boolean
* due_date: nullable
* created_at
* updated_at

**Tag**

* text: CharField(max_length=25)
* color: CharField(max_length=6)
* *many to many relationship with Task*

**List**

* user_id
* name
* created_at
* updated_at

**ListItem**

* list_id
* text
* created_at
* updated_at

**User**

* email (unique, used for login)
* password

**UserProfile**

* user_id
* first_name
* last_name
* image
* fb_profile
* twitter_profile
* linkedin_profile
* website

**Project**

* user_id
* title
* description
* created_at
* updated_at
* due_date (for version 2)

## API

**/users**

* GET
* POST

**/users/:id**

* GET
* PATCH
* DELETE

**/users/:id/tasks**

* GET
* POST

**/users/:id/tasks/:task_id**

* GET
* PATCH
* DELETE

**/users/:id/lists**

* GET
* POST

**/users/:id/lists/:list_id**

* GET
* PATCH
* DELETE

**/users/:id/lists/:list_id/list-items**

* POST

**/users/:id/list-items/:item_id**

* PATCH
* DELETE

**/tasks**

* GET

**/tasks/:id**

* GET

## Roadmap

### Version 1.0

* Auth endpoints
  * Login
  * Update password, forgot password
* Add searching, sorting, filtering for tasks and lists

### Version 1.1

* Recurring Tasks
  * recurring: Boolean, default=False
  * recurring_time: nullable
  * recurring_frequency: daily, weekly, monthly, yearly
  * recurring_custom: (based off of recurring frequency option, user can choose specific days/weeks, etc.)
* Reminders

### Version 1.2

* Nested & Dependant Tasks
  * Back-end: tasks should be able to be marked as dependant and sub-tasks
  * Front-end: Users can drag tasks to be nested under other tasks, they can also

### Version 1.3

* Calendar View

### Version 1.4

* Contact integration for tasks: Users can sync with contacts

### Version 1.5

* Markdown enabled in task descriptions

### Version 1.6

* Calendar Integrations
