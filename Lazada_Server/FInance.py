# client = lazop.LazopClient(url, appkey ,appSecret)
# request = lazop.LazopRequest('/finance/payout/status/get','GET')
# request.add_api_param('created_after', '2018-01-01')
# response = client.execute(request, access_token)
# print(response.type)
# print(response.body)

# -*- coding: utf-8 -*-

import lazop
from datetime import timedelta, date, datetime
from configparser import ConfigParser
from config import Lazada_setup


def getTransaction(token):
    # params 1 : gateway url
    # params 2 : appkey
    # params 3 : appSecret

    client = lazop.LazopClient(Lazada_setup['apiService'],
                               Lazada_setup['appKey'], Lazada_setup['appSecret'])
    # create a api request set GET mehotd
    # default http method is POST
    request = lazop.LazopRequest('/finance/transaction/detail/get', 'GET')
    request.add_api_param('trans_type', '-1')
    request.add_api_param('start_time', '2018-01-01')
    request.add_api_param('end_time', '2018-01-24')
    request.add_api_param('limit', '100')
    request.add_api_param('offset', '0')
    response = client.execute(request, token)
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
    getTransaction(token)
