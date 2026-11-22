first_seq = [int(x) for x in input().split()]
second_seq = [int(x) for x in input().split()]

only_in_first = [num for num in first_seq if num not in second_seq]
only_in_second = [num for num in second_seq if num not in first_seq]

print(" ".join(str(num) for num in only_in_first))
print(" ".join(str(num) for num in only_in_second))