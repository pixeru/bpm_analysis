"""Time conversion and formatting for reports and plots."""
import datetime


def timestamp_str() -> str:
    """Return current local time as 'YYYY-MM-DD HH:MM:SS' for reports and logs."""
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def seconds_to_datetime(seconds: float) -> datetime.datetime:
    """Elapsed seconds since epoch -> timezone-naive datetime (for Plotly/pandas)."""
    return datetime.datetime.fromtimestamp(0) + datetime.timedelta(seconds=seconds)
