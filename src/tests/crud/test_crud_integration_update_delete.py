#conftest
#Create Booking Id using fixture
#Update Booking -> with booking id, token
#Delete the Booking
import allure
import pytest

from conftest import get_booking_id
# Verify that with created booking id, should be able to update and delete the booking as well

from src.constants.api_constants import *
from src.helpers.api_requests_wrapper import *
from src.helpers.common_verification import *
from src.helpers.payload_manager import *
from src.utils.utils import Utils

class Test_CRUD_Update_Delete_Booking:
    @pytest.mark.put
    @allure.title("Test crud operation update using put request")
    @allure.description("Verify that booking is updated using the booking id and token")
    def test_update_booking_id_token(self,create_token,get_booking_id):
        update_url = APIConstants().url_put_patch_delete(booking_id=get_booking_id)
        response = put_requests(
                        url=update_url,
                        headers=Utils().common_header_put_delete_patch_cookie(token=create_token),
                        auth=None,
                        payload=payload_update_booking(),
                        in_json=False
        )

        verify_response_key(key=response.json()["firstname"],expected_data="Amit")
        verify_response_key(key=response.json()["lastname"],expected_data="Brown")
        verify_http_status_code(response_data=response,expected_data=200)


    def test_delete_booking(self,create_token,get_booking_id):
        delete_url = APIConstants().url_put_patch_delete(booking_id=get_booking_id)
        response = delete_requests(url=delete_url,headers=Utils().common_header_put_delete_patch_cookie(token=create_token),
                                   auth=None,in_json=False)
        verify_http_status_code(response_data=response,expected_data=201)
        verify_response_delete(response=response.text)
