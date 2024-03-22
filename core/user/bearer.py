from fastapi import Request,HTTPException
from fastapi.security import HTTPBearer,HTTPAuthorizationCredentials,OAuth2
from .utils import decodeJWT

class JWTBearer(HTTPBearer):
    def __init__(self, auto_error:bool=True):
        super(JWTBearer,self).__init__(auto_error=auto_error)

    async def __call__(self, request: Request):
        credentials: HTTPAuthorizationCredentials = await super().__call__(request)
        if credentials:
            if not credentials.scheme == "Bearer":
                raise HTTPException(status_code=403, detail="Invalid Authentication scheme.")
            if not self.verify_jwt(credentials.credentials):
                raise HTTPException(status_code=403, detail="Invalid token or expired token")
            return credentials.credentials
        else:
            raise HTTPException(status_code=403, detail="Invalid authorization code.")
        
    def verify_jwt(self,jwtoken: str)-> bool:
        isTokenVaild: bool =False

        try:
            payload=decodeJWT(jwtoken)
        except:
            payload=None
        if payload:
            isTokenVaild=True
        return isTokenVaild