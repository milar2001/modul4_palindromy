def palindromes(word):
    changed_word = "".join(e for e in word if e.isalnum()).replace(" ", "").lower()
    return changed_word == changed_word[::-1]