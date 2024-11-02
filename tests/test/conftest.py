import pytest

from utils.file_reader import read_file


@pytest.fixture
def context():
    return "test context"


@pytest.fixture(scope="session")
def create_data():
    yield read_file("payload.json")


@pytest.fixture(scope="session")
def update_data():
    yield read_file("update_booking.json")
