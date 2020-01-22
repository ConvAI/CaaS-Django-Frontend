# Django Backend for CaaS

To run this project in your development machine, follow these steps:

1. (optional) Create and activate a [virtualenv](https://virtualenv.pypa.io/) (you may want to use [virtualenvwrapper](http://virtualenvwrapper.readthedocs.org/)).

2. Fork this repo and clone your fork:

    `git clone https://github.com/sclorg/django-ex.git`

3. Install dependencies:

    `pip install -r requirements.txt`

4. Install mysql server and change settings like user, password, port,etc in `main_site/settings.py`

5. Create a development database:

    `./manage.py migrate`

6. If everything is alright, you should be able to start the Django development server:

    `./manage.py runserver`

7. Open your browser and go to http://127.0.0.1:8000
