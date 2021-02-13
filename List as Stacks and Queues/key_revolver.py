"""
Our favorite super-spy action hero Sam is back from his mission in another exam, and this time he has an even more
difficult task. He needs to unlock a safe. The problem is that the safe is locked by several locks in a row, which all
have varying sizes.
Our hero posesses a special weapon though, called the Key Revolver, with special bullets. Each bullet can unlock a lock
with a size equal to or larger than the size of the bullet. The bullet goes into the keyhole, then explodes, completely
destroying it. Sam doesn't know the size of the locks, so he needs to just shoot at all of them, until the safe runs out
of locks.What's behind the safe, you ask? Well, intelligence! It is told that Sam's sworn enemy – Nikoladze, keeps his
top secret Georgian Chacha Brandy recipe inside. It's valued differently across different times of the year, so Sam's boss
 will tell him what it's worth over the radio. One last thing, every bullet Sam fires will also cost him money, which will
be deducted from his pay from the price of the intelligence.
Good luck, operative.
After Sam receives all of his information and gear (input), he starts to shoot the locks front-to-back, while going
through the bullets back-to-front.
If the bullet has a smaller or equal size to the current lock, print "Bang!", then remove the lock. If not, print "Ping!",
leaving the lock intact. The bullet is removed in both cases.
If Sam runs out of bullets in his barrel, print "Reloading!" on the console, then continue shooting. If there aren't any
bullets left, don't print it. The program ends when Sam either runs out of bullets, or the safe runs out of locks.
"""

from collections import deque

bullet_price = 50
size_of_the_gun_barrel = 2
bullets = deque([11, 10, 5, 11, 10, 20])
locks = deque([15, 13, 16])
value = 1500

shots = 0
is_locket = False
bul = size_of_the_gun_barrel

while len(bullets) > 0:

    if size_of_the_gun_barrel <= 0:
        print(f'Reloading!')
        size_of_the_gun_barrel += bul

    if locks:
        current_bullet = bullets.pop()
        size_of_the_gun_barrel -= 1
        current_lock = locks[0]
        shots += 1
        if current_bullet <= current_lock:
            locks.popleft()
            print('Bang!')
        else:
            print('Ping!')
    else:
        is_locket = True
        break

if locks:
    print(f'Couldn\'t get through. Locks left: {len(locks)}')
else:

    total_price = bullet_price * shots
    print(f'{len(bullets)} bullets left. Earned ${value - total_price}')