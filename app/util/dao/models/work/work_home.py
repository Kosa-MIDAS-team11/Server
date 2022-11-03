from sqlalchemy import Column, ForeignKey, DATE
from sqlalchemy.orm import relationship

from app.util.dao import Base


class WorkContent(Base):
    __tablename__ = 'work_home'

    user_id = ForeignKey('work_date.user_id', nullable=False)
    work_day = ForeignKey('work_date.work_day', nullable=False, unique=True)
    start_at = Column(DATE, nullable=True)
    ent_at = Column(DATE, nullable=True)

    work_date = relationship('MyWorkDate')
