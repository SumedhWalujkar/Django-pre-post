[![Build Status](https://travis-ci.org/CSnap/Django-pre-post.svg?branch=master)](https://travis-ci.org/CSnap/Django-pre-post)

# Django-pre-post
This Django app provides the ability to create pre-post questions and answers. It was developed by the CSDTs team at RPI to embed pre-post tests for students in their website and to ease data collection.

# Installation & Integration

## Download and install:
Either use pip in terminal: `pip install django_pre_post`
Or add django_pre_post to your requirements / libraries file and run `pip install -r requirements.txt`

## Add the application to your site:
Include it in settings.py
```
INSTALLED_APPS = (
    ... your apps here ...
    'django_pre_post',
)
```
Include it in URLS.py
```
urlpatterns = [
    ... your pages here...
    url(r'^questionnaire/', include('django_pre_post.urls')),
]
```
# Testing

## Prerequisites
* VirtualBox
  * Linux: sudo apt-get install virtualbox
  * Windows & Mac: https://www.virtualbox.org/wiki/Downloads
* Vagrant
  * Linux: sudo apt-get install vagrant
  * Windows & Mac: https://www.vagrantup.com/downloads.html
* Git
  * Linux: sudo apt-get install git
  * Windows & Mac: https://git-scm.com/downloads
    * For windows Make sure C:\Program Files\Git\usr\bin [is in your path variable](http://www.computerhope.com/issues/ch000549.htm)

## Setup
```shell
git clone https://github.com/CSnap/Django-pre-post #get the code
cd Django-pre-post
vagrant up #build the system in a virtual machine
vagrant ssh #enter the virtual machine
cd /vagrant
python manage.py runserver 0.0.0.0:8000  #run the server
```
Navigate to localhost:8002/admin/