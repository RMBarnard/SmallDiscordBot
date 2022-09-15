import discord
import random

class Player:
    def __init__(self, name, start_health = 20):
        self.health = start_health
        self.alive = True
        self.x = 0
        self.y = 0
        self.name = name

    def __str__(self):
        return self.name

    def damage(self, amount):
        self.health -= amount
        if self.health <= 0:
            self.alive = False
    
    def heal(self, amount):
        self.health += amount


def battle(p1, p2):
    title=f"{p1} has challenged {p2} to a battle!"
    player1 = Player(p1)
    player2 = Player(p2)
    turn = random.choice([player1, player2])
    if turn == player1:
        other = player2
    else:
        other = player1
    description=f'By the ruling of Notch, {turn} will have the first move!\n\n'

    while turn.alive and other.alive:
        damage = 0
        level = ""
        flip = random.uniform(0,1)
        if flip < 0.15:
            damage = random.randrange(3, 7)
            level = "heal"
            turn.heal(damage)
            
        elif flip > .75:
            damage = random.randrange(9,14)
            level = "high"
            other.damage(damage)

        else:
            damage = random.randrange(2,9)
            level = "low"
            other.damage(damage)

        description += get_action(turn, other, level, damage)

        if not turn.alive:
            description += f"{other} is victorious!"
        elif not other.alive:
            description += f"{turn} is victorius!"
        
        temp = other
        other = turn
        turn = temp

    return discord.Embed(title = title, description=description)

def get_action(p1, p2, damage, amount):
    damage_low = [
        f"{p1} grabbed a wooden stick and smacked {p2} on the head with it for {amount} damage.\n",
        f"{p1} stuck an arrow in {p2}'s foot for {amount} damage.\n",
        f"{p1} threw a stack of snowballs at {p2} for {amount} damage.\n",
        f"{p1} snagged {p2} with a fishing rod for {amount} damage\n"
    ]

    damage_high = [
        f"{p1} hit {p2} with a sharpness 1000 stick and did {amount} damage\n",
        f"{p1} pushed {p2} into a lava pit for {amount} damage.\n",
        f"{p1} shot a flaming arrow at {p2} for {amount} damage.\n"
    ]

    heal_options = [
        f"{p1} consumed a potion of healing and regained {amount} health.\n",
        f"{p1} ate a golden apple to increase their health by {amount} points.\n"
    ]

    if damage == "high":
        return random.choice(damage_high) + f"**{p2} has {0 if p2.health < 0 else p2.health} health remaining.**\n\n"
    elif damage == "low":
        return random.choice(damage_low) + f"**{p2} has {0 if p2.health < 0 else p2.health} health remaining.**\n\n"
    else:
        return random.choice(heal_options) + f"**{p1} has {p1.health} health remaining.**\n\n"