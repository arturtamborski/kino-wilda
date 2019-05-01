help: # show help and quit
	@egrep '^\w' $(lastword $(MAKEFILE_LIST)) \
		| sed 's/:.*#/#/g' | awk -F'#' '{printf("%20s -%s\n", $$1, $$2)}'
.PHONY: help

all: prepare # run all targets required to start application locally
	@echo Done
.PHONY: all

prepare: # create virtualenv, install requirements
	-rm -r .venv
	python3 -m venv .venv
	source .venv/bin/activate && python3 -m pip install --upgrade pip
	source .venv/bin/activate && python3 -m pip install -r requirements.txt
.PHONY: prepare

run: # run the application locally
	source .venv/bin/activate && python3 manage.py runserver
.PHONY: run

remove-migrations: # remove all migrations
	-find . -path "*/migrations/*.py" -not -name "__init__.py" -delete
	-find . -path "*/migrations/*.pyc" -delete
.PHONY: remove-migrations

migrations: # make migrations and and migrate them
	python manage.py makemigrations
	python manage.py migrate
.PHONY: migrations

remove-database: # remove local database
	-rm local.sqlite3
.PHONY: remove-database
