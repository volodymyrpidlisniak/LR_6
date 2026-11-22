first_line = input().split()
second_line = input().split()

common_words = set(first_line) & set(second_line)

print(" ".join(common_words))