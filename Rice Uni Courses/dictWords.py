def count_letters(word_list):
    """ See question description """

    # ALPHABET = "abcdefghijklmnopqrstuvwxyz"

    letter_count = {}
    for word in word_list:
        for letter in word:
            if letter in letter_count:
                letter_count[letter] += 1
            else:
                letter_count[letter] = 1
    keys = list(letter_count.keys())
    max_key = keys[0]
    for i in range(len(keys)-1):
        if letter_count[keys[i]] > letter_count[max_key]:
            max_key = keys[i]
        elif letter_count[keys[i]] == letter_count[max_key]:
            if keys[i] < max_key:
                max_key = keys[i]
            else:
                max_key = max_key
    print(max_key)


monty_quote = "listen strange women lying in ponds distributing swords is no basis for a system of government supreme executive power derives from a mandate from the masses not from some farcical aquatic ceremony"

monty_words = monty_quote.split(" ")
count_letters(["hello", "world"])
count_letters(monty_words)
