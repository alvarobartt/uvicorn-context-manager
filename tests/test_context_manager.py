import httpx
import pytest
from fastapi import FastAPI

from uvicorn_context_manager import UvicornContextManager


@pytest.mark.usefixtures("asgi_app")
def test_uvicorn_context_manager(asgi_app: FastAPI) -> None:
    with UvicornContextManager(app=asgi_app) as server:
        assert server.started
        assert server.should_exit is False
        assert server.config.app == asgi_app

        response = httpx.get(
            url=f"http://{server.config.host}:{server.config.port}/docs"
        )
        assert response.status_code == 200
