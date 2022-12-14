from fastapi import APIRouter, HTTPException, Body, Depends, Response
from pydantic import EmailStr
from core.config import SALT
from core.mail import send_password_reset_email
from core.security import hash_password
from models.user import User, UserOut, UserAuth
from fastapi_jwt_auth import AuthJWT
router = APIRouter(prefix="/register", tags=["Register"])


@router.post("", response_model=UserOut)
async def user_registration(user_auth: UserAuth):
    user = await User.by_email(user_auth.email)
    if user is not None:
        raise HTTPException(409, "User with that email already exists")
    hashed = hash_password(user_auth.password, SALT)
    user = User(email=user_auth.email, password=hashed)
    await user.create()
    return user


@router.post("/forgot-password")
async def forgot_password(email: EmailStr = Body(..., embed=True), auth: AuthJWT = Depends()):
    """Sends password reset email"""
    user = await User.by_email(email)
    token = auth.create_access_token(user.email)
    await send_password_reset_email(email, token)
    return Response(status_code=200)


@router.post("/reset-password/{token}")
async def reset_password(token: str, pw: str, auth: AuthJWT = Depends()):
    """Updates users password with token"""
    auth._token = token
    user = await User.by_email(auth.get_jwt_subject())
    user.password = hash_password(pw, SALT)
    await user.save()
    return Response(status_code=200)
