# Load in our dependencies
from math import ceil


# Define our class
class Paginator(object):
    def __init__(self, total, items_per_page):
        """
        Constructor for pagination class

        :param int total: Count of items we are paginating
        :param int items_per_page: How many items to place on each page
        """
        # Save our information for later
        self.total = total
        self.items_per_page = items_per_page

    def get_page_count(self):
        """
        Calculates the amount of pages that exist

        Note: If your data has 0 items per page, you will receive a `ZeroDivisionError`

        :rtype: int
        :returns: Overall amount of pages (e.g. total=50, items_per_page=10 -> 5 pages)
        """
        # DEV: We must perform float division since we want to always return partial pages
        #   e.g. total=1 but items_per_page=5, we should still have 1 page
        return int(ceil(float(self.total) / float(self.items_per_page)))

    def get_page_info(self, page):
        """
        Collect information for a given page

        :param int page: Page to get info for
        :rtype: dict
        :returns: Informtation about requested page
            Signature should be `{
                overall: {first_page, last_page, pages, total},
                page: {current_page, next_page, previous_page}
            }`
        """
        # Perform calculations and complex logic upfront
        page_count = self.get_page_count()

        # DEV: For 0 items, we should always have last_page = first_page
        first_page = 1
        last_page = page_count if page_count else first_page

        # If we are after the first page, grab the previous page
        #   e.g. (page=1, first_page=1 -> NOPE; page=2, first_page=1 -> OKAY)
        previous_page = None
        if page > first_page:
            previous_page = page - 1
            # If we go over our last page, guarantee the previous page is our last page
            #   e.g. (page=2, last_page=2 -> NOPE; page=3, last_page=2 -> OKAY)
            if previous_page > last_page:
                previous_page = last_page
        # If we are before the last page, grab the next page
        #   e.g. (page=2, last_page=2 -> NOPE; page=1, last_page=2 -> OKAY)
        next_page = None
        if page < last_page:
            next_page = page + 1
            # If we go below our first page, guarantee the next page is our first page
            #   e.g. (page=1, first_page=2 -> NOPE; page=0, first_page=1 -> OKAY)
            if next_page < first_page:
                next_page = first_page

        # Format and return our data
        return {
            'overall': {
                'first_page': first_page,
                'last_page': last_page,
                'pages': page_count,
                'total': self.total,
            },
            'page': {
                'current_page': page,
                'next_page': next_page,
                'previous_page': previous_page,
            }
        }

    @classmethod
    def page_info(cls, page, *args, **kwargs):
        """
        Helper to retrieve pagination for a single page

        :param int page: Page to retrieve info for
        :param *args: Params to pass through to `get_page`
        :param **kwargs: Params to pass through to `get_page`
        :returns: Returns same as `get_page`
        """
        paginator = cls(*args, **kwargs)
        return paginator.get_page_info(page)
