from pydantic import BaseModel


class CollectProductReviewsRequest(BaseModel):
    product_url: str
