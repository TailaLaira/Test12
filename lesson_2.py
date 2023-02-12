#1 - Добавить 8 своих вопросов чтобы общее кол-во стало 10
#2 - Добавить возможность ввода своего вопроса из консоли
#3 - Добавить проверку кол-ва правильных ответов, <=50% - плохой результат, 50% - 75% - cредний результат, 75 - 100 - отличный результат


right_ans = 0 #Cчётчик правильных ответов

class Question():
    def __init__(self,question,answer1,answer2,answer3,answer4,right_answer):
        self.question = question
        self.answer1 = answer1
        self.answer2 = answer2
        self.answer3 = answer3
        self.answer4 = answer4
        self.right_answer = right_answer

qst0 = Question("Как зовут вашего преподавателя?","Олег","Сергей","Вадим","Андрей","Олег")
qst1 = Question("Какого цвета белый медведь?","Cерого","Жёлтого","Белого","Зелёного","Белого")
lst_q = [qst0,qst1]
for i in lst_q:
    print(i.question)
    print("-",i.answer1)
    print("-",i.answer2)
    print("-",i.answer3)
    print("-",i.answer4)
    my_ans = input("Введите ответ: ")
    if my_ans == i.right_answer:
        right_ans += 1
else:
    print("Количество верных ответов:",right_ans)