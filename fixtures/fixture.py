import pytest
import allure
import os
from selenium.webdriver import Chrome, Firefox, Edge
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from _pytest.fixtures import fixture
from page_object.main_page import ShadyMeadowsPageObject
from selenium.webdriver.chrome.options import Options as ChOptions
from selenium.webdriver.firefox.options import Options as FFOptions
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption("--env", action="store", help='Env name to use: chrome, edge, firefox, headlesschrome, headlessfirefox')


def get_browser(browser_name):
    if browser_name == "firefox":
        return Firefox(executable_path=GeckoDriverManager().install())
    elif browser_name == "chrome":
        return Chrome(executable_path=ChromeDriverManager().install())
    elif browser_name == "headlesschrome":
        chrome_options = ChOptions()
        chrome_options.add_argument('--disable-gpu')
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--headless')
        return webdriver.Chrome(options=chrome_options)
    elif browser_name == "headlessfirefox":
        firefox_options = FFOptions()
        firefox_options.add_argument('--disable-gpu')
        firefox_options.add_argument('--no-sandbox')
        firefox_options.add_argument('--headless')
        return webdriver.Chrome(options=firefox_options)
    elif browser_name == "edge":
        return Edge(executable_path=EdgeChromiumDriverManager().install())
    else:
        raise AssertionError("Browser can be only on from the following: firefox, chrome or edge")


def pytest_generate_tests(metafunc):
    if "shady_meadow_page" in metafunc.fixturenames:
        browsers = metafunc.config.getoption("--env").split(", ")
        metafunc.parametrize("shady_meadow_page", browsers, indirect=True)


@pytest.fixture()
def shady_meadow_page(request, custom_logger):
    global browser
    browser_name = request.param
    browser = get_browser(browser_name)
    browser.maximize_window()
    request.cls.driver = browser
    yield ShadyMeadowsPageObject(browser, custom_logger).open()

    browser.quit()


@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
    return rep


@pytest.fixture()
def log_on_failure(request):
    yield
    item = request.node
    if item.rep_call.failed:
        allure.attach(browser.get_screenshot_as_png(), name='screenshot', attachment_type=allure.attachment_type.PNG)


# @pytest.hookimpl(tryfirst=True, hookwrapper=True)
# def pytest_runtest_makereport(item, call):
#     outcome = yield
#     rep = outcome.get_result()
#     if rep.when == 'call' and rep.failed:
#         mode = 'a' if os.path.exists('failures') else 'w'
#         try:
#             with open('failures', mode) as f:
#                 if 'browser' in item.fixturenames:
#                     web_driver = item.funcargs['browser']
#                 else:
#                     print('Fail to take screen-shot')
#                     return
#             allure.attach(
#                 web_driver.get_screenshot_as_png(),
#                 name='screenshot',
#                 attachment_type=allure.attachment_type.PNG
#             )
#         except Exception as e:
#             print('Fail to take screen-shot: {}'.format(e))

### FOR ALLURE report
# @pytest.hookimpl(hookwrapper=True)
# def pytest_runtest_makereport(item, call):
    # outcome = yield
    # report = outcome.get_result()
    # if report.when == "call":
    #     xfail = hasattr(report, "wasxfail")
    #     if (report.skipped and xfail) or (report.failed and not xfail):
    #
    #         is_frontend_test = True if 'shady_meadow_page' in item.fixturenames else False
    #         if is_frontend_test:
    #
    #             results_dir = os.environ.get("RESULTS_DIR")
    #             if not results_dir:
    #                 raise Exception(f"Environment variable 'RESULTS_DIR' must be set.")
    #             driver_fixture = item.funcargs['request']
    #             allure.attach(driver_fixture.cls.browser.get_screenshot_as_png(),
    #                           name='screenshot',
    #                           attachment_type=allure.attachment_type.PNG)
    #             allure.attach()


