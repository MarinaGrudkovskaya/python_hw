
# Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя –
# школьница. Петя помогает Кате по математике. Он задумывает два
# натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. Для
# этого Петя делает две подсказки. Он называет сумму этих чисел S и их
# произведение P. Помогите Кате отгадать задуманные Петей числа.
# 4 4 -> 2 2
# 5 6 -> 2 3

s = int(input('the sum of nambers - '))
p = int(input('the product of nambers - '))

if s > 2000 or p > 1000000:
    print('mistake1')
else:
    for x in range(s):
        for y in range(s):
          if s == x + y and p == x*y:
              print(x,y)
if s != x + y and p != x*y: 
    print('mistake2')



