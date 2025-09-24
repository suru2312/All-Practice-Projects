def calculate_love_score(name1, name2):
    all_name = name1 + name2

    true_count = 0
    for i in "true":
        true_count += all_name.count(i)

    love_count = 0
    for j in "love":
        love_count += all_name.count(j)

    score = int(str(true_count) + str(love_count))

    print(f"Your love score is {score}")

    if score < 10 or score > 90:
        print("You go together like coke and mentos 💥")
    elif 40 <= score <= 50:
        print("You are alright together 💕")
    else:
        print("Keep trying, love finds its way ❤️")

name1 = input("Enter the First Name : ").lower()
name2 = input("Enter the Second Name : ").lower()
calculate_love_score(name1, name2)
