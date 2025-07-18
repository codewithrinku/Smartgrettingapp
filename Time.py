# This project is based on time like Good morning
import time
name = input("Enter your name : ")
name = name.capitalize()
present_time = time.strftime("%H:%M:%S")
present_time = int(time.strftime("%H"))
if (4<=present_time<=12):
    print(f"Good morning {name}", "it's time : ",present_time)
    print("Thanku sir ")
elif (12>= present_time <=5):
    print(f"Good Afternoon {name}", "it's time : ",present_time)
    print("Thanku sir ")
elif (5>= present_time <=8):
    print(f"Good evening {name}","it's time : ", present_time)
    print("Thanku sir ")
else :
    print(f"Good night {name}","it's time : ",present_time)
    print("Thanku sir ")
