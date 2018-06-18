from parser import Parser
from present import Present
from sender import Request, Initial


def initialize_list():
    request = Initial()
    response = request.initialize_presences_list()

    if response.status_code == 200:
        print('Lista de frequência inicializada com sucesso.')
    elif response.status_code == 500:
        print('Erro ao iniciar lista de frequência.')

def try_post_presence(present):
    request = Request()
    matricula = present.matricula
    response = request.post_presence(present=present)

    if response.status_code == 201:
        print('Presenca do aluno {} enviada com sucesso.'.format(matricula))
    elif response.status_code == 500:
        print('Aluno {} nao cadastrado na turma.'.format(matricula))

if __name__ == '__main__':
    chamada_file_name = 'Chamada.txt'
    try:
        with open(chamada_file_name, 'r') as chamada_file:
            
            initialize_list()

            data = chamada_file.readlines()

            p = Parser(data)
            tuples = p.get_tuples()

            for t in tuples:
                present = Present(*t)
                try_post_presence(present)

    except FileNotFoundError:
            print('Can\'t find file \'{}\' in the current directory.'.format(chamada_file_name))
