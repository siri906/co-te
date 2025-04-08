# # Q.
# # 0과 1로만 이루어진 문자열이 주어졌을 때, 이 문자열에 있는 모든 숫자를 전부 같게 만들려고 한다.
# # 할 수 있는 행동은 문자열에서 연속된 하나 이상의 숫자를 잡고 모두 뒤집는 것이다.
# # 뒤집는 것은 1을 0으로, 0을 1로 바꾸는 것을 의미한다.
# #
# # 예를 들어 S=0001100 일 때,
# #
# # 전체를 뒤집으면 1110011이 된다.
# # 4번째 문자부터 5번째 문자까지 뒤집으면 1111111이 되어서 2번 만에 모두 같은 숫자로 만들 수 있다.
# # 하지만, 처음부터 4번째 문자부터 5번째 문자까지 문자를 뒤집으면 한 번에 0000000이 되어서 1번 만에 모두 같은 숫자로 만들 수 있다.
# #
# # 주어진 문자열을 모두 0 혹은 모두 1로 같게 만드는 최소 횟수를 반환하시오.
#
# # input = "011110"
# input1 = '11011'
# # input2 = '0101010101'
#
#
# def find_count_to_turn_out_to_all_zero_or_all_one(string):
#     # 이 부분을 채워보세요!
#     string_arr = []
#     only_zero = []
#     only_one = []
#
#     for item in string:
#         string_arr.append(item)
#         if item == 0:
#             only_zero.append(item)
#         else:
#             only_one.append(item)
#     # 0이 더 클 경우
#     if len(only_zero) > len(only_one):
#         for index,item in enumerate(string_arr):
#             check_same_arr_1 = []
#             check_same_arr_1.append(item)
#             if  item == 0:
#                 check_same_arr_1.append(item)
#             else:
#                 break
#     else:
#         for index,item in enumerate(string_arr):
#             check_same_arr = []
#             check_same_arr.append(item)
#             if  check_same_arr[index] == item:
#                 check_same_arr.append(item)
#             else:
#                 break
#
#             print(check_same_arr, 'same')
#
#
#     return 1
#     # 0이 더 많을 경우
#
#
# result = find_count_to_turn_out_to_all_zero_or_all_one(input1)
# # result1 = find_count_to_turn_out_to_all_zero_or_all_one(input1)
# # result2 = find_count_to_turn_out_to_all_zero_or_all_one(input2)
# print(result)
# # print(result1)
# # print(result1)

# 새로운 파이썬 문법

# for x in ["맨유", '맨유', '1']:
#     if x != "맨유":
#         print('맨유 팬이 아닌 사람이 있습니다.')
#         break
# else:
#     print('모두 맨유 팬입니다.')

# 풀이

input = "011110"

# 문자열 뒤깁기 코드
# 개념 배우고 다시 돌아와서 풀이 해보기
def find_count_to_turn_out_to_all_zero_or_all_one(string):
    # 이 부분을 채워보세요!
    return 1


result = find_count_to_turn_out_to_all_zero_or_all_one(input)
print(result)