from selenium.webdriver import Chrome, Firefox, Edge
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from _pytest.fixtures import fixture
from page_object.main_page import ShadyMeadowsPageObject


def pytest_addoption(parser):
    parser.addoption("--env", action="store", help='Env name to use: chrome, edge, firefox')


def get_browser(browser_name):
    if browser_name == "firefox":
        return Firefox(executable_path=GeckoDriverManager().install())
    elif browser_name == "chrome":
        return Chrome(executable_path=ChromeDriverManager().install())
    elif browser_name == "edge":
        return Edge(executable_path=EdgeChromiumDriverManager().install())
    else:
        raise AssertionError("Browser can be only on from the following: firefox, chrome or edge")


def pytest_generate_tests(metafunc):
    if "shady_meadow_page" in metafunc.fixturenames:
        browsers = metafunc.config.getoption("--env").split(", ")
        metafunc.parametrize("shady_meadow_page", browsers, indirect=True)


@fixture
def shady_meadow_page(request, custom_logger):
    browser_name = request.param
    browser = get_browser(browser_name)
    browser.maximize_window()
    yield ShadyMeadowsPageObject(browser, custom_logger).open()

    browser.quit()
