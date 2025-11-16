from pydantic import BaseModel, Field


class MarzbanCoreStats(BaseModel):
    """Core statistics schema"""

    version: str = Field(..., title="Version")
    started: bool = Field(..., title="Started")
    logs_websocket: str = Field(..., title="Logs Websocket")
