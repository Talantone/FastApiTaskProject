import uvicorn
from core import jwt
from fastapi import FastAPI
from core.config import APP_ADDR, APP_PORT
from db.base import initiate_database
from routes.auth import router as AuthRouter
from routes.email import router as MailRouter
from routes.register import router as RegisterRouter
from routes.user import router as UserRouter


app = FastAPI(title='taskManagement')
app.include_router(AuthRouter)
app.include_router(MailRouter)
app.include_router(RegisterRouter)
app.include_router(UserRouter)


@app.on_event("startup")
async def startup():
    await initiate_database()


if __name__ == '__main__':
    uvicorn.run("main:app", port=APP_PORT, host=APP_ADDR, reload=True)
