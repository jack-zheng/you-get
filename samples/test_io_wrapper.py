import sys, io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf8')

sys.stdout.write('First line')
sys.stdout.flush()

sys.stdout.write('\r' + 'Second line')
sys.stdout.flush()