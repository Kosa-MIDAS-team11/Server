from fastapi import FastAPI

from app.core.user import user_router
from app.core.admin import admin_router
from app.core.employee import employee_router
from app.core.department import department_router

from fastapi.middleware.cors import CORSMiddleware


def create_app() -> FastAPI:
    app = FastAPI()

    app.include_router(user_router)
    app.include_router(admin_router)
    app.include_router(employee_router)
    app.include_router(department_router)

    app.add_middleware(
        CORSMiddleware,
        allow_origins=['http://localhost:8000', 'https://3a8e-211-36-133-106.jp.ngrok.io'],
        allow_credentials=True,
        allow_methods=['*'],
        allow_headers=["*"],
    )

    return app
