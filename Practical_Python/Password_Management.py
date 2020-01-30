from getpass import getpass as gp
import bcrypt as bc


password_dict = {'admin': 'admin',
                 'facebook_account': '11111',
                 'email_account': '22222',
                 'bank_account': '33333'}


def getPassword(msg):
    return gp(msg)


def VerifyPassword(goodPassword, givenPassword):
    hashed_Value = bc.hashpw(givenPassword.encode('utf-8'), bc.gensalt())
    return bc.checkpw(goodPassword.encode('utf-8'), hashed_Value)


if __name__ == "__main__":
    while True:
        account = input(f"Account ({', '.join(password_dict.keys())})\t:\t")
        if account in password_dict.keys():
            if VerifyPassword(password_dict[account], getPassword("Password\t:\t")):
                print("UnLocked")
            else:
                print("Still Locked")
            break
        else:
            print("Try Again...")

