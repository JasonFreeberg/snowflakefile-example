from src.functions import get_file_size
from snowflake.snowpark import Session
import pytest


@pytest.fixture
def test_session():
    # This fixture creates a Snowflake session for unit tests
    return Session.builder.config("connection_name", "pm-acct").create()  # Update with your connection name, mine is "pm-acct"


def test_get_file_size_with_local_file():
    """
    This unit-tests the file against a local file. The PyTest fixture isn't used here.
    """
    actual_size = get_file_size("test/test_file.txt")
    assert actual_size == 4.100799560546875e-05


def test_get_file_size_with_staged_file(test_session):
    """
    This unit-tests the file against a staged file in Snowflake. Of course this assumes that you a stage with this name exists and contains a file named test.txt. 
    """
    assert get_file_size("@my_stage/test.txt") == 1024
