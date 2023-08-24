import environment
import agent
import numpy
moves = [0,0,0,0,0,0,0,0,0,0]
perf  = [0,0,0,0,0,0,0,0,0,0]
is_clean = False
for j in range (1,8):
    n = pow(2,j)
    print('Tabla de ' + str(n) + 'x' + str(n) )

    for i in range (0,10):

        E = environment.Environment(n,n,0,0,0.8)
        A = agent.Agent(E)

        (moves[i],perf[i]) = A.think()

        del E
        del A

    print('> Moves: ' + str(moves))
    print('> Perf:  ' + str(perf))

    