    inventoryLevel: NeedInventory | None = None
    currency: Currency
    __typename: str


class Miners(BaseModel):
    available: bool
    id: int
    level: int
    name: str
    price: int
    currency: Currency
    minerLevel: list[MinerLevel]
    __typename: str


class Cart(BaseModel):
    auto: bool
    available: bool
    id: int
    image: str
    level: int
    name: str
    price: int
    volume: int
    currency: Currency
    miningCurrency: Currency
    __typename: str


class UserExpeditions(BaseModel):
    amount: int | None
    created_at: datetime
    status: str
    name: str
    image: str
    id: int
    price: int
    currency: Currency
    __typename: str