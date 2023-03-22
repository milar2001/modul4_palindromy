def palindromes(word):
    reversed_word = "".join(e for e in word if e.isalnum()).replace(" ", "").lower()[::-1]
    main_word = "".join(e for e in word if e.isalnum()).replace(" ", "").lower()
    return main_word == reversed_word
