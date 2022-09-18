import mysql.connector,datetime
jana =mysql.connector.connect(
            host="localhost",
            user="root",
            password="12345678",
            database="covid"
           
           )
def covidcase(state,district,village,positive,death,recovery):
            mycursor=jana.cursor()
            current_time = datetime.datetime.now()
            print (current_time)
            covidcase="insert into covidcase(state,district,village,positive_case,death_case,recovered_case) value(%s,%s,%s,%s,%s,%s)"
            data=(state,district,village,positive,death,recovery)
            mycursor.execute(covidcase,data)
            jana.commit()
            print("data added Successful!")
def village(v):
    mycursor=jana.cursor()
    mycursor.execute(f"select positive_case,death_case,recovered_case from covidcase where village='{v}'")
    result=mycursor.fetchall()
    if result!=[]:
        pk=result[0]
        print(f"{v} positive cases='{pk[0]}'")
        print(f"{v} death_cases='{pk[1]}'")
        print(f"{v} recovered_cases='{pk[2]}'")
    else:
        print("Enter valdi village name")
def distic(district):
    
    mycursor=jana.cursor()
    mycursor.execute(f"select village from covidcase where district='{district}' ")
    result=mycursor.fetchall()
    if result!=[]:
        for i in range(len(result)):
          pk=result[i]
          print(f"'{i}'",pk[0])
        v=input("enter your village: ")
        village(v)
    else:
        print("Please enter valid districtt")

def search(state):
    
            mycursor=jana.cursor()
            mycursor.execute(f"select district from covidcase where state='{state}' ")
            result=mycursor.fetchall()
            if result!=[]:
              for i in range(len(result)):
                 pk=result[i]
                 print(f"'{i}'",pk[0])
              district=input("Enter your district: ")
              distic(district)
            else:
               print("Please enter valid state")

user=int(input("If you want to enter 1 to add a data \n if you enter 2 to search you data\n"))
if user==1:
    state=input("Enter Your State: ")
    district=input("Enter Your district: ")
    village=input("Enter Your village: ")
    positive=input("Enter Your positive: ")
    death=input("Enter Your death: ")
    recovery=input("Enter Your recovery: ")
    covidcase(state,district,village,positive,death,recovery)
elif user==2:
    state=input("enter your state: ")
    search(state)
else:
    print("thanks for visit")




