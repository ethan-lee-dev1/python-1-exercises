def vowel_counter(sentence):
    vowels = ['a', 'e', 'i', 'o', 'u']
    counter = 0
    for char in sentence:
        if char in vowels:
            counter += 1
    print(f"Number of vowels: {counter}")