"""
@package utilities

CheckPoint class implementation
It provides functionality to assert the result

Example:
    self.check_point.mark_final("Test Name", result, "Message")
"""
from traceback import print_stack

import utilities.custom_logger as cl
import logging
from base.selenium_driver import SeleniumDriver


class TestStatus(SeleniumDriver):
    log = cl.custom_logger(logging.INFO)

    def __init__(self, driver):
        """
        Inits CheckPoint class
        """
        super(TestStatus, self).__init__(driver)
        self.result_list = []

    def set_result(self, result, result_message):
        try:
            if result is not None:
                if result:
                    self.result_list.append("PASS")
                    self.log.info(f"### VERIFICATION SUCCESSFUL :: {result_message}")
                else:
                    self.result_list.append("FAIL")
                    self.log.error(f"### VERIFICATION FAILED :: {result_message}")
                    self.screenshot(result_message)
            else:
                self.result_list.append("FAIL")
                self.log.error(f"### VERIFICATION FAILED :: {result_message}")
                self.screenshot(result_message)
        except:
            self.result_list.append("FAIL")
            self.log.error("### Exception Occurred !!!")
            self.screenshot(result_message)
            print_stack()

    def mark(self, result, result_message):
        """
        Mark the result of the verification point in a test case
        """
        self.set_result(result, result_message)

    def mark_final(self, test_name, result, result_message):
        """
        Mark the final result of the verification point in a test case
        This needs to be called at least once in a test case
        This should be final test status of the test case
        """
        self.set_result(result, result_message)

        if 'FAIL' in self.result_list:
            self.log.error(f'{test_name} ### TEST FAILED')
            self.result_list.clear()
            assert True == False
        else:
            self.log.info(f'{test_name} ### TEST SUCCESSFUL')
            self.result_list.clear()
            assert True == True
