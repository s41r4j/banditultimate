# Project name  : Bandit Ultimate
# Developer     : S41R4J
import os ,pyperclip ,sys ,time
def verify(x):
	if x>=0 and x<34:
		pass
	elif x==34:
		tp('''\n\nAt this moment, there are no more levels to play in this game.\nHowever, we are constantly working on new levels and will most\nlikely expand this game with more levels soon. Keep an eye out\nfor an announcement on our Discord channel!\n\n''')
		sys.exit()
	else:
		tp('''\nLevel not avalible !!\n 
This is Version ( v1.0 ), if more 'Levels'\nhave been added from 'Over The Wire' : 
Kindly download newer version of this software from ~ \n\n < https://github.com/s41r4j/BanditUltimate > !!\n\n''')
		sys.exit()	
def tp(text):
  for character in text:
    sys.stdout.write(character)
    sys.stdout.flush()
    time.sleep(0.01)
def tps(text):
  for character in text:
    sys.stdout.write(character)
    sys.stdout.flush()
    time.sleep(0.05)      
def ti(text):
  for character in text:
    sys.stdout.write(character)
    sys.stdout.flush()
    time.sleep(0.05)
  value = input()  
  return value  
def cls():
  os.system("clear")
pwd = ['bandit0',
'boJ9jbbUNNfktd78OOpsqOltutMc3MY1',
'CV1DtqXWVFXTvM2F0k09SHz0YwRINYA9',
'UmHadQclWmgdLOKQ3YNgjWxGoRMb5luK',
'pIwrPrtPN36QITSp3EQaw936yaFoFgAB',
'koReBOKuIDDepwhWk7jZC0RTdopnAYKh',
'DXjZPULLxYr17uwoI01bNLQbtFemEgo7',
'HKBPTKQnIay4Fw76bEy8PVxKEDQRKTzs',
'cvX2JJa4CFALtqS87jk27qwqGhBM9plV',
'UsvVyFSfZZWbi6wgC7dAFyFuR6jQQUhR',
'truKLdjsbJ5g7yyJ2X2R0o3a5HQJFuLk',
'IFukwKGsFW8MOq3IRFqrxE1hxTNEbUPR',
'5Te8Y4drgCRfCx8ugdwuEX8KFC6k2EUu',
'8ZjyCRiBWFYkneahHwxCv3wb2a1ORpYL',
'4wcYUJFw0k0XLShlDzztnTBHiqxU3b3e',
'BfMYroe26WYalil77FoDi9qh59eK5xNr',
'cluFn7wTiGryunymYOu4RcffSxQluehd',
'xLYVMN9WE5zQ5vHacb0sZEVqbrp7nBTn',
'kfBf3eYk5BPBRzwjqutbbfE887SVc5Yd',
'IueksS7Ubh8G3DCwVzrTd8rAVOwq3M5x',
'GbKksEFF4yrVs6il55v6gwY5aVje5f0j',
'gE269g2h3mw3pwgrj0Ha9Uoqen1c9DGr',
'Yk7owGAcWjwMVRwrTesJEwB7WVOiILLI',
'jc1udXuA1tiHqjIsL8yaapX5XIAI6i0n',
'jc1udXuA1tiHqjIsL8yaapX5XIAI6i0n',
'uNG9O58gUE7snukf3bvZ0rxhtnjzSGzG',
'5czgV9L3Xx8JPOyRbXh6lQbmIOWvPT6Z',
'3ba3118a22e93127a4ed485be72ef5ea',
'0ef186ac70e04ea33b4c1853d2526fa2',
'bbc96594b4e001778eee9975372716b2',
'5b90576bedb2cc04c86a9e924ce42faf',
'47e603bb428404d265f59c42920d81e5',
'56a9bf19c63d650ce78e6ec0354ee45e',
'c9c3199ddf4121b10cf581a98d51caee',]

cls()
tp('========================================\n')
tp('||          Bandit Ultimate           ||\n')
tp('========================================\n')
tp('                                 ~S41R4J\n')
tp('========================================\n')
tp('\nVisit Github page:\n')
tp('> https://github.com/s41r4j\n\n')
tp('========================================\n')
tp("Bandit is Over The Wire's wargame :     \n\n")
tp('https://overthewire.org/wargames/bandit/\n\n')
tp('========================================\n\n')
l= ti("[#] Connect with Bandit Level [ 0-34 ] : \n >  ")
ll = int(l)
verify(ll) 
s1 = 'ssh -p 2220 bandit'
s2 = '@bandit.labs.overthewire.org'
cmd = s1 + l + s2
pwds = pwd[ll]
pyperclip.copy(pwds)
cls()
tp('====================================\n')
tps('\nThe password of the level is copied \nin your clipboard ! \n\n')
tps("When prompted to 'Enter password' ,\npaste it with following two ways :\n\n")
tps('1)      Ctrl + Shift + V\n        (For Linux Terminal)\n\n')
tps("2)      Right click & select 'Paste'\n        (Recommended Way)")
tp('\n\n====================================\n') 
time.sleep(5)
cls()
tps('[#] Connecting to Bandit server .')
time.sleep(1)
tps('.')
time.sleep(1)
tps('.\n\n')
os.system(cmd)