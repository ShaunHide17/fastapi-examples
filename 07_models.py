from sqlmodel import Field, SQLModel, create_engine, Relationship
from datetime import datetime
import os

# Data Models
class Item(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True, index=True)
    name: str
    description: str | None = None
    price: float = Field(ge=0)
    tax: float | None = None
    basket_id: int | None = Field(default=None, foreign_key="baskets.id")
    __tablename__ = "items"

class Basket(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    user: str
    items: list[Item] = Relationship()
    total_price: float
    total_tax: float
    updated_at: datetime | None = Field(default=datetime.now())
    __tablename__ = "baskets"

if __name__ == "__main__":
  current_dir = os.path.dirname(os.path.abspath(__file__))
  sqlite_file_name = f"{current_dir}/database.db"
  sqlite_url = f"sqlite:///{sqlite_file_name}"

  engine = create_engine(sqlite_url, echo=True)

  SQLModel.metadata.create_all(engine)