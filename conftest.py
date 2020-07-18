import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from datetime import datetime

def pytest_addoption(parser):
    parser.addoption('--browser', action='store', default="chrome", help="Choose browser: chrome or firefox")
    parser.addoption('--language', default="en", action='store', help="Choose language")


@pytest.fixture(scope="class")
def browser(request):
    browser = request.config.getoption("browser")
    if browser.lower() == "chrome":
        print("\nstart chrome browser for test..")
        language = request.config.getoption('language')
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': language})
        browser = webdriver.Chrome(options=options)
    elif browser.lower()== "firefox":
        print("\nstart firefox browser for test..")
        language = request.config.getoption('language')
        fp = webdriver.FirefoxProfile()
        fp.set_preference("intl.accept_languages", language)
        browser = webdriver.Firefox(firefox_profile=fp)
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    yield browser
    # получаем переменную с текущей датой и временем в формате ГГГГ-ММ-ДД_ЧЧ-ММ-СС
    now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    # делаем скриншот с помощью команды Selenium'а и сохраняем его с именем "screenshot-ГГГГ-ММ-ДД_ЧЧ-ММ-СС"
    browser.save_screenshot('Screenshots/screenshot-%s.png' % now)
    print("\nquit browser..")
    browser.quit()
