import sender_stand_request
import data

def get_order_track():
    new_order = sender_stand_request.post_new_order(data.order_body)
    track = {'t': ''}
    track_numb = new_order.json()['track']
    #print(track)
    track['t'] = track_numb

    #return track
    get_order_by_track = sender_stand_request.get_order_by_track(track)
    return get_order_by_track

#result = get_order_track()
#print(result.status_code)
#result = sender_stand_request.get_order()
#print(result.json())

def positive_assert():
    result = get_order_track()
    assert result.status_code == 200

def test_status_code():
    positive_assert()


