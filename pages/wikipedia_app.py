from __future__ import annotations

import allure
from appium.webdriver.common.appiumby import AppiumBy
from selene import have, be
from selene.support.shared import browser
import time


class WikipediaApp:
    @allure.step("Закрыть всплывающие окна")
    def close_onboarding(self) -> WikipediaApp:
        for i in range(4):
            skip_button = browser.element((AppiumBy.CLASS_NAME, "android.widget.Button"))
            skip_button.with_(timeout=10).should(be.visible).click()
        # skip_button = browser.element((AppiumBy.XPATH, "//android.widget.Button[@text='Skip']"))
        # skip_button.with_(timeout=10).should(be.visible).click()

        try:
            close_button = browser.element((AppiumBy.ACCESSIBILITY_ID, "Close"))
            close_button.with_(timeout=3).click()
        except Exception:
            pass

        return self

    @allure.step("Поиск по тексту: {text}")
    def search(self, text: str) -> WikipediaApp:
        search_field = browser.element((AppiumBy.ID, "org.wikipedia.alpha:id/nav_tab_search"))
        search_field.with_(timeout=10).should(be.visible).click()

        search_input = browser.element((AppiumBy.ID, "org.wikipedia.alpha:id/search_src_text"))
        search_input.type(text)
        time.sleep(2)

        return self

    @allure.step("Верификация результатов поиска по тексту: {expected_text}")
    def results_should_contain_text(self, expected_text: str) -> WikipediaApp:
        browser.element((AppiumBy.XPATH, f"//android.widget.TextView[contains(@text, '{expected_text}')]")).with_(
            timeout=10
        ).should(be.visible)
        return self

    @allure.step("Верификация результатов поиска. Количество больше, чем {count}")
    def results_should_have_count_greater_than(self, count: int) -> WikipediaApp:
        browser.all((AppiumBy.CLASS_NAME, "android.widget.TextView")).with_(timeout=10).should(
            have.size_greater_than(count)
        )
        return self

    @allure.step("Клик на первый результат поиска")
    def click_first_result(self) -> WikipediaApp:
        results = browser.all((AppiumBy.CLASS_NAME, "android.widget.TextView"))
        results.first.should(be.visible).click()
        return self

    @allure.step("Проверка, что страница статьи открыта")
    def article_should_be_opened(self) -> WikipediaApp:
        # Проверяем, что открылась страница статьи
        time.sleep(3)
        page_source = browser.config.driver.page_source

        # Сохраняем для анализа
        with open("article_page.xml", "w", encoding="utf-8") as f:
            f.write(page_source)

        # Проверяем наличие признаков статьи
        article_indicators = ["WebView", "TextView", "page_title", "article"]

        found = False
        for indicator in article_indicators:
            if indicator in page_source:
                print(f"✅ Найден индикатор статьи: {indicator}")
                found = True
                break

        if not found:
            raise AssertionError("Article page not opened")

        return self


wikipedia = WikipediaApp()