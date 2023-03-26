# Дана строка (возможно, пустая), состоящая из буква A-Z:
# AAAABBBCCXYZDDDDEEEFFFAAAAAAABBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB
# Нужно написать функцию RLE, которая на выходе даст строку вида:
# A4B3C2XYZD4E3A6B28
# И сгенерирует ошибку, если на вход пришла невалидная строка.

# Пояснение: Если символ встречается 1 раз, он остается без изменений;
# Если символ повторяется более 1 раза, к нему добавляется количество повторений.

input_str = str(input("Строка:  "))


def rle(input_str):
    output_symbol = ''
    last_review_symbol = ''
    count = 1

    for i in input_str:
        if i != last_review_symbol:
            if last_review_symbol:
                output_symbol += last_review_symbol + str(count)
            count = 1
            last_review_symbol = i

        else:
            count += 1
    else:
        output_symbol += last_review_symbol + str(count)
        return output_symbol


if str.isupper(input_str):
    requested_str = rle(input_str)
    no_one_print = requested_str.replace('1', '')
    print(no_one_print)
else:
    print("Ошибка ввода строки")
