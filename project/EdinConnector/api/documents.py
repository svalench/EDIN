from typing import List

from fastapi import APIRouter, Body

from EdinConnector.EdinConnector import EDiNConnector
from EdinConnector.models.documents import ListDocumentsResponse, ListDocumentsRequest, GetDocumentRequest, \
    GetDocumentResponse, SendDocumentRequest, SendDocumentResponse

router =APIRouter(
    prefix='/documents',
)


@router.post('/', response_description="Список документов", response_model=List[ListDocumentsResponse])
async def get_list_doc(request: ListDocumentsRequest = Body(...)):
    edin = EDiNConnector()
    res = edin.send_soap_request('ListDocuments', request)
    print(res)
    return res


@router.post('/get/doc', response_description="Получение документа по ID", response_model=GetDocumentResponse)
async def get_doc(request: GetDocumentRequest = Body(...)):
    edin = EDiNConnector()
    res = edin.send_soap_request('GetDocument', request)
    print(res)
    return res


@router.post('/send/doc', response_description="Отправка документа", response_model=SendDocumentResponse)
async def send_doc(request: SendDocumentRequest = Body(...)):
    edin = EDiNConnector()
    res = edin.send_soap_request('SendDocument', request)
    print(res)
    return res