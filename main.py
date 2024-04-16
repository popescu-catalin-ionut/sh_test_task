"""
Main.py

This file is intended to be a main file where you can find all the code
"""

import uvicorn
from fastapi import FastAPI, Depends
from fastapi.security import OAuth2PasswordRequestForm

from v1.authentication import oauth2_scheme
from common.settings import documentation
from v1.views import get_access_token, get_user

app = FastAPI(
    title=documentation.title,
    description=documentation.description,
    summary=documentation.summary,
    version=documentation.version,
    terms_of_service=documentation.terms_of_service,
    contact=documentation.contact,
    license_info=documentation.license_info
)


# Endpoint to get a token
@app.post("/v1/auth")
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    access_token = get_access_token(form_data=form_data)
    return {"access_token": access_token, "token_type": "bearer"}


# Protected endpoint
@app.get("/v1/users/")
async def read_users(token: str = Depends(oauth2_scheme)):
    user = get_user(token=token)
    return user


if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8080,
        log_level="info",
        reload=True
    )
