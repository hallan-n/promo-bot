import asyncio
from stores.amazon import Amazon



asd = asyncio.run(Amazon().exec())
import json
print(json.dumps(asd, indent=4))

