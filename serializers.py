from typing import List, Optional
from datetime import datetime
from pydantic import BaseModel


class OverloadSerializer(BaseModel):
    id: str
    client_guid: str
    created_at: datetime
    updated_at: datetime
    action_type: str
    db_table: str
    row_id: Optional[int]
    model_name: Optional[str]
    user_id: Optional[str]
    is_active: bool


class OverloadListSerializer(BaseModel):
    detected_users: List[OverloadSerializer]
