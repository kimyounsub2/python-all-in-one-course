
# 1 ~ 100 까지 홀수 합계
total_even_numbers = 0
for T in range(1, 101, 2):
    total_even_numbers += T
print(total_even_numbers)

# 1 ~ 100 까지 짝수 합계
total_even_numbers = 0
for T in range(0, 101, 2):
    total_even_numbers += T
print(total_even_numbers)

# if문 포합 홀수 합계
total_even_numbers = 0
for T in range(1, 101):
    if T % 2 == 1:
        total_even_numbers += T
print(total_even_numbers)


# if문 포합 짝수 합계
total_even_numbers = 0
for T in range(1, 101):
    if T % 2 == 0:
        total_even_numbers += T
print(total_even_numbers)






