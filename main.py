def encode(password):
    encoded_pass_list = []
    encoded_pass = ''
    for i in range(len(password)):
        encoded_pass_list.append(int(password[i]) + 3)
    for char in encoded_pass_list:
        encoded_pass += str(char)
    return encoded_pass

def decode(encoded_pass):
    decoded_pass = ''.join(str((int(digit) - 3) % 10) for digit in encoded_password)
    return decoded_pass

def print_menu():
    print("Menu\n-------------\n1. Encode\n2. Decode\n3. Quit")
def main():
    global encoded_pass
    while True:
        print_menu()
        selection = int(input("Please enter an option: "))
        match selection:
            case 1:
                password = input("Please enter your password to encode: ")
                encoded_pass = encode(password)
                print("Your password has been encoded and stored!")
            case 2:
                decoded_pass = decode(encoded_pass)
                print(f"The encoded password is {encoded_pass}, and the original password is {decoded_pass}.")
            case 3:
                break
if __name__ == "__main__":
    main()
