import json


def read(file_name):
    try:
        with open(file_name, 'r', encoding='utf-8') as f:
            return json.load(f)
    except Exception as err:
        print(f"Error name: {type(err).__name__}\n Error:{err}\n Try again\n")


def save(info, file_name):
    try:
        with open(file_name, 'w', encoding='utf-8') as f:
            json.dump(info, f, indent=4)
    except Exception as err:
        print(f"Error name: {type(err).__name__}\n Error:{err}\n Try again\n")


def add_buss(info, buss):
    info['busses'].append(buss.m1())


def add_car(info, car):
    info['cars'].append(car.m1())


def add_truck(info, truck):
    info['trucks'].append(truck.m1())


def buss_destruction(info, name):
    info['busses'] = [buss for buss in info['busses'] if buss['name'] != name]


def car_destruction(info, name):
    info['cars'] = [car for car in info['cars'] if car['name'] != name]


def truck_destruction(info, name):
    info['trucks'] = [truck for truck in info['trucks'] if truck['name'] != name]