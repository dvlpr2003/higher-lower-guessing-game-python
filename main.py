from random import choice

follower_1 = {
    "vijay": {
        "ocupation": "actor",
        "nationality": "India",
        "followers": 100,
    },
    "virat koli": {
        "ocupation": "cricketer",
        "nationality": "India",
        "followers": 150,
    },
    "Thamanna": {
        "ocupation": "actress",
        "nationality": "India",
        "followers": 50,
    },
    "cristiano": {
        "ocupation": "Footboaller",
        "nationality": "brazil",
        "followers": 500,
    },
    "messy": {
        "ocupation": "Footballer",
        "nationality": "americal",
        "followers": 200,
    },
}
list_1 = []
list_2 = []
for i in follower_1:
    list_1.append(i)
choice_1 = choice(list_1)
choice_2 = choice(list_1)
for j in follower_1["Thamanna"]:
    list_2.append(j)


def change_choice():
    global choice_2
    choice_2 = choice(list_1)


if choice_1 == choice_2:
    change_choice()
# print(choice_1)
# print(choice_2)

print(
    f"compare A: {choice_1}, a {follower_1[choice_1][list_2[0]]}, from {follower_1[choice_1][list_2[1]]}"
)

print(
    "________________________________________________VS________________________________________________"
)
print(
    f"compare B: {choice_2}, a {follower_1[choice_2][list_2[0]]}, from {follower_1[choice_2][list_2[1]]}"
)
option = input("Who has more followers? Type 'A' or 'B': ")
if follower_1[choice_1]["followers"] > follower_1[choice_2]["followers"]:
    if option == "A" or option == "a":
        print("your guess is correct.")
    else:
        print("your guess is wrong.")
elif follower_1[choice_2]["followers"] > follower_1[choice_1]["followers"]:
    if option == "B" or option == "b":
        print("your guess is correct.")
    else:
        print("Your guess is wrong. ")
