from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QVBoxLayout, QGroupBox, QButtonGroup, QRadioButton , QPushButton, QLabel
from random import randint, shuffle

class Question():
    '''Класс для вопроса, правильного ответа и 3 неправильных'''
    def __init__(self, question, right_answer, wrong1, wrong2, wrong3):
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3
question_list = []
question_list.append(Question('Государственый язык Бразилии?','Португальский', 'Испанский', 'Английский', 'Бразильский'))
question_list.append(Question('какого цвета нет на флаге России?', 'Зеленый', 'Красный', 'синий','белый'))
question_list.append(Question('какого персанажа нет в доте ?', 'дед инсайд', 'шторм', 'акс', 'энигма'))
question_list.append(Question('какого бравлера нет в бравл старс?', 'пудж', 'леон', 'ворон', 'спайк'))
question_list.append(Question('какого имени нет в девчачем ЯЫыЫ аниме ?', 'негр', 'хината', 'сакура', 'хани'))


app = QApplication([])

#Интерфейс
btn_OK = QPushButton('Ответить')
lb_Question = QLabel('Самый сложный вопрос в мире!')

#группа вариантов ответов
RadioGroupBox = QGroupBox('Варианты ответов')
rbtn_1 = QRadioButton('Вариант 1')
rbtn_2 = QRadioButton('Вариант 2')
rbtn_3 = QRadioButton('Вариант 3')
rbtn_4 = QRadioButton('Вариант 4')

RadioGroup = QButtonGroup()
RadioGroup.addButton(rbtn_1)
RadioGroup.addButton(rbtn_2)
RadioGroup.addButton(rbtn_3)
RadioGroup.addButton(rbtn_4)

layout_ans1 = QHBoxLayout()
layout_ans2 = QVBoxLayout()
layout_ans3 = QVBoxLayout()
layout_ans2.addWidget(rbtn_1)
layout_ans2.addWidget(rbtn_2) #вертикальные будут внутри горизатального
layout_ans3.addWidget(rbtn_3)
layout_ans3.addWidget(rbtn_4) #два ответа в первый столбец

layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3) # разместили столбцы в одной строке 

RadioGroupBox.setLayout(layout_ans1)

AnsGroupBox = QGroupBox('Результат теста')
lb_Result = QLabel('прав ты или нет?') # размещение надписи правильно или нет
lb_Correct = QLabel('ответ будет тут!') # текст правильного ответа 

layout_res = QVBoxLayout()
layout_res.addWidget(lb_Result, alignment = (Qt.AlignLeft | Qt.AlignTop))
layout_res.addWidget(lb_Correct, alignment = Qt.AlignHCenter, stretch = 2)
AnsGroupBox.setLayout(layout_res)

layout_line1 = QHBoxLayout() # вопрос
layout_line2 = QHBoxLayout() #варианты ответа
layout_line3 = QHBoxLayout() # КНОПКА ОТВЕТИТЬ

layout_line1.addWidget(lb_Question, alignment = (Qt.AlignHCenter | Qt.AlignVCenter))
layout_line2.addWidget(RadioGroupBox)
layout_line2.addWidget(AnsGroupBox)
AnsGroupBox.hide() # скроем панель с оветом сначала должна быть видна панель с вопросом 

layout_line3.addStretch(1)

layout_line3.addWidget(btn_OK, stretch = 2) 
layout_line3.addStretch(1)

layout_card = QVBoxLayout()

layout_card.addLayout(layout_line1, stretch = 2)
layout_card.addLayout(layout_line2, stretch = 8)
layout_card.addStretch(1)
layout_card.addLayout(layout_line3, stretch = 1)
layout_card.addStretch(1)
layout_card.setSpacing(5) # пробелы между содержимы 

def show_result():
    '''показать панель ответов'''
    RadioGroupBox.hide()
    AnsGroupBox.show()
    btn_OK.setText('Следущий вопрос')

def show_question():
    '''показать панель вопросов'''
    RadioGroupBox.show()
    AnsGroupBox.hide()
    btn_OK.setText('Ответить')
    RadioGroup.setExclusive(False) #сняли ограничения
    rbtn_1.setChecked(False)
    rbtn_2.setChecked(False)
    rbtn_3.setChecked(False)
    rbtn_4.setChecked(False)
    RadioGroup.setExclusive(True) #вернули ограничения теперь только 1 кнопка может быть
answers = [rbtn_1,rbtn_2, rbtn_3, rbtn_4]
def ask(q: Question):


    '''Функция записывает значения вопроса и ответов соответственно в виджеты, случайным образом'''
    shuffle(answers)
    answers[0].setText(q.right_answer)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    lb_Question.setText(q.question)
    lb_Correct.setText(q.right_answer)
    show_question()

def show_correct(res):
    # показать результат - установка текста в надпись и показ нужной панели 
    lb_Result.setText(res)
    show_result()

def check_answer():
    #если выбран вариант ответа то проверка и показ панель ответов 
    if answers[0].isChecked():
        show_correct('Правильно!')
        window.score += 1
        print('Статистика/n -Всего вопросов:', window.total, '/n- Правильных ответов:', window.score)
        print('Рейтинг:', (window.score/window.total*100), '%')
    else:
        if answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked():
            # неправильный ответ
            show_correct('Неверно!')
            print('Рейтинг:', (window.score/window.total*100), '%')
            
def next_question():
    window.total += 1
    print('Статистика/n -Всего вопросов:', window.total, '/n- Правильных ответов:', window.score)
    cur_question = randint(0, len(question_list) - 1)
    q = question_list[cur_question]

    ask(q)
window = QWidget()
window.setLayout(layout_card)
window.setWindowTitle('Memory Card')



def click_OK():
    if btn_OK.text() == 'Ответить':
        check_answer()
    else:
        next_question()

window.score = 0
window.total = 0
next_question()
    
btn_OK.clicked.connect(click_OK)
next_question()
window.resize(400, 300)
window.show()
app.exec()