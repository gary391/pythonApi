#### How to activate the activate virtual environment

```
source venv/bin/activate

```
#### main is the name of the file and app is the application. 

- Reload flag allows you to check your changes without restarting the server.
- only used in the dev. 

```
uvicorn main:app --reload
```

#### Get vs Post request 
- post request we can send data to the api
- post request is used to Create


#### VS code shortcut
- `command + .` for importing


#### Why we need Schema 
- What if the user send incorrect formatted data?
  - Blank title.
- Define how you want the data to look like.
- It's a pain to get all the values from the body
- The client can send whatever data they want
- The data isn't getting validated
- We ultimately want to force the client to send in a  schema that we expect.


#### What is crud operation is ?

- Convention is use plurals instead of using the singluar example here is posts
  - or use Users and not User.
- Anytime you create an item in a DB, that DB will give that item a unique indentifier.
- using "id"
- Difference between PUT and PATCH - In PUT you will have to pass in all of the information, including those that are not changing. 
- In PATCH we will have to send in specific field that we want to change only.
  Example: If you want to update the title of a post, if you are using the PUT, in that case you will have to also pass in the pre existing content along with the new title, where as if you are using the 
  PATCH method you can pass in just the title information.
```
Create  ---> /posts ---> @app.post("/posts")
Read 
  - Get ---> /posts/:id ---> @app.get("/posts/{id}") # For one individual post 
  - Get ---> /posts  ---> @app.get("/posts/")
Update (PUT/PATCH)---> /posts/:id  ---> @app.put("/posts/{id}")
Delete ---> /posts/:id  ---> @app.delet("/posts/{id}")

```