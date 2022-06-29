# -*- coding: utf-8 -*-
import lazop
from datetime import timedelta, date, datetime
import time
from config import Lazada_setup

def renewToken(refreshToken):
    # params 1 : gateway url
    # params 2 : appkey
    # params 3 : appSecret
    print(refreshToken)
    client = lazop.LazopClient(Lazada_setup['authService'],
                               Lazada_setup['appKey'], Lazada_setup['appSecret'])
    # create a api request set GET mehotd
    # default http method is POST
    request = lazop.LazopRequest('/auth/token/refresh')
    # simple type params ,Number ,String
    request.add_api_param('refresh_token', refreshToken)
    # request.add_api_param('uuid', '38284839234')
    response = client.execute(request)
    # response type nil,ISP,ISV,SYSTEM
    # nil ：no error
    # ISP : API Service Provider Error
    # ISV : API Request Client Error
    # SYSTEM : Lazop platform Error

    # full response
    print(response.body)
    json_payload = response
    print(json_payload.body)
    return json_payload


if __name__ == "__main__":
    renewToken(refreshToken)
