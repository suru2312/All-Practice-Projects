from art import logo

print(logo)

alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(encode_or_decode, original_text, shift_amount):
    cipher_text = ""
    for i in original_text:
        if i not in alphabets:
            cipher_text += i
        else:
            if encode_or_decode == "decode":
                shifted_position = alphabets.index(i) - shift_amount
            elif encode_or_decode == "encode":
                shifted_position = alphabets.index(i) + shift_amount
            
            shifted_position = shifted_position % len(alphabets)
            cipher_text += alphabets[shifted_position]
    print(f"Here's the {encode_or_decode}d result : {cipher_text}")

should_continue = True
while should_continue:
    direction = input("Enter 'encode' to Encode and 'decode' to Decrypt : ").lower()
    text = input("Type your message here : ").lower()
    shift = int(input("Type the Shift Number : "))

    caesar(encode_or_decode=direction, original_text=text, shift_amount=shift)

    restart = input("Do you want to go again? Type 'yes' or 'no' : ").lower()
    if restart == "no":
        should_continue = False
        print("Goodbye 👋")