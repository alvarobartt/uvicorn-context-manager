import pytest
from fastapi import FastAPI


@pytest.fixture
def asgi_app() -> FastAPI:
    return FastAPI()
