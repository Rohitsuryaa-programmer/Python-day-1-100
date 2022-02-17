import random

#
# random_side = random.randint(0,1)
# if random_side == 1:
#     print("heads")
# else:
#     print("tails")

# random person buying

# names_string = input("give something with comma \n")
#
# names = names_string.split(",")
# num_items = (len(names))
# choose = random.randint(0, num_items-1)
# person = names[choose]
#
# print(f"the person who is going to pay is {person}")

# nested lists

# fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
# vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]
# dirty_dozen = [fruits, vegetables]
#
# print(dirty_dozen)
#
# print(dirty_dozen[0])
# print(dirty_dozen[1])
#
# print(dirty_dozen[1][2])
# print(dirty_dozen[1][3])


# rock paper scissors

# rock = '''
#     _______
# ---'   ____)
#       (_____)
#       (_____)
#       (____)
# ---.__(___)
# '''
#
# paper = '''
#     _______
# ---'   ____)____
#           ______)
#           _______)
#          _______)
# ---.__________)
# '''
#
# scissors = '''
#     _______
# ---'   ____)____
#           ______)
#        __________)
#       (____)
# ---.__(___)
# '''
# game_img = [rock, paper, scissors]
# user_choice = int(input("type 0 for rock 1 for paper 2 for scissors \n"))
# if user_choice >= 3 or user_choice < 0:
#     print("you typed a invalid number")
# else:
#     print(game_img[user_choice])
#     computer_choice = random.randint(0, 2)
#     print("computer chose: \n")
#     print(game_img[computer_choice])
#     if user_choice == 0 and computer_choice == 2:
#         print("you win")
#     elif computer_choice == 0 and computer_choice == 2:
#         print("you lose")
#     elif computer_choice > user_choice:
#         print("you lose")
#     elif user_choice > computer_choice:
#         print("you win")
#     elif user_choice == computer_choice:
#         print("its a draw")
