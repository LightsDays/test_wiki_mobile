import allure
import pytest
from pages.wikipedia_app import wikipedia


@allure.suite("Мобильные тесты Wikipedia")
@allure.tag("android", "search", "browserstack")
@allure.title("Поиск и возврат результатов поиска")
class TestWikipediaSearch:

    @allure.title("Поиск 'BrowserStack' и верификация результата")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.android
    def test_search_in_wikipedia__valid_query__should_find_results(self):
        wikipedia.close_onboarding()
        wikipedia.search("BrowserStack")
        wikipedia.results_should_contain_text("BrowserStack")