# REST API WITH DJANGO EXAMPLE
Some example Django's projects to desmonstrate the usage.

# Requirements

* Python (2.7, 3.4, 3.5, 3.6)
* Django (1.10, 1.11, 2.0)

# Installation

Install using `pip`...

    pip install djangorestframework

Add `'rest_framework'` to your `INSTALLED_APPS` setting.

    INSTALLED_APPS = (
        ...
        'rest_framework',
    )


## How to use:
From command line: 
```
$ cd projectfolder
$ python manage.py runserver portnumber
```
Change `projectfolder` and `portnumber` to the existing project and the wanted ip port. The application will be running in: http://127.0.0.1:portnumber/

## Project: 

### [Create a poll](https://github.com/Aleadinglight/DjangoRestAPI/tree/master/polls_vote)
Create a poll for voting purpose. Many-to-one relationships (ForeignKey).

### [Company](https://github.com/Aleadinglight/DjangoRestAPI/tree/master/company)
Users and groups in a company. Serializer is implemented. 
The app folder **group_user** is moved into inner project directory. The reason for this is the ```company/urls.py``` need to call the ```company/group_user/views.py``` and when moving **group_user** into inner **company** we can simply call ```from company.group_user import views```.


