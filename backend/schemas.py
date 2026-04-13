from pydantic import BaseModel

class ChurnInput(BaseModel):
    Age: int
    Family_size: int
    Late_Delivery: str
    Poor_Hygiene: str
    Bad_past_experience: str
    Long_delivery_time: str
    More_Offers_and_Discount: str
    Good_Food_quality: str
    Ease_and_convenient: str


class ChurnResponse(BaseModel):
    prediction: str