
import random


def num_choice():

    while True:

        list = []
        for i in range(1, 101):
            list.append(i)
        num = random.choice(list)

        user_input = input("数字を入力せんかい: qで終了")

        if user_input.lower() == "q":
            print("終了します")
            break

        if not user_input.isdigit():
            print("ちゃんと数字を入力しやがれ")
            continue
        user_num = int(user_input)
        if user_num not in range(1, 101):
            print("ちゃんと入力しやがれ")
            continue

        if user_num == num:
            print("正解")

        else:
            print("はずれ")


num_choice()
