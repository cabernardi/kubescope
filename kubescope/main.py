import os
from typing import Annotated, List

from fastapi import Depends, FastAPI, HTTPException, Query, status

import kubescope.auth as auth
import kubescope.db.database as db
from kubescope.config import config_file
from kubescope.exceptions import DatabaseNotConfigured

app = FastAPI()


@app.get("/health", include_in_schema=False)
def health():
    return {"status": "healthy"}


@app.get("/v1/protected", response_model=dict)
def protected_route(auth: Annotated[bool, Depends(auth.authenticate)]):
    """A protected route that requires authentication

    Args:
        auth (Annotated[bool, Depends): Authentication dependency

    Raises:
        HTTPException: If authentication fails

    Returns:
        dict: A message indicating the user is authenticated
    """
    return {"message": "You are authenticated!"}


@app.get("/v1/env/{env}")
def get_env(env: str):
    """Return the value of an environment variable set in the container

    Args:
        env (str): Environment variable name to read from

    Raises:
        HTTPException: If the environment variable is not found

    Returns:
        dict: Environment variable name and value
    """
    env_data = os.getenv(env, None)
    if not env_data:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Environment variable {env} not found")

    return {"variable": env, "value": os.getenv(env, None)}


@app.get("/v1/config/color", response_model=dict)
def get_color_config():
    """Read and return the content of the color configuration

    Raises:
        HTTPException: Unexpected error
        HTTPException: Unexpected error reading the config file

    Returns:
        dict: Dict containing the color configuration from the config file
    """
    try:
        data = {"color": config_file["general"]["color"]}
        return data
    except KeyError:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Configuration key 'general.color' not found in config file"
        )
    except Exception as e:
        print(e)
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))


@app.get("/v1/txt", response_model=str)
def get_txt_file(
    path: Annotated[str, Query(description="TXT file path", regex=r"^\/.*\.(?:txt)$")],
):
    """Read and return the content of a TXT file

    Args:
        auth (Annotated[bool, Depends): Authentication dependency
        path (Annotated[str, Query): Path to the YAML file to read

    Raises:
        HTTPException: File is not found on the container
        HTTPException: Error reading the file

    Returns:
        str: Content of the TXT file
    """
    if not os.path.exists(path):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"File {path} not found")

    try:
        with open(path, "r") as f:
            data = f.read()

        return data
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))


@app.post("/v1/db/init", response_model=dict)
def init_db_connection():
    """Initialize the database, if it isn't"""
    try:
        db.create_db()
        return {"status": "Database initialized"}
    except DatabaseNotConfigured as e:
        raise HTTPException(status_code=status.HTTP_501_NOT_IMPLEMENTED, detail=str(e))
    except Exception as e:
        print(e)
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Failed to initialize database")


@app.post("/v1/db/add", response_model=db.Person)
def add_to_db(name: str = Query(description="Name of the person to add")):
    """Add a person to the database"""
    try:
        return db.add_person(name)
    except DatabaseNotConfigured as e:
        raise HTTPException(status_code=status.HTTP_501_NOT_IMPLEMENTED, detail=str(e))
    except Exception as e:
        print(e)
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Failed to connect to database")


@app.get("/v1/db/get-all", response_model=List[db.Person])
def get_from_db():
    """Get all people from the database"""
    try:
        people = db.get_people()
        print(people)
        return people
    except DatabaseNotConfigured as e:
        raise HTTPException(status_code=status.HTTP_501_NOT_IMPLEMENTED, detail=str(e))
    except Exception as e:
        print(e)
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Failed to connect to database")
