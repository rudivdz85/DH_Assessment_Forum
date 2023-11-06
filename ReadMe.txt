# Forum Project

This is a simple forum API built with Django and Django REST framework. It allows users to create posts, retrieve posts, and like posts. Admin users can delete posts via the Django admin interface.

## Prerequisites

Before you begin, ensure you have met the following requirements:
* You have installed Python 3.7 or higher.
* You have installed Django and Django REST framework.

## Note
For ease of use purposes, AllowedHosts have been set to All (*), in production this would not be the case.

## Installing Forum Project

To install the Forum Project, follow these steps:

Linux and macOS:

{Using Bash}
git clone https://github.com/yourusername/forum_project.git
cd forum_project
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
-------------------------------------

Windows:

{Using Bash}
git clone https://github.com/yourusername/forum_project.git
cd forum_project
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
-------------------------------------

Using Forum Project
To use Forum Project, follow these steps:

{Using Bash}

python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser  # Follow the prompts to create an admin user
python manage.py runserver

Now, navigate to http://127.0.0.1:8000/admin/ in your web browser to open the Django admin site and log in with the superuser credentials you created.


Endpoints:

List all posts:

Endpoint: /posts/
Method: GET
Access: Public

Show details for a specific post:

Endpoint: /posts/<post_id>/
Method: POST
Access: Authenticated Users Only

Create a new post:

Endpoint: /posts/
Method: POST
Access: Authenticated Users Only

Like a post:

Endpoint: /posts/<post_id>/like/ (replace <post_id> with the ID of the post)
Method: POST
Access: Authenticated Users Only

List all likes on a specific post:

Endpoint: /posts/<post_id>/likes/
Method: GET
Access: Public

List all users:

Endpoint: /users/
Method: GET
Access: Admin Users Only



When using these endpoints, ensure that you replace <post_id> with the actual numerical ID of the post you want to like for the third endpoint. For the POST requests, authenticated users need to provide their credentials, such as a token, in the request's Authorization header.