from bronze.amazon import AmazonBronze
from logging import info
from cache import get
import json


class AmazonSilver():
    async def _get_values(self):
        values = await get('amazon')
        if values:
            info('Produtos Aamazon em cache.')
            return values

        return await AmazonBronze().exec()
    
    def _extract_product(product_raw: str):
        ...
        
    async def exec(self):
        values = await self._get_values()