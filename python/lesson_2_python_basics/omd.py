# Guido van Rossum <guido@python.org>

def make_choose():
    option = ''
    options = {'да': True, 'нет': False}
    while option not in options:
        print('Выберите: {}/{}'.format(*options))
        option = input()
    return options[option]


def step1():
    print(
        'Утка-маляр 🦆 решила выпить зайти в бар. '
        'Взять ей зонтик? ☂️'
    )
    option = make_choose()
    if option:
        return step2_umbrella()
    return step2_no_umbrella()


def step2_umbrella():
    print(
        'Топает утка в бар, а тут дождь начался.'
        'Обрадовалась, что зонтик с собой, пошла и напилась.'
    )
    return step4_choose_drink()


def step2_no_umbrella():
    print(
        'Топает утка в бар, а тут дождь начался.'
        'Утка развернулась и пошла домой к утятам?'
    )
    option = make_choose()
    if option:
        return step3_home()
    return step3_bar()


def step3_home():
    print(
        'Конечно, нет. Что там с утятами случится,'
        ' они же умеют плавать.'
    )
    return step4_choose_drink()


def step3_bar():
    print(
        'Правильно, имеет полное право пару часиков '
        'отдохнуть наша работяга. '
        'Пусть селезень хоть разок присмотрит за детьми'
    )
    return step4_choose_drink()


def step4_choose_drink():
    print('Выбери, что выпила утка в баре')
    drinks = ['сок', 'томатный сок', 'утиный сидр', 'сливочное пиво']
    option = ''
    while option not in drinks:
        print(f'Выберите: {"/".join(drinks)}')
        option = input()
    if option == 'утиный сидр':
        print('%s - отличный выбор, лайк от бармена' % option.title())
    elif option == 'сок' or option == 'сливочное пиво':
        print(
            '{} - хороший выбор, '
            'но селезень за соседним столом '
            'расстроился'.format(option.title())
        )
    else:
        print(option.title() + '...? Странная ты, утка...')

    how_many_glasses = 0
    while how_many_glasses <= 0 or how_many_glasses > 10:
        try:
            how_many_glasses = int(input('Сколько бокалов? (1-10): '))
            if how_many_glasses <= 0 or how_many_glasses > 10:
                print('Пожалуйста, введите число от 1 до 10!')
        except ValueError:
            print('Пожалуйста, введите целое число!')
            how_many_glasses = 0
    if option == 'утиный сидр':
        print(
            f'неполхо, но можно было бы '
            f'остановиться на {how_many_glasses - 1}')
    else:
        print('может ещё один?')


if __name__ == '__main__':
    print('История про утку-маляра')
    print('=' * 40)
    step1()
