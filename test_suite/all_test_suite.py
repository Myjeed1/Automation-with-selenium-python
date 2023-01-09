import unittest
from Testcase.new_test import CookieTest
from Testcase.playtest2 import Launch

maps_cookie = unittest.TestLoader().loadTestsFromTestCase(CookieTest)
maps_launch = unittest.TestLoader().loadTestsFromTestCase(Launch)

sanity_test = unittest.TestSuite([maps_cookie, maps_launch])
unittest.TextTestRunner().run(sanity_test)

