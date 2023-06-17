# import time
#
# import pytest
# from selenium import webdriver
# from pageObjects.LoginPage import LoginPage
# from utilities.readProperties import ReadConfig
# from pageObjects.AddcustomerPage import AddCustomer
# from pageObjects.SearchcustomerPage import SearchCustomer
# from utilities.customLogger import LogGen
#
# class Test_003_AddCustomer:
#
#     baseURL = ReadConfig.getApplicationURL()
#     username = ReadConfig.getUseremail()
#     password = ReadConfig.getPassword()
#
#     def test_searchCustomer(self,setup):
#         self.driver = setup
#         self.driver.get(self.baseURL)
#         self.lp = LoginPage(self.driver)
#         self.lp.setUserName(self.username)
#         self.lp.setPassword(self.password)
#         self.lp.clickLogin()
#
#         self.addCust = AddCustomer(self.driver)
#         self.addCust.clickOnCustomersMenu()
#         self.addCust.clickOnCustomersMenuItem()
#
#         self.searchCust = SearchCustomer(self.driver)
#         self.searchCust.setSearchEmail("sar@gmail.com")
#         self.searchCust.clickOnsearch()
#         time.sleep(5)
#         self.driver.close()


