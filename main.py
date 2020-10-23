#ИМПОРТ БИБЛИОТЕК
import re
from num2words import num2words
#КОНЕЦ ИМПОРТА БИБЛИОТЕК

#НАЧАЛО РАБОТЫ С ДАННЫМИ
digits_dict = {'ноль': 0,'один': 1,'два': 2,'три': 3, 'четыре': 4, 'пять': 5, 'шесть': 6, 'семь': 7,'восемь'
                  :8, 'девять': 9,'десять':10, 'одиннадцать': 11, 'двенадцать': 12, 'тринадцать': 13, 'четырнадцать':
                  14,'пятнадцать': 15, 'шестнадцать': 16, 'семнадцать': 17, 'восемнадцать': 18, 'девятнадцать':19,
                  'двадцать': 20,'тридцать': 30,'сорок': 40,'пятьдесят': 50, 'шестьдесят': 60, 'семьдесят': 70, 'восемьдесят':
                  80, 'девяносто': 90}
operation_dict = ['плюс', 'минус', 'умножить', 'разделить на']

after_dot = ['десятая', 'сотая', 'десятая', 'тысячная',  ]

small_nums = ['ноль','один','два','три', 'четыре', 'пять', 'шесть', 'семь','восемь', 'девять']
big_nums = ['двадцать','тридцать','сорок','пятьдесят', 'шестьдесят', 'семьдесят', 'восемьдесят', 'девяносто']

eror_dict =  ['десять','одиннадцать', 'двенадцать', 'тринадцать', 'четырнадцать','пятнадцать', 'шестнадцать', 'семнадцать', 'восемнадцать', 'девятнадцать'] #СПИСОК ДЛЯ ПРОВЕРКИ


#КОНЕЦ РАБОТЫ С ДАННЫМИ

#ФУНКЦИЯ ДЕЛЕНИЯ

def division(numerator, denominator):
    if (numerator % denominator == 0):
        ans= str(numerator//denominator)
        return ans
    else:
        ans= str(numerator//denominator)+ "."
        l={}
        index=0
        numerator = numerator%denominator
        l[numerator]=index
        t=False
        while t==False:
            if numerator==0:
                break
            digit = numerator*10//denominator
            numerator=numerator*10-(numerator*10//denominator)*denominator
            if numerator not in l:
                ans+=str(digit)
                index+=1
                l[numerator]=index
                t=False
            else:
                ans+=str(digit)+")"
                ans=ans[:l.get(numerator)+len(ans[:ans.index(".")+1])]+"("+ ans[l.get(numerator)+len(ans[:ans.index(".")+1]):]
                t=True
        return ans

#ФУНКЦИЯ ДЕЛЕНИЯ


def calc(main_str):    #ФУНКЦИЯ КАЛЬКУЛЯТОР, ЕСЛИ ВЫВОДИТСЯ ОТВЕТ "-1" - следовательно что-то сделано неверно!

	if not main_str:
		return -1
	current_operation = 'error'
	for string in operation_dict:   #ПОИСК ОПЕРАЦИИ В СТРОКЕ
		match = re.search(string, main_str)
		if match:
			current_operation = string   #ОПЕРАЦИЯ
	if current_operation == 'error':
		return -1

	tokens = main_str.split(' ' + current_operation + ' ')   #ДЕЛИМ ЧИСЛО УДАЛЯЯ ОПЕРАЦИЮ
	first_num, second_num = tokens[:-1], tokens[-1:]




	match = re.search(' ', first_num[0])    #ПРОВЕРКА НА СОСТАВНОЕ ЧИСЛО 1
	if match:
		first_num = first_num[0].split(' ')
		for string in eror_dict:
			if string == first_num[0] or string == first_num[1]:
				return -1

		first_flag = 0
		second_flag = 0
		for string in small_nums:
			if string == first_num[1]:
				first_flag += 1
		for string in big_nums:
			if string == first_num[0]:
				second_flag += 1

		if first_flag == 0 or second_flag == 0:
			return -1

		first_num = digits_dict[first_num[0]] + digits_dict[first_num[1]]
	else:
		first_num = digits_dict[first_num[0]]

	match = re.search(' ', second_num[0])  #ПРОВЕРКА НА СОСТАВНОЕ ЧИСЛО 2
	if match:
		second_num = second_num[0].split(' ')
		for string in eror_dict:
			if string == second_num[0] or string == second_num[1]:
				return -1

		first_flag = 0
		second_flag = 0
		for string in small_nums:
			if string == second_num[1]:
				first_flag += 1
		for string in big_nums:
			if string == second_num[0]:
				second_flag += 1

		if first_flag == 0 or second_flag == 0:
			return -1

		second_num = digits_dict[second_num[0]] + digits_dict[second_num[1]]
	else:
		second_num= digits_dict[second_num[0]]




	if current_operation == "плюс":
		ans = first_num + second_num
	elif current_operation == "умножить":
		ans = first_num * second_num
	elif current_operation == "минус":
		ans = first_num - second_num
	elif current_operation == "разделить на":
		ans = division(first_num, second_num)

	ans = num2words(ans, lang='ru')
	return ans


flag = True
while flag:
	line_main = input('Введите выражение: ')
	line_main = line_main.lower()

	ans = calc(line_main)
	if ans != -1:
		print('Ответ =',ans)
		flag = False
	else:
		flag = True
		print('Вы ввели неверное выражение!')


