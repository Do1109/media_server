
import random


def janken_battle():

    hands = ["グー", "チョキ", "パー"]

    while True:
        user_hand = input("手を選べ(グー/チョキ/パー)")
        if user_hand not in hands:
            print("もっかい入力せい")
            continue
        com_hand = random.choice(hands)
        print(f"キサマ : {user_hand}")
        print(f"わたし : {com_hand}")

        if user_hand == com_hand:
            print("あいこ")

        elif (
            (user_hand == "グー" and com_hand == "チョキ") or
            (user_hand == "チョキ" and com_hand == "パー") or
            (user_hand == "パー" and com_hand == "グー")
        ):
            print("あなたの勝ち")

        else:
            print("お前の負けwwwwww")


janken_battle()
