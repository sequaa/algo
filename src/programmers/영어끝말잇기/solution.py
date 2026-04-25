def solution(n, words):
    used_words = set()
    prev_word = words[0][0]

    for i, word in enumerate(words):
        if word in used_words or word[0] != prev_word[-1]:
            return [(i%n) + 1, (i//n) + 1]
        used_words.add(word)
        prev_word = word

    return [0, 0]