# from fastapi import FastAPI

# from json import dumps
# from enum import Enum
# from typing import Optional, List
# from pydantic import BaseModel
# import datetime
# from contextlib import closing
# from redis import ConnectionPool, Redis
# import os


# def create_app(*args):
#     app = FastAPI()

#     @app.get("/", status_code=201)
#     def welcome():
#         return "Hello World!"

#     @app.get("/ping", status_code=200)
#     def ping():
#         return "Alles Goed!"

# return app

#
# @app.post('/names/{name}', status_code=201)
# def post_name(name: str, redis=Depends(get_redis)):
#     redis.sadd(REDIS_NAMES_KEY, name)
#     return "OK!"
#
#
# @app.get('/names')
# def get_names(redis=Depends(get_redis)):
#     return redis.smembers(REDIS_NAMES_KEY)
#
#
# @app.get('/names/{name}')
# def get_name(name, redis=Depends(get_redis)):
#     if not redis.sismember(REDIS_NAMES_KEY, name):
#         raise HTTPException(404)
#
#     return f"hello {name}!"


# HTTP Methods
# GET - retrieves an item
# POST - makes a new item
# PUT - updates an item
# DELETE - delete an item
# HEAD - returns headers only
# OPTIONS - tells which operations are avaialble

# HTTP Status code:
# 100 - Continue
# 200 - OK
# 201 - created
# 301 - Moved permanently
# 304 - didn't change
# 400 - ???
# 401 - not authorized
# 403 - permission denied
# 405 - wrong method
# 404 - missing / not found
# 500 - internal server error
# 502 - bad gateway
# 504 - gateway timeout


# 418 - i'm a teapot
# 420 - calm down

# FASTAPI doesn't come with web server, use uvicorn

# Uvicorn - ASGI web server (asynchronous server gateway interface)
# Gunicorn - WSGI web server  (web server gateway interface - pep 333)
