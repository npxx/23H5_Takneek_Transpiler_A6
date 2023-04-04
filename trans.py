cond = 0
active_loc = 'start'


#Graph_Start
def init():
    global cond, active_loc
    result.write(f"{active_loc}, {cond}, oat_stage[1]\n")
    cond += 1
    result.write(f"oat_stage, {cond}, pronite_2\n")
    result.write(f"pronite_2, {cond}, mt_3_2\n")
    active_loc = "mt_3_2"

#Graph_End
def end_graph():
    global cond, active_loc
    result.write(f"{active_loc}, {cond}, oat_stage[1]\n")
    cond += 1
    result.write(f"oat_stage, {cond}, finish\n")
    active_loc = "finish"

#Auxilary function for push
def prep_insert():
    global cond, active_loc
    result.write(f"{active_loc}, {cond}, oat_stage[1]\n")
    cond += 1

    result.write(f"oat_stage, {cond}, rm_1\n")
    result.write(f"rm_1, {cond}, rm_2\n")
    result.write(f"rm_2, {cond}, rm_3\n")
    result.write(f"rm_3, {cond}, mt_3_2\n")
    result.write(f"mt_3_2, {cond}, hall_13_2\n")

    active_loc = "hall_13_2"

#Input function
def get_input(p):
    global cond, active_loc
    result.write(f"{active_loc}, {cond}, oat_stage[1]\n")
    cond += 1

    result.write(f"oat_stage, {cond}, ")
    if p == 1:
        result.write(f"iit_gate_in_1\n")
        active_loc = "iit_gate_in_1"
    elif p == 2:
        result.write(f"iit_gate_in_2\n")
        active_loc = "iit_gate_in_2"

#Output function
def pr_output(p):
    global cond, active_loc
    result.write(f"{active_loc}, {cond}, oat_stage[1]\n")
    cond += 1

    result.write(f"oat_stage, {cond}, ")

    if p == 1:
        result.write(f"iit_gate_out_1\n")
        active_loc = "iit_gate_out_1"
    elif p == 2:
        result.write(f"iit_gate_out_2\n")
        active_loc = "iit_gate_out_2"

#Pop function
def popf():
    global cond, active_loc
    result.write(f"{active_loc}, {cond}, oat_stage[1]\n")
    cond += 1

    result.write(f"oat_stage, {cond}, mt_2_3\n")
    result.write(f"mt_2_3, {cond}, hall_13_3\n")
    result.write(f"hall_13_3, {cond}, kd_1\n")
    result.write(f"kd_1, {cond}, kd_2\n")
    result.write(f"kd_2, {cond}, kd_3\n")

    active_loc = "kd_3"


#Arithmetic operations
def operations(hall):
    global cond, active_loc
    result.write(f"{active_loc}, {cond}, oat_stage[1]\n")
    cond += 1

    result.write(f"oat_stage, {cond}, {hall}\n")
    result.write(f"{hall}, {cond}, mt_1_3\n")
    result.write(f"mt_1_3, {cond}, pronite_2\n")
    result.write(f"pronite_2, {cond}, hall_13_3\n")
    result.write(f"hall_13_3, {cond}, kd_1\n")
    result.write(f"kd_1, {cond}, kd_2\n")
    result.write(f"kd_2, {cond}, kd_3\n")

    active_loc = "kd_3"

def mod():
    global cond, active_loc

    result.write(f"{active_loc}, {cond}, oat_stage[1]\n")
    cond += 1
    
    result.write(f"oat_stage, {cond}, hall_12\n")
    result.write(f"hall_12, {cond}, rm_1\n")
    result.write(f"rm_1, {cond}, rm_2\n")
    result.write(f"rm_2, {cond}, rm_3\n")
    result.write(f"rm_3, {cond}, hall_3\n")
    result.write(f"hall_3, {cond}, mt_1_3\n")
    result.write(f"mt_1_3, {cond}, hall_13_3\n")
    result.write(f"hall_13_3, {cond}, hall_13_2\n")
    result.write(f"hall_13_2, {cond}, kd_1\n")
    result.write(f"kd_1, {cond}, kd_2\n")
    result.write(f"kd_2, {cond}, kd_3\n")
    active_loc = "kd_3"

    operations("hall_5")

#Memory manipulations 
def swap():
    global cond, active_loc
    
    result.write(f"{active_loc}, {cond}, oat_stage[1]\n")
    cond += 1

    result.write(f"oat_stage, {cond}, mt_3_1\n")
    result.write(f"mt_3_1, {cond}, rm_3\n")
    result.write(f"rm_3, {cond}, mt_3_2\n")
    result.write(f"mt_3_2, {cond}, mt_1_3\n")
    result.write(f"mt_1_3, {cond}, hall_13_3\n")
    result.write(f"hall_13_3, {cond}, kd_3\n")
    result.write(f"kd_3, {cond}, mt_2_3\n")
    result.write(f"mt_2_3, {cond}, oat_stage[1]\n")
    cond += 1

    result.write(f"oat_stage, {cond}, rm_2\n")
    result.write(f"rm_2, {cond}, pronite_2\n")
    result.write(f"pronite_2, {cond}, kd_2\n")

    active_loc = "kd_2"

def cyc():
    global cond, active_loc
    
    result.write(f"{active_loc}, {cond}, oat_stage[1]\n")
    cond += 1

    result.write(f"oat_stage, {cond}, rm_3\n")
    result.write(f"rm_3, {cond}, oat_stage[1]\n")
    cond += 1

    result.write(f"oat_stage, {cond}, events_1\n")
    result.write(f"events_1_f, {cond}, mt_3_1\n")
    result.write(f"mt_3_1, {cond}, rm_3\n")
    result.write(f"rm_3, {cond}, mt_3_2\n")
    result.write(f"mt_3_2, {cond}, mt_1_3\n")
    result.write(f"mt_1_3, {cond}, hall_13_3\n")
    result.write(f"hall_13_3, {cond}, kd_3\n")
    result.write(f"kd_3, {cond}, mt_2_3\n")
    result.write(f"mt_2_3, {cond}, kd_1\n")
    result.write(f"kd_1, {cond}, kd_2\n")
    result.write(f"kd_2, {cond}, events_1\n")
    result.write(f"events_1_t, {cond}, oat_stage[1]\n")
    cond += 1

    result.write(f"oat_stage, {cond}, rm_1\n")
    result.write(f"rm_1, {cond}, rm_2\n")
    result.write(f"rm_2, {cond}, events_2\n")
    result.write(f"events_2_f, {cond}, rm_1\n")
    result.write(f"events_2_t, {cond}, kd_2\n")
    result.write(f"kd_2, {cond}, kd_1\n")
    result.write(f"kd_1, {cond}, hall_13_3\n")
    result.write(f"hall_13_3, {cond}, kd_3\n")

    active_loc = "kd_3"

def rcyc():
    global cond, active_loc
    result.write(f"{active_loc}, {cond}, oat_stage[1]\n")
    cond += 1
    
    result.write(f"oat_stage, {cond}, rm_3\n")
    result.write(f"rm_3, {cond}, oat_stage[1]\n")
    cond += 1
    
    result.write(f"oat_stage, {cond}, events_1\n")
    result.write(f"events_1_f, {cond}, kd_1\n")
    result.write(f"kd_1, {cond}, kd_2\n")
    result.write(f"kd_2, {cond}, events_1\n")
    result.write(f"events_1_t, {cond}, rm_1\n")
    result.write(f"rm_1, {cond}, rm_2\n")
    result.write(f"rm_2, {cond}, oat_stage[1]\n")
    cond += 1
    
    result.write(f"oat_stage, {cond}, events_2\n")
    result.write(f"events_2_f, {cond}, mt_3_1\n")
    result.write(f"mt_3_1, {cond}, rm_3\n")
    result.write(f"rm_3, {cond}, mt_3_2\n")
    result.write(f"mt_3_2, {cond}, mt_1_3\n")
    result.write(f"mt_1_3, {cond}, hall_13_3\n")
    result.write(f"hall_13_3, {cond}, kd_3\n")
    result.write(f"kd_3, {cond}, mt_2_3\n")
    result.write(f"mt_2_3, {cond}, rm_1\n")
    result.write(f"rm_1, {cond}, rm_2\n")
    result.write(f"rm_2, {cond}, events_2\n")
    result.write(f"events_2_t, {cond}, oat_stage[1]\n")
    cond += 1
    
    result.write(f"oat_stage, {cond}, kd_2\n")
    result.write(f"kd_2, {cond}, kd_1\n")
    result.write(f"kd_1, {cond}, hall_13_3\n")
    result.write(f"hall_13_3, {cond}, kd_3\n")
    
    active_loc = "kd_3"

def rev():
    global cond, active_loc
    result.write(f"{active_loc}, {cond}, oat_stage[1]\n")
    cond += 1

    result.write(f"oat_stage, {cond}, kd_2\n")
    result.write(f"kd_2, {cond}, kd_3\n")
    result.write(f"kd_3, {cond}, kd_1\n")
    result.write(f"kd_1, {cond}, events_1\n")
    result.write(f"events_1_f, {cond}, kd_2\n")
    result.write(f"events_1_t, {cond}, rm_2\n")
    result.write(f"rm_2, {cond}, rm_3\n")
    result.write(f"rm_3, {cond}, events_2\n")
    result.write(f"events_2_t, {cond}, oat_stage[1]\n")
    cond += 1

    result.write(f"oat_stage, {cond}, rm_1\n")
    result.write(f"rm_1, {cond}, oat_stage[1]\n")
    cond += 1

    result.write(f"oat_stage, {cond}, rm_1\n")
    result.write(f"rm_1, {cond}, rm_3\n")
    result.write(f"rm_3, {cond}, events_1\n")
    result.write(f"events_1_f, {cond}, rm_1\n")
    result.write(f"events_1_t, {cond}, oat_stage[1]\n")
    cond += 1

    result.write(f"oat_stage, {cond}, kd_1\n")
    result.write(f"kd_1, {cond}, mt_3_2\n")
    result.write(f"mt_3_2, {cond}, rm_2\n")
    result.write(f"rm_2, {cond}, oat_stage[1]\n")
    cond += 1

    result.write(f"oat_stage, {cond}, rm_3\n")
    result.write(f"rm_3, {cond}, mt_3_1\n")
    result.write(f"mt_3_1, {cond}, mt_2_3\n")
    result.write(f"mt_2_3, {cond}, kd_3\n")
    result.write(f"kd_3, {cond}, kd_1\n")
    result.write(f"kd_1, {cond}, rm_2\n")
    result.write(f"rm_2, {cond}, events_2\n")
    result.write(f"events_2_f, {cond}, rm_3\n")
    result.write(f"events_2_t, {cond}, oat_stage[1]\n")
    cond += 1

    result.write(f"oat_stage, {cond}, kd_2\n")
    result.write(f"kd_2, {cond}, events_2\n")
    result.write(f"events_2_f, {cond}, oat_stage\n")
    result.write(f"events_2_t, {cond}, oat_stage[1]\n")
    cond += 1

    result.write(f"oat_stage, {cond}, rm_1\n")
    result.write(f"rm_1, {cond}, rm_2\n")
    result.write(f"rm_2, {cond}, rm_3\n")
    result.write(f"rm_3, {cond}, mt_3_2\n")
    result.write(f"mt_3_2, {cond}, mt_1_3\n")
    result.write(f"mt_1_3, {cond}, kd_3\n")
    result.write(f"kd_3, {cond}, events_2\n")
    result.write(f"events_2_f, {cond}, oat_stage\n")
    result.write(f"events_2_t, {cond}, oat_stage[1]\n")
    cond += 1

    result.write(f"oat_stage, {cond}, hall_13_3\n")
    result.write(f"hall_13_3, {cond}, events_2\n")
    result.write(f"events_2_f, {cond}, hall_13_2\n")
    result.write(f"hall_13_2, {cond}, kd_2\n")
    result.write(f"kd_2, {cond}, kd_3\n")
    result.write(f"kd_3, {cond}, events_2\n")
    result.write(f"events_2_t, {cond}, oat_stage[1]\n")
    cond += 1

    result.write(f"oat_stage, {cond}, pronite_1\n")
    result.write(f"pronite_1, {cond}, kd_1\n")
    result.write(f"kd_1, {cond}, kd_2\n")
    result.write(f"kd_2, {cond}, oat_stage[1]\n")
    cond += 1

    result.write(f"oat_stage, {cond}, kd_1\n")

    active_loc = "kd_1"

def dup():
    global cond, active_loc
    
    result.write(f"{active_loc}, {cond}, oat_stage[1]\n")
    cond += 1
    
    result.write(f"oat_stage, {cond}, mt_3_2\n")
    result.write(f"mt_3_2, {cond}, rm_1\n")
    result.write(f"rm_1, {cond}, rm_2\n")
    result.write(f"rm_2, {cond}, rm_3\n")
    result.write(f"rm_3, {cond}, oat_stage[1]\n")
    cond += 1
    
    result.write(f"oat_stage, {cond}, rm_2\n")
    result.write(f"rm_2, {cond}, pronite_2\n")
    result.write(f"pronite_2, {cond}, kd_2\n")
    
    active_loc = "kd_2"

#Looping functions
def loop_start():
    global cond, active_loc
    
    result.write(f"{active_loc}, {cond}, oat_stage[1]\n")
    cond += 1
    loop_history.append(cond)

    result.write(f"oat_stage, {cond}, rm_1\n")
    result.write(f"rm_1, {cond}, rm_2\n")
    result.write(f"rm_2, {cond}, oat_stage[1]\n")
    cond += 1

    result.write(f"oat_stage, {cond}, rm_2\n")
    result.write(f"rm_2, {cond}, hall_13_2\n")
    result.write(f"hall_13_2, {cond}, lecture_hall_eq\n")
    result.write(f"lecture_hall_eq_f, {cond}, kd_1\n")
    result.write(f"kd_1, {cond}, kd_2\n")
    result.write(f"kd_2, {cond}, oat_stage[1]\n")
    cond += 1

    result.write(f"oat_stage, {cond}, kd_2\n")
    active_loc = "kd_2"

def loop_end():
    global cond, active_loc
    a = loop_history[len(loop_history) - 1] - cond
    loop_history.pop()
    
    result.write(f"{active_loc}, {cond}, oat_stage[{a}]\n")
    cond += a
    
    cond += 1
    result.write(f"lecture_hall_eq_t" + ", {cond}, " + "oat_stage[" + str(-a + 1) + "]\n")
    
    cond -= (a - 1)
    active_loc = "oat_stage"

#String IO
def asciiin():
    global cond, active_loc
    result.write(f"{active_loc}, {cond}, oat_stage[1]\n")
    cond += 1
    
    result.write(f"oat_stage, {cond}, airstrip_land_2\n")
    result.write(f"airstrip_land_2, {cond}, rm_2\n")
    result.write(f"rm_2, {cond}, rm_3\n")
    result.write(f"rm_3, {cond}, events_2\n")
    result.write(f"events_2_f, {cond}, rm_2\n")
    result.write(f"events_2_t, {cond}, kd_2\n")
    result.write(f"kd_2, {cond}, kd_3\n")
    result.write(f"kd_3, {cond}, mt_2_3\n")
    result.write(f"mt_2_3, {cond}, hall_13_3\n")
    result.write(f"hall_13_3, {cond}, oat_stage[1]\n")
    cond += 1
    
    result.write(f"oat_stage, {cond}, rm_1\n")
    cond += 1
    
    result.write(f"oat_stage, {cond}, rm_1\n")
    result.write(f"rm_1, {cond}, rm_3\n")
    result.write(f"rm_3, {cond}, events_1\n")
    result.write(f"events_1_f, {cond}, rm_1\n")
    result.write(f"events_1_t, {cond}, oat_stage[1]\n")
    cond += 1
    
    result.write(f"oat_stage, {cond}, airstrip_land_2\n")
    result.write(f"airstrip_land_2, {cond}, rm_2\n")
    result.write(f"rm_2, {cond}, rm_3\n")
    result.write(f"rm_3, {cond}, events_2\n")

    result.write(f"events_2_f, {cond}, rm_2\n")
    result.write(f"events_2_t, {cond}, kd_2\n")
    result.write(f"kd_2, {cond}, kd_3\n")
    result.write(f"kd_3, {cond}, mt_2_3\n")
    result.write(f"mt_2_3, {cond}, hall_13_3\n")
    result.write(f"hall_13_3, {cond}, oat_stage[1]\n")
    cond += 1

    result.write(f"oat_stage, {cond}, rm_1\n")
    cond += 1

    result.write(f"oat_stage, {cond}, rm_1\n")
    result.write(f"rm_1, {cond}, rm_3\n")
    result.write(f"rm_3, {cond}, events_1\n")

    result.write(f"events_1_f, {cond}, rm_1\n")
    result.write(f"events_1_t, {cond}, oat_stage[1]\n")
    cond += 1

    result.write(f"oat_stage, {cond}, kd_1\n")
    result.write(f"kd_1, {cond}, mt_3_2\n")
    result.write(f"mt_3_2, {cond}, rm_2\n")
    result.write(f"rm_2, {cond}, oat_stage[1]\n")
    cond += 1

    result.write(f"oat_stage, {cond}, rm_3\n")
    result.write(f"rm_3, {cond}, mt_3_1\n")
    result.write(f"mt_3_1, {cond}, mt_2_3\n")
    result.write(f"mt_2_3, {cond}, kd_3\n")
    result.write(f"kd_3, {cond}, kd_1\n")
    result.write(f"kd_1, {cond}, rm_2\n")

    result.write(f"rm_2, {cond}, events_2\n")
    result.write(f"events_2_f, {cond}, rm_3\n")
    result.write(f"events_2_t, {cond}, oat_stage[1]\n")
    cond += 1

    result.write(f"oat_stage, {cond}, kd_2\n")
    result.write(f"kd_2, {cond}, events_2\n")
    result.write(f"events_2_f, {cond}, kd_2\n")
    result.write(f"events_2_t, {cond}, oat_stage[1]\n")
    cond += 1

    result.write(f"oat_stage, {cond}, rm_1\n")
    result.write(f"rm_1, {cond}, rm_2\n")

    result.write(f"rm_2, {cond}, rm_3\n")
    result.write(f"rm_3, {cond}, mt_3_2\n")
    result.write(f"mt_3_2, {cond}, mt_1_3\n")
    result.write(f"mt_1_3, {cond}, kd_3\n")
    result.write(f"kd_3, {cond}, events_2\n")
    result.write(f"events_2_f, {cond}, rm_1\n")
    result.write(f"events_2_t, {cond}, oat_stage[1]\n")
    cond += 1
    result.write(f"oat_stage, {cond}, hall_13_3\n")
    result.write(f"hall_13_3, {cond}, events_2\n")
    result.write(f"events_2_f, {cond}, hall_13_2\n")
    result.write(f"hall_13_2, {cond}, kd_2\n")
    result.write(f"kd_2, {cond}, kd_3\n")
    result.write(f"kd_3, {cond}, events_2\n")
    result.write(f"events_2_t, {cond}, oat_stage[1]\n")
    cond += 1
    result.write(f"oat_stage, {cond}, pronite_2\n")
    result.write(f"pronite_2, {cond}, kd_1\n")
    result.write(f"kd_1, {cond}, kd_2\n")
    result.write(f"kd_2, {cond}, oat_stage[1]\n")
    cond += 1
    result.write(f"oat_stage, {cond}, kd_1\n")
    active_loc = "kd_1"

def asciiout():
    global cond, active_loc
    
    result.write(f"{active_loc}, {cond}, oat_stage[1]\n")
    cond += 1

    result.write(f"oat_stage, {cond}, nankari_gate_out_2\n")
    
    active_loc = "nankari_gate_out_2"

#Debug function for printing the complete stack
def debug():
    global cond, active_loc
    
    result.write(f"{active_loc}, {cond}, oat_stage[1]\n")
    cond += 1
    
    result.write(f"oat_stage, {cond}, kd_1\n")
    result.write(f"kd_1, {cond}, kd_2\n")
    result.write(f"kd_2, {cond}, events_1\n")
    result.write(f"events_1_f, {cond}, kd_1\n")
    result.write(f"events_1_t, {cond}, events_2\n")
    result.write(f"events_2_f, {cond}, iit_gate_out_2\n")
    result.write(f"iit_gate_out_2, {cond}, rm_2\n")
    result.write(f"rm_2, {cond}, rm_1\n")
    result.write(f"rm_1, {cond}, events_2\n")
    result.write(f"events_2_t, {cond}, oat_stage[1]\n")
    cond += 1
    
    result.write(f"oat_stage, {cond}, kd_2\n")
    result.write(f"kd_2, {cond}, kd_1\n")
    
    active_loc = "kd_1"

#Auxiliary function to check if a string is a number
#Required for pushing numbers to the stack
def is_num(s):
    global cond, active_loc
    for char in s:
        if not char.isdigit():
            return False
    return True

result = open("output.iitkv", "w")
active_loc = "start"
path = "path.txt"

with open(path, "r") as infile:
    tokens = infile.read().split()

init()

for a in tokens:
    if a == "input":
        prep_insert()
        get_input(2)
    elif a == "output":
        pr_output(2)
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
    elif a == "rcycle":
        rcyc()
    elif a == "rev":
        rev()
    elif a == "dup":
        dup()
    elif a == "if":
        loop_start()
    elif a == "fi":
        loop_end()
    elif a == "inputascii":
        prep_insert()
        result.write(f"{active_loc}, {cond}, hall_13_3\n")
        active_loc = "hall_13_3"
        asciiin()
    elif a == "outputascii":
        asciiout()
        popf()
    elif a == "debug":
        debug()
    elif a == "quit":
        end_graph()
    elif is_num(a):
        n = int(a)
        push(n)
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
