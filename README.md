# Flask_Rest_API

Project using python version 3.12

## Step to setup for firt run

If installed "pipenv" should be run this command first to use the correct python version of the project

```sh
pipenv shell
```

### Step 1: Create virtual environment

#### macOS/Linux:

```sh
python3 -m venv .venv
```

#### Windows:

```sh
py -3 -m venv .venv
```

### Step 2: Activate the virtual environment

#### macOS/Linux:

```sh
. .venv/bin/activate
```

#### Windows:

```sh
.venv\Scripts\activate
```

### Step 3: Install all libraries and dependencies for project

#### Installed pipenv

Install dependencies from Pipfile

```sh
pipenv install
```

#### Not install pipenv

Install dependencies from requirements.txt

```sh
pip install -r requirements.txt
```

### Step 4: Create file .env in config folder ex: development.env include

```sh
FLASK_ENV=development
SECRET_KEY=yoursecretkey
DATABASE_USER=username
DATABASE_PASSWORD=password
DATABASE_HOST=localhost
DATABASE_PORT=3306
DATABASE_NAME=databasename
```

## Run

FLASK_RUN_PORT: Server port will run

FLASK_ENV: environment file name.

FLASK_DEBUG: 1 Activate debug mode || 0 Turn off debugging mode.

```sh
export FLASK_RUN_PORT=5001 && export FLASK_APP=run.py && export FLASK_ENV=development && export FLASK_DEBUG=1 && flask run
```

## Install dependencies

#### Installed pipenv

```sh
pipenv install <package_name>
```

#### Not install pipenv

```sh
pip install <package_name>
```

## Update requirements.txt

#### Installed pipenv

```sh
pipenv requirements
```

#### Not install pipenv

```sh
pip freeze > requirements.txt
```
