from datetime import datetime
from enum import Enum
from typing import Optional

from pydantic import BaseModel, Field


class ResponseStatus(str, Enum):
    OK = '00000000'  # Выполнено успешно
    ERROR_AUTH = '00000001'  # Ошибка авторизации
    INTERNAL_ERROR = '00000002'  # Внутренняя ошибка ИС «ЭДиН»
    ERROR_PARAMS = '00000003'  # Ошибка в передаваемых параметрах, может быть только в случае если в changeDocumentStatus передать в качестве статуса что-то отличное от {"R", "N"}
    ERROR_SAVE_IN_ARCH = '00000101'  #Ошибка сохранения в архив
    ERROR_SIGNIN = '00000102'  # Ошибка подписи сообщения
    ERROR_SEND = '00000103'  # Ошибка отправки сообщения
    DAMAGED_SIGNATURE = '00000104'  # Повреждение в подписи сообщения


class DocumentTypes(str, Enum):
    """модель описывает типы документов ЭДиН"""
    BLRWBL = 'BLRWBL'  # Накладная(ЭТТН)
    BLRWBR = 'BLRWBR'  # Ответ на накладную(ЭТТН)
    BLRAPN = 'BLRAPN'  # Системное сообщения(ЭТТН, ЭТН)
    BLRDLN = 'BLRDLN'  # Накладная(ЭТН)
    BLRDNR = 'BLRDNR'  # Ответ на накладную(ЭТН)
    ORDERS = 'ORDERS'  # Заказ
    ORDRSP = 'ORDRSP'  # Ответ на заказ
    DESADV = 'DESADV'  # Уведомление об отгрузке
    RETANN = 'RETANN'  # Возврат товаров
    RECADV = 'RECADV'  # Уведомление о приемке
    APERAK = 'APERAK'  # Системной сообщение(все документы, исключая группу накладных)
    DELCAT = 'DELCAT'  # Каталог организации(организация, торговые точки и т.д.)
    PRODCAT = 'PRODCAT'  # Каталог продуктов
    INVRPT = 'INVRPT'  # Отчет об остатках
    SLSRPT = 'SLSRPT'  # Отчет о продажах
    PRICAT = 'PRICAT'  # Каталог цен PDF Документ в формате
    PDF = 'PDF'
    INVOICE = 'INVOICE'  # Акт выполненных работ
    PARTIN = 'PARTIN'  # Приглашение контрагента

class BaseRequest(BaseModel):
    """Модель с базовыми полями для запроса в систему ЭДиН"""
    Name: str = Field(...)  # Логин для авторизации в системе
    Password: str = Field(...)  # Пароль для авторизации в системе
    #date: Optional[datetime] = Field(default_factory=datetime.now)