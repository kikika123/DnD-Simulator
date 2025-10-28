# file: combat_core.py
import random, time

def roll(low, high):
    return random.randint(low, high)

# Entities
player = {
    "name": "Hero",
    "hp": 30, "max": 30,
    "atk": (4, 8),
    "exp": 0,
    "inventory": {"Potion": 2}
}
enemy = {
    "name": "Goblin",
    "hp": 20, "max": 20,
    "atk": (2, 6),
    "exp_value": 15,
    "loot": {"Potion": 1}
}

turn = "player"
print(f"A wild {enemy['name']} appears!\n")

while True:
    if player["hp"] <= 0:
        print("You were defeated.")
        break
    if enemy["hp"] <= 0:
        print(f"{enemy['name']} defeated! +{enemy['exp_value']} EXP")
        player["exp"] += enemy["exp_value"]
        for item, qty in enemy["loot"].items():
            player["inventory"][item] = player["inventory"].get(item, 0) + qty
        print(f"Looted: {enemy['loot']}")
        print(f"Total EXP: {player['exp']}")
        break

    if turn == "player":
        dmg = roll(*player["atk"])
        enemy["hp"] = max(enemy["hp"] - dmg, 0)
        print(f"{player['name']} hits {enemy['name']} for {dmg} damage.  ({enemy['hp']}/{enemy['max']}) HP left.")
        turn = "enemy"
    else:
        dmg = roll(*enemy["atk"])
        player["hp"] = max(player["hp"] - dmg, 0)
        print(f"{enemy['name']} hits {player['name']} for {dmg} damage.  ({player['hp']}/{player['max']}) HP left.")
        turn = "player"

    time.sleep(1)
