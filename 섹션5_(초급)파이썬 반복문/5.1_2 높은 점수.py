# 78 65 89 86 55 91 64 89
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])
print(student_scores)

# max 최댓값 min 최소값으로 구할수 있다
print(max(student_scores))
print(min(student_scores))

###############################################################################################################
student_scores = [78, 65, 89, 86, 55, 91, 64, 89]
# for문으로 최댓값 구하기
scores_height = 0
for H in student_scores: # 이 반복문은 계속해서 실행될거고 모든 H가 student_scores내부에 있고 확인할 때 까지
    if H > scores_height: # student_scores를 계속 반복시켜 H가 크면 아래 줄로 넘어가고 작으면 계속 반복
        scores_height = H # 1개의 = 는 할당이고 2개 == 는 확인을 말한다. 즉 H에 할당된 78이 scores_height를 0-> 78로 변환해준다
print(f"The highest score in the class is: {scores_height}")

