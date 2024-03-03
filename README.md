# Entrata-Project
This project is a set of automated tests written in Python using the pytest framework and Selenium WebDriver to explore and validate the functionality of the website entrata.com.

Here's an explanation of the key components:

Imports: The code imports necessary modules from pytest, Selenium, and Selenium WebDriver.

Fixture: The browser fixture is a setup method that initializes the WebDriver instance before each test function and quits the WebDriver after each test function finishes execution. It ensures that each test starts with a fresh browser session and closes the browser afterward.

Test Functions:

test_homepage_title: This test verifies that the title of the homepage of entrata.com is "Property Management Software | Entrata".
test_navigation_to_features: This test navigates to the "Features" page by clicking on the corresponding link and verifies that the page title contains the word "Features".
test_search_functionality: This test interacts with the search functionality by entering "Property Management" into the search box, submitting the form, and verifying that the search results page is loaded by checking the presence of the heading "Search Results" in the title.
Execution: To run the tests, you need to have Python, pytest, and Selenium installed. You also need to download the Chrome WebDriver (chromedriver) and specify its path in the webdriver.Chrome() call. Once everything is set up, you can execute the tests using pytest, which automatically discovers and runs the test functions.
