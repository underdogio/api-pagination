# Load in dependencies
from unittest import TestCase
from api_pagination import Paginator


# Define our tests
class ApiPaginationTestCase(TestCase):
    def test_single_page(self):
        """
        Pagination info for a single page
            under overall
                it lists pages
                it lists total
            under page
                it lists first page
                it lists last page
                it lists current page
                it has no previous page
                it has no next page
        """
        page_info = Paginator.page_info(page=1, total=50, items_per_page=100)
        self.assertEqual(page_info, {
            'overall': {
                'pages': 1,
                'total': 50,
                'first_page': 1,
                'last_page': 1,
            },
            'page': {
                'current_page': 1,
                'previous_page': None,
                'next_page': None,
            },
        })

    def test_multiple_pages(self):
        """
        Pagination info for multiple pages
            under overall
                it lists pages
                it lists total
            under page
                it lists first page
                it lists last page
                it lists current page
                it lists previous page
                it lists next page
        """
        page_info = Paginator.page_info(page=2, total=50, items_per_page=10)
        self.assertEqual(page_info, {
            'overall': {
                'first_page': 1,
                'last_page': 5,
                'pages': 5,
                'total': 50,
            },
            'page': {
                'current_page': 2,
                'previous_page': 1,
                'next_page': 3,
            },
        })

    def test_non_exact_pages(self):
        """
        Pagination info for multiple pages that aren't exactly divisible
            under overall
                it lists pages rounded up
                it lists total
        """
        page_info = Paginator.page_info(page=2, total=45, items_per_page=10)
        self.assertEqual(page_info['overall'], {
            'first_page': 1,
            'last_page': 5,
            'pages': 5,
            'total': 45,
        })

    def test_exact_pages(self):
        """
        Pagination info for multiple pages that are exactly divisible
            under overall
                it lists pages rounded up
                it lists total
        """
        page_info = Paginator.page_info(page=2, total=50, items_per_page=10)
        self.assertEqual(page_info['overall'], {
            'first_page': 1,
            'last_page': 5,
            'pages': 5,
            'total': 50,
        })

    def test_first_page(self):
        """
        Pagination info for the first page of multiple pages
            under page
                it lists current page
                it has no previous page
                it lists next page
        """
        page_info = Paginator.page_info(page=1, total=50, items_per_page=10)
        self.assertEqual(page_info['page'], {
            'current_page': 1,
            'previous_page': None,
            'next_page': 2,
        })

    def test_last_page(self):
        """
        Pagination info for the last page of multiple pages
            under page
                it lists current page
                it lists previous page
                it has no next page
        """
        page_info = Paginator.page_info(page=5, total=50, items_per_page=10)
        self.assertEqual(page_info['page'], {
            'current_page': 5,
            'previous_page': 4,
            'next_page': None,
        })

    def test_under_first_page(self):
        """
        Pagination info for the a page before the first page of multiple pages
            under page
                it lists current page
                it has no previous page
                it lists first page as next page
        """
        page_info = Paginator.page_info(page=6, total=50, items_per_page=10)
        self.assertEqual(page_info['page'], {
            'current_page': 6,
            'previous_page': 5,
            'next_page': None,
        })

    def test_over_last_page(self):
        """
        Pagination info for the a page after the last page of multiple pages
            under page
                it lists current page
                it lists last page as previous page
                it has no next page
        """
        page_info = Paginator.page_info(page=0, total=50, items_per_page=10)
        self.assertEqual(page_info['page'], {
            'current_page': 0,
            'previous_page': None,
            'next_page': 1,
        })

    def test_zero_items(self):
        """
        Pagination info for 0 items
            under page
                it lists 1 as the first page
                it lists 1 as the last page
                it lists current page
                it has no previous page
                it has no next page
            when before the first page (1)
                it has 1 was the next page
            when after the last page (1)
                it has 1 was the previous page
        """
        page_info = Paginator.page_info(page=1, total=0, items_per_page=10)
        self.assertEqual(page_info['page'], {
            'current_page': 1,
            'previous_page': None,
            'next_page': None,
        })

        page_info = Paginator.page_info(page=0, total=0, items_per_page=10)
        self.assertEqual(page_info['page']['next_page'], 1)

        page_info = Paginator.page_info(page=2, total=0, items_per_page=10)
        self.assertEqual(page_info['page']['previous_page'], 1)
