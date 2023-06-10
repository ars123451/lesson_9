import random
import logging

log_d = logging.getLogger("TAD")
# log = logging.getLogger('Only main')
# log.setLevel(logging.INFO)
# fh = logging.FileHandler("Only_main.log", 'w', 'utf-8')
# formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
# fh.setFormatter(formatter)
# log.addHandler(fh)


# log_d = logging.getLogger('Debugger')
# log_d.setLevel(logging.DEBUG)
# fh_d = logging.FileHandler("Only_debug.log", 'w', 'utf-8')
# formatter_d = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
# fh_d.setFormatter(formatter_d)
# log_d.addHandler(fh_d)

logging.basicConfig(level=logging.DEBUG)


# logging.basicConfig(level=logging.INFO)

def do_throw_ball(skittle_counter=10):
    ball_1 = random.randint(0, skittle_counter)
    ball_2 = random.randint(0, skittle_counter - ball_1)
    return ball_1, ball_2


def frame(frame_counter, ball_1, ball_2):
    if ball_1 == 10:
        log_d.info(f'{frame_counter}.1 - ***STRIKE!!!***')
        return 'X'
    else:
        if ball_1 == 0:
            log_d.debug(f'{frame_counter}.1 - You missed the ball 1!')
        else:
            log_d.debug(f'{frame_counter}.1 - {ball_1}')
        if ball_2 == 0:
            log_d.debug(f'{frame_counter}.2 - You missed the ball 2!')
        else:
            log_d.debug(f'{frame_counter}.2 - {ball_2}')
        if ball_1 + ball_2 == 10:
            log_d.info(f'{frame_counter}.2 - SPARE!')
            return str(ball_1) + '/'
        else:
            return str(ball_1) + str(ball_2)


def full_game():
    score_counter = ''
    for counter in range(10):
        ball_1, ball_2 = do_throw_ball()
        score_counter += frame(counter + 1, ball_1, ball_2)
    return score_counter


def get_score(self, game_result):
    pass


if __name__ == '__main__':
    print(full_game())

# Всего 10 кеглей. Игра состоит из 10 фреймов. В одном фрейме до 2х бросков, цель - сбить все кегли.
# Результаты фрейма записываются символами:
#   «Х» – «strike», все 10 кеглей сбиты первым броском
#   «<число>/», например «4/» - «spare», в первый бросок сбиты 4 кегли, во второй – остальные
#   «<число><число>», например, «34» – в первый бросок сбито 3, во второй – 4 кегли.
#   вместо <число> может стоять прочерк «-», например, «-4» - ни одной кегли не было сбито за бросок (первый или второй)
# Результат игры – строка с записью результатов фреймов. Символов-разделителей между фреймами нет.
# Например, для игры из 3 фреймов запись результатов может выглядеть так:
#   «Х4/34»
# Предлагается упрощенный способ подсчета количества очков:
#   «Х» – 20 очков, «4/» - 15 очков, «34» – сумма 3+4=7
# То есть для игры «Х4/34» сумма очков равна 20+15+7=42
#
# Надо написать python-модуль (назвать bowling), предоставляющий API расчета количества очков:
# функцию get_score, принимающую параметр game_result. Функция должна выбрасывать исключения,
# когда game_result содержит некорректные данные. Использовать стандартные исключения по максимуму,
# если не хватает - создать свои.
#
# Обязательно написать тесты на этот модуль. Расположить в папке tests.

# Из текущего файла сделать консольную утилиту для определения количества очков, с помощью пакета argparse
# Скрипт должен принимать параметр --result и печатать на консоль:
#   Количество очков для результатов ХХХ - УУУ.

# При написании кода помнить, что заказчик может захотеть доработок и новых возможностей...
# И, возможно, вам пригодится паттерн проектирования "Состояние",
#   см https://clck.ru/Fudd8 и https://refactoring.guru/ru/design-patterns/state
