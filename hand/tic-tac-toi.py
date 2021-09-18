

text = input(">> ")
#biniam

"""
     b , 0 -> 6
     i , 1 -> 5
     n , 2 -> 4
"""
def reverse(text):
    letter_list = []
    reverse_letter_list = []

    for i in text:
        letter_list.append(i)
    for i in range(len(letter_list)):
        print(f"{letter_list[i]} , {i} -> {len(letter_list) - 1 - i}")

        letter_list[i] = letter_list[len(letter_list) - 1 - i]
    print(letter_list)



reverse(text)