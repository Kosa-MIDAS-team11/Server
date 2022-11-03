from sqlalchemy import Column, ForeignKey, TIME
from sqlalchemy.orm import relationship

from app.util.dao import Base


class WorkContent(Base):
    __tablename__ = 'work_time'

    user_id = ForeignKey('work_date.user_id', nullable=False)
    work_day = ForeignKey('work_date.work_day', nullable=False, unique=True)
    start_at = Column(TIME, nullable=True)
    end_at = Column(TIME, nullable=True)

    work_date = relationship('MyWorkDate')
