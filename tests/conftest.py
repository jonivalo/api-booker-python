import pytest
from playwright.sync_api import Playwright, APIRequestContext

# Get API Authentication Token
@pytest.fixture(scope="session")
def get_authenticated(
        playwright: Playwright,
) -> [APIRequestContext, None, None]:
    headers = {
        "Content-Type": "application/json"
    }
    request_context = playwright.request.new_context(
        base_url="https://restful-booker.herokuapp.com", extra_http_headers=headers
    )
    data = {
        "username": "admin",
        "password": "password123"
    }
    auth_response = request_context.post("/auth", data=data)
    token = auth_response.json()["token"]
    request_context.token = token
    yield request_context
    request_context.dispose()

# API Context for Authenticated Requests
@pytest.fixture(scope="session")
def api_context(
        playwright: Playwright,
        get_authenticated: APIRequestContext
) -> [APIRequestContext, None, None]:
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Cookie": f"token={get_authenticated.token}",
    }
    request_context = playwright.request.new_context(
        base_url="https://restful-booker.herokuapp.com", extra_http_headers=headers
    )
    yield request_context
    request_context.dispose()
