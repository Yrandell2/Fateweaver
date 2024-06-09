import random
import time
import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)


class Game:

    def __init__(self):
        # all numbers used in the game by category
        self.numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26
                         , 27, 28, 29, 30, 31, 32, 33, 34, 35, 36]
        self.black = [2, 4, 8, 10, 11, 13, 16, 17, 20, 22, 24, 26, 28, 29, 33, 35]
        self.red = [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]
        self.odd = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35]
        self.even = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36]
        # valid answers
        self.valid = ["Red", "red", "Black", "black", "Odd", "odd", "Even", "even",
                      "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17",
                      "18",
                      "19",
                      "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31", "32", "33", "34", "35",
                      "36"]

        self.red_mult = 1.5
        self.black_mult = 1.5
        self.even_mult = 1.5
        self.odd_mult = 1.5
        self.num_mult = 3
        self.z_mult = 5

        self.money = 300
        print("base money : 300")

        self.play_phase = True
        self.shop_phase = False
        self.turn = 0
        self.previous_turn = self.turn

        def give(amount):
            self.money += amount

    def run(self):
        running = True
        # game loop
        while running:
            # play phase

            while self.play_phase:
                # title
                print("")
                # stats
                print(f"{Fore.GREEN}you have {self.money}$ \n")
                if self.money <= 0:
                    self.play_phase = False
                print(f"{Fore.BLUE}YOUR STATS: \n Red : Mult : x{self.red_mult}$ \n Black : Mult : x{self.black_mult}$"
                      f" \n Even : Mult : x{self.even_mult}$ \n Odd : Mult : x{self.odd_mult}$ \n")
                # questions
                bid_answer = input(
                    "Choose One option from the following: You can bid on \n - Red or Black \n - Even or Odd \n "
                    "- Any number between 0 and 36 \n >>>")
                # exceptions
                if str(bid_answer) not in self.valid:
                    print(f"error, wrong answer. answer should not be {bid_answer}")
                    continue
                # questions

                # game
                if str(bid_answer) == "Red" or "red":
                    bid = int(input("how much ? \n >>>"))
                    # exceptions
                    if bid > self.money:
                        print("you don't have this much >:")
                        continue
                    self.money -= bid
                    n = random.choice(self.numbers)
                    if n in self.red:
                        print(f"the number is {n}, red : {Fore.GREEN} Won !")
                        self.money += bid * self.red_mult
                        for i in range(2):
                            time.sleep(1)
                            print(".")
                        self.play_phase = False
                        self.shop_phase = True
                    else:
                        print(f"the number is {n}, black : {Fore.RED} lose :(")
                        for i in range(2):
                            time.sleep(1)
                            print(".")
                        self.play_phase = False
                        self.shop_phase = True
                elif str(bid_answer) == "Black" or "black":
                    bid = int(input("how much ? \n >>>"))
                    # exceptions
                    if bid > self.money:
                        print("you don't have this much >:")
                        continue
                    self.money -= bid
                    n = random.choice(self.numbers)
                    if n in self.black:
                        print(f"the number is {n}, black : {Fore.GREEN} Won !")
                        self.money += bid * self.black_mult
                        for i in range(2):
                            time.sleep(1)
                            print(".")
                        self.play_phase = False
                        self.shop_phase = True
                    else:
                        print(f"the number is {n}, red : {Fore.RED} lose :(")
                        for i in range(2):
                            time.sleep(1)
                            print(".")
                        self.play_phase = False
                        self.shop_phase = True
                elif str(bid_answer) == "Odd" or "odd":
                    bid = int(input("how much ? \n >>>"))
                    # exceptions
                    if bid > self.money:
                        print("you don't have this much >:")
                        continue
                    self.money -= bid
                    n = random.choice(self.numbers)
                    if n in self.odd:
                        print(f"the number is {n}, odd : {Fore.GREEN} Won !")
                        self.money += bid * self.odd_mult
                        for i in range(2):
                            time.sleep(1)
                            print(".")
                        self.play_phase = False
                        self.shop_phase = True
                    else:
                        print(f"the number is {n}, even : {Fore.RED} lose :(")
                        for i in range(2):
                            time.sleep(1)
                            print(".")
                        self.play_phase = False
                        self.shop_phase = True
                elif str(bid_answer) == "Even" or "even":
                    bid = int(input("how much ? \n >>>"))
                    # exceptions
                    if bid > self.money:
                        print("you don't have this much >:")
                        continue
                    self.money -= bid
                    n = random.choice(self.numbers)
                    if n in self.even:
                        print(f"the number is {n}, even : {Fore.GREEN} Won !")
                        for i in range(2):
                            time.sleep(1)
                            print(".")
                        self.money += bid * self.even_mult
                        self.play_phase = False
                        self.shop_phase = True
                    else:
                        print(f"the number is {n}, odd : {Fore.RED} lose :(")
                        for i in range(2):
                            time.sleep(1)
                            print(".")
                        self.play_phase = False
                        self.shop_phase = True
                elif int(bid_answer) in self.numbers and int(bid_answer) != 0:
                    bid = int(input("how much ? \n >>>"))
                    # exceptions
                    if bid > self.money:
                        print("you don't have this much >:")
                        continue
                    self.money -= bid
                    n = random.choice(self.numbers)
                    if n in self.numbers:
                        print(f"the number is {n} : {Fore.GREEN} Won !!!")
                        self.money += bid * self.num_mult
                        for i in range(2):
                            time.sleep(1)
                            print(".")
                        self.play_phase = False
                        self.shop_phase = True
                    else:
                        print(f"the number is {n} : {Fore.RED} lose :(")
                        for i in range(2):
                            time.sleep(1)
                            print(".")
                        self.play_phase = False
                        self.shop_phase = True
                elif int(bid_answer) == 0:
                    bid = int(input("how much ? \n >>>"))
                    # exceptions
                    if bid > self.money:
                        print("you don't have this much >:")
                        continue
                    self.money -= bid
                    n = random.choice(self.numbers)
                    if n == 0:
                        print(f"the number is {n} !!! You {Fore.GREEN} Won !!!")
                        self.money += bid * self.z_mult
                        for i in range(2):
                            time.sleep(1)
                            print(".")
                        self.play_phase = False
                        self.shop_phase = True
                    else:
                        print(f"the number is {n} : {Fore.RED} lose :(")
                        # delay
                        for i in range(2):
                            time.sleep(1)
                            print(".")
                        self.play_phase = False
                        self.shop_phase = True
                else:
                    continue

            # shop phase
            while self.shop_phase:
                print(f"{Fore.BLUE}{Back.LIGHTBLACK_EX}SHOP PHASE !")
                print("what do you want to buy ?")
                print(f"you have {self.money}$")
                print("  >> Double Red (red now give *3 money) --> 300$")
                print("  >> Double Black (green now give *3 money) --> 300$")
                print("  >> Double Odd (odd now give *3 money) -R-> 300$")
                print("  >> Double Even (even now give *3 money) --> 300$")
                print("say skip if you're good...")
                shop_answer = input(">>")
                if shop_answer == 'skip':
                    self.shop_phase = False
                elif shop_answer == "Double Red" or "double red":
                    if self.money < 300:
                        print("you don't have this much")
                        continue
                    if self.money >= 300:
                        self.red_mult = 3
                        print("Double Red Owned ! Red now give *3 money !")
                        continue
                elif shop_answer == "Double Black" or "double black":
                    if self.money < 300:
                        print("you don't have this much")
                        continue
                elif shop_answer == "Double Odd" or "double odd":
                    if self.money < 300:
                        print("you don't have this much")
                        continue
                elif shop_answer == "Double Even" or "double even":
                    if self.money < 300:
                        print("you don't have this much")
                        continue
            self.play_phase = True
        # END
