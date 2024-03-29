from fastapi import FastAPI, Depends
from passlib.context import CryptContext

from jwtservice import get_current_user

pwd_context =CryptContext(schemes=["bcrypt"], deprecated="auto")

app = FastAPI(docs_url='/')


@app.get('/home')
async def home():
    return 'It is worked!!!!'


@app.post('/register')
async def register():
    return 'register page'


@app.post('/login')
async def login():
    return 'Login age'


@app.get("/secure-data")
async def secure_data(current_user: dict = Depends(get_current_user)):
    return {"message": "This data is secure", "user": current_user}
