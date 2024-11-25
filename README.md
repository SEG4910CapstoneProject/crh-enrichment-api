# enrichment-api

This service hosts and creates an api to access the ML Models

## Environment Variables

### Database
| Environment Variable | Description                                                 |
|----------------------|-------------------------------------------------------------|
| ENRICHMENT_HOST      | The host of this service                                    |
| ENRICHMENT_PORT      | The port on which to host this service                      |
| MONGO_HOST           | The hostname of the mongodb database                        |
| MONGO_PORT           | The port of the mongodb database                            |
| MONGO_USERNAME       | The username for access. Should container write permissions |
| MONGO_PASSWORD       | Mongodb password for authentication                         |
| MONGO_DB_NAME        | Mongodb Database name                                       |
| MONGO_ML_COLLECTION  | The collection on the mongo db to find the ml model         |

## Running Unit Tests
To run unit tests execute the below command. Must be executed on root of the project as working directory
```commandline
python -m unittest discover
```
## Running the Service
To run the service execute the below command  Must be executed on root of the project as working directory.
```commandline
python ./__main__.py
```
