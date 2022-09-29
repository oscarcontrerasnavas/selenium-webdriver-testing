from unittest import TestCase
from booking.booking import Booking


class BookingTest(TestCase):
    def test_booking_search(self):

        city = "New York"

        bot = Booking()
        bot.land_home_page()
        bot.select_currency()
        bot.select_place_to_go(city)
        bot.select_dates("2022-09-30", "2022-10-01")
        bot.select_adults(4)
        bot.select_adults(2)
        bot.submit_search()
        title = bot.get_page_title()
        results = bot.get_result_length()

        self.assertIn(city, title)
        self.assertEqual(26, results)
