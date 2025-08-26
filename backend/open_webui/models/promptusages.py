from typing import Optional
from open_webui.internal.db import Base, get_db

from pydantic import BaseModel, ConfigDict
from sqlalchemy import Column, String, Integer

class PromptUsage(Base):
    __tablename__ = "prompt_usage"
    
    command = Column(String, primary_key=True)
    uses = Column(Integer, default=0)

class PromptUsageModel(BaseModel):
    command: str
    uses: int
    model_config = ConfigDict(from_attributes=True)

class PromptUsageTable:
    def increment(
            self, command: str
    ) -> Optional[PromptUsageModel]:
        try:
            with get_db() as db:
                result = (
                    db.query(PromptUsage)
                    .filter_by(command=command)
                    .first()
                )
                if result is None:
                    result = PromptUsage(
                        command=command,
                        uses=1,
                    )
                    db.add(result)
                else:
                    result.uses += 1
                db.commit()
                db.refresh(result)
                return PromptUsageModel.model_validate(result)
        except Exception:
            return None

    def get_usage_by_command(self, command: str) -> list[PromptUsageModel]:
        try:
            with get_db() as db:
                result = (
                    db.query(PromptUsage)
                    .filter_by(command=command)
                    .first()
                )
                return PromptUsageModel.model_validate(result)
        except Exception:
            return None

PromptUsages = PromptUsageTable()