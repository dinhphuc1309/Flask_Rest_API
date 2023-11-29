# Flask_Rest_API

## Step to setup for firt run

Step 1: Create virtual environment

### macOS/Linux:

```sh
python3 -m venv .venv
```

### Windows:

```sh
py -3 -m venv .venv
```

Step 2: Activate the virtual environment

```sh
. .venv/bin/activate
```

### Windows:

```sh
.venv\Scripts\activate
```

Step 3: Install libraries and dependencies

```sh
pip install -r requirements.txt
```

Step 4: Create file .env in config folder ex: development.env include:

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

FLASK_ENV: environment file name.

FLASK_DEBUG: 1 Activate debug mode || 0 Turn off debugging mode.

```sh
export FLASK_APP=run.py && export FLASK_ENV=development && export FLASK_DEBUG=1 && flask run
```
