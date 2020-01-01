def initial():
    samp_string = "  This is a very important string      "
    print(samp_string.lstrip())
    print(samp_string.rstrip())
    samp_string = samp_string.strip()
    print(samp_string.capitalize())
    print(samp_string.upper())
    print(samp_string.lower())
    a_list = ["This", "is", "a", "very", "important", "string"]
    print(a_list)
    print(" ".join(a_list))
    print(samp_string.replace("a ", "a kind of "))
    samp_string = "z"
    print(samp_string.isalnum())
    print(samp_string.isalpha())
    print(samp_string.isdigit())
    print(samp_string.isspace())
    print(samp_string.isupper())
    print(samp_string.islower())
    return


def test_1():
    original_string = input("Convert to Acronym : ")
    original_string = original_string.upper()
    list_of_words = original_string.split()
    for words in list_of_words:
        print(words[0], end="")
    print()
    return


def do(message="", key=0):
    enc_message = ""
    for char in message:
        if char.isalpha():
            char_code = ord(char) + key
            if char.isupper():
                if char_code > ord('Z'):
                    char_code -= 26
                elif char_code < ord('A'):
                    char_code += 26
            else:
                if char_code > ord('z'):
                    char_code -= 26
                elif char_code < ord('a'):
                    char_code += 26
            enc_message += chr(char_code)
        else:
            enc_message += char
    return enc_message


def test_2():
    message = input("Enter Your Message : ")
    key = int(input("Key Shift (1-26) : "))
    secret_message = do(message, key)
    print("Encrypted :", secret_message)
    message = do(secret_message, -key)
    print("Decrypted :", message)
    return

    
if __name__ == "__main__":
    initial()
    # test_1()
    # test_2()
