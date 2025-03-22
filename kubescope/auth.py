import os
import secrets
from typing import Annotated

from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBasic, HTTPBasicCredentials

USERNAME = os.environ.get("USERNAME")
PASSWORD = os.environ.get("PASSWORD")

if USERNAME and PASSWORD:
    security = HTTPBasic()

    def authenticate(credentials: Annotated[HTTPBasicCredentials, Depends(security)]) -> bool:
        correct_username = secrets.compare_digest(credentials.username, USERNAME)
        correct_password = secrets.compare_digest(credentials.password, PASSWORD)
        if not (correct_username and correct_password):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Incorrect username or password",
                headers={"WWW-Authenticate": "Basic"},
            )
        return True

else:

    def authenticate() -> bool:
        return True
