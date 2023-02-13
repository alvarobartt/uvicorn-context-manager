# 🚀 Context Manager to run `uvicorn` ASGI applications

`uvicorn_context_manager` is a Python package that exposes a class named
`UvicornContextManager` that inherits from `uvicorn.Server` and
contains a Python context manager to deploy an ASGI application inside a context
and then gracefully shut it down.

The motivation was to provide a way to easily deploy an ASGI application
when running tests or wanting to interact temporarily with ASGI applications.

This could have been a GitHub Gist or just a code snippet, but I think that 
this can be useful for many `uvicorn` users, and it just contains the `uvicorn`
dependency so there's no overhead.

## ⚒️ Installation

Python greater than 3.7 and lower than 3.11

```bash
pip install uvicorn_context_manager
```

Or install it in development mode as:

```bash
pip install -e .
```

## 👨🏻‍💻 Usage

### ⚡️ With `fastapi`

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

## 🥇 Credits

Credits go to [@florimondmanca](https://github.com/florimondmanca) due to the
solution provided at [encode/uvicorn#1103](https://github.com/encode/uvicorn/discussions/1103#discussioncomment-941726),
as the motivation to create this package was based on that code snippet.

