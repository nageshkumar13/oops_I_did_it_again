##############################################################################################
#                           Smart Home System
##############################################################################################

class SmartDevice:
    def __init__(self, device_id):
        self.device_id = device_id
        self.connected = False

    def connect_to_wifi(self):
        self.connected = True
        print(f"{self.device_id} connected to wifi.") 

    def disconnect_wifi(self):
        self.connected = False
        print(f"{self.device_id} is disconnected from wifi.")

    def is_connected(self):
        return self.connected
               
class SmartVaccum(SmartDevice):
    def clean_floor(self):
        if self.is_connected():
            print(f"{self.device_id} : Vacuming the floor.")
        else:
            print(f"{self.device_id} not connected to wifi.")    

class SmartCam(SmartDevice):
    def detect_motion(self):
        if self.is_connected():
            print(f"{self.device_id} : Detected motion.")
        else:
            print(f"{self.device_id} not connected to wifi.")    

cleaner = SmartVaccum("Vaccume_bot")
cleaner.clean_floor()
cleaner.connect_to_wifi()
cleaner.clean_floor()
cleaner.disconnect_wifi()
cleaner.clean_floor()