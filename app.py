import uvicorn
from fastapi import FastAPI
from database import Base,engine
from core.user.routes import user_router
from core.profile.routes import profile_router
from fastapi.middleware.cors import CORSMiddleware

app=FastAPI()

origins = [
    "http://localhost:8080",
    "http://localhost:3000",
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
Base.metadata.create_all(bind=engine)


if __name__=="__main__":
    uvicorn.run('app:app',host='0.0.0.0',port=8080,reload=True)
