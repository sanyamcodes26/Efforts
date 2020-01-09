# import re


def display(data):
    new_data = data
    emoji_dict = {":)": "🙂", ":(": "🙁", ":P": "😋", ":/": "😕",
                  "<3": "❤", "(butt)": "(‿|‿)"}
    # regex = re.compile(r"[:)]|[:(]|[:P]|[:/]|[<3]|[(butt)]")
    # data_new = re.sub(regex, emoji_dict[regex], data)
    # print(data)
    # print(regex.__str__())
    for i in emoji_dict.keys():
        if i in data:
            new_data = new_data.replace(i, emoji_dict[i])
    print("OLD :", data)
    print("NEW :", new_data)
    return


if __name__ == "__main__":
    text = input("Type your Message : ")
    display(text)
