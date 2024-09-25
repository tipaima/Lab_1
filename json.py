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


def add_classic(info, song):
    info['classic'].append(song.m1())


def add_pop(info, song):
    info['pop'].append(song.m1())


def add_rep(info, song):
    info['rep'].append(song.m1())


def classic_destruction(info, name):
    info['classic'] = [buss for buss in info['classic'] if buss['name'] != name]


def pop_destruction(info, name):
    info['pop'] = [car for car in info['pop'] if car['name'] != name]


def rep_destruction(info, name):
    info['rep'] = [truck for truck in info['rep'] if truck['name'] != name]
