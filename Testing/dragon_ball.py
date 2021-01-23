from pprint import pprint


class DBCharacter:
    def __init__(self, short_name, id, evolution_name, tags, ability_bonus):
        self.short_name = short_name
        self.evolution_name = evolution_name
        self.ability_bonus = ability_bonus
        self.id = id
        self.tags = []
        self.tags += tags


class DBGodKi (DBCharacter):
    def __init__(self, short_name, id, evolution_name, tags, ability_bonus):
        tags_ki = ["God Ki"]
        tags_ki += tags
        DBCharacter.__init__(self, short_name, id, evolution_name, tags_ki, ability_bonus)


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
                          ability_bonus=23*2)

    character_2 = DBGodKi("Goku Black",
                          "DBL18-06S",
                          "Super Saiyan Rose",
                          {"Saiyan", "Future", "Powerful opponent"},
                          ability_bonus=19)

    characters = (character_1, character_2)
    ability_bonus = calc_ability_bonus(characters)
    print(f"Ability bonus: {ability_bonus}")

    character_3 = DBGodKi("Goku",
                          "DBL20-05S",
                          "Super Saiyan God",
                          {"Saiyan", "Son Family"},
                          ability_bonus=19)

    characters = (character_1, character_2, character_3)
    ability_bonus = calc_ability_bonus(characters)
    print(f"Ability bonus: {ability_bonus}")

      # character_4 = DBCharacter("Goku",
    #                           "Super Saiyan God SS",
    #                           {"god_ki", "Saiyan", "Son Family"})
    #
    # character_5 = DBCharacter("Goku",
    #                           "Super Saiyan God SS",
    #                           {"god_ki", "Saiyan", "Son Family"})
    #
    # character_6 = DBCharacter("Goku",
    #                           "Super Saiyan God SS",
    #                           {"god_ki", "Saiyan", "Son Family"})
    # pprint(character_1.__dict__)
    # pprint(character_2.__dict__)
    # pprint(character_3.__dict__)
