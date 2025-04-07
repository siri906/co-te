#
# Q. 정수를 입력 했을 때, 그 정수 이하의 소수를 모두 반환하시오.
#
# 소수는 자신보다 작은 두 개의 자연수를 곱하여 만들 수 없는 1보다 큰 자연수이다.
#
# # 20이 입력된다면, 아래와 같이 반환해야 합니다!
# [2, 3, 5, 7, 11, 13, 17, 19]


input = 20


# def find_prime_list_under_number(number):
#     # 이 부분을 채워보세요!
#     check_arr = []
#     div_arr = []
#     for n in range(2, number + 1):
#         for i in range(2, n):
#             if n % i == 0:
#                 div_arr.append(n)
#                 break
#             else:
#                 check_arr.append(n)
#
#
#
#     print(check_arr, 'check')
#
#
#     return []

# def find_prime_list_under_number(number):
#     prime_list = []
#     for n in range(2, number + 1):
#         for i in range(2, n):
#             if n % i == 0:
#                 break
#         else:
#             prime_list.append(n)
#
#     return prime_list

# 개선 .ver

input = 20


def find_prime_list_under_number(number):
    prime_list = []

    for n in range(2, number + 1):
        for i in prime_list:
            if n % i == 0 and i * i <= n:
                break
        else:
            prime_list.append(n)

    return prime_list


result = find_prime_list_under_number(input)
print(result)

