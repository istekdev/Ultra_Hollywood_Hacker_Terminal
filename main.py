from termcolor import colored
import random
import time
import os

def hack():
  while True:
    rng = random.getrandbits(10)
    randomhex = os.urandom(32).hex()
    print(colored(f"{randomhex}", "green", attrs=[""]))
    if rng == random.getrandbits(10):
      print(colored("Successfully Hacked The Pentagon", "green", attrs=[""]))
      break
    else:
      print(colored("Failed To Hack The Pentagon", "red", attrs=[""]))
      break
      
print(colored(">> Welcome To The Ultra Hollywood Hacker Terminal.", "green", attrs=[""]))
time.sleep(1)
hack = input(colored(">> ", "green", attrs=[""]))
hack()

