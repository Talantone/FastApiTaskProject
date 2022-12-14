from fastapi import Request
from fastapi.responses import JSONResponse
from fastapi_jwt_auth import AuthJWT
from fastapi_jwt_auth.exceptions import AuthJWTException
from main import app
from core.config import JWTConfig


@AuthJWT.load_config
def get_config():
    """Load AuthJWT settings"""
    return JWTConfig


@app.exception_handler(AuthJWTException)
def jwt_exception_handler(request: Request, exc: AuthJWTException):
    """Returns any authentication failures"""
    return JSONResponse(status_code=exc.status_code, content={"detail": exc.message})
