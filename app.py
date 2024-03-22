import uvicorn
from fastapi import FastAPI
from database import Base,engine
from core.user.routes import user_router
from core.profile.routes import profile_router

app=FastAPI()

app.include_router(user_router,prefix='/user',tags=['users'])
app.include_router(profile_router,prefix='/profile',tags=['profile'])
Base.metadata.create_all(bind=engine)

if __name__=="__main__":
    uvicorn.run('app:app',host='0.0.0.0',port=8080,reload=True)
