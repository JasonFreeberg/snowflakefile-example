from snowflake.snowpark.session import Session

def example_stored_procedure(session: Session):
    # Example logic for a stored procedure
    result = session.sql("SELECT * FROM my_table").collect()
    return result
