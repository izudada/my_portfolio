# A Completed HNG Internship Stage 2 Task 

Deployed to:

-    Heroku live project. Link at [here](https://izudada.herokuapp.com/)

## Task 1

To run Task 1 (Which is to print my name):
```sh
$ python print_name.py
```

## Setup For My Portfolio (Task 2)

The first thing to do is to clone the repository:

```sh
$ git clone https://github.com/izudada/my_portfolio.git
```

Create a virtual environment to install dependencies and activate it use the link below first to install pipenv:

https://pypi.org/project/pipenv/

then to activate a virtual enviroment:

```sh
$ pipenv shell
```

Then install the dependencies:

```sh
(env)$ pip install -r requirements.txt
```
Note the `(folder_name)` in front of the prompt. This indicates that this terminal
session operates in a virtual environment set up by `pipenv` using your folder or root directory name.

Use migrate command to effect database model:
```sh
(folder_name)$ python manage.py migrate
```

Once `pip` has finished downloading the dependencies:
```sh
(folder_name)$ python manage.py runserver
```
And navigate to `http://127.0.0.1:8000/`.