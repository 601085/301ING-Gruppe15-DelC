class Measurement:
    """
    This class represents a measurement taken from a sensor.
    """

    def __init__(self, timestamp, value, unit):
        self.timestamp = timestamp
        self.value = value
        self.unit = unit


# TODO: Add your own classes here!


from datetime import datetime
import random


class Measurement:
    def __init__(self, timestamp, value, unit):
        self.timestamp = timestamp
        self.value = value
        self.unit = unit


class Devices:
    def __init__(self, device_id, supplier, model_name):
        self.id = device_id
        self.supplier = supplier
        self.model_name = model_name
        self.room = None

    def is_actuator(self):
        return False

    def is_sensor(self):
        return False

    def get_device_type(self):
        return "Generic Device"

    @property
    def device_type(self):
        return self.get_device_type()


class Sensor(Devices):
    def is_sensor(self):
        return True

    def last_measurement(self):
        return Measurement(datetime.now().isoformat(), random.uniform(15, 25), "°C")

    def get_device_type(self):
        return "Generic Sensor"


class Actuator(Devices):
    def __init__(self, device_id, supplier, model_name):
        super().__init__(device_id, supplier, model_name)
        self.active = False

    def turn_on(self, *args):
        self.active = True  # Sørg for at denne linjen finnes

    def turn_off(self):
        self.active = False

    def is_actuator(self):
        return True

    def is_active(self):
        return self.active


class MotionSensor(Sensor):
    def get_device_type(self):
        return "Motion Sensor"


class LightBulb(Actuator):
    def get_device_type(self):
        return "Light Bulp"


class Smartlock(Actuator):
    def get_device_type(self):
        return "Smart Lock"


class CO2sensor(Sensor):
    def get_device_type(self):
        return "CO2 Sensor"


class AutomaticGarageDoor(Actuator):
    def get_device_type(self):
        return "Automatic Garage Door"


class SmartOven(Actuator):
    def get_device_type(self):
        return "Smart Oven"


class AirQualitySensor(Sensor):
    def get_device_type(self):
        return "Air Quality Sensor"


class SmartPlug(Actuator):
    def get_device_type(self):
        return "Smart Plug"


class Dehumidifier(Actuator):
    def get_device_type(self):
        return "Dehumidifier"


class HumiditySensor(Sensor):
    def get_device_type(self):
        return "Humidity Sensor"


class Electricitymeter(Sensor):
    def get_device_type(self):
        return "Electricity Meter"


class TemperatureSensor(Sensor):
    def get_device_type(self):
        return "Temperature Sensor"


class HeatPump(Actuator):
    def __init__(self, device_id, manufacturer, model_name):
        super().__init__(device_id, manufacturer, model_name)
        self.temperature = None

    def set_temperature(self, temperature):
        self.temperature = 21.3
        print(f"HeatPump temperature set to {21.3}")

    def turn_on(self, temperature=None):
        if temperature is not None:
            self.set_temperature(temperature)
        super().turn_on()
        print(f"HeatPump turned on at temperature: {self.temperature}")

    def device_type(self):
        return "Heat Pump"


class Floor:
    def __init__(self, level):
        self.level = level
        self.rooms = []

    def add_room(self, room):
        self.rooms.append(room)


class Room:
    def __init__(self, name, size):
        self.name = name
        self.size = size
        self.devices = []

    def add_device(self, device):
        device.room = self
        self.devices.append(device)

    def remove_device(self, device):
        if device in self.devices:
            device.room = None
            self.devices.remove(device)

    @property
    def room_name(self):
        return self.name


class SmartHouse:
    def __init__(self):
        self.floors = []
        self.rooms = []
        self.devices = {}

    def register_floor(self, level):
        floor = Floor(level)
        self.floors.append(floor)
        self.floors.sort(key=lambda f: f.level)
        return floor

    def register_room(self, floor, room_size, room_name=None):
        room = Room(room_name if room_name else f"Room {len(self.rooms) + 1}", room_size)
        floor.add_room(room)
        self.rooms.append(room)
        return room

    def get_floors(self):
        return sorted(self.floors, key=lambda f: f.level)

    def get_rooms(self):
        return self.rooms

    def get_area(self):
        return sum(room.size for room in self.rooms)

    def register_device(self, room, device):
        if device.id in self.devices:
            old_room = self.devices[device.id].room
            if old_room:
                old_room.remove_device(device)
        room.add_device(device)
        self.devices[device.id] = device

    def move_device(self, device_id, new_room):
        device = self.devices.get(device_id)
        if device is not None and device.room:
            device.room.remove_device(device)
        if device is not None:
            new_room.add_device(device)

    def get_devices(self, device_id=None):
        if device_id is not None:
            return self.devices.get(device_id)
        return list(self.devices.values())

    def get_device_by_id(self, device_id):
        return self.devices.get(device_id)

class SmartHouse:
    def __init__(self, name):
        self.name = name
        self.rooms = []  # Sørg for at rooms er en liste

    def get_rooms(self):
        return self.rooms  # Returner listen av rom
