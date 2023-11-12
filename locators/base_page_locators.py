from selenium.webdriver.common.by import By

from locators.base_locators import BaseLocators


class BasePageLocators(BaseLocators):
    LET_ME_HACK_BUTTON = (By.CSS_SELECTOR, 'button.btn.btn-primary')
    HOTEL_LOGO_URL = (By.CLASS_NAME, 'hotel-logoUrl')
    BOOK_THIS_ROOM_BUTTON = (By.CSS_SELECTOR, 'button.btn.btn-outline-primary.float-right.openBooking')
    ORDER_ROOM_TAB = (By.CSS_SELECTOR, 'div.row.hotel-room-info')
    CANCEL_BUTTON = (By.CSS_SELECTOR, 'button.btn.btn-outline-danger.float-right.book-room')
    BOOK_BUTTON = (By.CSS_SELECTOR, 'button.btn.btn-outline-primary.float-right.book-room')
    CALENDAR = (By.CSS_SELECTOR, 'div.rbc-calendar')
    FIRST_NAME = (By.CSS_SELECTOR, 'input.form-control.room-firstname')
    LAST_NAME = (By.CSS_SELECTOR, 'input.form-control.room-lastname')
    EMAIL = (By.CSS_SELECTOR, 'input.form-control.room-email')
    PHONE = (By.CSS_SELECTOR, 'input.form-control.room-phone')
    CONTACT_BLOCK_PERSONS_NAME = (By.CSS_SELECTOR, 'input#name.form-control')
    CONTACT_BLOCK_EMAIL = (By.CSS_SELECTOR, 'input#email.form-control')
    CONTACT_BLOCK_SUBJECT = (By.CSS_SELECTOR, 'input#subject.form-control')
    CONTACT_BLOCK_PHONE = (By.CSS_SELECTOR, 'input#phone.form-control')
    CONTACT_BLOCK_MESSAGE = (By.CSS_SELECTOR, 'textarea#description.form-control')
    CONTACT_BLOCK_SUBMIT_BUTTON = (By.CSS_SELECTOR, 'button#submitContact.btn.btn-outline-primary.float-right')
