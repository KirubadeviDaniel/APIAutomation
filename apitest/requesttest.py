#!/usr/bin/env python#!
import requests
import json
import random
def test():
    baseurl = "https://restful-booker.herokuapp.com/booking"
    headers = {
        "Content-Type": "application/json"
    }
    body = {
        "firstname": "Jim",
        "lastname": "Brown",
        "totalprice": 111,
        "depositpaid": True,
        "bookingdates":
        {
            "checkin": "2018-01-01",
            "checkout": "2019-01-01"
        },
        "additionalneeds": "Breakfast"
    }
    # need to remove json.dumps for headers as headers need to be passed as dict not as json string
    # headers = json.dumps(headers)
    body = json.dumps(body)
    res = requests.post(url=baseurl,headers=headers,data=body)
    print(res.status_code)
    if res.status_code == 200:
        print(res.json())
    else:
        print("else")
    response_data=res.text
    print(response_data)

test()