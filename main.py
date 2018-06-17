from parser import Parser
from present import Present


if __name__ == '__main__':
    chamada_file_name = 'Chamada.txt'
    try:
        with open(chamada_file_name, 'r') as chamada_file:
            print('File \'{}\' opened successfully.'.format(chamada_file_name))
            data = chamada_file.readlines()

            p = Parser(data)
            tuples = p.get_tuples()
            for t in tuples:
                present = Present(*t)
                print(present)

    except FileNotFoundError:
            print('Can\'t find file \'{}\' in the current directory.'.format(chamada_file_name))
