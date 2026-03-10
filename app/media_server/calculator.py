
def calculator():
    while True:
        user_choice = input("電卓アプリ: 1/足し算 2/引き算 3/掛け算 4/割り算 :qで終了")
        if user_choice.lower() == "q":
            print("じゃあな")
            break

        if user_choice not in ["1", "2", "3", "4"]:
            print(f"{user_choice}は想定された値ではありまへん")
            continue

        input1 = input("1つ目の数字を入力しやがれ")
        input2 = input("2つ目の数字を入力しやがれ")
        if not input1.isdigit() or not input2.isdigit():
            print("数字を入力してくれ")
            continue

        user_math1 = int(input1)
        user_math2 = int(input2)

        match user_choice:
            case "1":
                print(user_math1 + user_math2)
            case "2":
                print(user_math1 - user_math2)
            case "3":
                print(user_math1 * user_math2)
            case "4":
                print(user_math1 / user_math2)


calculator()
