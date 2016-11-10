import sys
import random
import time


def random_list(size, max_value, seed):
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


def get_primes(num_list):
    return filter(is_prime, num_list)


def write_primes(file_name, primes):
    file = open(file_name, 'w')
    for p in primes:
        file.write(str(p) + '\n')
    file.close()


def write_execution_time(file_name, time):
    with open(file_name, 'a') as file:
        file.write(str(time) + " seconds")


if __name__ == '__main__':
    size = int(sys.argv[1])
    max_value = int(sys.argv[2])
    random_seed = int(sys.argv[3])
    file_name = sys.argv[4]

    start_time = time.clock()
    write_primes(
        file_name,
        get_primes(random_list(size, max_value, random_seed))
    )
    end_time = time.clock() - start_time
    write_execution_time(file_name, end_time)
