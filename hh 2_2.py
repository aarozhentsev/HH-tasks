n = int(input()) #Вводим n
m = int(input()) #Вводим m
count = 0 #Счетчик действий
while n!=m:
    if m-1==n:
        m-=1
        count+=1
    elif m%2!=0:
        if ((m-1)/2)<m-4 and ((m-1)/2)>=n:
            m = (m-1)/2
            count+=2
        else:
            m-=2
            count+=1
    elif m%2==0:
        if m/2<m-2 and m/2>=n:
            m/=2
            count+=1
        else:
            m-=2
            count+=1
print(count) #Выводим ответ
