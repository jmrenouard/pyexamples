#!/usr/bin/python3
import time


def timeit(method):
    def timed(*args, **kw):
        ts = time.time()
        result = method(*args, **kw)
        te = time.time()

        print('%r%r Exec time: %2.2f sec' % (method.__name__, args, te - ts))
        return result

    return timed


def traceit(method):
    def timed(*args, **kw):
        print('START - %s =>%r%r' % (time.strftime("%a, %d %b %Y %H:%M:%S", time.gmtime()), method.__name__, args))
        result = method(*args, **kw)
        print('END -%s <=%r%r' % (time.strftime("%a, %d %b %Y %H:%M:%S", time.gmtime()), method.__name__, args))
        return result

    return timed

def avanttapres(method):
    def innerfct(*args, **kw):
        print('Avant %s' % method.__name__)
        result = method(*args, **kw)
        print('Apres %s' % method.__name__)
        return result

    return innerfct

#@traceit
#@timeit
@avanttapres
def attendre(nb_sec=1):
    print("J'attend %d sec." % nb_sec)
    time.sleep(nb_sec)

for i in range(1, 5):
    attendre(i)