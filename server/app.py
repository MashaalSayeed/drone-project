from fastapi import FastAPI, HTTPException
from drone import Drone
from schemas import ChangeStatusRequest, CommandRequest

app = FastAPI()
command_list = ['takeoff', 'land', 'hover', 'move', 'rotate']
status_list = ['fly', 'standby', 'off']
drone = Drone()


@app.post("/command")
def post_command(request: CommandRequest):
    command = request.command

    if command not in command_list:
        raise HTTPException(status_code=400, detail="Invalid command")

    drone.command_queue.append(command)
    return {"result": "success", "command": command}

@app.get("/command")
def get_command_list():
    return drone.command_queue


@app.post("/status")
def change_status(request: ChangeStatusRequest):
    status = request.status

    if status not in status_list:
        raise HTTPException(status_code=400, detail="Invalid status")

    drone.drone_status['state'] = status
    return {"result": "success", "status": status}


@app.get("/status")
def get_drone_status():
    return drone.drone_status