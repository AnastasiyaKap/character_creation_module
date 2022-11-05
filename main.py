from random import randint


def attack(char_name, char_class):
    if char_class == 'warrior':
        return (f' {char_name} нанёс урон противнику равный '
                f' {5 + randint(3, 5)}')
    if char_class == 'mage':
        return (f'{char_name} нанёс урон противнику равный '
                f'{5 + randint(5, 10)}')
    if char_class == 'healer':
        return (f'{char_name} нанёс урон противнику равный '
                f'{5 + randint(-3, -1)}')
    return (f'{char_name} не применил специальное умение')


def defence(char_name, char_class):
    if char_class == 'warrior':
        return (f'{char_name} блокировал {10 + randint(5, 10)} урона')
    if char_class == 'mage':
        return (f'{char_name} блокировал {10 + randint(-2, 2)} урона')
    if char_class == 'healer':
        return (f'{char_name} блокировал {10 + randint(2, 5)} урона')
    return (f'{char_name} не блокировал урон')


def special(char_name, char_class):
    if char_class == 'warrior':
        return (f'{char_name}применил специальное умение '
                f' «Выносливость {80 + 25}»')
    if char_class == 'mage':
        return (f'{char_name} применил специальное умение «Атака {5 + 40}»')
    if char_class == 'healer':
        return (f'{char_name} применил специальное умение «Защита {10 + 30}»')
    return (f'{char_name} не применил специальное умение')


def start_training(char_name: str, char_class: str):
    if char_class == 'warrior':
        print(f'{char_name}, ты Воитель — отличный боец ближнего боя.')
    if char_class == 'mage':
        print(f'{char_name}, ты Маг — превосходный укротитель стихий.')
    if char_class == 'healer':
        print(f'{char_name}, ты Лекарь — чародей, способный исцелять раны.')
    print('Потренируйся управлять своими навыками.')
    print('Введи одну из команд: attack — чтобы атаковать противника, '
          'defence — чтобы блокировать атаку противника '
          'special — чтобы использовать свою суперсилу.')
    print('Если не хочешь тренироваться, введи команду skip.')
    cmd = None
    while cmd != 'skip':
        cmd = input('Введи команду: ')
        if cmd == 'attack':
            print(attack(char_name, char_class))
        if cmd == 'defence':
            print(defence(char_name, char_class))
        if cmd == 'special':
            print(special(char_name, char_class))
    return 'Тренировка окончена.'


def choice_char_class():
    approve_choice = None
    char_class = None
    while approve_choice != 'y':
        hero_input = "Введи название персонажа, за которого хочешь играть"
        hero_1 = "Воитель — warrior"
        hero_2 = "Маг — mage"
        hero_3 = "Лекарь — healer"
        char_class = input(f'{hero_input}:{hero_1},{hero_2},{hero_3}:')
        if char_class == 'warrior':
            warrior_char1 = "Воитель — дерзкий воин ближнего боя."
            warrior_char2 = "Cильный, выносливый и отважный."
            print(f'{warrior_char1} {warrior_char2 }')
        if char_class == 'mage':
            mage_char1 = "Маг — находчивый воин дальнего боя."
            mage_char2 = "Обладает высоким интеллектом."
            print(f'{mage_char1} {mage_char2}')
        if char_class == 'healer':
            healher_char1 = "Лекарь — могущественный заклинатель."
            healher_char2 = "Черпает силы из природы, веры и духов."
            print(f'{healher_char1} {healher_char2}')
        buttons = "Нажми (Y), чтобы подтвердить выбор, или любую другую кнопку"
        other_hit = "чтобы выбрать другого персонажа"
        approve_choice = input(f'{buttons},{other_hit}').lower()
    return char_class


def main():
    print('Приветствую тебя, искатель приключений!')
    print('Прежде чем начать игру...')
    char_name = input('...назови себя: ')
    print(f'Здравствуй, {char_name}! '
          'Сейчас твоя выносливость — 80, атака — 5 и защита — 10.')
    print('Ты можешь выбрать один из трёх путей силы:')
    print('Воитель, Маг, Лекарь')
    char_class = choice_char_class()
    print(start_training(char_name, char_class))


main()
