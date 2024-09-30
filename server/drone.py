class Drone:
    """
    Class that will be connected to the drone and will store information and commands
    """

    def __init__(self):
        self.connected = False
        self.command_queue = []
        self.drone_status = {
            "state": "off",
            "battery": 100,
        }