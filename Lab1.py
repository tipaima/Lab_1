import json
import xml
from Info import Classic, Pop, Rep


def get_long_of_song(x):
    while True:
        try:
            seconds = int(input(x))
            if seconds > 0:
                return seconds
            else:
                print("Need a positive number!")
        except ValueError:
            print("Need integer!")
        except Exception as e:
            print(f"Произошла ошибка: {str(e)}")


def print_from_file(info, filename):
    if filename == 'json':
        print('Data from json:')
    elif filename == 'xml':
        print('Data from xml:')

    print('\n-----------------------------\nClassic songs:')
    for classic in info['classics']:
        print(f'\nName: {classic["name"]} \nGenre: {classic["genre"]}')

    print('\n-----------------------------\nPop songs:')
    for pop in info['pops']:
        print(f'\nName: {pop["name"]} \nGenre: {pop["genre"]} \nDuration: {pop["long"]}')

    print('\n-----------------------------\nRep songs:')
    for rep in info['reps']:
        print(f'\nName: {rep["name"]} \nGenre: {rep["genre"]} \nDuration: {rep["long"]} \nAuthor: {rep["pip"]}')


def main():
    print('Choose file format (json/xml):')
    file_format = input().lower()  # lower превращает все большое в маленькое
    file_name_json = 'info.json'
    file_name_xml = 'info.xml'
    if file_format == 'json':
        file_name = 'info.json'
        info = json.read(file_name)

    elif file_format == 'xml':
        file_name = 'info.xml'
        info = xml.load_from_xml(file_name)

    else:
        print('\nWrong format')
        return

    k = 0

    while True:
        print('\nChoose:'
              '\n1 - add classic song'
              '\n2 - add pop song'
              '\n3 - add rep song'
              '\n4 - delete classic song'
              '\n5 - delete pop song'
              '\n6 - delete rep song'
              '\n9 - exit')

        choice = input().strip() # strip удаляет ненужные пробелы

        if choice == '1':
            name = input()
            genre = input()
        elif choice == '2':
            name = input()
            genre = input()
            long = input()
        elif choice == '3':
            name = input()
            genre = input()
            long = input()
            pip = input()
        elif choice == '4':
            name = input()
        elif choice == '5':
            name = input()
        elif choice == '6':
            name = input()
        elif choice == '9':
            break

