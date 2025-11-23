import math

def lottery_Chance(N, K, M):
    # все исходы
    total_num = math.comb(N, K)

    # сумма исходов которые подходят
    good_outcomes = 0
    for i in range(M, K + 1):
        good_outcomes += math.comb(K, i) * math.comb(N - K, K - i)

    # округление до 4 знаков после запятой
    return (f'{(good_outcomes / total_num) * 100:.4f}')

while True:
    try:
        print('Лотерея "Шанс"!')
        N = int(input('Введите N (всего чисел): '))
        K = int(input('Введите K (сколько выбирается): '))
        M = int(input('Введите M (минимальное совпадение): '))

        if M > K or K > N or M < 0:
            print('Ошибка: некорректные значения!')
        else:
            result = lottery_Chance(N, K, M)
            print(f'Вероятность выигрыша в лотерею: {result}%')
            break
    except ValueError:
        print('Ошибка: введите целые числа!')