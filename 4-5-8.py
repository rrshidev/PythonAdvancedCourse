"""
Ходы коня

На шахматной доске 8×88 \times 88×8 стоит конь. Напишите программу, которая отмечает положение коня на доске и все
клетки, которые бьет конь. Клетку, где стоит конь, отметьте английской буквой N, клетки, которые бьет конь, отметьте
символами *, остальные клетки заполните точками.

Формат входных данных
На вход программе подаются координаты коня на шахматной доске в шахматной нотации (то есть в виде e4, где сначала
записывается номер столбца (буква от a до h, слева направо), затем номеру строки (цифра от 111 до 888, снизу вверх)).

Формат выходных данных
Программа должна вывести на экран изображение доски, разделяя элементы пробелами.

Примечание. Шахматная доска имеет вид:

Тестовые данные 🟢

Sample Input 1:

b6

Sample Output 1:

* . * . . . . .
. . . * . . . .
. N . . . . . .
. . . * . . . .
* . * . . . . .
. . . . . . . .
. . . . . . . .
. . . . . . . .
"""


def chess_knight(position):
    xs = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    x = xs.index(position[0])
    y = 8 - int(position[1])

    chess_board = []
    for number in range(8):
        place = []
        for letter in range(8):
            if letter == x and number == y:
                place.append('N')
            elif letter == x - 2 and number == y - 1:
                place.append('*')
            elif letter == x + 2 and number == y - 1:
                place.append('*')
            elif letter == x - 1 and number == y - 2:
                place.append('*')
            elif letter == x + 1 and number == y - 2:
                place.append('*')
            elif letter == x - 2 and number == y + 1:
                place.append('*')
            elif letter == x + 2 and number == y + 1:
                place.append('*')
            elif letter == x - 1 and number == y + 2:
                place.append('*')
            elif letter == x + 1 and number == y + 2:
                place.append('*')
            else:
                place.append('.')
        chess_board.append(place)
        print(*place)


coordinate = input()
chess_knight(coordinate)
