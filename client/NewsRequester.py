import base64
import logging
import ntpath
from typing import List, Union

from reportlab.lib.units import inch
from reportlab.pdfgen import canvas
from zeep import Client, Settings

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
        try:
            all_news = self.client.service.GetAllNews()
            news_by_id: Union[dict, None] = next((x for x in all_news if x.id == news_id), {})
        except Exception:
            log.exception(f"[get_news_by_id] Problem with request.")
            return {}
        return news_by_id

    def get_news_by_date(self, date: str) -> List:
        try:
            all_news = self.client.service.GetAllNews()
            news_by_date = [x for x in all_news if x.date == date]
        except Exception:
            log.exception(f"[get_news_by_id] Problem with request.")
            return []
        return news_by_date

    def get_news_by_date_and_category(self, date: str, category_id: int) -> List:
        try:
            all_news = self.client.service.GetAllNews()
            news_by_date_and_category = [x for x in all_news if x.date == date and x.categoryId == category_id]
        except Exception:
            log.exception(f"[get_news_by_id] Problem with request.")
            return []
        return news_by_date_and_category

    def get_news_by_category(self, category_id: int) -> List:
        try:
            all_news = self.client.service.GetAllNews()
            news_by_category = [x for x in all_news if x.categoryId == category_id]
        except Exception:
            log.exception(f"[get_news_by_id] Problem with request.")
            return []
        return news_by_category

    def create_news(self, name: str, desc: str, date: str, category_id: int) -> dict:
        try:
            create_news = self.client.service.CreateNews(name, desc, date, category_id)
        except Exception:
            log.exception(f"[create_news] Problem with request.")
            return {}
        return create_news

    def update_news(self, id: int, name: str, desc: str, date: str, category_id: int) -> dict:
        try:
            self.client.service.UpdateNews(id, name, desc, date, category_id)
            news_by_id = self.get_news_by_id(id)
        except Exception:
            log.exception(f"[update_news] Problem with request.")
            return {}
        return news_by_id

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

    def load_file(self, filepath: str, save_path: str = "imageToSave.png") -> str:
        try:
            result = self.client.service.LoadFile(filepath)
            with open(save_path, "wb") as fh:
                b_decode = base64.standard_b64decode(result.fileData)
                fh.write(b_decode)
        except Exception:
            log.exception(f"[store_file] Problem with making request.")
            return "Problem"
        return save_path

    def generate_pdf(self, news_id: int, filename: str):
        news_by_id = self.get_news_by_id(news_id)
        if not news_by_id:
            return "Problem with generating pdf file, cannot load news"
        path = self.load_file(news_by_id["imagePath"])
        pdf = canvas.Canvas(filename)
        pdf.setTitle(news_by_id['name'])
        pdf.setFont('Courier', 30)
        pdf.drawCentredString(300, 770, news_by_id['name'])
        pdf.setFont('Courier', 20)
        pdf.drawCentredString(300, 750, "Kategoria: " + news_by_id['categoryName'])
        pdf.drawCentredString(300, 730, news_by_id['date'])
        pdf.drawCentredString(300, 710, "Opis")
        text = pdf.beginText(20, 690)
        text.setFont('Courier', 20)

        desc_ = news_by_id['desc']
        desc__split = desc_.split("\n")
        text.textLines(desc__split)
        pdf.drawText(text)
        pdf.drawInlineImage(path, 40, 10, 7*inch,7*inch )
        pdf.save()
