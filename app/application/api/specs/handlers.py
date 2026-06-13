from fastapi import APIRouter, status

router = APIRouter(tags=["Specs"])

@router.post(
    path="/",
    status_code=status.HTTP_201_CREATED,
    description="Endpoint receives OpenAPI specification via file",
)
async def upload_openapi_specification():
    pass
