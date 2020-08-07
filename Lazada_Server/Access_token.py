# -*- coding: utf-8 -*-

import lazop
from datetime import timedelta, date, datetime
from config import Lazada_setup


def Createtoken(appKey, appSecret, code):
    # params 1 : gateway url
    # params 2 : appkey
    # params 3 : appSecret
    print(appKey)
    print(appSecret)
    print(code)
    client = lazop.LazopClient(Lazada_setup['authService'],
                               appKey, appSecret)
    # create a api request set GET mehotd
    # default http method is POST
    request = lazop.LazopRequest('/auth/token/create')
    # simple type params ,Number ,String
    request.add_api_param('code', code)
    # request.add_api_param('uuid', '38284839234')
    response = client.execute(request)
    # ISP : API Service Provider Error
    # ISV : API Request Client Error
    # SYSTEM : Lazop platform Error
    print(response.type)
    # response code, 0 is no error
    print(response.code)

    # response error message
    print(response.message)

    # response unique id
    print(response.request_id)

    # full response
    print(response.body)
    json_payload = response
    print(json_payload.body)
    return json_payload


if __name__ == "__main__":
    Createtoken(appKey, appSecret, code)
