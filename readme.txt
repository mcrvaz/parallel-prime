Os parametros são respectivamente, número de elementos, valor máximo, random seed e arquivo de saída.
Na versão paralela é necessário indicar quantos processos serão abertos.

Exemplos de uso:


Paralelo:
    Utiliza 8 processos, gerando uma lista de 100.000 elementos com seu maior valor sendo 100.000.
    Utiliza 2 como seed para o gerador de números aleatórios e escreve a saída no arquivo output_mpi.txt.

    mpiexec /np 8 python parallel_prime_mpi.py 100000 100000 2 output_mpi.txt
Sequencial:
    Gera uma lista de 100.000 elementos com seu maior valor sendo 100.000.
    Utiliza 2 como seed para o gerador de números aleatórios e escreve a saída no arquivo output.txt.

    python prime.py 100000 100000 2 output.txt