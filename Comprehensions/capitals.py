cities = input().split(', ')
capitals = input().split(', ')

result = {cities[index]: capitals[index] for index in range(len(cities))}


print(*[f'\n{key} -> {value}' for key, value in result.items()])