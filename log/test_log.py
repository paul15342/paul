from log.Log import *
import codecs
log.info('this is testing')

def fun(x,y):
    """随意测试"""
    return x/y

try:
    fun(2,0) >0
except Exception as e:
    log.error('分母不能为0 {}'.format(e))