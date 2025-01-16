from random import choice


class Weapon:
    def __init__(self) -> None:
        pass


class Armour:
    def __init__(self) -> None:
        pass


class Words:
    def __init__(self) -> None:
        self.read_words_from_storage()

    def read_words_from_storage(self) -> None:
        with open("storage/adjectives.csv") as storage_adjectives:
            self.adjectives = list()
            for adjective in storage_adjectives:
                self.adjectives.append(adjective.strip("\n"))
        with open("storage/nouns_armour.csv") as storage_nouns_armour:
            self.nouns_armour = list()
            for noun in storage_nouns_armour:
                self.nouns_armour.append(noun.strip("\n"))
        with open("storage/nouns_weapons.csv") as storage_nouns_weapons:
            self.nouns_weapons = list()
            for noun in storage_nouns_weapons:
                self.nouns_weapons.append(noun.strip("\n"))
        with open("storage/nouns_of.csv") as storage_nouns_of:
            self.nouns_of = list()
            for noun in storage_nouns_of:
                self.nouns_of.append(noun.strip("\n"))

    def random_adjective(self) -> str:
        return choice(self.adjectives)

    def random_noun_weapon(self) -> str:
        return choice(self.nouns_weapons)

    def random_noun_armour(self) -> str:
        return choice(self.nouns_armour)

    def random_noun_of(self) -> str:
        return choice(self.nouns_of)


if __name__ == "__main__":
    words = Words()
    print(words.random_adjective())
    print(words.random_noun_armour())
    print(words.random_noun_weapon())
    print(words.random_noun_of())
