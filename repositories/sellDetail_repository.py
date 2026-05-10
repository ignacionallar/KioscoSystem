from typing import List, Optional
from sqlmodel import Session, select
from models.sellDetail import SellDetail, SellDetailCreate, SellDetailRead, SellDetailUpdate


class ItemRepository:

    def create(self, session: Session, item_in: SellDetailCreate) -> SellDetailRead:
        item = SellDetail.model_validate(item_in)
        session.add(item)
        session.commit()
        session.refresh(item)
        return SellDetailRead.model_validate(item)

    def get_by_id(self, session: Session, item_id: int) -> Optional[SellDetailRead]:
        item = session.get(SellDetail, item_id)
        if not item:
            return None
        return SellDetailRead.model_validate(item)

    def get_all(self, session: Session) -> List[SellDetailRead]:
        items = session.exec(select(SellDetail)).all()
        return [SellDetailRead.model_validate(i) for i in items]

    def get_by_sell(self, session: Session, sell_id: int) -> List[SellDetailRead]:
        items = session.exec(select(SellDetail).where(SellDetail.sell_id == sell_id)).all()
        return [SellDetailRead.model_validate(i) for i in items]

    def update(
        self, session: Session, item_id: int, item_in: SellDetailUpdate
    ) -> Optional[SellDetailRead]:
        item = session.get(SellDetail, item_id)
        if not item:
            return None
        update_data = item_in.model_dump(exclude_unset=True)
        item.sqlmodel_update(update_data)
        session.add(item)
        session.commit()
        session.refresh(item)
        return SellDetailRead.model_validate(item)

    def delete(self, session: Session, item_id: int) -> bool:
        item = session.get(SellDetail, item_id)
        if not item:
            return False
        session.delete(item)
        session.commit()
        return True