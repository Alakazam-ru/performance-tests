from httpx import Response
from clients.http.client import HTTPXClient
from typing import TypedDict

class CreateCartRequestDict(TypedDict):
    """
         Структура данных для создания новой карты.
    """
    userId: str
    accountId: str

class CardsGatewayHTTPClient(HTTPXClient):
    """
        Клиент для взаимодействия с /api/v1/cards сервиса http-gateway.
    """
    def issue_physical_card_api(self, request: CreateCartRequestDict) -> Response:
        """
                    Создание новой физической карты.

                    :param request: Словарь с данными новой карты.
                    :return: Ответ от сервера (объект httpx.Response).
        """
        return self.post("/api/v1/cards/issue-physical-card", json=request)
    def issue_virtual_card_api(self, request: CreateCartRequestDict) -> Response:
        """
                    Создание новой виртуальной карты.

                    :param request: Словарь с данными новой карты.
                    :return: Ответ от сервера (объект httpx.Response).
        """
        return self.post("/api/v1/cards/issue-virtual-card", json=request)