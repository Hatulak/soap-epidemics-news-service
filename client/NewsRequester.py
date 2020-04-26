import base64
import ntpath
from typing import List

from zeep import Client, Settings
import logging

log = logging.getLogger(__name__)


class NewsRequester:
    def __init__(self) -> None:
        self.wsdl = 'http://localhost:8080/service/news.wsdl'
        self.settings = Settings(strict=False, xml_huge_tree=True)
        self.client = Client(wsdl=self.wsdl, settings=self.settings)

    def get_all_news(self) -> List:
        try:
            all_news = self.client.service.GetAllNews()
        except Exception:
            log.exception(f"[get_all_news] Problem with request.")
            return []
        return all_news

    def get_news_by_id(self, news_id: int) -> dict:
        # fixme i dont know why but it dont work :c
        try:
            news_by_id = self.client.service.GetNewsById(news_id)
        except Exception:
            log.exception(f"[get_news_by_id] Problem with request.")
            return {}
        return news_by_id

    def create_news(self, name: str, desc: str, date: str, category_id: int) -> dict:
        try:
            create_news = self.client.service.CreateNews(name, desc, date, category_id)
        except Exception:
            log.exception(f"[create_news] Problem with request.")
            return {}
        return create_news

    def delete_news(self, id: int) -> str:
        try:
            result = self.client.service.DeleteNewsById(id)
        except Exception:
            log.exception(f"[delete_news] Problem with request.")
            return "Problem"
        return result

    def store_file(self, filepath: str, news_id: int) -> str:
        try:
            with open(filepath, "rb") as file:
                encoded_string = base64.b64encode(file.read())
                name = ntpath.basename(filepath)
                self.client.service.StoreFile(name, news_id, encoded_string)
        except Exception:
            log.exception(f"[store_file] Problem with making request.")
            return "Problem"

    def load_file(self, filepath: str):
        try:
            result = self.client.service.LoadFile(filepath)
            # fixme only for testing 
            with open("imageToSave.png", "wb") as fh:
                b_decode = base64.standard_b64decode(result.fileData)
                fh.write(b_decode)
        except Exception:
            log.exception(f"[store_file] Problem with making request.")
            return "Problem"
        return result
