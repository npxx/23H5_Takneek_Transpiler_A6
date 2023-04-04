cond = 0
active_loc = 'start'

def init():
    global cond, active_loc
    result.write(f"{active_loc}, {cond}, oat_stage[1]\n")
    cond += 1
    result.write(f"oat_stage, {cond}, pronite_2\n")
    result.write(f"pronite_2, {cond}, mt_3_2\n")
    active_loc = "mt_3_2"

def end_graph():
    global cond, active_loc
    result.write(f"{active_loc}, {cond}, oat_stage[1]\n")
    cond += 1
    result.write(f"oat_stage, {cond}, finish\n")
    active_loc = "finish"

result = open("output.iitkv", "w")
active_loc = "start"
path = "path.txt"

with open(path, "r") as infile:
    tokens = infile.read().split()

init()

for a in tokens:
    if a == "input":
        prep_insert()
        take_input(2)
    elif a == "output":
        output(2)
        popf()
    elif a == "pop":
        popf()
    elif a == "add":
        operations("hall_2")
    elif a == "sub":
        operations("hall_5")
    elif a == "mul":
        operations("hall_3")
    elif a == "div":
        operations("hall_12")
    elif a == "mod":
        mod()
    elif a == "swap":
        swap()
    elif a == "cycle":
        cyc()
    elif a == "rev":
        rev()
    elif a == "dup":
        dup()
    elif a == "outputascii":
        asciiout()
        popf()
    elif a == "debug":
        debug()
    elif a == "rcycle":
        rcyc()
    elif is_num(a):
        n = int(a)
        push(n)
    elif a == "quit":
        end_graph()
    elif a == "if":
        loop_start()
    elif a == "fi":
        loop_end()
    elif a == "inputascii":
        prep_insert()
        result.write(f"{active_loc}, {cond}, hall_13_3\n")
        active_loc = "hall_13_3"
        asciiin()
    elif a == "and":
        bitwise_and()
    elif a == "xor":
        bitwise_xor()
    elif a == "or":
        bitwise_or()
    elif a == "not":
        bitwise_not()
    elif a == "nand":
        bitwise_and()
        bitwise_not()
    elif a == "nor":
        bitwise_or()
        bitwise_not()

end_graph()
