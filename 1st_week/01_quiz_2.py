# Q. 다음과 같이 영어로 되어 있는 문자열이 있을 때,
# 이 문자열에서 반복되지 않는 첫번째 문자를 반환하시오.
# 만약 그런 문자가 없다면 _ 를 반환하시오.

def find_not_repeating_first_character(string):
    # 이 부분을 채워보세요!
    alpha_array = [0] * 26
    # print(alpha_array)
    for index , alpha in enumerate(string):
       arrindex = ord(alpha) - ord('a')
       print(arrindex, 'index')
       alpha_array[arrindex] += 1

    print(alpha_array)
    return "_"


result = find_not_repeating_first_character
print(result("abadabac"))
# print("정답 = d 현재 풀이 값 =", result("abadabac"))
# print("정답 = c 현재 풀이 값 =", result("aabbcddd"))
# print("정답 =_ 현재 풀이 값 =", result("aaaaaaaa"))