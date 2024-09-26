import json


def read(file_name):
    try:
        with open(file_name, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        return {'classics': [], 'pops': [], 'reps': []}


def save(info, file_name):
    with open(file_name, 'w', encoding='utf-8') as f:
        json.dump(info, f, indent=4)


def add_classic(info, classic):
    info['classics'].append(classic.m1())


def add_pop(info, pop):
    info['pops'].append(pop.m1())


def add_rep(info, rep):
    info['reps'].append(rep.m1())


def classic_destruction(info, name):
    info['classics'] = [buss for buss in info['classics'] if buss['name'].lower() != name.lower()]


def pop_destruction(info, name):
    info['pops'] = [car for car in info['pops'] if car['name'].lower() != name.lower()]


def rep_destruction(info, name):
    info['reps'] = [truck for truck in info['reps'] if truck['name'].lower() != name.lower()]
