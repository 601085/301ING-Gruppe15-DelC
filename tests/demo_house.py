from smarthouse.domain import SmartHouse, Smartlock, Electricitymeter, HeatPump, SmartPlug, MotionSensor, CO2sensor, \
    Dehumidifier, HumiditySensor, SmartOven, AirQualitySensor, AutomaticGarageDoor, LightBulb, TemperatureSensor

DEMO_HOUSE = SmartHouse()

# Building house structure

# TODO: continue registering the remaining floor, rooms and devices

# Registrer første etasje
ground_floor = DEMO_HOUSE.register_floor(1)
entrance = DEMO_HOUSE.register_room(ground_floor, 13.5, "Entrance")
living_room_kitchen = DEMO_HOUSE.register_room(ground_floor, 35.0, "Living Room/Kitchen")
bathroom_gf = DEMO_HOUSE.register_room(ground_floor, 6.3, "Bathroom")
garage = DEMO_HOUSE.register_room(ground_floor, 19.0, "Garage")
guest_room_1 = DEMO_HOUSE.register_room(ground_floor, 7.0, "Guest Room 1")

# Registrer andre etasje
first_floor = DEMO_HOUSE.register_floor(2)
master_bedroom = DEMO_HOUSE.register_room(first_floor, 15.0, "Master Bedroom")
guest_room_2 = DEMO_HOUSE.register_room(first_floor, 12.0, "Guest Room 2")
guest_room_3 = DEMO_HOUSE.register_room(first_floor, 14.0, "Guest Room 3")
bathroom_ff = DEMO_HOUSE.register_room(first_floor, 9.0, "Bathroom")
dressing_room = DEMO_HOUSE.register_room(first_floor, 4.0, "Dressing Room")
office = DEMO_HOUSE.register_room(first_floor, 11.75, "Office")
hallway = DEMO_HOUSE.register_room(first_floor, 10.0, "Hallway")

# Legg til enheter i rommene
DEMO_HOUSE.register_device(entrance, Smartlock("4d5f1ac6-906a-4fd1-b4bf-3a0671e4c4f1", "MythicalTech", "Guardian Lock 7000"))
DEMO_HOUSE.register_device(entrance, Electricitymeter("a2f8690f-2b3a-43cd-90b8-9deea98b42a7", "MysticEnergy Innovations", "Volt Watch Elite"))

DEMO_HOUSE.register_device(living_room_kitchen, HeatPump("5e13cabc-5c58-4bb3-82a2-3039e4480a6d", "ElysianTech", "Thermo Smart 6000"))
DEMO_HOUSE.register_device(living_room_kitchen, MotionSensor("cd5be4e8-0e6b-4cb5-a21f-819d06cf5fc5", "NebulaGuard Innovations", "MoveZ Detect 69"))
DEMO_HOUSE.register_device(living_room_kitchen, CO2sensor("8a43b2d7-e8d3-4f3d-b832-7dbf37bf629e", "ElysianTech", "Smoke Warden 1000"))

DEMO_HOUSE.register_device(bathroom_gf, HumiditySensor("3d87e5c0-8716-4b0b-9c67-087eaaed7b45", "AetherCorp", "Aqua Alert 800"))

DEMO_HOUSE.register_device(guest_room_1, SmartOven("8d4e4c98-21a9-4d1e-bf18-523285ad90f6", "AetherCorp", "Pheonix HEAT 333"))

DEMO_HOUSE.register_device(garage, AutomaticGarageDoor("9a54c1ec-0cb5-45a7-b20d-2a7349f1b132", "MythicalTech", "Guardian Lock 9000"))

DEMO_HOUSE.register_device(master_bedroom, SmartOven("c1e8fa9c-4b8d-487a-a1a5-2b148ee9d2d1", "IgnisTech Solutions", "Ember Heat 3000"))
DEMO_HOUSE.register_device(master_bedroom, TemperatureSensor("4d8b1d62-7921-4917-9b70-bbd31f6e2e8e", "AetherCorp", "SmartTemp 42"))

DEMO_HOUSE.register_device(guest_room_2, LightBulb("6b1c5f6b-37f6-4e3d-9145-1cfbe2f1fc28", "Elysian Tech", "Lumina Glow 4000"))

DEMO_HOUSE.register_device(guest_room_3, AirQualitySensor("7c6e35e1-2d8b-4d81-a586-5d01a03bb02c", "CelestialSense Technologies", "AeroGuard Pro"))

DEMO_HOUSE.register_device(bathroom_ff, Dehumidifier("9e5b8274-4e77-4e4e-80d2-b40d648ea02a", "ArcaneTech Solutions", "Hydra Dry 8000"))

DEMO_HOUSE.register_device(office, SmartPlug("1a66c3d6-22b2-446e-bf5c-eb5b9d1a8c79", "MysticEnergy Innovations", "FlowState X"))

