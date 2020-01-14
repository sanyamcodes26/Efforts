emoji_dict = {":)": "🙂", ":(": "🙁", ":P": "😋", ":/": "😕", "<3": "❤"}


def display(data):
    new_data = data

    if data == "ADMIN":
        emo_1 = input("Emoji RAW : ")
        emo_2 = input("Emoji OP : ")
        emoji_dict[emo_1] = emo_2
        print("Emoji inserted...")
    else:
        for i in emoji_dict.keys():
            if i in data:
                new_data = new_data.replace(i, emoji_dict[i])
        print("OLD :", data)
        print("NEW :", new_data)
    return


if __name__ == "__main__":
    while True:
        text = input("Type your Message : ")
        if text == "N" or text == "n":
            break
        else:
            display(text)
    print("--END--")
