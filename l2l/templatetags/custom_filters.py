from django import template
from datetime import datetime

register = template.Library()

@register.filter(expects_localtime=True) # Converts datetime objects into configured time zone in TIME_ZONE variable.
# Default setting is UTC.
def formatDate(date):
    if isinstance(date, str):
        # Replace T character with space character.
        return date.replace("T", " ")

    # If date is object then format the date as "%Y-%m-%d %H:%M:%S"
    return date.strftime("%Y-%m-%d %H:%M:%S")