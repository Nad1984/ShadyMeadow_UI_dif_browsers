from enum import Enum


class BaseLocators(Enum):
    def __init__(self, by, locator):
        self.by = by
        self.locator = locator

