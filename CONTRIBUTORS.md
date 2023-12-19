# Contributor

## Host application locally

Clone the repository

```sh
git clone git@github.com:shama2025/student-injury.git
```

Install requirements.txt

```sh
python -m pip install requirements.txt
```

Install [node](https://nodejs.org/en/download/)

Install angular cli

```sh
npm install -g @angular/cli
```

Run the angular application

```sh
ng serve
```

Run the flask backend

```sh
python -m flask run
```

Click locally hosted application link

http://localhost:4200/

## Frontend

The frontend is built using the [Angular Framework](https://angular.io/docs). The frontend consist of a login page, a new account creation page, a page with downloadable pdfs, and a email form to send an email to whoever. It also includes services that help communicate with the backend, which is built using python Flask.

## API

The backend is built using pythons [Flask](https://flask.palletsprojects.com/en/3.0.x/) library. The code is stores in app.py and it features api endpoints for logging in, creating a new account, and sending an email. The backend calls functions in the api_util.py file. In the api_util.py file, there are several functions and a connection to a mysql database that allows for user creation and checking when logging in or creating a new account.

## Running Tests

The test files, built using python and integrated [python playwright](https://playwright.dev/python/docs/intro) for ui and [flask testing](https://flask.palletsprojects.com/en/3.0.x/testing/) for api, test created features.Use the NPM scripts, in this order, to run both the ui and api tests

### Ui testing

1.) ng serve
2.) run ui-test

### Api testing

1.) run api
2.) run api-test
