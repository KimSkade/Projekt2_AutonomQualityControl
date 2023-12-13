from aas2openapi_client import client
from aas2openapi_client.api.quality_data_aas.get_items_quality_data_aas_get import sync

client = client.Client(base_url="http://127.0.0.1:8000")
aas = sync(client=client)

print(aas)
