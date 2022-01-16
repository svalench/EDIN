from pydantic import BaseSettings


class Settings(BaseSettings):
    service_host: str = '127.0.0.1'
    service_port: int = 5000
    service_reload: bool = True
    wsdl_url: str = 'https://soap-test.edn.by/webservice/soap?wsdl'
    request_timeout: int = 60


settings = Settings(
    _env_file='.env',
    _env_file_encoding='utf-8',
)
