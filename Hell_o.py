#прост балуюсь с питоном: нет ; каждая новая строка - это реально новая строка
#12 - интеджер, целое число
#12.0 - флоат, число с точкой
#1/0 - булеан
# всё что написано в кавычках - это строки
import random #импортирование модуля
print("Хелло!")
test = 12 #задание переменной, имя нельзя начинать с цифры, чувствительны к регистру, не должны совпадать с зарезервированными именами, но не надо указывать тип
username = "%username%" #задание переменной типа строка
plus = random.randint(1, 5)
name = str(input("Кто в курсе что тут происходит?\n")) #приведение переменной к строке и перевод указателя на следующую строку
if(name=="я"):
    print("Ты уверен, что ты не Алоша?")
elif(name=="ты"):
    print("ОЙ, ВСЁ! (ты не Алоша)")
elif(name!="хуй"): #если не равно
    print("И где найти этого", name,",", username,"?")
else:
    print("Сама ты хуй!", end ='') #отсутствие перевода на следующую строку
num = float (input ("Введи число, будь не Алошей: ")) #приведение переменной к числу
print("Ты ввёл в меня ", num,"??? Да ты прирожденный Алоша!")
num += plus # перезапись переменной увеличенной на рандомную переменную plus
print("Да ты Алоша! А", num,"не хочешь себе в пещеры?")
plus = plus // 5 +1
num *= plus # перезапись переменной умноженной на plus
print("А", num,", ", username,"?")
if(name=="хуй"):
    print("Вот и кто теперь", username,"?")
del test # удаление переменной
