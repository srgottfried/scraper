import json
from bs4 import BeautifulSoup
import requests
from scripts.read_config import read_conf

class WebScraper:
    def __init__(self, url: str) -> None:
        self._url = url
        self._all_data = {}
        self._soup = self._get_soup(url)
        self._title = self._scrap_title()
        self._description = self._scrap_description()
        
    def _get_soup(self) -> None:
        try:
            response = requests.get(self._url)
            if response.status_code == 200:
                html = response.content
                self._soup = BeautifulSoup(html, 'lxml')
            raise requests.RequestException('status code: ' + response.status_code)
        except:
            raise requests.RequestException('Invalid web site')

    def _scrap_title(self) -> None:
        try:
            self._all_data["title"] = self._soup.title.string
        except:
            self._all_data["title"] = None

    def _scrap_description(self) -> None:
        try:
            ctrl_size = 0
            conf = read_conf()
            for label in conf.get("labels"):
                for attr in label.get("attrs"):
                    description = self._soup.find(label.get("label"), attrs=attr)
                    if description and len(description['content']) > ctrl_size:
                        self._all_data["description"] = description['content']
                        ctrl_size = len(self._all_data["description"])
        except:
            self._all_data["description"] = None
            
    @property
    def get_title(self) -> str:
        return self._all_data["title"]
    
    @property
    def get_description(self) -> str:
        return self._all_data["description"]
    
    @property
    def get_all_data(self) -> dict:
        return self._all_data
