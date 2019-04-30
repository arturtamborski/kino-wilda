all: prepare # run all targets required to start application locally
	@echo Done
.PHONY: all

help: # show help
	@grep "\w+:" makefile
.PHONY: help

prepare: # create virtualenv, install requirements
	-rm -r .venv
	python3 -m venv .venv
	source .venv/bin/activate && python3 -m pip install --upgrade pip
	source .venv/bin/activate && python3 -m pip install -r requirements.txt
.PHONY: prepare

# target: run    - run the application locally
run:
	source .venv/bin/activate && python3 manage.py runserver
.PHONY: run

clear-migrations:
	-find . -path "*/migrations/*.py" -not -name "__init__.py" -delete
	-find . -path "*/migrations/*.pyc" -delete
.PHONY: clear-migrations

make-migrations:
	python manage.py makemigrations
	python manage.py migrate
.PHONY: make-migrations

clear-database:
	-rm local.sqlite3
.PHONY: clear-database
