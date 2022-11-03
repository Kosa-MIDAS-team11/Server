from sqlalchemy import Column, ForeignKey, DATE, Boolean, TIME, TEXT
from sqlalchemy.orm import relationship

from app.util.dao import Base


class WorkDate(Base):
    __tablename__ = 'work_adte'

    work_day = Column(DATE, primary_key=True)
    user_email = Column(ForeignKey('user.email'), primary_key=True)
    at_home = Column(Boolean, nullable=False, default=False)
    end_at = Column(TIME)
    start_at = Column(TIME)
    home_start_at = Column(DATE)
    home_end_at = Column(DATE)
    todo = Column(TEXT)
    done = Column(TEXT)

    user = relationship('User')
