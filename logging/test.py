

from test import *


def fun(x,y):
    if y==0:
        log.error('y cant be 0')
    return (x/y)

try:
    fun(2,0)
except Exception as e:
    log.error(e)
	