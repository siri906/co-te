# 점근법이란 ? (알기 위해 하단 문제 풀어보기)
# 빅오 => 최악의 경우
# 빅오메가 => 최선의 경우


# # 내 풀이 (N만큼의 시간복잡도 존재)
# def is_number_exist(number, array):
#     # 이 부분을 채워보세요!
#     check_value = False
#     for item in array:
#         if item == number:
#             check_value = True
#
#     return check_value

# 강의 풀이 (N만큼의 시간복잡도 존재)
def is_number_exist(number, array):
    # 이 부분을 채워보세요!
    for item in array:
        if item == number:
           return True
    return False


result = is_number_exist
# 운이 좋으면 하단의 실행 결과 시간 복잡도는 1밖에 걸리지 않는다.
# 최선의 경우는 1만큼만 걸린다 (빅오메가/ Ω(1))
print("정답 = True 현재 풀이 값 =", result(3, [3,5,6,1,2,4]))
# 운이 좋이 않으면 시간 복잡도는 n 만큼으로 걸린다 (빅오 / O(N))
print("정답 = Flase 현재 풀이 값 =", result(7, [6,6,6]))
print("정답 = True 현재 풀이 값 =", result(2, [6,9,2,7,1888]))

# 결과 값은 대부분 최선은 걸리지 않음 (운빨 망겜)
# 그래서 최악의 경우를 대비해서 복잡도를 생각하는게 맞음