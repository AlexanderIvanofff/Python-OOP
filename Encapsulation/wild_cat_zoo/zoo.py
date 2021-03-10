class Zoo:
    def __init__(self, name, budget, animal_capacity, workers_capacity):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals = []
        self.workers = []

    def add_animal(self, animal, price):
        if self.__budget >= price and len(self.animals) < self.__animal_capacity:
            self.animals.append(animal)
            self.__budget -= price
            return f"{animal.name} the {animal.__class__.__name__} added to the zoo"
        elif len(self.animals) < self.__animal_capacity and self.__budget < price:
            return f'Not enough budget'
        return f'Not enough space for animal'

    def hire_worker(self, worker):
        if len(self.workers) < self.__workers_capacity:
            self.workers.append(worker)
            return f"{worker.name} the {worker.__class__.__name__} hired successfully"
        return f'Not enough space for worker'

    def fire_worker(self, worker_name):
        try:
            worker = [w for w in self.workers if w.name == worker_name][0]
            self.workers.remove(worker)
            return f'{worker_name} fired successfully'
        except IndexError:
            return f'There is no {worker_name} in the zoo'

        # if worker_name not in self.workers:
        #     return f'There is no {worker_name} in the zoo'
        # else:
        #     self.workers.remove(worker_name)
        #     return f'{worker_name} fired successfully'

    def pay_workers(self):
        all_salary = sum([c.salary for c in self.workers])
        if self.__budget >= all_salary:
            self.__budget -= all_salary
            return f'You payed your workers. They are happy. Budget left: {self.__budget}'
        return f"You have no budget to pay your workers. They are unhappy"

    def tend_animals(self):
        all_cost_for_animals = sum([t.get_needs() for t in self.animals])
        if self.__budget >= all_cost_for_animals:
            self.__budget -= all_cost_for_animals
            return f"You tended all the animals. They are happy. Budget left: {self.__budget}"
        return f"You have no budget to tend the animals. They are unhappy."

    def profit(self, profit):
        self.__budget += profit

    def animals_status(self):
        lions = [a for a in self.animals if a.__class__.__name__ == 'Lion']
        tigers = [a for a in self.animals if a.__class__.__name__ == 'Tiger']
        cheetah = [a for a in self.animals if a.__class__.__name__ == 'Cheetah']

        result = f'You have {len(self.animals)} animals' + '\n'

        result += f'----- {len(lions)} Lions:' + "\n"
        result += "{}".format('\n'.join([repr(l) for l in lions])) + "\n"

        result += f'----- {len(tigers)} Tigers:' + "\n"
        result += "{}".format('\n'.join([repr(t) for t in tigers])) + "\n"

        result += f'----- {len(cheetah)} Cheetahs:' + "\n"
        result += "{}".format('\n'.join([repr(c) for c in cheetah]))
        return result

    def workers_status(self):
        keepers = [k for k in self.workers if k.__class__.__name__ == 'Keeper']
        caretakers = [c for c in self.workers if c.__class__.__name__ == 'Caretaker']
        vets = [v for v in self.workers if v.__class__.__name__ == 'Vet']

        result = f'You have {len(self.workers)} workers' + '\n'

        result += f'----- {len(keepers)} Keepers:' + '\n'
        result += '{}'.format('\n'.join([repr(k) for k in keepers])) + '\n'

        result += f'----- {len(caretakers)} Caretakers:' + "\n"
        result += '{}'.format('\n'.join([repr(c) for c in caretakers])) + '\n'

        result += f'----- {len(vets)} Vets:' + "\n"
        result += '{}'.format('\n'.join([repr(v) for v in vets]))
        return result
