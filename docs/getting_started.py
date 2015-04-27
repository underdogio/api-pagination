# Load in dependencies
from api_pagination import Paginator

# Generate a paginator and get info about a page
paginator = Paginator(total=100, items_per_page=10)
page_info = paginator.get_page_info(page=2)
{
    'overall': {
        'first_page': 1,
        'last_page': 10,
        'pages': 10,
        'total': 100
    },
    'page': {
        'current_page': 2,
        'next_page': 3,
        'previous_page': 1
    }
}
import json
print json.dumps(page_info, indent=4, sort_keys=True).replace('"', '\'').replace('null', 'None')

# Use a classmethod to get info in one fell swoop
page_info = Paginator.page_info(page=1, total=100, items_per_page=10)
{
    'overall': {
        'first_page': 1,
        'last_page': 10,
        'pages': 10,
        'total': 100
    },
    'page': {
        'current_page': 1,
        'next_page': 2,
        'previous_page': None
    }
}
import json
print json.dumps(page_info, indent=4, sort_keys=True).replace('"', '\'').replace('null', 'None')

# Handle out of bounds properly
page_info = Paginator.page_info(page=20, total=100, items_per_page=10)
{
    'overall': {
        'first_page': 1,
        'last_page': 10,
        'pages': 10,
        'total': 100
    },
    'page': {
        'current_page': 20,
        'next_page': None,
        'previous_page': 10
    }
}
import json
print json.dumps(page_info, indent=4, sort_keys=True).replace('"', '\'').replace('null', 'None')
