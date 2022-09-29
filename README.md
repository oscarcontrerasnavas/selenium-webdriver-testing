# Testing automation with selenium webdriver

Personal notes and small project to show off my testing automation skills with selenium webdriver. This project will create a bot to automate the testing of [Booking.com](https://booking.com) using the [Bot pattern](https://www.selenium.dev/documentation/test_practices/design_strategies/#bot-pattern) pattern as described in Selenium documentation

This example selects elements by `ID`, `CSS_SELECTOR` and `XPATH` to demonstrate them, but `ID` should always be preferred if available. 

## Pre-requirements

In order to start working whit this repository, your system should fullfil some requirements. Since I use a virtual environment and dot-env to manage its variables, along with pip as package manager, you can run the following command to set it up.

**Note:** I run this commands in a MacBook terminal.

Let's create a virtual environment with the name `venv`.

```shell
(base) python3 -m venv venv
(base) source venv/bin/activate
```

Now, download and add to your path the webdriver you are using. In my case, [Chrome](https://chromedriver.chromium.org/). Follow this [instructions](https://www.kenst.com/including-the-chromedriver-location-in-macos-system-path/) to add it in a Mac device or Google it for your machine. Or, you can use [WebDriverManger](https://github.com/SergeyPirogov/webdriver_manager)