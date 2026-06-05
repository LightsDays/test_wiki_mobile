import os

from pydantic_settings import BaseSettings
from appium.options.android import UiAutomator2Options
from appium.options.ios import XCUITestOptions


class Settings(BaseSettings):
    # BrowserStack credentials
    browserstack_username: str = os.getenv("BROWSERSTACK_USERNAME", "")
    browserstack_access_key: str = os.getenv("BROWSERSTACK_ACCESS_KEY", "")
    remote_url: str = os.getenv("REMOTE_URL", "http://hub.browserstack.com/wd/hub")

    # Android capabilities
    platform_name: str = os.getenv("PLATFORM_NAME", "android")
    platform_version: str = os.getenv("PLATFORM_VERSION", "9.0")
    device_name: str = os.getenv("DEVICE_NAME", "Google Pixel 3")
    app_url: str = os.getenv("APP_URL", "")

    # Timeouts
    timeout: float = float(os.getenv("TIMEOUT", "10.0"))

    # Browser management
    hold_browser_open: bool = os.getenv("HOLD_BROWSER_OPEN", "false").lower() == "true"
    save_page_source_on_failure: bool = os.getenv("SAVE_PAGE_SOURCE_ON_FAILURE", "true").lower() == "true"

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

    @property
    def driver_options_android(self) -> UiAutomator2Options:
        """Configure Android driver options for BrowserStack"""
        options = UiAutomator2Options()
        options.load_capabilities({
            "platformName": self.platform_name,
            "platformVersion": self.platform_version,
            "deviceName": self.device_name,
            "app": self.app_url,
            "appWaitActivity": "org.wikipedia.*",
            "bstack:options": {
                "userName": self.browserstack_username,
                "accessKey": self.browserstack_access_key,
                "projectName": "Mobile QA Automation Project",
                "buildName": "Wikipedia Android Tests",
                "sessionName": f"Android test on {self.device_name}",
                "local": "false",
                "debug": "true",
                "networkLogs": "true",
                "consoleLogs": "info",
            }
        })
        return options

    @property
    def driver_options_ios(self) -> XCUITestOptions:
        """Configure iOS driver options for BrowserStack"""
        options = XCUITestOptions()
        options.load_capabilities({
            "platformName": "ios",
            "platformVersion": "16.0",
            "deviceName": "iPhone 14",
            "app": self.app_url,
            "bstack:options": {
                "userName": self.browserstack_username,
                "accessKey": self.browserstack_access_key,
                "projectName": "Mobile QA Automation Project",
                "buildName": "Wikipedia iOS Tests",
                "sessionName": "iOS test on iPhone 14",
                "local": "false",
                "debug": "true",
                "networkLogs": "true",
                "consoleLogs": "info",
            }
        })
        return options


settings = Settings()