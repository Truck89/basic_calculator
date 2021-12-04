
is_valid = False
result = 0
memory = 0
[answer1, answer2, answer3] = ["z", "y", "z"]
msg_index = 10
msg = ["Enter an equation", 
    "Do you even know what numbers are? Stay focused!", 
    "Yes ... an interesting math operation. You've slept through all classes, haven't you?", 
    "Yeah... division by zero. Smart move...", 
    "Do you want to store the result? (y / n):", 
    "Do you want to continue calculations? (y / n):", 
    " ... lazy", 
    " ... very lazy", 
    " ... very, very lazy", 
    "You are", 
    "Are you sure? It is only one digit! (y / n)", 
    "Don't be silly! It's just one number! Add to the memory? (y / n)", 
    "Last chance! Do you really want to embarrass yourself? (y / n)"]


def is_one_digit(v):
    if type(v) is int and -10 < v < 10:
        return True
    else:
        return False
        
        
def check(v1, v2, v3):
    check_msg = ""
    if is_one_digit(v1) and is_one_digit(v2):
        check_msg = check_msg + msg[6]
    if (int(v1) == 1 or int(v2) == 1) and v3 == "*":
        check_msg = check_msg + msg[7]
    if (int(v1) == 0 or int(v2) == 0) and v3 in ["+","-","*"]:
        check_msg = check_msg + msg[8]
    if check_msg != "":
        print(msg[9] + check_msg)

while answer2 == "y":
    
    print(msg[0])
    calc = input()
    x, oper, y = calc.split()
    
    if x == "M":
        x = memory
    if y == "M":
        y = memory
    
    try:
        x, y = float(x), float(y)
    except:
        print(msg[1])
        continue
    
    if oper in ["+","-","*","/"]:
        is_valid = True
    else:
        is_valid = False
        print(msg[2])
        continue
    
    if x % 1 == 0:
        x = int(x)
    if y % 1 == 0:
        y = int(y)
        
    check(x, y, oper)
        
    if oper == "+":
        result = x + y
    elif oper == "-":
        result = x - y
    elif oper == "*":
        result = x * y
    elif oper == "/" and y == 0:
        print(msg[3])
        continue
    else:  # division
        result = x / y
        
    print(float(result))
    
    #  Check whether user wants to save result
    answer1 = "z"
    while answer1 != "y" and answer1 != "n":
        print(msg[4])
        answer1 = input()
        
    if answer1 == "y":
        # memory = result
        msg_index = 10
        if not is_one_digit(result):
            memory = result
        else:
            
            while True:
                print(msg[msg_index])
                answer3 = input()
                
                if answer3 == "y":
                    if msg_index < 12:
                        msg_index += 1
                        continue
                    else:
                        memory = result
                        break
                elif answer3 == "n":
                    break
                else:
                    continue
    
    #  Check whether user wants to make another calculation
    answer2 = "z"
    while answer2 != "y" and answer2 != "n":
        print(msg[5])
        answer2 = input()
        
