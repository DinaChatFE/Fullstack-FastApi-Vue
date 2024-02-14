from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
import api
import uvicorn
from core import settings
from core import tags_metadata
from fastapi import FastAPI
from pony.orm import db_session
from starlette.requests import Request
from test_log import test_api
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.httpsredirect import HTTPSRedirectMiddleware

def create_app():
    app = FastAPI(title='Event News project',
                  debug=True,
                  openapi_tags=tags_metadata,
                  version=0.1)

    @app.on_event("startup")
    def _enter_session():
        session = db_session()
        Request.pony_session = session
        session.__enter__()

    @app.on_event("shutdown")
    async def _exit_session(exception):
        session = getattr(Request, 'pony_session', None)
        if session is not None:
            session.__exit__(exc=exception)

    # Register CORS
    origins = ['*']

    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    app.include_router(router=api.auth_router)
    app.include_router(router=api.event_router)
    app.include_router(router=api.register_route)
    app.include_router(router=api.news_router)
    app.include_router(router=test_api.route)
    app.include_router(router=api.category_route)

    @app.get('/home')
    def home():
        return "welcome"

    # register static site include image etc....
    app.mount("/static", StaticFiles(directory="static"), name="static")
    return app


app = create_app()
# if the start program start with main.py it will compile these code below
if __name__ == "__main__":
    uvicorn.run(app, host=settings.SERVER_HOST, port=settings.SERVER_PORT, reload=True)
