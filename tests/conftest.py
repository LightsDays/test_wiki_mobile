import pytest
from appium.options.android import UiAutomator2Options
from selene import browser
from appium import webdriver
import config
from utils import attach


@pytest.fixture(scope='function', autouse=True)
def mobile_management():
    options = UiAutomator2Options().load_capabilities({
        "platformName": config.settings.platform_name,
        "platformVersion": config.settings.platform_version,
        "deviceName": config.settings.device_name,
        "app": config.settings.app_url,
        "appWaitActivity": "org.wikipedia.*",
        'bstack:options': {
            "projectName": "Mobile QA Automation Project",
            "buildName": "Wikipedia Android Tests",
            "sessionName": f"Android test on {config.settings.device_name}",
            "userName": config.settings.browserstack_username,
            "accessKey": config.settings.browserstack_access_key,
        }
    })

    browser.config.driver = webdriver.Remote(config.settings.remote_url, options=options)
    browser.config.timeout = config.settings.timeout

    session_id = browser.driver.session_id

    yield

    attach.add_screenshot(browser)
    attach.add_xml(browser)
    attach.add_video(session_id, config.settings.browserstack_username, config.settings.browserstack_access_key)
    browser.quit()