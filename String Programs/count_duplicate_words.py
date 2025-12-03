def count_duplicate_words(sequence):
    print(f"Given sequence : {sequence}")
    sequence = sequence.lower()

    words = sequence.split(" ")

    duplicate_words = {}
    checked_words = []

    for word in words:
        if word not in checked_words:
            count = 0

            for w in words:
                if word == w:
                    count+=1

            if count>1:
                duplicate_words[word] = count
                # print(f"{word} --> {count}")

        checked_words.append(word)


    return duplicate_words

seq = """Many novice writers tend to make a sharp distinction between content and style, thinking that a paper can be strong in one and weak in the other, but focusing on organization shows how content and style converge in deliberative academic writing. Your professors will view even the most elegant prose as rambling and tedious if there isn’t a careful, coherent argument to give the text meaning. Paragraphs are the “stuff ” of academic writing and, thus, worth our attention here."""
print(count_duplicate_words(seq))














