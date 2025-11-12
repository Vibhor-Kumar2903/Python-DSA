def remove_duplicates_alphabets(str):
    print(f"\nOriginal string : {str}")
    str = str.lower()
    unique_alpha = set(str)
    print(f"\nUnique alpha, unordered : {unique_alpha}")
    ordered_alpha = "".join(dict.fromkeys(str))
    print(f"\nUnique alpha, ordered : {ordered_alpha}")



given_string = "MyNameIsKhan"
# remove_duplicates_alphabets(given_string)


def remove_duplicates_words(str):
        words = str.split()  # Split the string into a list of words
        unique_words = []
        seen_words = set()

        for word in words:
            if word not in seen_words:
                unique_words.append(word)
                seen_words.add(word)

        return ' '.join(unique_words)  # Join the unique words back into a string


# given_string = "MyNameIsKhan"
given_string = "My Name Is Khan and His Name Is King"
print(remove_duplicates_words(given_string))