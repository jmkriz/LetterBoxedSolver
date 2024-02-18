def calculate_solutions(letter_box):
    possible_words = calculate_word_list(letter_box)
    solutions = {1: [],
                 2: []}
    for first_word in possible_words:
        if has_all_letters(letter_box, first_word):
            solutions[1].append(first_word)
        else:
            for second_word in possible_words:
                if first_word[-1] == second_word[0]:
                    if has_all_letters(letter_box, first_word + second_word[1:]):
                        solutions[2].append(first_word + "-" + second_word)
    return solutions


def calculate_word_list(letter_box):
    with open('words_alpha.txt', 'r') as f:
        word_list = f.read().splitlines()
    found_words = []
    for word in word_list:
        if valid_word(letter_box, word):
            found_words.append(word)
    return found_words


def has_all_letters(letter_box, phrase):
    letter_counts = {}
    for side in letter_box:
        for letter in letter_box[side]:
            if letter not in letter_counts:
                letter_counts[letter] = 1
            else:
                letter_counts[letter] += 1
    for letter in phrase:
        if letter in letter_counts:
            letter_counts[letter] -= 1
    for letter in letter_counts:
        if letter_counts[letter] > 0:
            return False
    return True


def valid_word(letter_box, word, current_side=None):
    if not current_side:
        for side in letter_box:
            if word[0] in letter_box[side]:
                if valid_word(letter_box, word[1:], side):
                    return True
    elif not word:
        return True
    else:
        for side in letter_box:
            if side != current_side and word[0] in letter_box[side]:
                if valid_word(letter_box, word[1:], side):
                    return True
    return False


if __name__ == "__main__":
    print("Welcome to the Letter Boxed solver!\n"
          "This solver will find all solutions to a given letter-boxed puzzle that use one or two words.\n")

    letter_box = {"top": [],
                  "bottom": [],
                  "left": [],
                  "right": []
                  }

    for side_name in letter_box:
        letter_box[side_name] = list(input("Please enter the letters on the " + side_name + " side: "))

    solutions = calculate_solutions(letter_box)
    print("\nThere are " + str(len(solutions[1])) + " one-word solutions: ")
    for solution in solutions[1]:
        print(solution)
    print("\nThere are " + str(len(solutions[2])) + " two-word solutions: ")
    for solution in solutions[2]:
        print(solution)
