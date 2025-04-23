from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


from CalcPage import CalcPage


def test_calculator():
    browser = webdriver.Chrome(service=Service(ChromeDriverManager().
                                               install()))

    calc_page = CalcPage(browser)
    calc_page.delay_input(45)
    calc_page.click_button_1('7')
    calc_page.click_button_2('+')
    calc_page.click_button_2('8')
    calc_page.click_button_2('=')
    calc_page.result(15)

    browser.quit()
