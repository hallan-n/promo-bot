from fastapi import Request, HTTPException
from fastapi.exceptions import RequestValidationError


async def model_validation_handler(request: Request, exc: RequestValidationError):
    errors = []

    for error in exc.errors():
        errors.append(f"{error['loc'][-1]}: {error['msg']}")

    raise HTTPException(
        status_code=422,
        detail=str("|".join(errors))
    )