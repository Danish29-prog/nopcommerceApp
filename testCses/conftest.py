from selenium import webdriver
import pytest
import pytest_html
import pytest_metadata

@pytest.fixture()
def setup(browser):
    if browser == 'chrome':
        driver = webdriver.Chrome()
    elif browser == 'Firefox':
        driver = webdriver.Firefox()
    else:
        driver= webdriver.Ie
    return driver

def pytest_addoption(parser):
    parser.addoption("--browser")

@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")

def pytest_configure(config):
    print(">>>>>>>>>>>>>>", config)

    #config._metadata['Project Name'] = 'nop commerce'
    #config._metadata['Module Name'] = 'Customers'
    #config._metadata['Tester Name'] = 'Danish'


#@pytest.mark.optionalHook
#def pytest_Metadata(metadata):
    #metadata.pop("JAVA_HOME", None)
   # metadata.pop("Plugins", None)