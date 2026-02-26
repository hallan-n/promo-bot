from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError, HTTPException
import uvicorn
from api.middlewares import model_validation_handler
from models import Ingestion
from tasks import ingestion


app = FastAPI(title="Promo BOT")
app.add_exception_handler(RequestValidationError, model_validation_handler)


@app.post("/", status_code=200, summary="Realiza a ingestão de produtos")
async def realize_products_ingestion(ingestions: list[Ingestion]):
    try:
        await ingestion(ingestions)
        return {"success": True}
    except Exception as e:
        raise HTTPException(500, f"Erro na ingestão: {e}")


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
