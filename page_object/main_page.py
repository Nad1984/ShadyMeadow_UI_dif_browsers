import sys
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.base_page_locators import BasePageLocators
from allure import step, attach, attachment_type
from logging import Logger
from selenium.webdriver import Remote


class ShadyMeadowsPageObject:
    def __init__(self, web_driver: Remote, logger: Logger):
        self.__logger: Logger = logger
        self.__web_driver: Remote = web_driver
        self.__wait = WebDriverWait(self.__web_driver, 15)
        self.__action = ActionChains(self.__web_driver)
        self.__test__ = True

    @property
    def web_driver(self):
        return self.__web_driver

    @property
    def action(self):
        return self.__action

    @property
    def wait(self):
        return self.__wait

    @property
    def logger(self):
        return self.__logger

    @property
    def command_key(self):
        if sys.platform == 'darwin':
            return Keys.COMMAND
        else:
            return Keys.CONTROL

    def open(self):
        url = "https://automationintesting.online/"
        with step(f"Navigating to the environmental URL:{url}"):
            self.logger.info(f"Navigating to the environmental URL: {url}")
            self.web_driver.get(url)
            return self

    @step(f"Click on 'Let me hack' button")
    def click_on_let_me_hack_button(self):
        try:
            self.logger.info(f"Waiting for 'Let me hack' button clickable")
            self.logger.debug(
                f"Searching web element by strategy {BasePageLocators.LET_ME_HACK_BUTTON.by} and locator {BasePageLocators.LET_ME_HACK_BUTTON.locator}")
            button = self.wait.until(
                EC.element_to_be_clickable((BasePageLocators.LET_ME_HACK_BUTTON.by,
                                            BasePageLocators.LET_ME_HACK_BUTTON.locator)))
        except TimeoutError:
            self.logger.error(
                f"Web element by strategy {BasePageLocators.LET_ME_HACK_BUTTON.by} and locator {BasePageLocators.LET_ME_HACK_BUTTON.locator} is not found")
            raise
        self.logger.info(f"Move to'Let me hack' button and click on it")
        self.__action.move_to_element(button).click().perform()
        return self

    @step("Find logo picture.")
    def get_logo_picture_element(self):
        attach(self.__web_driver.get_screenshot_as_png(), name="Logo picture.",
               attachment_type=attachment_type.PNG)
        try:
            self.logger.info(f"Getting 'LOGO' picture")
            self.logger.debug(
                f"Searching web element by strategy {BasePageLocators.HOTEL_LOGO_URL.by} and locator {BasePageLocators.HOTEL_LOGO_URL.locator}")
            element = self.__wait.until(EC.presence_of_element_located(
                (BasePageLocators.HOTEL_LOGO_URL.by,
                 BasePageLocators.HOTEL_LOGO_URL.locator)))
        except TimeoutError:
            self.logger.error(
                f"Web element by strategy {BasePageLocators.HOTEL_LOGO_URL.by} and locator {BasePageLocators.HOTEL_LOGO_URL.locator} is not found")
            raise
        return element

    @step("'Book_this_room_button' is present on the page.")
    def book_this_room_button_is_present(self):
        try:
            self.logger.info(f"Search for 'Book_this_room_button'.")
            self.logger.debug(
                f"Searching web element by strategy {BasePageLocators.BOOK_THIS_ROOM_BUTTON.by} and locator {BasePageLocators.BOOK_THIS_ROOM_BUTTON.locator}")
            elements = self.wait.until(EC.presence_of_all_elements_located((BasePageLocators.BOOK_THIS_ROOM_BUTTON.by,
                                                                            BasePageLocators.BOOK_THIS_ROOM_BUTTON.locator)))
        except TimeoutError:
            self.logger.error(
                f"Web element by strategy {BasePageLocators.BOOK_THIS_ROOM_BUTTON.by} and locator {BasePageLocators.BOOK_THIS_ROOM_BUTTON.locator} is not found")
            raise
        element = elements[0]
        return element

    @step("Move to 'rooms_block'.")
    def move_to_rooms_block(self):
        try:
            self.logger.info(f"Searching for 'rooms_block'.")
            self.logger.debug(
                f"Searching web element by strategy {BasePageLocators.ORDER_ROOM_TAB.by} and locator {BasePageLocators.ORDER_ROOM_TAB.locator}")
            elements = self.wait.until(EC.visibility_of_all_elements_located((BasePageLocators.ORDER_ROOM_TAB.by,
                                                                              BasePageLocators.ORDER_ROOM_TAB.locator)))
        except TimeoutError:
            self.logger.error(
                f"Web element by strategy {BasePageLocators.ORDER_ROOM_TAB.by} and locator {BasePageLocators.ORDER_ROOM_TAB.locator} is not found")
            raise
        element = elements[1]
        self.logger.info(f"Move to 'rooms_block")
        self.__action.move_to_element(element).perform()
        # attach(self.__web_driver.get_screenshot_as_png(), name="Rooms block.",
        #        attachment_type=attachment_type.PNG)
        return self

    @step("Find whole rooms_block calendar.")
    def get_rooms_block_calendar(self):
        try:
            self.logger.info(f"Searching for rooms_block calendar.")
            self.logger.debug(
                f"Searching web element by strategy {BasePageLocators.CALENDAR.by} and locator {BasePageLocators.CALENDAR.locator}")
            elements = self.wait.until(EC.visibility_of_all_elements_located((BasePageLocators.CALENDAR.by,
                                                                              BasePageLocators.CALENDAR.locator)))
        except TimeoutError:
            self.logger.error(
                f"Web element by strategy {BasePageLocators.CALENDAR.by} and locator {BasePageLocators.CALENDAR.locator} is not found")
            raise
        return elements

    @step("Find rooms_block 'First name' field.")
    def get_rooms_block_first_name_field(self):
        try:
            self.logger.info(f"Searching for rooms_block 'First name' field.")
            self.logger.debug(
                f"Searching web element by strategy {BasePageLocators.FIRST_NAME.by} and locator {BasePageLocators.FIRST_NAME.locator}")
            element = self.wait.until(EC.visibility_of_element_located((BasePageLocators.FIRST_NAME.by,
                                                                        BasePageLocators.FIRST_NAME.locator)))
        except TimeoutError:
            self.logger.error(
                f"Web element by strategy {BasePageLocators.FIRST_NAME.by} and locator {BasePageLocators.FIRST_NAME.locator} is not found")
            raise
        return element

    @step("Find rooms_block 'Last name' field.")
    def get_rooms_block_last_name_field(self):
        try:
            self.logger.info(f"Searching for rooms_block 'Last name' field.")
            self.logger.debug(
                f"Searching web element by strategy {BasePageLocators.LAST_NAME.by} and locator {BasePageLocators.LAST_NAME.locator}")
            element = self.wait.until(EC.visibility_of_element_located((BasePageLocators.LAST_NAME.by,
                                                                        BasePageLocators.LAST_NAME.locator)))
        except TimeoutError:
            self.logger.error(
                f"Web element by strategy {BasePageLocators.LAST_NAME.by} and locator {BasePageLocators.LAST_NAME.locator} is not found")
            raise
        return element

    @step("Find rooms_block 'Email' field.")
    def get_rooms_block_email_field(self):
        try:
            self.logger.info(f"Searching for rooms_block 'Email' field.")
            self.logger.debug(
                f"Searching web element by strategy {BasePageLocators.EMAIL.by} and locator {BasePageLocators.EMAIL.locator}")
            element = self.wait.until(EC.visibility_of_element_located((BasePageLocators.EMAIL.by,
                                                                        BasePageLocators.EMAIL.locator)))
        except TimeoutError:
            self.logger.error(
                f"Web element by strategy {BasePageLocators.EMAIL.by} and locator {BasePageLocators.EMAIL.locator} is not found")
            raise
        return element

    @step("Find rooms_block 'Phone' field.")
    def get_rooms_block_phone_field(self):
        try:
            self.logger.info(f"Searching for rooms_block 'Phone' field.")
            self.logger.debug(
                f"Searching web element by strategy {BasePageLocators.PHONE.by} and locator {BasePageLocators.PHONE.locator}")
            element = self.wait.until(EC.visibility_of_element_located((BasePageLocators.PHONE.by,
                                                                        BasePageLocators.PHONE.locator)))
        except TimeoutError:
            self.logger.error(
                f"Web element by strategy {BasePageLocators.PHONE.by} and locator {BasePageLocators.PHONE.locator} is not found")
            raise
        return element

    @step("Find rooms_block 'Cancel' button.")
    def get_rooms_block_cancel_order_room_button(self):
        try:
            self.logger.info(f"Searching for rooms_block 'Cancel' button.")
            self.logger.debug(
                f"Searching web element by strategy {BasePageLocators.CANCEL_BUTTON.by} and locator {BasePageLocators.CANCEL_BUTTON.locator}")
            cancel_order_room_button = self.wait.until(
                EC.visibility_of_all_elements_located((BasePageLocators.CANCEL_BUTTON.by,
                                                       BasePageLocators.CANCEL_BUTTON.locator)))
        except TimeoutError:
            self.logger.error(
                f"Web element by strategy {BasePageLocators.CANCEL_BUTTON.by} and locator {BasePageLocators.CANCEL_BUTTON.locator} is not found")
            raise
        element = cancel_order_room_button[0]
        return element

    @step("Find rooms_block 'Book' button.")
    def get_rooms_block_book_button(self):
        try:
            self.logger.info(f"Searching for rooms_block 'Book' button.")
            self.logger.debug(
                f"Searching web element by strategy {BasePageLocators.BOOK_BUTTON.by} and locator {BasePageLocators.BOOK_BUTTON.locator}")
            element = self.wait.until(EC.visibility_of_element_located((BasePageLocators.BOOK_BUTTON.by,
                                                                        BasePageLocators.BOOK_BUTTON.locator)))
        except TimeoutError:
            self.logger.error(
                f"Web element by strategy {BasePageLocators.BOOK_BUTTON.by} and locator {BasePageLocators.BOOK_BUTTON.locator} is not found")
            raise
        return element

    @step("Find 'Name' field in contact block.")
    def get_contact_block_name_field(self):
        try:
            self.logger.info(f"Searching for 'Name' field in contact block.")
            self.logger.debug(
                f"Searching web element by strategy {BasePageLocators.CONTACT_BLOCK_PERSONS_NAME.by} and locator {BasePageLocators.CONTACT_BLOCK_PERSONS_NAME.locator}")
            elements = self.wait.until(
                EC.visibility_of_all_elements_located((BasePageLocators.CONTACT_BLOCK_PERSONS_NAME.by,
                                                       BasePageLocators.CONTACT_BLOCK_PERSONS_NAME.locator)))
        except TimeoutError:
            self.logger.error(
                f"Web element by strategy {BasePageLocators.CONTACT_BLOCK_PERSONS_NAME.by} and locator {BasePageLocators.CONTACT_BLOCK_PERSONS_NAME.locator} is not found")
            raise
        element = elements[0]
        return element

    @step("Find 'Email' field in contact block.")
    def get_contact_block_email_field(self):
        try:
            self.logger.info(f"Searching for 'Email' field in contact block.")
            self.logger.debug(
                f"Searching web element by strategy {BasePageLocators.CONTACT_BLOCK_EMAIL.by} and locator {BasePageLocators.CONTACT_BLOCK_EMAIL.locator}")
            elements = self.wait.until(EC.visibility_of_all_elements_located((BasePageLocators.CONTACT_BLOCK_EMAIL.by,
                                                                              BasePageLocators.CONTACT_BLOCK_EMAIL.locator)))
        except TimeoutError:
            self.logger.error(
                f"Web element by strategy {BasePageLocators.CONTACT_BLOCK_EMAIL.by} and locator {BasePageLocators.CONTACT_BLOCK_EMAIL.locator} is not found")
            raise
        element = elements[0]
        return element

    @step("Find contact_block 'Phone' field.")
    def get_contact_block_phone_field(self):
        try:
            self.logger.info(f"Searching for contact_block 'Phone' field.")
            self.logger.debug(
                f"Searching web element by strategy {BasePageLocators.CONTACT_BLOCK_PHONE.by} and locator {BasePageLocators.CONTACT_BLOCK_PHONE.locator}")
            elements = self.wait.until(EC.visibility_of_all_elements_located((BasePageLocators.CONTACT_BLOCK_PHONE.by,
                                                                              BasePageLocators.CONTACT_BLOCK_PHONE.locator)))
        except TimeoutError:
            self.logger.error(
                f"Web element by strategy {BasePageLocators.CONTACT_BLOCK_PHONE.by} and locator {BasePageLocators.CONTACT_BLOCK_PHONE.locator} is not found")
            raise
        element = elements[0]
        return element

    @step("Find contact_block 'Subject' field.")
    def get_contact_block_subject_field(self):
        try:
            self.logger.info(f"Searching for contact_block 'Subject' field.")
            self.logger.debug(
                f"Searching web element by strategy {BasePageLocators.CONTACT_BLOCK_SUBJECT.by} and locator {BasePageLocators.CONTACT_BLOCK_SUBJECT.locator}")
            elements = self.wait.until(EC.visibility_of_all_elements_located((BasePageLocators.CONTACT_BLOCK_SUBJECT.by,
                                                                              BasePageLocators.CONTACT_BLOCK_SUBJECT.locator)))
        except TimeoutError:
            self.logger.error(
                f"Web element by strategy {BasePageLocators.CONTACT_BLOCK_SUBJECT.by} and locator {BasePageLocators.CONTACT_BLOCK_SUBJECT.locator} is not found")
            raise
        element = elements[0]
        return element

    @step("Find contact_block 'Message' field.")
    def get_contact_block_message_field(self):
        try:
            self.logger.info(f"Searching for contact_block 'Message' field.")
            self.logger.debug(
                f"Searching web element by strategy {BasePageLocators.CONTACT_BLOCK_MESSAGE.by} and locator {BasePageLocators.CONTACT_BLOCK_MESSAGE.locator}")
            elements = self.wait.until(
                EC.visibility_of_all_elements_located((BasePageLocators.CONTACT_BLOCK_MESSAGE.by,
                                                       BasePageLocators.CONTACT_BLOCK_MESSAGE.locator)))
        except TimeoutError:
            self.logger.error(
                f"Web element by strategy {BasePageLocators.CONTACT_BLOCK_MESSAGE.by} and locator {BasePageLocators.CONTACT_BLOCK_MESSAGE.locator} is not found")
            raise
        element = elements[0]
        return element

    @step("Find contact_block 'Submit_button'.")
    def get_contact_block_submit_button(self):
        try:
            self.logger.info(f"Searching for contact_block 'Submit_button'.")
            self.logger.debug(
                f"Searching web element by strategy {BasePageLocators.CONTACT_BLOCK_SUBMIT_BUTTON.by} and locator {BasePageLocators.CONTACT_BLOCK_SUBMIT_BUTTON.locator}")
            elements = self.wait.until(
                EC.visibility_of_all_elements_located((BasePageLocators.CONTACT_BLOCK_SUBMIT_BUTTON.by,
                                                       BasePageLocators.CONTACT_BLOCK_SUBMIT_BUTTON.locator)))
        except TimeoutError:
            self.logger.error(
                f"Web element by strategy {BasePageLocators.CONTACT_BLOCK_SUBMIT_BUTTON.by} and locator {BasePageLocators.CONTACT_BLOCK_SUBMIT_BUTTON.locator} is not found")
            raise
        element = elements[0]
        return element

    @step("Check that contact_block 'Submit_button' is clickable.")
    def go_to_contact_block_submit_button(self):
        submit_button = self.get_contact_block_submit_button()
        self.logger.info(f"Move to contact_block 'Submit_button'.")
        self.__action.move_to_element(submit_button).perform()
        return self

    @step(f"Scroll to 'Submit' button on contact block and click on it.")
    def contact_block_submit_button_is_clickable_second(self):
        submit_button = self.get_contact_block_submit_button()
        self.logger.info(f"Move to contact_block 'Submit_button'.")
        self.__action.move_to_element(submit_button).perform()
        self.logger.info(f"Click on contact_block 'Submit_button'.")
        self.get_contact_block_submit_button().click()
        return self

    @step("Scroll to Book_this_room button in rooms block.")
    def move_to_book_this_room_button(self):
        book_this_room_button = self.book_this_room_button_is_present()
        self.logger.info(f"Move to Book_this_room button in rooms block.")
        self.__action.move_to_element(book_this_room_button).perform()
        return self

    @step("Click on Book_this_room button.")
    def click_book_this_room_button(self):
        self.logger.info(f"Click on Book_this_room button.")
        self.book_this_room_button_is_present().click()
        return self

    @step("Scroll to 'Cancel' button in rooms block and click on it.")
    def click_cancel_button(self):
        cancel_button = self.get_rooms_block_cancel_order_room_button()
        self.logger.info(f"Move to 'Cancel' button in rooms block.")
        self.__action.move_to_element(cancel_button).perform()
        self.logger.info(f"Click on 'Cancel' button in rooms block.")
        self.get_rooms_block_cancel_order_room_button().click()
        return self
