from __future__ import annotations

import allure
import pytest

from pages.wikipedia_app import wikipedia


@allure.suite("Мобильные тесты Wikipedia - iOS")
@allure.tag("ios", "search", "browserstack")
@allure.title("iOS: Wikipedia поиск")
@pytest.mark.skip(reason="iOS должен быть загружен и настроен")
class TestIOSWikipedia:

    @allure.title("iOS: поиск 'BrowserStack' на iPhone")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.ios
    def test_ios_search_in_wikipedia__valid_query__should_find_results(self):
        # Given: Wikipedia iOS app is open
        wikipedia.close_onboarding()

        # When: User searches for "BrowserStack"
        # Note: iOS selectors might differ from Android
        wikipedia.search("BrowserStack")

        # Then: Search results should be displayed
        wikipedia.results_should_contain_text("BrowserStack")

        allure.attach(
            "iOS тесты запущены BrowserStack\n"
            "Примечание: Актуальный iOS селектор должен быть адаптирован под приложение Wikipedia iOS",
            name="ios_test_info",
            attachment_type=allure.attachment_type.TEXT
        )