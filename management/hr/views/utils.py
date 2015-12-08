from datetime import datetime


''' converts date obtained from HTML to datetime object for storing in DB '''

ABSURD_VALUES = ['undefined', 'null', 'None', '', None, 'Not Selected Yet']


def convert_date_for_backend(date_obj):
    try:
        intermediate_obj = datetime.strptime(date_obj, '%m/%d/%Y')
    except Exception as e:
        return None
    else:
        modified_time_obj = intermediate_obj.strftime('%Y-%m-%d')
    return modified_time_obj
