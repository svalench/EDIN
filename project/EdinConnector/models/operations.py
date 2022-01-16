from typing import Optional

from pydantic import BaseModel

from EdinConnector.models.base import BaseRequest, ResponseStatus


class ChangeDocumentStatusRequest(BaseRequest):
    """модель данных для запроса изменение статуса документа"""
    TrackingId: str  # Уникальный идентификатор документа
    Status: str  # Статус документа (R = read)


class ChangeDocumentStatusResponse(BaseModel):
    """модель данных ответа запроса изменения статуса документа"""
    Response: ResponseStatus  # Код ответа на запрос
    tracking_id: str  # Уникальный идентификатор документа
    new_document_status: str  # Статус документа (только R)


class SignWithMobileIdRequest(BaseRequest):
    """модель данных для запроса подписи документа"""
    Phone: str  # Номер телефона
    AttributeCertificateUniquePayerNumber: Optional[str]  # УНП
    DocumentId: Optional[str]  # Уникальный идентификатор документа
    Data: Optional[str]  # Контент документа в кодировке base64


class SignWithMobileIdResponse(BaseModel):
    """модель данных ответа по запросу подписи документа"""
    Response: ResponseStatus  # Код ответа на запрос
    Content: str  # Уникальный идентификатор документа
