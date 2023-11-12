import logging
from io import StringIO

import allure
import pytest


@pytest.fixture
def custom_logger(request):
    custom_logger = logging.getLogger(request.function.__name__)
    custom_logger.setLevel("DEBUG")
    string_io = StringIO()

    console_handler = logging.StreamHandler()
    console_handler.setLevel("WARNING")

    stream_handler = logging.StreamHandler(stream=string_io)
    stream_handler.setLevel("DEBUG")
    console_handler_format = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    stream_handler_format = logging.Formatter('%(asctime)s == %(process)d == %(name)s == %(levelname)s: %(message)s')

    console_handler.setFormatter(console_handler_format)
    stream_handler.setFormatter(stream_handler_format)

    custom_logger.addHandler(console_handler)
    custom_logger.addHandler(stream_handler)

    yield custom_logger

    stream_handler.flush()
    string_io.flush()
    log = string_io.getvalue()
    string_io.close()

    allure.attach(log, name="Test Log file", attachment_type=allure.attachment_type.TEXT)
