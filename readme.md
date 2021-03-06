Simple Movie App
----------------

This is a demo of a simple REST API written in `Python` with `Django` and `djangorestframework`.
It's not too advanced but serves as a good template / starting point for such applications.

https://kino-wilda.herokuapp.com/


### List of endpoints

- `/top`
    - `GET`
      - `REQUEST`
        - fetches list of all movies present in DB ranking based on a number of comments added in specified time range.
      - `RESPONSE`
        - returns list of top movies with their id, position and number of comments in provided timespan.


- `/movies`
    - `GET`
      - `REQUEST`
        - empty
      - `RESPONSE`
        - returns list of all movies already present in application DB.
        - offers additional sorting and filtering trough parameters.
    - `POST`
      - `REQUEST`
        - accepts movie title, fetches more info and saves to local DB.
      - `RESPONSE`
        - all info about given title


- `/comments`
    - `GET`
      - `REQUEST`
        - fetches list of all comments present in DB.
      - `RESPONSE`
        - returns list of all comments already present in application DB.
        - offers additional filtering trough parameters.
    - `POST`
      - `REQUEST`
        - contains ID of movie already present in DB and the comment text.
      - `RESPONSE`
        - returns the comment.


### Examples


### How to get help?

```bash
make

# or...
make help
```


### How to run it?

```bash
make all
```
