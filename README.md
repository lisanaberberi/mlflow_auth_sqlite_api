# mlflow_auth_sqlite_db
A REST API to query the list of all users and specific permissions they have for experiments and registered Models
Query the basic_auth sqlite database where by default all these info on user management and permissions are stored
Missing /list-all-users from the existing endpoint in mlflow version 2.7.1

####  MLflow Authentication introduces several new API endpoints to manage users and permissions.

## Getting started

Implementing new feature of basic User Authentication in MLFlow.
There are the following python scripts that will serve admins to manage users and permission for specific resources: experiments and registered models.

To run the api execute command:

```python
# Example script of an API cal:
uvicorn main:app --host 0.0.0.0 --port 8000 --reload


```
## Add your files
* [main.py](https://github.com/lisanaberberi/mlflow_auth_sqlite_api/blob/main/main.py): 
Contains all the API endpoints




## Authors and acknowledgment
This work is co-funded by AI4EOSC project that has received funding from the European Union''s Horizon Europe 2022 research and innovation programme under agreement No 101058593

## License
For open source projects, say how it is licensed.
