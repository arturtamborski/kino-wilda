help: # show help and quit
	@perl -ne '/^([A-Za-z0-9-_]+):.*#\s+(.*)/ && \
		printf "%*s%s\n", 23, $$1, $$2 ? " - $$2" : ""' makefile

.PHONY: help



all: prepare migrations tests run-local # run all targets required to start application locally
	@echo Done

.PHONY: all



prepare: # create virtualenv, install requirements
	-rm -r .venv
	python3 -m venv .venv
	source .venv/bin/activate && python3 -m pip install --upgrade pip
	source .venv/bin/activate && python3 -m pip install -r requirements.txt

.PHONY: prepare



tests: # run all tests
	source .venv/bin/activate && python3 manage.py test

.PHONY: tests



run-local: # run the application locally
	source .venv/bin/activate && python3 manage.py runserver

.PHONY: run-local



remove-local-migrations: # remove all local migrations
	-find ./backend/ -path "*/migrations/*.py" -not -name "__init__.py" -delete
	-find ./backend/ -path "*/migrations/*.pyc" -delete

.PHONY: remove-local-migrations



local-migrations: # make migrations and and migrate them
	source .venv/bin/activate && python3 manage.py makemigrations
	source .venv/bin/activate && python3 manage.py migrate

.PHONY: local-migrations



remove-local-database: # remove local database
	-rm local.sqlite3
.PHONY: remove-local-database
