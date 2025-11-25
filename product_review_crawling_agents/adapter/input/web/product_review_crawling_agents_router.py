from fastapi import APIRouter

from product_review_crawling_agents.adapter.input.web.request.collect_product_reviews_request import \
    CollectProductReviewsRequest
from product_review_crawling_agents.application.usecase.product_review_crawling_agents_usecase import \
    ProductReviewAgentsUseCase

product_review_crawling_agents_router = APIRouter(tags=["product_review_crawling_agents"])

usecase = ProductReviewAgentsUseCase.get_instance()


@product_review_crawling_agents_router.post("/naver")
async def crawling_reviews(request: CollectProductReviewsRequest):
    url = request.product_url
    reviews = await usecase.crawling_naver_review_agents(url)
    return reviews
