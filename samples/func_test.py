import os, sys
print('version info: %s' % (sys.version_info, ))
print('file real path: %s' % os.path.realpath(__file__))
print('file dir: %s' % os.path.dirname(os.path.realpath(__file__)))
print('file name: %s' % os.path.dirname(sys.argv[0]))
print(sys.argv, len(sys.argv))
print(sys.argv[0])

'''
Console output:

version info: sys.version_info(major=3, minor=7, micro=5, releaselevel='final', serial=0)
file dir: /Users/i306454/gitStore/you-get/build_in_func_test.py
file name: 
'''


def multi_args(**kwargs):
    print(kwargs)
    
kws = {'first':'jack01', 'second':'jack02', 'third':'jack03'}
multi_args(**kws)
