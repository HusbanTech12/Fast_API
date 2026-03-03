from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def main():
    return {'data':{'name': 'Husban'}}


@app.get('/about')

def about():
    return {'Page':'About'}