def DigitAndX(s,var):
    i = 0
    while i<len(s)-1:
        if s[i].isdigit():
            if s[i+1]==var:
                s = s.replace(s[i]+s[i+1],s[i]+'*'+s[i+1])
        if s[i].isdigit() or s[i]==var:
            if s[i+1]=='(':
                s = s.replace(s[i]+s[i+1],s[i]+'*'+s[i+1]) 
        i+=1
    return s

def FindVar(s):
    i=0
    while i<len(s):
        if s[i].isalpha():
            x = s[i]
            break
        i+=1
    return(x)

z = str(input()) #Вводим нашу строку
import sympy #Используем библеотеку sympy
x = FindVar(z) #Ищем нашу переменную
z = z.replace('^','**') #Преобразуем в нужный для sympy вид
z = z.replace(')(',')*(') #Преобразуем в нужный для sympy вид
z = DigitAndX(z,x) #Преобразуем в нужный для sympy вид
x = sympy.Symbol(x) #Вводим переменную в sympy
z = sympy.sympify(z) #Преобразуем нашу строку в вид sympy
z = str(z.expand()) #Раскрываем скобки и выполняем арифметические операции
z = z.replace('**','^') #Преобразую обратно в наш вид
z = z.replace('*','') #Преобразую обратно в наш вид
print(z) #Выводим ответ
