from pprint import pprint


class DBCharacter:
    def __init__(self, short_name, id, evolution_name, tags, ability_bonus, color):
        self.short_name = short_name
        self.evolution_name = evolution_name
        self.ability_bonus = ability_bonus
        self.id = id
        self.tags = []
        self.tags += tags
        self.color = color


class DBGodKi (DBCharacter):
    def __init__(self, short_name, id, evolution_name, tags, ability_bonus, color):
        tags_ki = ["God Ki"]
        tags_ki += tags
        DBCharacter.__init__(self, short_name, id, evolution_name, tags_ki, ability_bonus, color)


def calc_ability_bonus_two(char1, char2):
    val = (char1.ability_bonus + character_2.ability_bonus) * 2
    return val


def calc_ability_bonus(characters=list()):
    val = 0
    for character in characters:
        val += character.ability_bonus
    val = val * len(characters)
    # print(f"Characters: {character_1.short_name},{character_2.short_name} \n Ability bonus: {ability_bonus}")

    return val


if __name__ == "__main__":
    character_1 = DBGodKi("Goku",
                          "DBL13-01S",
                          "Super Saiyan God SS",
                          tags={"Saiyan", "Son Family"},
                          ability_bonus=23*2,
                          color="Blue")

    character_2 = DBGodKi("Goku Black",
                          "DBL18-06S",
                          "Super Saiyan Rose",
                           tags={"Saiyan", "Future", "Powerful opponent"},
                          ability_bonus=19,
                          color="red")

    characters = (character_1, character_2)
    ability_bonus = calc_ability_bonus(characters)
    print(f"Ability bonus: {ability_bonus}")

    character_3 = DBGodKi("Goku",
                          "DBL20-05S",
                          "Super Saiyan God",
                          tags={"Saiyan", "Son Family"},
                          ability_bonus=19,
                          color="purple")
    character_4 = DBGodKi("beerus",
                          "dbl07 11s",
                          "God of Destruction",
                          tags={"Powerful ", "Twins"},
                          ability_bonus=19,
                          color="green")

    character_5 = DBGodKi("beerus",
                          "dbl07 11s",
                          "God of Destruction",
                          tags={"Powerful ", "Twins"},
                          ability_bonus=23,
                          color="yellow")

    character_6 = DBGodKi("Goku",
                          "DBL15-07S",
                          "Super Saiyan God SS",
                          tags={"Saiyan", "Son Family"},
                          ability_bonus=24,
                          color="Yellow")

    characters = (character_1,character_2,character_3,character_4, character_5, character_6)  # , character_5,)
    ability_bonus = calc_ability_bonus(characters)
    print(f"Ability bonus: {ability_bonus}")

    # characters = (character_1, character_2, character_3, character_4 ) #, character_5,)
    # ability_bonus = calc_ability_bonus(characters)
    # print(f"Ability bonus: {ability_bonus}")



    # character_6 = DBCharacter("Goku",
    #                           "Super Saiyan God SS",
    #                           {"god_ki", "Saiyan", "Son Family"})
    # pprint(character_1.__dict__)
    # pprint(character_2.__dict__)
    # pprint(character_3.__dict__)
