# Caesar_Cipher.py

def encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            shifted_char = chr((ord(char) - base + shift) % 26 + base)
            encrypted_text += shifted_char
        else:
            encrypted_text += char
    return encrypted_text


def decrypt(text, shift):
    return encrypt(text, -shift)


def main():
    print("=== Caesar Cipher Tool ===")

    message = input("Enter the message: ")
    
    while True:
        try:
            shift = int(input("Enter shift value (e.g., 3): "))
            break
        except ValueError:
            print("❌ Invalid number. Try again.")

    action = input("Choose (E)ncrypt or (D)ecrypt: ").lower()

    if action == 'e':
        result = encrypt(message, shift)
        print("\n🔐 Encrypted message:", result)
    elif action == 'd':
        result = decrypt(message, shift)
        print("\n🔓 Decrypted message:", result)
    else:
        print("❌ Invalid choice. Use 'E' or 'D'.")


if __name__ == "__main__":
    main()
