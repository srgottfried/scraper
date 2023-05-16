import json
import requests
from bs4 import BeautifulSoup
from datetime import date
from exceptions import ScrapCustomMetadataException, ScrapDefaultMetadataException

class WebScraper:
    def __init__(self, url: str) -> None:
        self.DEFAULT_CONFIG_URI = "config/options.json"
        self._url = url
        self._all_data = {}
        self._get_soup()
        self._get_conf()
        self._scrap_default_metadata()
        self._scrap_custom_metadata()
        
    def _get_soup(self) -> None:
        try:
            response = requests.get(self._url)
            if response.status_code == 200:
                html = response.content
                self._soup = BeautifulSoup(html, 'lxml')
            else:
                raise requests.RequestException('status code: ' + response.status_code)
        except:
            raise requests.RequestException('Invalid web site')
            
    def _get_conf(self) -> dict:
        try:
            file = open(file=self.DEFAULT_CONFIG_URI, mode="r", encoding="UTF8")
            self._conf = json.loads(file.read())
            file.close()
        except:
            raise FileNotFoundError('options.json file not found')

    def _scrap_default_metadata(self) -> None:
        try:
            self._all_data["title"] = self._soup.title.string
            self._all_data["date"] = str(date.today())
        except:
            raise ScrapDefaultMetadataException()

    def _scrap_custom_metadata(self) -> None:
        try:
            for simple_data in self._conf["metadata"]:
                ctrl_size = 0
                name = simple_data["name"]
                for attr in simple_data["attrs"]:
                    content = self._soup.find(simple_data["label"], attrs=attr)
                    if content and len(content['content']) > ctrl_size:
                        self._all_data[name] = content['content']
                        ctrl_size = len(self._all_data[name])
                for class_ in simple_data["class_"]:
                    content = self._soup.find(simple_data["label"], class_=class_)
                    if content and len(content['content']) > ctrl_size:
                        self._all_data[name] = content['content']
                        ctrl_size = len(self._all_data[name])
        except:
            raise ScrapCustomMetadataException()
            
    @property
    def get_title(self) -> str:
        return self._all_data["title"]

    @property
    def get_date(self) -> str:
        return self._date["date"]
    
    @property
    def get_all_data(self) -> dict:
        return self._all_data
    
    
