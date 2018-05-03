import os 
os.getcwd()
cd /Users/tangqihao/Documents/GitHub/Python_spring2018
fp=open(r'pi_million_digits.txt','r')
pi=fp.read()
if '19940610'in pi:
    print('Bingo!')
else:
    print('Sorry!')