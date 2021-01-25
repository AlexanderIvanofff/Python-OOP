word = [x for x in input().split()]

even_word = [x for x in word if len(x) % 2 == 0]

print('\n'.join(even_word))