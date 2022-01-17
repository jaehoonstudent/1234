 
#교재 57페이지 연습문제 2.12 2.18, 2.24 (첨부파일 참조),
s1 = '-'
s2 = '+'
print('12-(a) = ', s1 + s2)
print('12-(b) = ', s1 + s2 + s1)
print('12-(c) = ', s2 + s1*2)
print('12-(d) = ', (s2 + s1*2)*2) 
print('12-(e) = ', s2 + (s1*2 + s2)*10) 
print('12-(f) = ', (s2 + s1 + s2*3 + s1*2)*5)

# 추가로 모범답안에 포함했습니다.
print('15-(a) = ', len('anachronistically') == len('counterintuitive')+1)
print('15-(b) = ', 'misinterpretation' < 'misrepresentation')
print('15-(c) = ', 'e' not in 'floccinaucinihilipilification')
print('15-(c) = ', 0 == 'floccinaucinihilipilification'.count('e')) # (c)의 다른 답
print('15-(d) = ', len('counterrevolution') == len('counter') + len('resolution'))


flowers = ['rose', 'bougainvillea', 'yucca', 'marigold', 'daylilly']
print('18-(a) = ', flowers)
print('18-(b) = ', 'patato' in flowers) # 없으므로 False가 출력된다.
throny = flowers[:3]
print('18-(c) = ', throny)
poisonous = flowers[-3:]
print('18-(d) = ', poisonous)
dangerous = throny + poisonous
print('18-(e) = ', dangerous)


grades = ['B', 'B', 'F', 'C', 'B', 'A', 'A', 'D', 'C', 'D', 'A', 'A', 'B']
count = [grades.count('A'),
         grades.count('B'),
         grades.count('C'),
         grades.count('D'),
         grades.count('F')]     
print('24 = ', count)

# 또 다른 방법
count = []
count.append(grades.count('A'))
count.append(grades.count('B'))
count.append(grades.count('C'))
count.append(grades.count('D'))
count.append(grades.count('F'))
print('24 = ', count)

# 또 다른 방법
# 아직 배우지는 않았지만 예습하세요.
count = [grades.count(grade) for grade in ['A', 'B', 'C', 'D', 'F']]
print('24 = ', count)

# 또 다른 방법
# 아직 배우지는 않았지만 예습하세요.
count = []
for grade in ['A', 'B', 'C', 'D', 'F']:
    count.append(grades.count(grade))
print('24 = ', count)

# 또 다른 방법
# 아직 배우지는 않았지만 예습하세요.
count = [grades.count(grade) for grade in sorted(set(grades))]
print('24 = ', count)

#또 다른 방법이 얼마든지 있을 수 있습니다.


