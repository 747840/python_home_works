import allure
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


from lesson10.CalcPage import CalcPage


@allure.severity("blocker")
@allure.title("Проверка функциональности калькулятора")
@allure.description("Вывод результата в поле вывода после задержки")
@allure.feature("Поле ввода задержки, локатор #delay")
def test_calculator():
    browser = webdriver.Chrome(service=Service(ChromeDriverManager().
                                               install()))
    with allure.step("Открыть страницу калькулятора"):
        calc_page = CalcPage(browser)
    with allure.step("Установить задержку в поле локатора"):
        calc_page.delay_input(45)
    with allure.step("Нажать кнопку 7 на калькуляторе"):
        calc_page.click_button_1('7')
    with allure.step("Нажать кнопку + на калькуляторе"):
        calc_page.click_button_2('+')
    with allure.step("Нажать кнопку 8 на калькуляторе"):
        calc_page.click_button_2('8')
    with allure.step("Нажать кнопку = на калькуляторе"):
        calc_page.click_button_2('=')
    with allure.step("Проверить, что в окне отобразится результат"
                     " 15 через 45 секунд"):
        calc_page.result(15)

    browser.quit()
