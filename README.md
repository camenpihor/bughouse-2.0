# Repository for thebughouse.io

## Instructions for running the website locally

1. Clone the bughouse repository to a local directory and navigate into it
    1. Run `git clone <https://github.com/camenpihor/bughouse-2.0.git>`
    2. Run `cd bughouse-2.0`

2. Create a .env file in the repository's root

      1. Run `touch .env`
      2. Copy the following to your `.env` file, substituting desired values for everything within `< >`

      ```bash
      SECRET_KEY="<ask camenpihor to send you the secret key>"
      DB_NAME="<name of postgres database>"
      DB_USER="<username>"
      DB_PASSWORD="<password>"
      DB_HOST="<host of database `127.0.0.1` if localhost>"
      DB_PORT="<port of database `5432` if default>"
      DB_SCHEMA="<name of schema for tables to add>"
      DB_LOCAL_URL="postgresql://${DB_USER_PASSWORD}@${DB_HOST}:${DB_PORT}/${DB_NAME}"
      ```

      1. Run `set -o allexport; source .env; set + allexport;`

3. Set up a local PostgreSQL database
    1. Run `./scripts/setup_local_db`

4. Set up the virtual environment and activate
    1. Run `tox -r --notest`
    2. Run `source ".tox/py36/bin/activate"`

5. Run the server (see [here](https://docs.djangoproject.com/en/2.0/ref/django-admin/#runserver]) for more information)
    1. Run `./manage.py runserver 127.0.0.1:8000`
    2. In your browser navigate to <http://127.0.0.1:8000/>

## Current development step

1. ~~Set up django project~~
2. ~~Set up posgres database~~
3. ~~Add instructions to run locally~~
4. ~~Set up django app~~
5. ~~Set up sitemap~~
6. Initial base html
