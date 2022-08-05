"""
Искусственный интеллект Антон, созданный Гилфойлом, взломал сеть умных холодильников. Теперь он использует их в качестве серверов "Пегого дудочника". Помогите владельцу фирмы отыскать все зараженные холодильники.
Для каждого холодильника существует строка с данными, состоящая из строчных букв и цифр, и если в ней присутствует слово "anton" (необязательно рядом стоящие буквы, главное наличие последовательности букв), то холодильник заражен и нужно вывести номер холодильника, нумерация начинается с единицы

Формат входных данных
В первой строке подаётся число nnn – количество холодильников. В последующих nnn строках вводятся строки, содержащие латинские строчные буквы и цифры, в каждой строке от 555 до 100100100 символов.

Формат выходных данных
Программа должна вывести номера зараженных холодильников через пробел. Если таких холодильников нет, ничего выводить не нужно.

TEST INPUT:
9
osfjwoiergwoignaewpjofwoeijfnwfonewfoignewtowenffnoeiwowjfninoiwfen
anton
aoooooooooontooooo
elelelelelelelelelel
ntoneeee
tonee
253235235a5323352n25235352t253523523235oo235523523523n
antoooooooooooooooooooooooooooooooooooooooooooooooooooon
unton
"""


def has_sequence(string, sequence):
    if len(string) < len(sequence):
        return False

    seq_idx = 0
    for ch in string:
        if ch == sequence[seq_idx]:
            seq_idx += 1

            if seq_idx == len(sequence):
                return True  # found it!

    return False


n = int(input())
result = []
for i in range(n):
    test_str = input()
    if has_sequence(test_str, "anton"):
        result.append(i + 1)
print(result)
