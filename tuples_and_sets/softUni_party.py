def input_to_list(list_count):
    return [input() for _ in range(list_count)]


def input_to_list_until_command(command):
    result = []

    while True:
        line = input()
        if line == command:
            break
        result.append(line)

    return result


def get_not_arrived_guest(guest, guest_arrived):
    guest_set = set(guest)
    [guest_set.remove(guest) for guest in guest_arrived]
    return guest_set


def print_result(result):
    result = sorted(result)
    print(len(result))
    [print(guest) for guest in result if guest[0].isdigit]
    [print(guest) for guest in result if not guest.isdigit]


guests = input_to_list(int(input()))
current_guest_arrived = input_to_list_until_command('END')

print_result(get_not_arrived_guest(guests, current_guest_arrived))
