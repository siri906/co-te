# Q. 다음과 같이 영어로 되어 있는 문자열이 있을 때,
# 이 문자열에서 반복되지 않는 첫번째 문자를 반환하시오.
# 만약 그런 문자가 없다면 _ 를 반환하시오.
from fileinput import close


def find_not_repeating_first_character(string):
    # 이 부분을 채워보세요!
    alpha_array = [0] * 26
    not_repeating_array = []
    # print(alpha_array)
    # 시간 복잡도 N
    for index , alpha in enumerate(string):
       arrindex = ord(alpha) - ord('a')
       alpha_array[arrindex] += 1

    # 시간 복잡도 26 = alpha_array
    for index, item in enumerate(alpha_array):
        if item == 1:
            not_repeating_array.append(chr(index + ord('a')))

    # print(not_repeating_array, 'arr')
    # 시간 복잡도 n
    for char in string:
        # print(char, 'char')
        if char in not_repeating_array:
            return char

    return "_"


result = find_not_repeating_first_character
# print(result("abadabac"), 'test')
print("정답 = d 현재 풀이 값 =", result("abadabac"))
print("정답 = c 현재 풀이 값 =", result("aabbcddd"))
print("정답 =_ 현재 풀이 값 =", result("aaaaaaaa"))