from datetime import datetime

''' converts date obtained from HTML to datetime object for storing in DB '''


def convert_date(date_obj):
    intermediate_obj = datetime.strptime(date_obj, '%m/%d/%Y')
    modified_time_obj = intermediate_obj.strftime('%Y-%m-%d')
    return modified_time_obj
