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
