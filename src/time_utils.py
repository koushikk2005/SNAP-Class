from datetime import datetime, timedelta, timezone


INDIA_TIMEZONE = timezone(timedelta(hours=5, minutes=30))


def current_attendance_timestamp():
    return datetime.now(INDIA_TIMEZONE).isoformat(timespec="seconds")


def format_attendance_timestamp(timestamp):
    parsed_timestamp = datetime.fromisoformat(timestamp)
    if parsed_timestamp.tzinfo is not None:
        parsed_timestamp = parsed_timestamp.astimezone(INDIA_TIMEZONE)

    return parsed_timestamp.strftime("%Y-%m-%d %I:%M %p")
