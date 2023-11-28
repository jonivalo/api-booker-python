This project provides a set of API tests using Playwright for a RESTful booking service hosted at "https://restful-booker.herokuapp.com". The tests focus on creating, retrieving, updating, and deleting booking information.
Testing Functions

    Create Booking (POST)
        Function: test_post(api_context: APIRequestContext)
        Description: Sends a POST request to create a new booking with specified details.
        Usage: To add a new booking to the system.
        Note: The booking ID from the response can be used in subsequent GET, PUT, or DELETE commands.

    Get Bookings (GET)
        Function: test_get(api_context: APIRequestContext)
        Description: Sends a GET request to retrieve a list of all bookings.
        Usage: To fetch and display all existing bookings.
        Note: Uncomment and add the booking ID to the endpoint for specific booking retrieval.

    Update Booking (PUT)
        Function: test_put(api_context: APIRequestContext)
        Description: Sends a PUT request to update an existing booking with new details.
        Usage: To modify the details of a specific booking.
        Note: Uncomment and add the booking ID to the endpoint for the booking to be updated.

    Delete Booking (DELETE)
        Function: test_delete(api_context: APIRequestContext)
        Description: Sends a DELETE request to remove a booking from the system.
        Usage: To delete a specific booking from the system.
        Note: Uncomment and add the booking ID to the endpoint for the booking to be deleted.

Authentication

The project includes fixtures for obtaining and using an authentication token for API requests. The token is retrieved during test setup and utilized in subsequent authenticated requests.
Usage

    Ensure Playwright is installed (pip install playwright).
    Run the tests using a testing framework like Pytest.

Dependencies

    Playwright
    Pytest
