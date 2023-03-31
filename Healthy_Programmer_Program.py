import time
from pygame import mixer
from datetime import datetime
from Eye import eye
from Physical import physical
from Water import water
from concurrent.futures import ThreadPoolExecutor

s2=datetime.now().hour
s3=datetime.now().weekday()
if s2>9 and s2<17 and s3<5 :
    print("Dear Programmer, to take care of your health, you will do the following tasks druing your workday:\n 1. Drink a 250ml glass of water every 35 mins during this workday \n 2. Perform eye exercise every 30 mins \n 3. Perform some Physical Activity every 45 mins \n \n You will need to make a specific entry once you have done these tasks.")

    def main():
        with ThreadPoolExecutor() as pool:
            pool.submit(eye)
            pool.submit(physical)
            pool.submit(water)
    if __name__ == "__main__":
        main()
    
    exit()
else :
    print("You don't need to work right now! Go and Chill!")
    exit()