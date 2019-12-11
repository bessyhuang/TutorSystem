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

## Run TutorSystem

```
$ cd TutorSystem
$ python manage.py runserver
```
