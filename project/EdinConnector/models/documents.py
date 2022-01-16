from datetime import datetime, date
from typing import Optional

from pydantic import BaseModel

from EdinConnector.models.base import BaseRequest, DocumentTypes, ResponseStatus


class ListDocumentsRequest(BaseRequest):
    """модель данных запроса списка документов"""
    pass


class ListDocumentsResponse(BaseModel):
    """модель данных ответа по запросу списка документов"""
    Response: ResponseStatus  # Код ответа на запрос
    partner_iln: str  # Идентификатор отправителя документа
    tracking_id: str  # Уникальный идентификатор документа
    document_type: DocumentTypes  # Тип документа
    document_version: str  # Версия документа
    document_standard: str  # Стандарт документа
    document_test: str  # Признак тестирования
    document_status: str  # Статус документа (новый, копия)
    document_number: str  # Номер документа
    document_date: date  # Дата документа
    receive_date: datetime  # Дата получения документа платформой
    file_name: str  # Имя файла
    delivery_iln: str  # Идентификатор точки доставки
    ship_from_iln: str  # Идентификатор точки загрузки
    status: str  # Системный статус документа
    receiver_iln: str  # Идентификатор получателя
    content_waybill_number: Optional[str]  # Номер накладной
    content_reference_document_number: Optional[str]  # Ссылка на номер документа
    content_error_or_acknowledgement_code: Optional[str]  # Код ошибки или подтверждения


class GetDocumentRequest(BaseRequest):
    """модель данных для запроса одного документа"""
    PartnerIln: Optional[str]  # Идентификатор получателя
    DocumentType: Optional[DocumentTypes]  # Тип документа
    TrackingId: str  # Уникальный идентификатор документа


class GetDocumentResponse(BaseModel):
    """модель данных ответа по запросу документа"""
    Response: ResponseStatus  # Код ответа на запрос
    FileName: str  # Имя файла
    FileData: str  # Контент документа в кодировке base64


class SendDocumentRequest(BaseRequest):
    """модель данных для запроса отправки документа в ЭДиН"""
    PartnerIln: Optional[str]  # Идентификатор получателя
    DocumentType: Optional[DocumentTypes]  # Тип документа
    FileName: str  # Имя файла
    Data: str  # Контент документа в кодировке base64


class SendDocumentResponse(BaseModel):
    """модель данных ответа по запросу отправки документа в ЭДиН"""
    Response: ResponseStatus  # Код ответа на запрос
    Content: str  # Уникальный идентификатор документа


class SendDraftRequest(BaseRequest):
    """модель данных для запроса отправки черновика в ЭДиН"""
    SenderIln: str  # Идентификатор отправителя
    PartnerIln: str  # Идентификатор получателя
    DocumentType: DocumentTypes  # Тип документа
    FileName: str  # Имя файла
    DocumentNumber: Optional[str]  # Номер документа
    Data: str  # Контент документа в кодировке base64


class SendDraftResponse(BaseModel):
    """модель данных ответа по запросу отправки черновика в ЭДиН"""
    Response: ResponseStatus  # Код ответа на запрос
    Content: str  # Уникальный идентификатор документа