# TutorSystem
A conversation collection system build with Django framework and integrate Google Dialogflow.

## Creating a virtual environment

```
$ python3 -m venv <your_venv>
```

## Activate your virtual environment

* Windows

  `
  $ .\<your_venv>\Scripts\activate
  `

* Linux / macOS

  `
  $ source ./<your_venv>/bin/activate
  `

## Install packages

```
$ pip install -r requirements.txt
```

## Synchronize all models onto database

```
$ python manage.py makemigrations
$ python manage.py migrate
```

## Create superuser

```
$ python manage.py createsuperuser
```

## Run TutorSystem

```
$ cd TutorSystem
$ python manage.py runserver
```

## Go to http://127.0.0.1:8000/admin

* Adding questions (including questions' title, content and files)
