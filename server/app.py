from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

drone_status = {"state": "standby"}

class CommandRequest(BaseModel):
    command: str

@app.post("/command")
def command(request: CommandRequest):
    command = request.command

    if command not in ["fly", "standby"]:
        raise HTTPException(status_code=400, detail="Invalid command")

    drone_status['state'] = command
    return {"status": "success", "command": command}


@app.get("/status")
def status():
    return drone_status