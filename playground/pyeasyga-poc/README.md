In order to run the server run the following command inside the pyeasyga-poc directory

```
$ uvicorn api:app --reload
```

Description:

```
The command uvicorn api:app refers to:

api: the file api.py (the Python "module").
app: the object created inside of api.py with the line app = FastAPI().
--reload: make the server restart after code changes. Only do this for development.
```
