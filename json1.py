import json


def read(file_name):
    try:
        with open(file_name, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        return {'classics': [], 'rock': [], 'pops': [], 'reps': []}


def save(info, file_name):
    with open(file_name, 'w', encoding='utf-8') as f:
        json.dump(info, f, indent=4)


def add_classic(info, classic):
    info['classics'].append(classic.m1())


def add_rock(info, rock):
    info['rocks'].append(rock.m1())


def add_pop(info, pop):
    info['pops'].append(pop.m1())


def add_rep(info, rep):
    info['reps'].append(rep.m1())


def classic_destruction(info, name):
    info['classics'] = [classic for classic in info['classics'] if classic['name'].lower() != name.lower()]


def rock_destruction(info, name):
    info['rocks'] = [rock for rock in info['rocks'] if rock['name'].lower() != name.lower()]


def pop_destruction(info, name):
    info['pops'] = [pop for pop in info['pops'] if pop['name'].lower() != name.lower()]


def rep_destruction(info, name):
    info['reps'] = [rep for rep in info['reps'] if rep['name'].lower() != name.lower()]
