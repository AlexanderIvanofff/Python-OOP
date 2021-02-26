from project.pokemon import Pokemon


class Trainer:
    def __init__(self, name):
        self.name = name
        self.pokemon = []

    def add_pokemon(self, pokemon: Pokemon):
        if pokemon in self.pokemon:
            return f"This pokemon is already caught"

        self.pokemon.append(pokemon)
        return f"Caught {pokemon.name} with health {pokemon.health}"

    def release_pokemon(self, pokemon_name: str):
        player = [p for p in self.pokemon if p.name == pokemon_name]
        if not player:
            return f"Pokemon is not caught"
        current_pokemon = player[0]
        self.pokemon.remove(current_pokemon)
        return f"You have released {pokemon_name}"

    def trainer_data(self):
        res = f"Pokemon Trainer {self.name}\nPokemon count {len(self.pokemon)}\n"
        for p in self.pokemon:
            res += f'- {p.pokemon_details()}\n'
        return res


pokemon = Pokemon("Pikachu", 90)
print(pokemon.pokemon_details())
trainer = Trainer("Ash")
print(trainer.add_pokemon(pokemon))
second_pokemon = Pokemon("Charizard", 110)
print(trainer.add_pokemon(second_pokemon))
print(trainer.release_pokemon("Pikachu"))
print(trainer.trainer_data())
