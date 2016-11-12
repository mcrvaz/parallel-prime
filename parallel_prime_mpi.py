import sys
import random
import time
from mpi4py import MPI
from mpi4py.MPI import ANY_SOURCE


def random_list(size, max_value, seed):
    if(seed):
        random.seed(seed)
    r_list = []
    for i in range(0, size):
        r_list.append(random.randint(0, max_value))
    return r_list


def is_prime(num):
    n = num // 2
    if num <= 1:
        return False
    for i in range(2, n + 1):
        if (num % i == 0):
            return False
    return True


def write_primes(file_name, primes):
    with open(file_name, 'w') as file:
        for p in primes:
            file.write(str(p) + '\n' if p is not None else "")


def write_execution_time(file_name, time):
    with open(file_name, 'a') as file:
        file.write(str(time) + " seconds")


def get_next(list):
    if(len(list) > 0):
        return list.pop()
    else:
        return None


if __name__ == '__main__':
    size = int(sys.argv[1])
    max_value = int(sys.argv[2])
    random_seed = int(sys.argv[3])
    file_name = sys.argv[4]

#   Inicialização do comunicador dos processos
    comm = MPI.COMM_WORLD
#   Listagem dos ranks dos processos
    rank = comm.Get_rank()
#   Quantidade de processos
    num_process = comm.Get_size()
    primes = []
    r_list = random_list(size, max_value, random_seed)

#   Procedimentos a serem realizados pelo master
    if rank == 0:
        start_time = time.clock()
        status = MPI.Status()

#       Envia os primeiros números para os processos
        for i in range(1, num_process):
            n = get_next(r_list)
            if not n:
                break
            else:
                comm.send(n, i)

#       Recebe um resultado de um processo
#       e envia um novo número para o processo avaliar
        while True:
            n = get_next(r_list)
            if not n:
                break
            primes.append(comm.recv(None, source=ANY_SOURCE, status=status))
            comm.send(n, status.Get_source())

#       Recebe os últimos resultados enviados pelos slaves
        for i in range(1, num_process):
            primes.append(comm.recv(None, source=ANY_SOURCE, status=status))

#       Envia valores nulos para finalizar os processos(poison pill)
        for i in range(1, num_process):
            comm.send(None, i)

        write_primes(file_name, primes)
        end_time = time.clock() - start_time
        write_execution_time(file_name, end_time)
#   Procedimentos a serem realizados pelos slaves
    else:
#       Processo espera receber um valor para avaliar
        while True:
            n = comm.recv(None, source=0)
#           Caso o valor recebido seja None, finaliza processo
            if n is None:
                break
#           Caso contrário, envia o número para o master
            comm.send(n if is_prime(n) else None, 0)
