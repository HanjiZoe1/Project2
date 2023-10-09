import data
import sender

def test_positive_assert_post_order_and_get_track():
    post_order = sender.create_new_order(data.order_body)
    track = {"t": post_order.json()["track"]}
    get_track = sender.track_new_order(track)
    assert get_track.status_code == 200

# Пудовкина Анастасия, 8-а когорта, дипломная работа. Инженер по тестированию плюс