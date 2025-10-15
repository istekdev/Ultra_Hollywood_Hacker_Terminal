from termcolor import colored
import random
import time
import os

def hack():
  while True:
    rng = random.getrandbits(10)
    randomhex = os.urandom(32).hex()
    print(colored(f"{randomhex}", "green"))
    if rng == random.getrandbits(10):
      print(colored("Successfully Hacked The Pentagon", "green"))
      break
    elif rng == random.getrantbits(10):
      print(colored("Failed To Hack The Pentagon", "red"))
      break
      
print(colored(">> Welcome To The Ultra Hollywood Hacker Terminal.", "green"))
time.sleep(1)
input(colored(">> ", "green"))
hack()

