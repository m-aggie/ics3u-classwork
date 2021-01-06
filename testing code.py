def main():
    print("The amazing text-ceterer program.")
    word = input("Enter a word. ")
    while True:
        try:
            width = int(input("Enter the width of the terminal. "))
            break
        except ValueError:
            print("Invalid")

    center_string(word, width)
    print("The final result is:")
    print(center_string)

def center_string(word, width):
    left_spaces = (width - len(word))//2
    result = " "*left_spaces + word
    return result


def tests():
    assert center_string("a", 3) == " a"
    assert center_string("aa", 4) == " aa"
    assert center_string("b", 5) == "  b"
    assert center_string("hello", 11) == "   hello"
    print("all passed!")


if __name__ == "__main__":
    tests()
    main()

