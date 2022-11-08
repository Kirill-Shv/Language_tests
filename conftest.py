import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def pytest_addoption(parser):
    parser.addoption('--language', action='store', default="ru",
        help="Choose language: ru or fr")
    
@pytest.fixture(scope="function")
def browser(request):
    user_language = request.config.getoption("language")
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
    if user_language=="ru":
        browser = webdriver.Chrome(options=options)
    elif user_language=="fr":
        browser = webdriver.Chrome(options=options)
    elif user_language=="es":
        browser = webdriver.Chrome(options=options)
    else:
        raise pytest.UsageError("--language should be ru or fr or es")
    yield browser
    print("\nquit browser..")
    browser.quit()