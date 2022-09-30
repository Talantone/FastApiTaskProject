from pydantic import BaseModel
from starlette.config import Config

config = Config(".env")

DATABASE_URL = config("DATABASE_URL", cast=str, default="mongodb://localhost:27017/")
DATABASE_NAME = config("DATABASE_NAME", cast=str, default="mongodb")
APP_ADDR = config("APP_ADDR", cast=str, default="127.0.0.1")
APP_PORT = config("APP_PORT", cast=int, default=8000)
SALT = config("SALT", cast=str, default="")

class JWTSettings(BaseModel):
    authjwt_secret_key = config("JWT_SECRET_KEY", cast=str, default="secret")


class EmailSettings(BaseModel):
    root_url = config("ROOT_URL", cast=str, default="")
    mail_console = config("MAIL_CONSOLE", cast=bool, default=False)
    mail_username = config("MAIL_USERNAME", cast=str, default="")
    mail_password = config("MAIL_PASSWORD", cast=str, default="")
    mail_from = config("MAIL_FROM", cast=str, default="noreply@myserver.io")
    mail_port = config("MAIL_PORT", cast=int, default=587)
    mail_server = config("MAIL_SERVER", cast=str, default="smtp.myserver.io")


EmailConfig = EmailSettings()
JWTConfig = JWTSettings()