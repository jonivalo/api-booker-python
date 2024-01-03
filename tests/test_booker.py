from playwright.sync_api import APIRequestContext

# Use the command pytest -v -s to run the test cases with output displayed.

def test_post(api_context: APIRequestContext):
    data = {
        "firstname": "John",
        "lastname": "Doe",
        "totalprice": 99,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2023-09-05",
            "checkout": "2023-09-06"
        },
        "additionalneeds": "English breakfast"
    }
    new_booking = api_context.post(
        "/booking", data=data
    )

    print(new_booking.body())
    assert new_booking.ok
    assert new_booking.status == 200

# Add the ID from the 'post' command to the 'get', 'put' or 'delete' command ("/booking/ + booking_ID")



# def test_get(api_context: APIRequestContext):
#     bookings = api_context.get(
#     "/booking/"
#     )
#
#     print(bookings.body())
#     assert bookings.ok
#     assert bookings.status == 200

# def test_put(api_context: APIRequestContext):
#
#     data = {
#         "firstname": "Jane",
#         "lastname": "Doe",
#         "totalprice": 99,
#         "depositpaid": True,
#         "bookingdates": {
#             "checkin": "2023-09-05",
#             "checkout": "2023-09-06"
#         },
#         "additionalneeds": "English breakfast"
#     }
#     put_booking = api_context.put(
#         "/booking/", data=data
#     )
#
#     print(put_booking.body())
#     assert put_booking.ok
#     assert put_booking.status == 200

# def test_delete(api_context: APIRequestContext):
#
#
#     delete_booking = api_context.delete(
#         "/booking/"
#     )
#
#     print(delete_booking)
#     assert delete_booking.ok
#     assert delete_booking.status == 201
