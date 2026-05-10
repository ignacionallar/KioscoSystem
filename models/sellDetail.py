from typing import Optional
from sqlmodel import SQLModel, Field, Relationship


class SellDetailBase(SQLModel):
    quantity: int
    unit_price: float
    product_id: int = Field(foreign_key="product.id")
    sell_id: int = Field(foreign_key="sell.id")


class SellDetail(SellDetailBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    sell: Optional["Sell"] = Relationship(back_populates="details") # pyright: ignore


class SellDetailCreate(SellDetailBase):
    pass


class SellDetailRead(SellDetailBase):
    id: int


class SellDetailUpdate(SQLModel):
    quantity: Optional[int] = None
    unit_price: Optional[float] = None