import os
from typing import Annotated

import yaml
from fastapi import Depends, FastAPI, HTTPException, Query, status

import kubescope.auth as auth

app = FastAPI()


@app.get("/health")
def health():
    return {"status": "healthy"}


@app.get("/v1/env/{env}")
def get_env(env: str, auth: Annotated[bool, Depends(auth.authenticate)]):
    env_data = os.getenv(env, None)
    if not env_data:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Environment variable {env} not found")

    return {"variable": env, "value": os.getenv(env, None)}


@app.get("/v1/yaml")
def get_yaml(
    path: Annotated[str, Query(description="YAML file path", regex=r"^\/.*\.(?:yaml|yml)$")],
    auth: Annotated[bool, Depends(auth.authenticate)],
):
    if not os.path.exists(path):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"File {path} not found")

    try:
        with open(path) as f:
            data = yaml.safe_load(f)

        return data
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))


@app.get("/v1/configmap/{namespace}/{name}")
def get_configmap_data(namespace: str, name: str, auth: Annotated[bool, Depends(auth.authenticate)]):
    raise HTTPException(status_code=status.HTTP_501_NOT_IMPLEMENTED, detail="Not implemented yet")
