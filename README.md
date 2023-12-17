# student-injury [![code style: prettier](https://img.shields.io/badge/code_style-prettier-ff69b4.svg?style=flat-square)](https://github.com/prettier/prettier) [![Code Style black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black) [![Tests: Ui Tests](https://github.com/shama2025/student-injury/actions/workflows/uiTesting.yml/badge.svg)](https://github.com/shama2025/student-injury/actions/workflows/uiTesting.yml) [![Tests: API Tests](https://github.com/shama2025/student-injury/actions/workflows/apiTesting.yml/badge.svg)](https://github.com/shama2025/student-injury/actions/workflows/apiTesting.yml)

## Locally Host

### Flask API Production Deployment

Clone the repository

```sh
git clone git@github.com:shama2025/student-injury.git
```

Then you will need to create a new virtual environment. Navigate to the project folder and enter the following command.

```sh
python3 -m venv venv
```

Then activate the environment

```sh
source venv/bin/activate
```

Once you have activated your environment, you need to install all the requirements if you haven't already installed them.

```sh
pip install -r requirements.txt
pip install gunicorn
```

Then all that is left is to start the server using gunicorn using the following command

```sh
gunicorn -w 4 -b 0.0.0.0:8000 app:app
```

Once you have run that command you should be able to connect to your server on 0.0.0.0:8000
For further help, refer to the [Gunicorn documentation](https://gunicorn.org/).

### Production Deployment for Angular frontend

Type in this on your local machine

```sh
https://<user_name>.github.io/<project_name>
```
