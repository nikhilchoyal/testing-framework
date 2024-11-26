from assertpy import assert_that, soft_assertions
from services.first.first_service import FirstClient
from conftest import *
import sys

client = FirstClient()

def test_create_record(context, create_data):
    response = client.create_call(create_data)

    with soft_assertions():
        assert_that(response.status_code).is_equal_to(200)
        assert_that(response.as_dict).is_not_empty()
        assert_that(response.as_dict).contains("bookingid")
        assert_that(response.as_dict["bookingid"]).is_not_none()

def test_check():

    print(sys.executable)
    print(sys.path)