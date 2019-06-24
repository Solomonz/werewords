#! /usr/bin/env python3

from random import choice, shuffle
from subprocess import run, PIPE
import sys

if __name__ == "__main__":
    names = list(set(map(lambda name: name.strip(), sys.argv[1:])))
    if len(names) != 5:
        print('must have 5 players!')
        sys.exit(1)
    shuffle(names)
    mayor = choice(names)

    wolf = choice(names)
    
    seer = choice(names)
    while seer == wolf:
        seer = choice(names)

    run(['bash', '-c', 'rm -rf game && mkdir game'], stdout=PIPE, stderr=PIPE)

    for name in names:
        with open('game/' + name, "w") as f:
            if name == mayor:
                f.write('mayor\n')

            if name == wolf:
                f.write('wolf\n')

            if name == seer:
                f.write('seer\n')

            if name not in {mayor, wolf, seer}:
                f.write('villager\n')
