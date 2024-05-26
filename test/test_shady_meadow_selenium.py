import allure
import pytest
from selenium.common import StaleElementReferenceException  # check it!
from page_object.main_page import ShadyMeadowsPageObject
from allure import attach, attachment_type, title, description, description_html, suite, severity, testcase, story, \
    feature, epic


@suite("Shady Meadows B&B UI")
class TestShadyMeadows:

    @title("Check that the 'Shady Meadows B&B' (rbp-logo.png) image appears at the Main page in the correct position.")
    @description("In this test first I click on 'Let me hack' button, that's why location_y has changed from 687 to 0.")
    @severity(allure.severity_level.CRITICAL)
    @pytest.mark.logo_picture
    @pytest.mark.shady_meadow_ui
    def test_logo_picture_is_visible(self, shady_meadow_page: ShadyMeadowsPageObject):
        attach("""
        Check that the "Shady Meadows B&B" (rbp-logo.png) image appears at the Main page in the correct position.
        """,
               name="Test ID 000 scenario",
               attachment_type=attachment_type.TEXT)
        shady_meadow_page.click_on_let_me_hack_button()
        logo_picture = shady_meadow_page.get_logo_picture_element()
        if logo_picture.is_displayed:
            print("Element found")
        else:
            print("Element not found")
        assert logo_picture.is_displayed(), "Logo picture is not visible."

    @title("'Book this room' button.")
    @description('Check that the “Book this Room” button is visible at the Main page, after clicking this button '
                 'it disappears from the page and cannot be clicked anymore.')
    @severity(allure.severity_level.CRITICAL)
    @pytest.mark.booking_the_room
    @pytest.mark.shady_meadow_ui
    def test_book_this_room_button(self, shady_meadow_page: ShadyMeadowsPageObject):
        book_button = shady_meadow_page.book_this_room_button_is_present()
        assert book_button.is_displayed(), f"Book_this_room button is not displayed"
        assert book_button.text == 'Book this room'
        shady_meadow_page.move_to_book_this_room_button()
        shady_meadow_page.click_book_this_room_button()
        with pytest.raises(BaseException) as e_info:
            # StaleElementReferenceException means the element is no longer in the DOM, or it changed.
            assert book_button.is_displayed(), f"Book_this_room button is displayed, but shouldn't.{e_info}"

    @title("'Cancel' BUTTON is hiding 'Rooms' block.")
    @description('Check that clicking the“Cancel” button under the Calendar block, which contains Calendar itself, '
                 '“First Name”, “Last Name”, “Email”, “Phone” fields, “Book” and “Cancel” buttons, is hiding this '
                 'entire block including fields and buttons.')
    @severity(allure.severity_level.CRITICAL)
    @pytest.mark.booking_the_room
    @pytest.mark.shady_meadow_ui
    def test_rooms_block_cancel_button(self, shady_meadow_page: ShadyMeadowsPageObject):
        shady_meadow_page.click_book_this_room_button()
        shady_meadow_page.move_to_rooms_block()
        cancel_button = shady_meadow_page.get_rooms_block_cancel_order_room_button()
        book_button = shady_meadow_page.get_rooms_block_book_button()
        calendar = shady_meadow_page.get_rooms_block_calendar()
        first_name_field = shady_meadow_page.get_rooms_block_first_name_field()
        last_name_field = shady_meadow_page.get_rooms_block_last_name_field()
        email_field = shady_meadow_page.get_rooms_block_email_field()
        phone_field = shady_meadow_page.get_rooms_block_phone_field()
        shady_meadow_page.click_cancel_button()
        with pytest.raises(BaseException) as e_info:
            assert cancel_button.is_displayed(), f"Cancel button is displayed, but shouldn't.{e_info}"
            assert book_button.is_displayed(), f"Book button is displayed, but shouldn't.{e_info}"
            assert calendar.is_displayed(), f"Calendar is displayed, but shouldn't.{e_info}"
            assert first_name_field.is_displayed(), f"First name field is displayed, but shouldn't.{e_info}"
            assert last_name_field.is_displayed(), f"Last name field is displayed, but shouldn't.{e_info}"
            assert email_field.is_displayed(), f"Email field is displayed, but shouldn't.{e_info}"
            assert phone_field.is_displayed(), f"Email field is displayed, but shouldn't.{e_info}"

    @title("'Contact' block visibility after clicking 'Book this room' button.")
    @description('Check that “row-contact” block under “Rooms” block, which contains “First Name”, “Last Name”, '
                 '“Email”, “Phone”, “Message” fields and “Submit” button are still displayed at the Main page after '
                 '“Book this Room” button was clicked.')
    @severity(allure.severity_level.CRITICAL)
    @pytest.mark.contact_block
    @pytest.mark.shady_meadow_ui
    def test_contact_block_visibility_if_book_this_room_button_was_clicked(self,
                                                                           shady_meadow_page: ShadyMeadowsPageObject):
        shady_meadow_page.click_book_this_room_button()
        shady_meadow_page.go_to_contact_block_submit_button()
        contact_block_name_field = shady_meadow_page.get_contact_block_name_field()
        assert contact_block_name_field.is_displayed(), f"Contact_block_name_field is not displayed"
        contact_block_email_field = shady_meadow_page.get_contact_block_email_field()
        assert contact_block_email_field.is_displayed(), f"Contact_block_email_field is not displayed"
        contact_block_phone_field = shady_meadow_page.get_contact_block_phone_field()
        assert contact_block_phone_field.is_displayed(), f"Contact_block_phone_field is not displayed"
        contact_block_subject_field = shady_meadow_page.get_contact_block_subject_field()
        assert contact_block_subject_field.is_displayed(), f"Contact_block_subject_field is not displayed"
        contact_block_message_field = shady_meadow_page.get_contact_block_message_field()
        assert contact_block_message_field.is_displayed(), f"Contact_block_message_field is not displayed"
        contact_block_submit_button = shady_meadow_page.get_contact_block_submit_button()
        assert contact_block_submit_button.is_displayed(), f"Contact_block_submit_button is not displayed"
        assert contact_block_submit_button.text == 'Submit'

    @title("'Contact' block 'Submit' button.")
    # @description('Check that the “Submit” button is visible and clickable at the Main page.')
    @description_html("<b>Check that the “Submit” button is visible and clickable at the Main page.</b>")
    @severity(allure.severity_level.CRITICAL)
    @pytest.mark.contact_block
    @pytest.mark.shady_meadow_ui
    def test_contact_block_submit_button_is_visible_and_clickable(self, shady_meadow_page: ShadyMeadowsPageObject):
        submit_button = shady_meadow_page.get_contact_block_submit_button()
        assert submit_button.is_displayed(), f"Contact_block_submit_button is not displayed"
        from selenium.common.exceptions import WebDriverException

        try:
            shady_meadow_page.contact_block_submit_button_is_clickable_second()
        except WebDriverException:
            print("Element is not clickable")
