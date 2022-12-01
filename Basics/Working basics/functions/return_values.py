def sum_weights(beep_weight, bop_weight):
    total_weight = beep_weight + bop_weight
    return total_weight


def calc_avg_weight(beep_weight, bop_weight):
    avg_weight = sum_weights (beep_weight, bop_weight) / 2
    return avg_weight

def run():
    print("what is the weight of beep")
    beep_weight = int(input())
    print("what is the weight of bop")
    bop_weight = int(input())
    print("what shall i calculate sum or average")
    action = input()
    if action == "sum":
        answer = sum_weights(beep_weight, bop_weight)
        print(f"the sum of beep and bops weight is {answer}")
    elif action == "average":
        answer = calc_avg_weight(beep_weight, bop_weight)
        print(f"Beep and Bops average weight is {answer}")
    else:
        print("im not sure what you want me to do")
run()