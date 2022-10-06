from venv import create
from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove, Update
from telegram.ext import (
    Updater,
    CommandHandler,
    MessageHandler,
    Filters,
    ConversationHandler,
    CallbackContext,
)

first_question, want_play, exit_play, choose_num_can, choose_max_num, start_play, \
    create_name, step_first_pl, step_second_pl, want_count = range(10)

def get_rational(update, _):
    #logger.my_log(update, CallbackContext, f'Ввел выражение {update.message.text}.')
    expr_temp = (update.message.text).replace(' ', '')
    expr_temp = expr_temp('\\' , '/')
    for i in expr_temp:
        if i.isalpha():
            update.message.replay_text(
                f'В вашем выражении есть букв, напишите заново без букв')
        return want_count

# list_dig = []
# list_operator = []


    list_number = []
    expr = expr_temp + ' '
    temp = ''
    for i in expr:
        if i.isdigit():
            temp += i
        else:
            list_number.append(temp)
            temp = ''
    list_number = list(filter(lambda x: x != '', list_number))
    list_number = list(map(float, list_number))
    list_operation = list(filter(lambda x: x == '/' or x == '*' or x == '+' or x == '-', expr))

    while len(list_operation) > 0:
        while '/' in list_operation:
            for i, elem in enumerate(list_operation):
                if elem == '/':
                    list_number[i] = list_number[i] / list_number[i+1]
                    del list_number[i + 1]
                    del list_operation[i]
        while '*' in list_operation:
            for i, elem in enumerate(list_operation):
                if elem == '*':
                    list_number[i] = list_number[i] * list_number[i+1]
                    del list_number[i + 1]
                    del list_operation[i]
        while '+' in list_operation:
            for i, elem in enumerate(list_operation):
                if elem == '+':
                    list_number[i] = list_number[i] + list_number[i+1]
                    del list_number[i + 1]
                    del list_operation[i]
        while '-' in list_operation:
            for i, elem in enumerate(list_operation):
                if elem == '-':
                    list_number[i] = list_number[i] - list_number[i+1]
                    del list_number[i + 1]
                    del list_operation[i]
    res =  list_number[0]

    update.message.reply_text(f'Ответ: {res}')

    reply_keyboard = [['Калькулятор', 'Игра', 'Выход']]
    markup_key = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)
    update.message.reply_text(
        f'{update.effective_user.first_name}, что вы хотите сделать?',
        reply_markup = markup_key,)
