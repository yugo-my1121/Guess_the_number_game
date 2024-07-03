import sys
import random

print('Number Game Start!')
sys.stdout.buffer.write(b'minNumber>')
sys.stdout.flush()

#最小値入力
minNumber = int(sys.stdin.buffer.readline())

sys.stdout.buffer.write(b'maxNumber>')
sys.stdout.flush()

#最大値入力
maxNumber = int(sys.stdin.buffer.readline())

#探す番号を最小値~最大値の間でランダムに決定
targetNumber = random.randint(minNumber,maxNumber)

print('--------------------------------------')

print('START')

#数字が当たるまでループ
while True:
    sys.stdout.buffer.write(b'number>')
    sys.stdout.flush()

    number = int(sys.stdin.buffer.readline())

    if targetNumber == number :
        break
    else:
        print('No!!!!!!!!')

print('Game Clear!!!!!')
