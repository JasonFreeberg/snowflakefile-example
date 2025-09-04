from snowflake.snowpark.files import SnowflakeFile
import os



def get_file_size(file_path):
    """
    Dummy UDF Handler code for a UDF that uses SnowflakeFile.
    """
    with SnowflakeFile.open(file_path, 'rb') as f:
        f.seek(0, os.SEEK_END)
        file_size = f.tell() / (1024 * 1024)

    return file_size
