from sqlalchemy import Column, ForeignKey, TEXT
from sqlalchemy.orm import relationship

from app.util.dao import Base


class WorkContent(Base):
    __tablename__ = 'work_content'

    user_id = ForeignKey('work_date.user_id', nullable=False)
    work_day = ForeignKey('work_date.work_day', nullable=False, unique=True)
    todo = Column(TEXT, nullable=True)
    done = Column(TEXT, nullable=True)

    work_date = relationship('MyWorkDate')
