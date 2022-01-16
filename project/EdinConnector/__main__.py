import uvicorn
from .settings import settings

uvicorn.run(
    'EdinConnector.app:app',
    host=settings.service_host,
    port=settings.service_port,
    reload=settings.service_reload,
    )
