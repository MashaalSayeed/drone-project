from pydantic import BaseModel


class CommandRequest(BaseModel):
    command: str

class ChangeStatusRequest(BaseModel):
    status: str