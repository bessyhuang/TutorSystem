# TutorSystem
A conversation collection system build with Django framework and integrate Google Dialogflow.

#### _App: Main_
  * index.html
  
#### _App: Account_
  * register
  * login
  * logout
  
#### _App: Question_
  * qu_listSelect
    > First, Adding the "Question title" and Uploading the "Question data" in Website backend.
    >
    > So that, we can select the "Question title" and get the corresponding data.
    
  * qu_downloadData
  
    > According to "Question title", we can Download the corresponding data.
  
#### _App: Step1_
  * qu_step1
  
    > Integrate Dialogflow into Website and Write messages into database.
  
#### _App: Upload_
  * file_upload_view
  
    > Students upload their file by using this Website Interface.
  
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
$ python manage.py makemigrations <app_name>
$ python manage.py migrate <app_name>
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
