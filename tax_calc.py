x= int(input("enter the salary"))
if x<10000 :
    print("no tax ")
elif x<20000:
    print(f"the tax mt req to pay is {(x-10000)*0.1}")
else:
    print(f'tax= {(x-20000)*0.2+1000}')

