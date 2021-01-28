


def solution(bridge_length, weight, truck_weights):
    answer = 0
    # Initialize variables
    timer=[]
    bridge=[]
    curweight=weight
    # 1st car entering the bridge
    car=truck_weights.pop(0)
    bridge.append(car)
    curweight-=car
    timer.append(1)
    answer+=1
    # As There is a car at the bridge
    while bridge:
        # If the Car reached the end of bridge
        if timer[0]==bridge_length:
            timer.pop(0)
            curweight+=bridge.pop(0)

        # If bridge is not full, load
        if len(truck_weights)!=0:
            if truck_weights[0]<=curweight:
                car2=truck_weights.pop(0)
                curweight-=car2
                bridge.append(car2)
                timer.append(0)

        timer=[n+1 for n in timer]
        answer+=1



    return answer




if __name__ == '__main__':
    bridge_length=100
    weight=100
    truck_weights=[10,10,10,10,10,10,10,10,10,10]
    print(solution(bridge_length,weight,truck_weights))