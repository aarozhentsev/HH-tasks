n = int(input()) #Вводим n
m = int(input()) #Вводим m
count = 0 #Счетчик действий
while m != n:
    if (m<6 or m//2<n) and m-n>1: 
        m-=2
    elif m-1==n or m%2!=0: 
        m-=1
    else: 
        m//=2
    count+=1
print(count) #Выводим ответ
