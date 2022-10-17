# from fastapi import FastAPI

# app = FastAPI()


# @app.get("/")
# def read_root():
#     return {"Hello": "World"}


# @app.get("/items/{item_id}/{q}")
# def read_item(item_id: int, q: str):
#     return [item_id,q]

# from enum import Enum

# from fastapi import FastAPI


# class ModelName(str, Enum):
#     alexnet = "alexnet"
#     resnet = "resnet"
#     lenet = "lenet"


# app = FastAPI()


# @app.get("/models/{model_name}")
# async def get_model(model_name: ModelName):
#     if model_name is ModelName.alexnet:
#         return {"model_name": model_name, "message": "Deep Learning FTW!"}

#     if model_name.value == "lenet":
#         return {"model_name": model_name, "message": "LeCNN all the images"}

#     return {"model_name": model_name, "message": "Have some residuals"}


# from typing import List, Set, Union

# from fastapi import FastAPI
# from pydantic import BaseModel, HttpUrl

# app = FastAPI()


# class Image(BaseModel):
#     url: HttpUrl
#     name: str


# class Item(BaseModel):
#     name: str
#     description: Union[str, None] = None
#     price: float
#     tax: Union[float, None] = None
#     tags: Set[str] = set()
#     images: Union[List[Image], None] = None


# @app.put("/items/{item_id}")
# async def update_item(item_id: int, item: Item):
#     results = {"item_id": item_id, "item": item}
#     return results


# from typing import Union

# from fastapi import Body, FastAPI, status
# from fastapi.responses import JSONResponse

# app = FastAPI()

# items = {"foo": {"name": "Fighters", "size": 6}, "bar": {"name": "Tenders", "size": 3}}

# @app.put("/items/{item_id}")
# async def upsert_item(
#     item_id: str,
#     name: Union[str, None] = Body(default=None),
#     size: Union[int, None] = Body(default=None),
# ):
#     if item_id in items:
#         item = items[item_id]
#         item["name"] = name
#         item["size"] = size
#         return item
#     else:
#         item = {"name": name, "size": size}
#         items[item_id] = item
#         print(items)
#         return JSONResponse(status_code=status.HTTP_201_CREATED, content=item)