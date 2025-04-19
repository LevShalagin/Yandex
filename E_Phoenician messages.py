
digit_to_letters = {
    '2': 'ABC',
    '3': 'DEF',
    '4': 'GHI',
    '5': 'JKL',
    '6': 'MNO',
    '7': 'PQRS',
    '8': 'TUV',
    '9': 'WXYZ'
}

def decode_message(digits):
    result = []
    i = 0
    while i < len(digits):
        digit = digits[i]
        count = 1
        while i + 1 < len(digits) and digits[i + 1] == digit:
            count += 1
            i += 1
        result.append(digit_to_letters[digit][count - 1])
        i += 1
    return ''.join(result)

def find_words(message, dictionary):
    result = []
    i = 0
    while i < len(message):
        for word in dictionary:
            if message[i:i+len(word)] == word:
                result.append(word)
                i += len(word)
                break
        else:
            i += 1
    return result

message = input()
n = int(input())
dictionary = set()
for _ in range(n):
    dictionary.add(input().upper())

decoded_message = decode_message(message)

words = find_words(decoded_message, dictionary)

print(' '.join(words))