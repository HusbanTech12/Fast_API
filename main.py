from fastapi import FastAPI
from typing import Optional
app = FastAPI()


# Base Path
@app.get('/')

def main():
    return {'data':{'name': 'Husban'}}




# blog Path with Quary parameter means limit blogs show 
@app.get('/blog')

# Only get 10 published blogs.
#  
def blog(limit= 20, published: bool = True, sort:Optional[str] = None):
     
    # return published 
    if published:
       return {'data': f'{limit} published blogs from the db'}
   
    else:
       return {'data': f'{limit} blogs from the db'}





# blog with published blogs Path
@app.get('/blog/published')
def published():
    return {'data':'These published blogs'}





# blog with dynanic id Path
@app.get('/blog/{id}')

def blog_id(id:int): 
     return {'data':{'bolg':id}}





# blog with dynanic id and comments Path
@app.get('/blog/{id}/comments')

def comments(id):
     return {'data':{'comment': 'my first comment'}}

