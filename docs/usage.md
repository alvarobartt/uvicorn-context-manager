# 👨🏻‍💻 Usage

## ⚡️ With `fastapi`

As mentioned before, the context manager as `uvicorn`, lets you deploy any
ASGI application. Since `fastapi` is one of the most used Python frameworks for 
web development according to a JetBrains survey, see https://twitter.com/tiangolo/status/1624002347776065538.

So on, we think it's useful to showcase how to use `uvicorn_context_manager` with
`fastapi`.

```bash
pip install fastapi
```

Once installed, you can deploy your ASGI application in a Python context manager as:

```python
from fastapi import FastAPI
from uvicorn_context_manager import UvicornContextManager

api = FastAPI()
with UvicornContextManager(api) as server:
    ...
```
