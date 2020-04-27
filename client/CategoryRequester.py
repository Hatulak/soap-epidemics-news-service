import logging
from typing import List, Union
from zeep import Client, Settings

log = logging.getLogger(__name__)


class CategoryRequester:
    def __init__(self) -> None:
        self.wsdl = 'http://localhost:8080/service/category.wsdl'
        self.settings = Settings(strict=False, xml_huge_tree=True)
        self.client = Client(wsdl=self.wsdl, settings=self.settings)

    def get_all_category(self) -> List:
        try:
            all_category = self.client.service.GetAllCategory()
        except Exception:
            log.exception(f"[get_all_category] Problem with request.")
            return []
        return all_category

    def get_category_by_id(self, category_id: int) -> dict:
        # fixme i dont know why but it dont work :c
        try:
            all_category: List = self.client.service.GetAllCategory()
            category_by_id: Union[dict, None] = next((x for x in all_category if x.id == category_id), {})
        except Exception:
            log.exception(f"[get_category_by_id] Problem with request.")
            return {}
        return category_by_id

    def create_category(self, name: str) -> dict:
        try:
            create_category = self.client.service.CreateCategory(name)
        except Exception:
            log.exception(f"[create_category] Problem with request.")
            return {}
        return create_category

    def update_category(self, id: int, name: str) -> dict:
        try:
            self.client.service.UpdateCategory(id, name)
            category_by_id = self.get_category_by_id(id)
        except Exception:
            log.exception(f"[update_category] Problem with request.")
            return {}
        return category_by_id

    def delete_category(self, id: int) -> str:
        try:
            result = self.client.service.DeleteCategoryById(id)
        except Exception:
            log.exception(f"[delete_category] Problem with request.")
            return "Problem"
        return result

    def authorize(self, login: str, password: str) -> bool:
        try:
            result = self.client.service.Authorize(login, password)
        except Exception:
            log.exception(f"[authorize] Problem with request.")
            return False
        return result
