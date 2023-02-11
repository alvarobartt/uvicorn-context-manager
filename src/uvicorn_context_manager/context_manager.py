import threading
import time
from typing import Any, Dict, List, Union

from uvicorn import Config, Server


class UvicornContextManager(Server):
    def __init__(
        self,
        app: Any,
        uvicorn_config_kwargs: Union[Dict[str, Any], None] = None,
    ) -> None:
        uvicorn_config_kwargs = (
            uvicorn_config_kwargs
            if isinstance(uvicorn_config_kwargs, dict)
            and len(uvicorn_config_kwargs) > 0
            else {
                "host": "127.0.0.1",
                "port": 8080,
                "log_level": "info",
                "loop": "asyncio",
            }
        )
        self.config = Config(
            app=app,
            **uvicorn_config_kwargs,
        )

        super().__init__(config=self.config)
        self.thread = threading.Thread(target=self.run)

    def install_signal_handlers(self) -> None:
        pass

    def __enter__(self) -> "UvicornContextManager":
        self.thread.start()
        while not self.started:
            time.sleep(1e-3)
        return self

    def __exit__(self, *args: List[Any], **kwargs: Dict[str, Any]) -> None:
        self.should_exit = True
        self.thread.join()
