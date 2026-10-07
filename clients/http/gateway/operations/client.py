from typing import TypedDict
from clients.http.client import HTTPXClient
from httpx import Response, QueryParams

class GetOperationQueryDict(TypedDict):
    """
         Структура данных для получения списка операций для определенного счета.
    """
    accountId: str

class GetOperationSummaryQueryDict(TypedDict):
    """
         Структура данных для получения статистики по операциям для определенного счета.
    """
    accountId: str

class PostOperationMakeFreeRequestDict(TypedDict):
    """
         Структура данных для создания операции комиссии.
    """
    status: str
    amount: int
    cardId: str
    accountId: str

class PostOperationMakeTopUpDict(TypedDict):
    """
         Структура данных для создания операции пополнения.
    """
    status: str
    amount: int
    cardId: str
    accountId: str

class PostOperationMakeCashBackDict(TypedDict):
    """
         Структура данных для создания операции кэшбэка.
    """
    status: str
    amount: int
    cardId: str
    accountId: str

class PostOperationMakeTransferDict(TypedDict):
    """
         Структура данных для создания операции перевода.
    """
    status: str
    amount: int
    cardId: str
    accountId: str

class PostOperationMakePurchaseDict(TypedDict):
    """
         Структура данных для создания операции покупки.
    """
    status: str
    amount: int
    cardId: str
    accountId: str

class PostOperationMakeBillPaymentDict(TypedDict):
    """
         Структура данных для создания операции оплаты по счету.
    """
    status: str
    amount: int
    cardId: str
    accountId: str

class PostOperationMakeCashWithdrawalDict(TypedDict):
    """
         Структура данных для создания операции снятия наличных денег.
    """
    status: str
    amount: int
    cardId: str
    accountId: str

class OperationsGatewayHTTPClient(HTTPXClient):
    """
    Клиент для взаимодействия с /api/v1/operations сервиса http-gateway.
    """
    def get_operations_api(self, query: GetOperationQueryDict) -> Response:
        """
                    Получение списка операций для определенного счета.

                    :param query: строка с id определенного счета.
                    :return: Ответ от сервера (объект httpx.Response).
        """
        return self.get("/api/v1/operations", params=QueryParams(**query))

    def get_operations_summary_api(self, query: GetOperationSummaryQueryDict) -> Response:
        """
                    олучение статистики по операциям для определенного счета.

                    :param query: строка с id определенного счета.
                    :return: Ответ от сервера (объект httpx.Response).
        """
        return self.get("/api/v1/operations/operations-summary", params=QueryParams(**query))

    def get_operation_receipt_api(self, operation_id: str) -> Response:
        """
                     Получение чека по операции.

                    :param query: строка с id определенной операции.
                    :return: Ответ от сервера (объект httpx.Response).
        """
        return self.get(f"/api/v1/operations/operation-receipt/{operation_id}")

    def get_operation_api(self, operation_id: str) -> Response:
        """
                     Получение информации об операции.

                    :param query: строка с id определенной операции.
                    :return: Ответ от сервера (объект httpx.Response).
        """
        return self.get(f"/api/v1/operations/{operation_id}")

    def make_fee_operation_api(self, request: PostOperationMakeFreeRequestDict) -> Response:
        """
                     Создание операции комиссии.

                    :param request: словарь с данными по операции комиссии.
                    :return: Ответ от сервера (объект httpx.Response).
        """
        return self.post("/api/v1/operations/make-fee-operation", json=request)

    def make_top_up_operation_api(self, request: PostOperationMakeTopUpDict) -> Response:
        """
                     Создание операции пополнения.

                    :param request: словарь с данными по операции пополнения.
                    :return: Ответ от сервера (объект httpx.Response).
        """
        return self.post("/api/v1/operations/make-top-up-operation", json=request)

    def make_cashback_operation_api(self, request: PostOperationMakeCashBackDict) -> Response:
        """
                     Создание операции кэшбэка.

                    :param request: словарь с данными по операции кэшбэка.
                    :return: Ответ от сервера (объект httpx.Response).
        """
        return self.post("/api/v1/operations/make-cashback-operation", json=request)

    def make_transfer_operation_api(self, request: PostOperationMakeTransferDict) -> Response:
        """
                     Создание операции перевода.

                    :param request: словарь с данными по операции перевода.
                    :return: Ответ от сервера (объект httpx.Response).
        """
        return self.post("/api/v1/operations/make-transfer-operation", json=request)

    def make_purchase_operation_api(self, request: PostOperationMakePurchaseDict) -> Response:
        """
                     Создание операции покупки.

                    :param request: словарь с данными по операции покупки.
                    :return: Ответ от сервера (объект httpx.Response).
        """
        return self.post("/api/v1/operations/make-purchase-operation", json=request)

    def make_bill_payment_operation_api(self, request: PostOperationMakeBillPaymentDict) -> Response:
        """
                     Создание операции оплаты по счету.

                    :param request: словарь с данными по операции оплаты по счету.
                    :return: Ответ от сервера (объект httpx.Response).
        """
        return self.post("/api/v1/operations/make-bill-payment-operation", json=request)

    def make_cash_withdrawal_operation_api(self, request: PostOperationMakeCashWithdrawalDict) -> Response:
        """
                     Создание операции снятия наличных денег.

                    :param request: словарь с данными по операции снятия наличных денег.
                    :return: Ответ от сервера (объект httpx.Response).
        """
        return self.post("/api/v1/operations/make-cash-withdrawal-operation", json=request)