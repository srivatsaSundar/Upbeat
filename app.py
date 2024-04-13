import uvicorn
from fastapi import FastAPI
from database import Base,engine
from core.user.routes import user_router
from core.profile.routes import profile_router
from core.genai.routes import mental_health
from fastapi.middleware.cors import CORSMiddleware
from mangum import Mangum

app=FastAPI()

origins = [
    "http://localhost:8080",
    "http://localhost:3000",
    "https://main.d2xz3cyvwx48d0.amplifyapp.com/",
    "https://lxqwnpuexkh74m4i7yjbc74u7a0ifzmz.lambda-url.ap-south-1.on.aws/",
    "https://upbeat-8f6t.onrender.com/"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(user_router,prefix='/user',tags=['users'])
app.include_router(profile_router,prefix='/profile',tags=['profile'])
app.include_router(mental_health,prefix='/mental_health',tags=['mental health'])
Base.metadata.create_all(bind=engine)

def lambda_handler(event, context): 
    headers = {
        'Content-Type': 'application/json', 
        'Access-Control-Allow-Origin': '*',
        'Access-Control-Allow-Methods':'*',
        'Access-Control-Allow-Headers':'*',
        'Accept':'*/*'  
    }
    response = Mangum(app)(event, context)
    response.headers.update(headers)
    return response

if __name__=="__main__":
    uvicorn.run('app:app',host='0.0.0.0',port=8080,reload=True,proxy_headers=True)