import configuration
import requests
import data

def post_new_order(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER_PATH, json=body)

def get_order_by_track(track):
    return requests.get(configuration.URL_SERVICE + configuration.GET_ORDER_TRACK, params=track)

#result = get_order_by_track(track={"t" : 331866})
#print(result.json())

def get_order():
    return requests.get(configuration.URL_SERVICE + configuration.CREATE_ORDER_PATH)

#print(get_order().json())