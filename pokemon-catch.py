import random
import time
import colorama
from colorama import Fore, Style, init

wild_pokemon = random.choice(["Chikorita", "Snorlax", "Eevee", "Psyduck", "Charizard", "Wheezing", "Magicarp", "Jigglypuff"])
print(Fore.CYAN + f"A wild {wild_pokemon} just appeared!")
if random.random() < 0.05:
    wild_pokemon = "✨ Shiny " + wild_pokemon

time.sleep(1)

inventory = {
    "Pokeball": 5,
    "Great Ball": 2,
    "Ultra Ball": 1
}

catch_rates = {
    "Jigglypuff": 0.9,
    "Magicarp": 0.8,
    "Charizard": 0.7,
    "Chikorita": 0.6,
    "Eevee": 0.5,
    "Psyduck": 0.4,
    "Snorlax": 0.3,
    "Wheezing": 0.1
}

def throw_pokeball():
    ball_bonus = {"Pokeball": 1, "Great Ball": 1.5, "Ultra Ball": 2}
    chosen_ball = input("Choose a ball (Pokeball/Great Ball/Ultra Ball): ")
    rate = catch_rates[wild_pokemon] * ball_bonus[chosen_ball]

    print(Fore.GREEN + f"You threw your Pokeball....")
    time.sleep(1)
    print("*shake*")
    time.sleep(1)
    print("*shake...*")
    time.sleep(1)
    print("*click!*")
    time.sleep(1)
    fun_messages = [
        "You whisper 'gotta catch 'em all' under your breath.",
        "The Pokéball wobbles dramatically...",
        "Your hands are sweating. This is intense.",
        "You deserve a Forest type pokemon so you can touch grass.."
        "Even a Snorlax is more relaxed than you..."
        "You're gonna get caught instead bestie...."
    ]
    print(Fore.MAGENTA + random.choice(fun_messages))
    time.sleep(1)
    if random.random() < rate:
        print(Fore.LIGHTMAGENTA_EX + f"You caught {wild_pokemon}! 🎉")
    else:
        print(Fore.RED + f"{wild_pokemon} broke free! 💨")

while True:
    throw_pokeball()

    try_again = input("\nWanna try again? (yes/no): ")
    if try_again not in ["yes", "y"]:
        print("See you next time, Trainer!")
        break