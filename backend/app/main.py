from fastapi import FastAPI
from fastapi.exceptions import HTTPException

from app.api.article import article

from app.core.handle.exception import handle_exception
from app.core.handle.http_exception import handle_http_exception

# App
app = FastAPI()

# Routes
app.include_router(article, prefix="/public/article", tags=["article"])

# Handlers
app.add_exception_handler(Exception, handle_exception)
app.add_exception_handler(HTTPException, handle_http_exception)