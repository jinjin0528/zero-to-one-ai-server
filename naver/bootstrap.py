from fastapi import FastAPI

from naver.adapter.input.web.naver_router import get_naver_usecase, naver_router
from naver.application.usecase.naver_usecase import NaverUseCase
from naver.infrastructure.client.naver_search_adapter import NaverSearchApiAdapter


def setup_module(app: FastAPI) -> None:
    """Wire Naver module into the FastAPI app."""
    search_adapter = NaverSearchApiAdapter()
    naver_usecase = NaverUseCase(repository=search_adapter)

    app.dependency_overrides[get_naver_usecase] = lambda: naver_usecase
    app.include_router(naver_router, prefix="/naver")
