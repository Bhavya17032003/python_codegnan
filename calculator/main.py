# importing modules
import Addition as add
import subraction as sb
from multiplication import mul
from Division import div

# main
if __name__=="__main__":
    print("welcome to calculator")
    operations = (
        "1.Addition.py \n",
        "2.subraction.py \n",
        "3.Division.py \n",
        "4.multiplication.py \n"
    )

    print(*operations)
    choice = int(input("select your operation: "))
    if choice == 1:
        a, b = map(int, input().split())
        res = add.Addition(n1 =a, n2 = b)
        print(res)
    elif choice == 2:
        a, b = map(int, input().split())
        res = sb.sub(n1 =a, n2 = b)
        print(res)
    elif choice == 3:
        a, b = map(int, input().split())
        res = div(n1 =a, n2 = b)
        print(res)
    elif choice == 4:
        a, b = map(int, input().split())
        res = mul(n1 =a, n2 = b)
        print(res)
    else:
        print("select correct operation")
    
    