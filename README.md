# pollsite
Sample Django Pollsite app
############################################

INPROGRESS To Be Completed
############################################


Django Tutorial
============

Helper Documentation for Django
https://docs.djangoproject.com/en/1.10/ref/django-admin/

Authentication Docs
==================
https://docs.djangoproject.com/en/1.11/topics/auth/default/

PollSite Docs
==============
https://docs.djangoproject.com/en/1.11/intro/tutorial01/


Authentication Tutorial
=======================
https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Authentication


These files are:
* The outer mysite/ root directory is just a container for your project. Its name doesn’t matter to Django; you can rename it to anything you like.
* manage.py: A command-line utility that lets you interact with this Django project in various ways. You can read all the details about manage.py in django-admin and manage.py.
* The inner mysite/ directory is the actual Python package for your project. Its name is the Python package name you’ll need to use to import anything inside it (e.g. mysite.urls).
* mysite/__init__.py: An empty file that tells Python that this directory should be considered a Python package. If you’re a Python beginner, read more about packages in the official Python docs.
* mysite/settings.py: Settings/configuration for this Django project. Django settings will tell you all about how settings work.
* mysite/urls.py: The URL declarations for this Django project; a “table of contents” of your Django-powered site. You can read more about URLs in URL dispatcher.
* mysite/wsgi.py: An entry-point for WSGI-compatible web servers to serve your project. See How to deploy with WSGI for more details.


Creating a python virtual environment:
Setup Instructions
1. python3 -m venv myvenv
2. source gwcenv/bin/activate
3. pip install django~=1.10.0
4. python3 -m django --version
5. django-admin startproject pollsite
6. ls -lR pollapp
7. cd pollsite/
8. python3 manage.py startapp pollapp
9. python3 manage.py runserver
10. python3 manage.py migrate
11. Update mysite/settings.py
    1. Add the poll app in settings.py
    2. Update timezone to match US-Pacific or standard timezone
12. Update <webapp>/models.py to add the model pertinent to your web app. E.g
	from django.db import models
	class Question(models.Model):
   		 question_text = models.CharField(max_length=200)
   		 pub_date = models.DateTimeField('date published')
	class Choice(models.Model):
   		 question = models.ForeignKey(Question, on_delete=models.CASCADE)
    		choice_text = models.CharField(max_length=200)
    		votes = models.IntegerField(default=0)
13. Update mysite/settings.py to add the web app to installed apps
    1. ‘<webapp>.apps.<function name>',
14. Convert the db changes into a migration and store the migrations
    1. python3 manage.py makemigrations pollapp (once poll app is added to installed apps in settings.py)
    2. Output is as follows:
        1. Migrations for 'pollapp':
        2. pollapp/migrations/0001_initial.py:
        3. - Create model Choice
        4.  - Create model Question
        5.  - Add field question to choice
15. To view(not run) the SQL commands the migration will execute try the following:
    1. python manage.py sqlmigrate pollapp 0001
16. Finally run the migration itself:
    1. python manage.py migrate
17. Configure the default root “127.0.0.1:8000” to go to your web app:
    1. Inside your webapp/urls.py add the following line
        1. url(r'^', include('pollapp.urls')),
        2. url(r'^pollapp/', include('pollapp.urls')),
        3. url(r'^admin/', admin.site.urls),
18. Create a super user to login to the admin interface:
    1.  python manage.py createsuperuser
    2. Specify username, password and email address
19. Update <webapp>admin.py to register your web app models with the admin interface
    1. from .models import Question
    2. admin.site.register(Question)
20. Adding new views to Django
    1. in <webapp>/urls.py
		# ex: /polls/
   			 url(r'^$', views.index, name='index'),
    		# ex: /polls/5/
    			url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
    		# ex: /polls/5/results/
    			url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name='results'),
    		# ex: /polls/5/vote/
   			 url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
		]
		2. in <webapp>/views.py
			def detail(request, question_id):
   		 		return HttpResponse("You're looking at question %s." % question_id)

			def results(request, question_id):
    				response = "You're looking at the results of question %s."
    				return HttpResponse(response % question_id)

			def vote(request, question_id):
   				 return HttpResponse("You're voting on question %s." % question_id)
 	21. Add your own templates
		1. Create a directory under <webapp>/ 
			mkdir templates/<webapp>
		2. Add your index.html and other resources as if it were your web app root here i believe. 
	

