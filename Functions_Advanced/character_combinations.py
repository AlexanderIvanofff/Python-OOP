# Write a program that reads a single string and prints all the possible combinations of the characters in that string.
# Submit your solution in the judge system.

permutation = set()


def generate(k: int, array: list):
    if k == 1:
        permutation.add("".join(array))
    else:
        generate(k - 1, array)

        for i in range(k):
            # Swap choice dependent on parity of k (even or odd)
            if k % 2 == 0:
                array[i], array[k-1] = array[k-1], array[i]
            else:
                array[0], array[k - 1] = array[k - 1], array[0]

            generate(k - 1, array)


s = list(input())

generate(len(s), s)
print("\n".join(list(permutation)))