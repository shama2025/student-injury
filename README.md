# student-injury [![code style: prettier](https://img.shields.io/badge/code_style-prettier-ff69b4.svg?style=flat-square)](https://github.com/prettier/prettier) [![Code Style black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

## Overview

The purpose of this project is to practice constructing a frontend and backend of a site and to simplify the process that student athletes take when filling out "Patient Outcome Reported Measures" forms

![Patient Outcome Reported Measures example](./DashExample.png)

## Locally Host in Deployment environment

### Local Machine setup/install

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

### Run Application

Run the angular application

```sh
ng serve
```

Run the flask backend

```sh
python -m flask run
```

Run MySql Server (Windows)

-   Navigate to the Services application
-   Scroll down to MySql and click start

Click locally hosted application link

http://localhost:4200/
