def find_max_occurred_alphabet(string):
    # 이 부분을 채워보세요!
    # 배열 선언(초기화)
    alphabet_occurrence_array = [0] * 26
    # print('알파벳 배열',alphabet_occurrence_array)
    index_check = 0
    max_num = 0
    for index, alpha in enumerate(string):
        # print(alpha)
        # print(index,'index')
        if not alpha.isalpha():
            continue
        arr_index = ord(alpha) - ord('a')
        alphabet_occurrence_array[arr_index] += 1

    for index, alpha_item in enumerate(alphabet_occurrence_array, 0):
        if alpha_item > max_num:
            max_num = alpha_item
            index_check = index

    result_alpha = chr(index_check+ ord('a'))
    # return alphabet_occurrence_array, result_index
    return result_alpha





# 문자열인지 확인하는 함수
# print("a".isalpha())    # True
# print("1".isalpha())    # False

# 각각 아이템이 몇번 나왔는지 분석해야함 빈도수 하려면
# 빈도수를 저장하기 위한 가장 쉬운 방법은 아스키코드 라고 한다
# ord('a') => 97 아스키 코드값을 찾아주는 함수

# ord('a') - 97 = 0 // 0번째 index
# ord('b') - 97 = 1 // 1번째 index
# ord('c') - 97 = 2 // 2번째 index

# 만약에 반대로 1번째 index에 무슨 알파벳을 넣은건지 확인하는 함수
# chr(97) => a   아스키 코드 => 문자





result = find_max_occurred_alphabet
print("정답 = i ")
print(" 현재 풀이 값 =", result("hello my name is dingcodingco"))
print("정답 = e 현재 풀이 값 =", result("we love algorithm"))
print("정답 = b 현재 풀이 값 =", result("best of best youtube"))
