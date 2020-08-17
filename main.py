
# Server
import uvicorn
from fastapi import FastAPI, HTTPException, Form,Depends,Request
import json
from Lazada_Server import Access_token
from Lazada_Server import Refresh_token
from Lazada_Server import FInance
from pydantic import BaseModel


# App
app = FastAPI()

class LoginForm:
    def __init__(self, grant_type:str = Form(...), redirect_uri:str = Form(...), client_id: str = Form(...), client_secret: str = Form(...), code : str = Form(...)):
        self.grant_type = grant_type
        self.redirect_url = redirect_uri
        self.client_id = client_id
        self.client_secret = client_secret
        self.code = code

@app.get('/CreateToken')
async def getToken(code : str):

    """This Method is to Create Token from the Auth code and save 
        to the data base.

        Parameters:
        code (str): Parameter contains Seller code which is 
        used to generate token from lazada server.

        Returns:
        schema: which contains token of a seller.
   """

#grant_type=authorization_code
# redirect_uri=http%3A%2F%2Flazada-seller-auth.herokuapp.com%2Fauth%2Flazada%2Fredirect
# client_id=121585
# client_secret=spUZHteZ4tlglG48rZlawPS75OtxXuYf
# code=0_121585_WZ8ZzvD6Zw5PbgMnP36vOf3L63534

    # return  login

    # appKey = client_id
    # print(appKey)
    # appSecret = client_secret
    print(code)
    response = Access_token.Createtoken(code)  # Response from lazada server
    if response.code == '0':  # checking response is OK (200)
        token = response.body
        return token
    else:  # If Response has some error message raise Exception
        raise HTTPException(status_code=400, detail=response.message)


    



@app.get('/RenewToken')
async def getRenew_token(refreshtoken: str):
    """This Method is to Regenerate the New token from LazadaServer
        and update it to DB.

        Parameters:
        account (str): Parameter contains expired token 
        Seller account id used to regenerate token from refresh token
        through lazada server.

        Returns:
        schema: refresh token schema and update it in DB
   """
    response = Refresh_token.renewToken(
        refreshtoken)  # Response from Lazada server

    # checking response if OK (200)
    if response.code == '0':
        renewToken = response.body
        return renewToken
    else:  # Return error Message
        raise HTTPException(
            status_code=400, detail=response.message)


@app.post('/Transaction/Finance/{acessToken}')
async def sellerTrans(accessToken: str):
    """This Method to Extract Transaction data from Lazada server
        with the help of access token.

        Parameters:
        account (str): Parameter contains 
        accesstoken used to generate Transaction data 
        through lazada server.

        Returns:
        schema: Contains Transaction schema.
   """
    response = FInance.getTransaction(accessToken)
    getTransaction = response.body
    if response.code == '0':  # If response is ok then return Transaction data
        return getTransaction
    else:  # Return Error response
        raise HTTPException(
            status_code=500, detail=response.message)
