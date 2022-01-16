
METHODS = ['GET', 'POST']


ERRORS_TEXT = {
    'BAD_METHOD':  f'Не верный тип запроса. Используйте метод из списка: {" ".join(METHODS)}',
    'BAD_PREFIX': 'Путь  запроса не верный',
    'BAD_REQUEST': 'Запрос завершился с ошибкой. Статус %s',
    'BAD_RESPONSE_JSON': 'Ошибка обработки ответ в JSON. Статус %s',
}