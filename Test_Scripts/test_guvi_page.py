import pytest
import requests
from Page_Objects.login_page import LoginPage
from Test_Data.data import Data
from Configuration.confest import driver


#Test-case-1: Check whether the URL https://www.guvi.in Is valid or not.
def test_url(driver):
    try:
        # Try sending a GET request to the website
        response = requests.get(Data.url)

        # Check if the response is OK (status code 200)
        assert response.status_code == 200

        print("SUCCESS: This is valid URL")

    except Exception as e:
        # Catch any kind of error (request or assertion)
        print(f"[ERROR] URL check failed: {e}")
        pytest.fail("URL validation failed")



#Test-case-2: Check the title of the webpage is “GUVI | Learn the code in your native language” or not.
def test_title(driver):
    try:
        # Open the target URL in the browser
        driver.get(Data.url)
        # Assert that the actual page title matches the expected title from test data
        assert driver.title == Data.expected_title, f"[FAIL] Title mismatch: Expected '{Data.expected_title}', Got '{driver.title}'"
        print("SUCCESS: Title is valid")
        print(f"Title: {driver.title}")
        print(f"Title is matched: {Data.expected_title}")
    except Exception as e:
    # Catch any error (e.g., page not loading, title mismatch)
        print(f"[ERROR] Title validation failed: {e}")
        pytest.fail("Title check failed")


#Test-case-3:
# 1) Test whether the login button is visible or not.
# 2) Test whether the login button is Clickable or not.
def test_login_button(driver):

    try:
        # Open the target URL in the browser
        driver.get(Data.url)
        login_page = LoginPage(driver)
        login_btn_link = login_page.check_login()
        assert login_btn_link, "[FAIL] Login button not visible or clickable"
    except Exception as e:
        print(f"[ERROR] Login button check failed: {e}")
        pytest.fail("Could not verify login button")


#Test-case-4:
# 1) Test whether the Sign_up button is visible or not.
# 2) Test whether the Sign_up button is Clickable or not.
def test_sign_up_button(driver):

    try:
        driver.get(Data.url)
        login_page = LoginPage(driver)
        sign_up_btn_link = login_page.check_sign_up_btn()
        assert sign_up_btn_link, "[FAIL] Login button not visible or clickable"
    except Exception as e:
        print(f"[ERROR] Login button check failed: {e}")
        pytest.fail("Could not verify login button")


#Test-case-5: Click on the URL https://www.guvi.in/sign-in/ using the sign-up button to check whether the web-page exists or not.
def test_sign_up_url(driver):
    url = "https://www.guvi.in/sign-in/"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            print(f"SUCCESS: {url} exists (Status Code: 200)")
        else:
            print(f"WARNING: {url} returned status code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"ERROR: Could not access {url}")
        print(f"Exception: {str(e)}")


#Test-case-6:   Login into your guvi account using valid email and password to verify whether the login is successful or not.
def test_valid_login(driver):
    try:
        # Open the GUVI homepage
        driver.get(Data.url)
        # Create an instance of the LoginPage class
        login_page = LoginPage(driver)
        # Click on the login button on the homepage to go to the login form
        login_page.click_login_home()
        # Enter a valid email & password address from test data
        login_page.enter_email(Data.username)
        login_page.enter_email_password(Data.password)
        # Click on the login button to attempt login
        login_page.click_login()
        # If no error occurred, print login success message
        print("SUCCESS: Login successful")
        # Click on the dropdown (usually profile or settings) after login
        login_page.click_drop_down()
        # Click logout to end the session
        login_page.click_logout()
        # If logout succeeded, print confirmation
        print("SUCCESS: Logout successful")
    except Exception as e:
    # If any step fails, catch the exception and mark the test as failed
        print(f"[ERROR] Valid login test failed: {e}")
        pytest.fail("Valid login test did not complete successfully")


#Test-case-7    Login into your guvi account using invalid email and password and catch the error message.
def test_invalid_login(driver):
    try:
        driver.get(Data.url)
        login_page = LoginPage(driver)
        login_page.click_login_home()

        login_page.enter_email("test_001")
        login_page.enter_email_password("info@123")

        login_page.click_login()

        print("Incorrect Email or Password")

    except Exception as e:
        # Catch any error during the login process and mark the test as failed
        print(f"[ERROR] Invalid login test failed: {e}")
        pytest.fail("Invalid login test encountered an error")



