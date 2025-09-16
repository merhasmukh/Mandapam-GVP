from datetime import datetime, timedelta

def calculate_time_difference(start_time, end_time):
    """
    Calculate the time difference between two datetime objects.

    Args:
        start_time (datetime): The start time.
        end_time (datetime): The end time.

    Returns:
        dict: A dictionary containing the difference in hours, minutes, and seconds.
    """
    if not isinstance(start_time, datetime) or not isinstance(end_time, datetime):
        raise ValueError("Both start_time and end_time must be datetime objects.")

    time_difference = end_time - start_time

    if time_difference.total_seconds() < 0:
        raise ValueError("end_time must be greater than start_time.")

    hours, remainder = divmod(time_difference.total_seconds(), 3600)
    minutes, seconds = divmod(remainder, 60)

    return {
        "hours": int(hours),
        "minutes": int(minutes),
        "seconds": int(seconds)
    }

def add_time_duration(start_time, duration):
    """
    Add a duration to a given datetime object.

    Args:
        start_time (datetime): The start time.
        duration (timedelta): The duration to add.

    Returns:
        datetime: The resulting datetime after adding the duration.
    """
    if not isinstance(start_time, datetime) or not isinstance(duration, timedelta):
        raise ValueError("start_time must be a datetime object and duration must be a timedelta object.")

    return start_time + duration

def is_time_within_range(check_time, start_time, end_time):
    """
    Check if a given time is within a specified range.

    Args:
        check_time (datetime): The time to check.
        start_time (datetime): The start of the range.
        end_time (datetime): The end of the range.

    Returns:
        bool: True if check_time is within the range, False otherwise.
    """
    if not all(isinstance(t, datetime) for t in [check_time, start_time, end_time]):
        raise ValueError("All inputs must be datetime objects.")

    return start_time <= check_time <= end_time
