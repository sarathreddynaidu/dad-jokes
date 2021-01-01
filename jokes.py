from art import *
from termcolor import colored
from colorama import init
import requests
from random import choice

init()

heading = text2art("Dad Joke !!!")
print(colored(heading, "cyan"))

user_input = input("Let me tell you a joke! Give me a topic: ")

url = "https://icanhazdadjoke.com/search"

res = requests.get(
	url,
	headers = {"Accept": "application/json"},
	params = {"term": user_input}
	).json()

# print(res)

num_jokes = res["total_jokes"]

results = res["results"]

if num_jokes == 1:
	print(f"I've got one joke about {user_input}. Here it is:")
	print(results[0]["joke"])
elif num_jokes > 1:
	print(f"I've got {num_jokes} jokes about {user_input}. Here's one:")
	print(choice(results)["joke"])
else:
	print(f"Sorry, I don't have any jokes about {user_input}! Please try again")
