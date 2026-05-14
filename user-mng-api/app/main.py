from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

from app.api.routes.user_routes import router
from app.exceptions.custom_exception import UserNotFoundException


app = FastAPI(
    title="Production Style FastAPI"
)


app.include_router(router)


@app.get("/")
def home():

    return {
        "message": "FastAPI User Management"
    }


@app.exception_handler(UserNotFoundException)
def user_not_found_exception_handler(
    request: Request,
    exc: UserNotFoundException
):

    return JSONResponse(
        status_code=404,
        content={
            "message": str(exc)
        }
    )