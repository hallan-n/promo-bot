from bronze.mercadolivre import MercadolivreBronze
from logging import info
from cache import get
import json


class MercadolivreSilver():
    async def _get_values(self):
        values = await get('mercadolivre')
        if values:
            info('Produtos MercadoLivre em cache.')
            return values

        return await MercadolivreBronze().exec()
    
    def _extract_product(product_raw: str):
        ...
        
    async def exec(self):
        values = await self._get_values()