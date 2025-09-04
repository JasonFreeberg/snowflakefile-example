# snowflakefile-example

Setup:

1. `python -m venv venv`
1. `source venv/bin/activate`
1. `pip install -r requirements.txt`
1. `python -m pytest`

The file [`functions.py`](src/functions.py) has a UDF handler that uses SnowflakeFile. Then under the `tests/` directory, there are two PyTest cases for this UDF handler. The first one tests the function against [`test_file.txt`](test/test_file.txt). 

```python
def test_get_file_size_with_local_file():
    """
    This unit-tests the file against a local file. The PyTest fixture isn't used here.
    """
    actual_size = get_file_size("test/test_file.txt")
    assert actual_size == 4.100799560546875e-05
```

The second connects to the developer's Snowflake account to read a file from a stage using the Snowflake Session.

```python
@pytest.fixture
def test_session():
    # This fixture creates a Snowflake session for unit tests
    return Session.builder.config("connection_name", "pm-acct").create()  # Update with your connection name, mine is "pm-acct"

def test_get_file_size_with_staged_file(test_session):
    """
    This unit-tests the file against a staged file in Snowflake. Of course this assumes that you a stage with this name exists and contains a file named test.txt. 
    """
    assert get_file_size("@my_stage/test.txt") == 1024
```