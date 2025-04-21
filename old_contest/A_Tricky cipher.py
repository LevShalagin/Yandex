def get_code(data: str):
    person_data = data.split(',')

    date = sum(map(int, list(person_data[-3])))
    month = sum(map(int, list(person_data[-2])))

    num1 = len(set(list(person_data[0] + person_data[1] + person_data[2])))
    num2 = (date + month) * 64
    num3 = (ord(person_data[0][0].upper()) - 64) * 256
    res = hex(num1 + num2 + num3)[-3:].upper().zfill(3)
    
    return res

for _ in range(int(input())):
    print(get_code(input()), end=' ')