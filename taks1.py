# Caesar Cipher Program

def encrypt(text, shift):
    result = ""

    for char in text:
        if char.isalpha():
            if char.isupper():
                result += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
            else:
                result += chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
        else:
            result += char

    return result


def decrypt(text, shift):
    return encrypt(text, -shift)


def main():
    print("===== Caesar Cipher =====")

    while True:
        print("\n1. Encrypt")
        print("2. Decrypt")
        print("3. Exit")

        choice = input("Enter your choice (1/2/3): ")

        if choice == "1":
            message = input("Enter the message: ")
            shift = int(input("Enter shift value: "))
            encrypted = encrypt(message, shift)
            print("Encrypted Message:", encrypted)

        elif choice == "2":
            message = input("Enter the encrypted message: ")
            shift = int(input("Enter shift value: "))
            decrypted = decrypt(message, shift)
            print("Decrypted Message:", decrypted)

        elif choice == "3":
            print("Thank you!")
            break

        else:
            print("Invalid choice! Please try again.")


if __name__ == "__main__":
    main()