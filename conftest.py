import pytest
import allure
from requests import session

from src.constants.api_constants import APIConstants
from src.helpers.api_requests_wrapper import *
from src.helpers.payload_manager import *
from src.utils.utils import Utils
from src.helpers.common_verification import *

@pytest.fixture(scope="session")
def create_token():
    response = post_request(url=APIConstants().url_create_token(),
                            headers=payload_create_token(),
                            auth=None,
                            in_json=False)
    verify_http_status_code(response_data=response,expected_data=200)
    verify_json_key_for_not_null(response.json()["token"])
    return response.json()["token"]


@pytest.fixture(scope="session")
def get_booking_id():
    response = post_request(url=APIConstants().url_create_booking(),
                            headers=payload_create_booking(),
                            auth=None,
                            in_json=False)
    booking_id = response.json()["bookingid"]
    verify_http_status_code(response_data=response, expected_data=200)
    verify_json_key_for_not_null(booking_id)
    return booking_id