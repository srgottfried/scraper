from datetime import date
import pytest
import requests
from WebScraper import WebScraper, ScrapCustomMetadataException, ScrapDefaultMetadataException

def test_get_title():
    url = "https://example.com"
    scraper = WebScraper(url)
    expected_title = "Example Domain"
    assert scraper.get_title == expected_title

def test_get_date():
    url = "https://example.com"
    scraper = WebScraper(url)
    expected_date = str(date.today())
    assert scraper.get_date == expected_date

def test_get_all_data():
    url = "https://example.com"
    scraper = WebScraper(url)
    all_data = scraper.get_all_data
    assert isinstance(all_data, dict)
    assert "title" in all_data
    assert "date" in all_data

def test_invalid_url():
    invalid_url = "httpsinvalidurlcom"
    with pytest.raises(requests.RequestException):
        WebScraper(invalid_url)

def test_scrap_custom_metadata_exception():
    url = "https://example.com"
    invalid_options = {
        "metadata": [
            {
                "invalid_name": "custom_data",
                "invalid_label": "custom_data",
                "invalid_attrs": [],
                "invalid_class_": []
            }
        ]
    }
    with pytest.raises(ScrapCustomMetadataException):
        scraper = WebScraper(url)
        scraper._conf = invalid_options
        scraper._scrap_custom_metadata()
