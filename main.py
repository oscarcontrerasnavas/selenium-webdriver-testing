from booking.booking import Booking

with Booking() as bot:
    bot.land_home_page()
    bot.select_currency()
    bot.select_place_to_go("New York")
    bot.select_dates("2022-09-30", "2022-10-01")
    bot.select_adults(4)
    bot.select_adults(2)
    bot.submit_search()
