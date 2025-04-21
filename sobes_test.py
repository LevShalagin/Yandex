'''
Дан массив целых чисел X длиной N.
Входной массив отсортирован оп возростанию.
Написать функцию, котороая из этого массива
получит массив квадратов чисел, упорядоченный по возрастанию.
Пример:
[-3, 2, 4] => [4, 9, 16]

1) числа по краям исходного массива дадут большие квадраты
2) далее рассматриваем меньшее из прошлой пары чисел и 
новое следующее от страого по индексу
'''

def get_squares(array: list) -> list:
    
    answerArray = [0] * len(array)
    ptrL, ptrR, ptrAns = 0, -1, -1

    for _ in range(len(array)):
        if abs(array[ptrL]) <= abs(array[ptrR]):
            answerArray[ptrAns] = array[ptrR] ** 2
            ptrR -= 1
        else:
            answerArray[ptrAns] = array[ptrL] ** 2
            ptrL += 1
        ptrAns -= 1
    
    return answerArray

inputArray = [-4, -2, 24, 25]
print(inputArray, get_squares(inputArray))