def count_duplicate_alphabets(sequence):
    print(f"Given sequence = {sequence}")

    duplicate_alpha = {}
    checked_alpha = ""

    for char in sequence:
        if char not in checked_alpha:
            count = 0

            for ch in sequence:
                if char == ch:
                    count+=1

            if count > 1:
                # print(f"{char} --> {count}")
                duplicate_alpha[char] = count

            checked_alpha+=char

    return duplicate_alpha


seq = "Airtel's senior QA engineer interview questions focus on technical skills like SQL, API"
print(count_duplicate_alphabets(seq))