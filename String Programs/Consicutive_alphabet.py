from itertools import groupby

inp = "AAAARRTPPPRRRRQQQABB"
out = "4A2R1T3P4R3Q1A2B"

def count_consecutive_alpha_1(sequence):
    print(f"Given sequence : {sequence}")
    result = ""
    counting = 1

    for i in range(1, len(sequence)):
        if sequence[i] == sequence[i-1]:
            counting+=1
        else:
            result += str(counting) + sequence[i-1]
            counting = 1

    #The loop does not encounter a change after the final group,
    #so it never triggers the output for the last repeated characters.
    result += str(counting) + sequence[-1]

    return result


def count_consecutive_alpha_2(sequence):
    print(f"Given sequence : {sequence}")

    result = "".join(str(len(list(g))) + k for k, g in groupby(inp))
    return result


print(count_consecutive_alpha_1(inp))
# print(count_consecutive_alpha_2(inp))

