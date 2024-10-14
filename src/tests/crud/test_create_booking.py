from logging import Logger

import pytest
import allure
from src.constants.api_constants import APIConstants
from src.helpers.api_requests_wrapper import post_request
from src.helpers.common_verification import *
from src.helpers.payload_manager import payload_create_booking
from src.utils.utils import Utils
import logging

class TestCreateBooking:
    @pytest.mark.positive
    @allure.title("Verify that create booking status and booking id should not be null")
    @allure.description("create booking - With correct payload the booking id should not be null and status code should be 200")
    def test_create_booking_positive(self):
        Logger = logging.getLogger(__name__)
        response = post_request(url=APIConstants().url_create_booking(),
                                auth=None,
                                headers=Utils().common_headers_json(),
                                payload=payload_create_booking(),
                                in_json=False)
        verify_http_status_code(response_data=response,expected_data=200)
        verify_json_key_for_not_null(response.json()["bookingid"])
        Logger.info(response.json()["bookingid"])
        Logger.info("Positive testcase")



    @pytest.mark.negative
    @allure.title("Verify create booking with no payload")
    @allure.description("verify the booking id and status code should be 500 without payload")
    def test_create_booking_negative(self):
        response = post_request(url=APIConstants().url_create_booking(),
                                auth=None,
                                headers=Utils().common_headers_json(),
                                payload={},
                                in_json=False)
        verify_http_status_code(response_data=response, expected_data=500)