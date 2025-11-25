from product_review_crawling_agents.infrastructure.external.naver_product_crawling_agent import \
    get_naver_shopping_product_reviews


class ProductReviewAgentsUseCase:
    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)

        return cls.__instance

    @classmethod
    def get_instance(cls):
        if cls.__instance is None:
            cls.__instance = cls()
        return cls.__instance

    async def crawling_naver_review_agents(self, product_url: str):
        return get_naver_shopping_product_reviews(product_url)
