import xml.etree.ElementTree as ET


def Otstupi(elem, level=0):
    i = "\n" + level * "  "
    if len(elem):
        if not elem.text or not elem.text.strip():
            elem.text = i + "  "
        if not elem.tail or not elem.tail.strip():
            elem.tail = i
        for subelem in elem:
            Otstupi(subelem, level + 1)
        if not subelem.tail or not subelem.tail.strip():
            subelem.tail = i
    else:
        if level and (not elem.tail or not elem.tail.strip()):
            elem.tail = i


def save(info, filename):
    root = ET.Element('info')

    classics = ET.SubElement(root, 'classics')
    for classic in info['classics']:
        classic_element = ET.SubElement(classics, 'classic')
        for key, value in classic.items():
            branch = ET.SubElement(classic_element, key)
            branch.text = str(value)

    pops = ET.SubElement(root, 'pops')
    for pop in info['pops']:
        pop_element = ET.SubElement(pops, 'pop')
        for key, value in pop.items():
            branch = ET.SubElement(pop_element, key)
            branch.text = str(value)

    reps = ET.SubElement(root, 'reps')
    for rep in info['reps']:
        rep_element = ET.SubElement(reps, 'rep')
        for key, value in rep.items():
            branch = ET.SubElement(rep_element, key)
            branch.text = str(value)

    Otstupi(root)

    tree = ET.ElementTree(root)
    tree.write(filename, encoding='utf-8', xml_declaration=True)


def load_from_xml(filename):
    try:
        tree = ET.parse(filename)
        root = tree.getroot()
    except FileNotFoundError:
        return {'classics': [], 'rocks': [], 'pops': [], 'reps': []}

    info = {'classics': [], 'rocks': [], 'pops': [], 'reps': []}

    for classic in root.find('classics'):
        classic_info = {}
        for branch in classic:
            classic_info[branch.tag] = branch.text
        info['classics'].append(classic_info)

    for rock in root.find('rocks'):
        rock_info = {}
        for branch in rock:
            rock_info[branch.tag] = branch.text
        info['rocks'].append(rock_info)

    for pop in root.find('pops'):
        pop_info = {}
        for branch in pop:
            pop_info[branch.tag] = branch.text
        info['pops'].append(pop_info)

    for rep in root.find('reps'):
        rep_info = {}
        for branch in rep:
            rep_info[branch.tag] = branch.text
        info['reps'].append(rep_info)

    return info


def add_classic(info, classic):
    info['classics'].append(classic.m1())


def add_rock(info, rok):
    info['rocks'].append(rok.m1())


def add_pop(info, pop):
    info['pops'].append(pop.m1())


def add_rep(info, rep):
    info['reps'].append(rep.m1())


def classic_destruction(info, name):
    space = []
    for classic in info['classics']:
        if classic['name'].lower() != name.lower():
            space.append(classic)

    info['classics'] = space


def rock_destruction(info, name):
    space = []
    for rock in info['rocks']:
        if rock['name'].lower() != name.lower():
            space.append(rock)

    info['rocks'] = space


def pop_destruction(info, name):
    space = []
    for pop in info['pops']:
        if pop['name'].lower() != name.lower():
            space.append(pop)

    info['pops'] = space


def rep_destruction(info, name):
    space = []
    for rep in info['reps']:
        if rep['name'].lower() != name.lower():
            space.append(rep)

    info['reps'] = space
