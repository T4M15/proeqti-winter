import random
import time

start_game = input("გინდა თამაშის დაწყება? (კი/არა): ")

if start_game != "კი":
    exit()

print("level 1 = 1-100")
print("level 2 = 1-200")
print("level 3 = 1-300")

choose_level = int(input("აირჩიე სირთულე: (1/2/3): "))

if choose_level == 1:
    max_number = 100
elif choose_level == 2:
    max_number = 200
elif choose_level == 3:
    max_number = 300
else:
    print("Wrong level")
    exit()

number = random.randint(1, max_number)
start_time = time.time()

while True:
    guess_number = int(input(f"გამოიცანი რიცხვი 1-დან  {max_number}-მდე: "))

    if guess_number > number:
        print("მაღალია")
    elif guess_number < number:
        print("დაბალია")
    else:
        print("საღოლ გამოიცანი!")
        break

end_time = time.time()
total_time = end_time - start_time

print("შენ დახარჯე", round(total_time, 2), "წამი")