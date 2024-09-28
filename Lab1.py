import json1
import xml1
from Info import Classic, Rock, Pop, Rep


class FormatError(Exception):
    pass


def get_genre(genre_name):
    while True:
        try:
            print('\nEnter genre name: ')
            genre = str(input())
            if genre.lower() == genre_name:
                return genre
            else:
                print(f'\n---------\n{genre}\n-----------------\n')
                print('\nWrong genre!')
        except Exception as e:
            print(f'Error; {str(e)}')


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
            print(f"Error: {str(e)}")


def print_from_file(info, file_format):
    if file_format == 'json':
        print('Data from json:')
    elif file_format == 'xml':
        print('Data from xml:')

    print('\n-----------------------------\nClassic songs:')
    for classic in info['classics']:
        print(f'\nName: {classic["name"]} \nGenre: {classic["genre"]}')

    print('\n-----------------------------\nRock songs:')
    for rock in info['rocks']:
        print(f'\nName: {rock["name"]} \nGenre: {rock["genre"]}')

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
        info = json1.read(file_name)
        xfile = json1
    elif file_format == 'xml':
        file_name = 'info.xml'
        info = xml1.load_from_xml(file_name)
        xfile = xml1
    else:
        print('\nWrong format')
        return

    while True:
        print('\nChoose:'
              '\n1 - add classic song'
              '\n2 - add rock song'
              '\n3 - add pop song'
              '\n4 - add rep song'
              '\n5 - delete classic song'
              '\n6 - delete rock song'
              '\n7 - delete pop song'
              '\n8 - delete rep song'
              '\n9 - show json'
              '\n10 - show xml'
              '\n11 - save'
              '\n12 - exit')

        choice = input().strip() # strip удаляет ненужные пробелы

        if choice == '1':
            genre_name = 'классика'
            name = input('\nEnter song name: ')
            genre = get_genre(genre_name)

            classic = Classic(name, genre)
            xfile.add_classic(info, classic)

        if choice == '2':
            genre_name = 'рок'
            name = input('\nEnter song name: ')
            genre = get_genre(genre_name)

            rock = Rock(name, genre)
            xfile.add_rock(info, rock)

        elif choice == '3':
            genre_name = 'поп'
            name = input('\nEnter song name: ')
            genre = get_genre(genre_name)
            long = get_long_of_song('\nEnter song duration in seconds: ')

            pop = Pop(name, genre, long)
            xfile.add_pop(info, pop)

        elif choice == '4':
            genre_name = 'рэп'
            name = input('\nEnter song name: ')
            genre = get_genre(genre_name)
            long = get_long_of_song('\nEnter song duration in seconds: ')
            pip = input('\nEnter song author: ')

            rep = Rep(name, genre, long, pip)
            xfile.add_pop(info, rep)

        elif choice == '5':
            name = input('\nEnter song name: ')

            xfile.classic_destruction(info, name)
            print('\nDestruction complete!')

        elif choice == '6':
            name = input('\nEnter song name: ')

            xfile.rock_destruction(info, name)
            print('\nDestruction complete!')

        elif choice == '7':
            name = input('\nEnter song name: ')

            xfile.pop_destruction(info, name)
            print('\nDestruction complete!')

        elif choice == '8':
            name = input('\nEnter song name: ')

            xfile.rep_destruction(info, name)
            print('\nDestruction complete!')

        elif choice == '9':
            try:
                if file_format != 'json':
                    print('\nI cant do this, because you choose another format!')
                else:
                    print_from_file(info, file_format)
            except FormatError as e:
                print(f"Error: {e}")

        elif choice == '10':
            try:
                if file_format != 'xml':
                    print('\nI cant do this, because you choose another format!')
                else:
                    print_from_file(info, file_format)
            except FormatError as e:
                print(f"Error: {e}")

        elif choice == '11':
            if json1 == xfile:
                json1.save(info, file_name_json)
            elif xml1 == xfile:
                xml1.save(info, file_name_xml)
            print('\nSave complete!')

        elif choice == '12':
            print('\nThe program is shutting down!')
            break


main()