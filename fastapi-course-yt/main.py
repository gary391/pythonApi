from typing import Optional
from fastapi import Body, FastAPI, Response, status, HTTPException
from pydantic import BaseModel # For defining the schema 
from random import randrange
# instance of FastAPI 
app = FastAPI()

# Title str, content str
# This is the schema for the post request
class Post(BaseModel):
    title: str # title : <Python Data type>
    content: str # content: <Python Data type>
    published: bool = True # Default value
    rating: Optional[int] = None # Optional field


# In memory storage for the posts.
my_posts = [{"title": "title of post 1", "content": "content of post 1", "id": 1}, 
            {"title": "favourite foods", "content": "I like pizza", "id": 2}]


def find_post(id):
    """
    Return the post which has a specific id
    """
    for p in my_posts:
        if p['id'] == id:
            return p
        
def find_index_post(id):
    """
    Return the index of the post which has a specific id
    """
    for i, p in enumerate(my_posts):
        if p['id'] == id:
            return i

# Path operation or route
# @ <app> <method> <path>
@app.get("/") # route path - Help us to identify the actual path we need to take. 
def root(): # name of the function doesn't matter.
    # What ever is returned here, is what is returned to the user.
    return {"message": "Welcome to My first API !!!!"} # FastAPI converts this to JSON automatically.

# The first path operation that matches will be run
# The order does matter if you have the same path.
# When we call this endpoint from postman, FastAPI is returning the my_post data after serializing it 
# so the return value is in json format already.
@app.get("/posts")
def get_posts():
    return {"data": my_posts}


# post request
# If we sent data to this endpoint from example postman app
# This returns a message "successful create post"
# In order to see the content of the post requst we can use 
# body with ... 
# This will extract all the fields from the body
# and converts it into a dictionary and store into a variable called payload.

# Without the use of pydantics

# @app.post("/createposts")
# def create_posts(payload: dict = Body(...)):
#     print(payload)
#     return {"new_post": f"title: {payload['title']} content: {payload['content']}"}

# With the use of pydantics

@app.post("/posts", status_code=status.HTTP_201_CREATED) # This will send the correct status code of 201 as per the standard 
def create_posts(post: Post):
    post_dict = post.dict() # This converts the pydantic model to a dictionary
    post_dict['id'] = randrange(0, 1000000)
    # print(post.rating) # This stored as a pydantic model
    # print(post.dict()) # This converts the pydantic model to a dictionary
    my_posts.append(post_dict)
    return {"data": post_dict}

# For getting the lastest post.
# Order matter
# @app.get("/posts/latest")
# def get_latest_post():
#     post = my_posts[len(my_posts)-1]
#     return {"detail": post}

# For getting a individual post, using path parameter.
@app.get("/posts/{id}")
# def get_post(id: int, response: Response): # Using int fastAPI will convert this into an integer or perform the basic validation.
def get_post(id: int): # Using int fastAPI will convert this into an integer or perform the basic validation.
    post = find_post(id) # This will return the post if it exists. also id should be converted to a int.
    if not post:
        # response.status_code = status.HTTP_404_NOT_FOUND
        # return {"message": f"post with id: {id} was not found"}
        # Instead of doing the above we can use HTTPException
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"post with id: {id} was not found")
    return {"post_detail": post}


@app.delete("/posts/{id}", status_code=status.HTTP_204_NO_CONTENT) # This will update the default status code.
def delete_post(id: int):
    # Deleting post
    # find the index in the array that has required ID
    # my_posts.pop(index)
    index = find_index_post(id) # This will return None if the id doesn't exist.
    if index is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id: {id} does not exist")
    my_posts.pop(index)
    # return {'message': 'post was successfully deleted'}
    # When you are deleting any data, you don't send any data back.
    # Instead you just send the status_code. 
    return Response(status_code=status.HTTP_204_NO_CONTENT)