### Quick overview

This small project is a quick rendition of the Django official documentation introductory
tutorial's first two parts ([part1](https://docs.djangoproject.com/en/4.1/intro/tutorial01/), [part2](https://docs.djangoproject.com/en/4.1/intro/tutorial01/))

### My personal touch

Unlike the original tutorial, the app references companies and employees instead of the questions
and answers of a polls.

In practice, I changed the main app name's to "companies", the simple view part to welcome
you to the "companies" index and also the URL that lead to it to `/companies/`.

However, the main changes were done in the models part.

Companies are referred by their name and their SIRET number (French identication number
for a company at a specific address). Then there are getters to get the SIREN and NIC numbers
which both are components of the SIRET number.

Employees are referred by their first name, last name, date of birth and employer. Employer being
a foreign key from a Company object.

A company and two employees were filled out using the interactive python shell ran with
`manage.py`.

### Other technical details

Most of the original settings are kept as is. The database engine used is SQLite. An
admin account was created with the username `admin` and password `password`.

The SQLite database is included in this repository since it's quite small and for simplicity sake.

The admin page can be accessed at the `/admin/` endpoint.

### Run the project

To run the project, you need python, at least version `3.8` and the `Django` library version `4.1`
Install it with pip by running
```shell
pip install Django==4.1
```

Then to run the project in a local server, place yourself in the project's root directory and run
```shell
python manage.py runserver
```

You then will be able to access the website at URL <http://128.0.0.1:8000/>
