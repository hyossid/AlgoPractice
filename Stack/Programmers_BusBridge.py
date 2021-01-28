import collections

class Bus:
    def __init__(self,weight,time):
        self.weight=weight
        self.time=time

def solution(bridge_length,weight,truck_weights):

    # I will regard truck_weights as a queue
    sum=0
    realtime=0
    queue=truck_weights[:]
    Bridge=[]
    while len(queue)!=0 or len(Bridge)!=0:
        realtime+=1
        # Load Bus to the bridge
        if sum<weight and len(queue)!=0:
            if sum+queue[0]<weight:
                cur=queue.pop(0)
                sum+=cur
                bus=Bus(cur,0)
                Bridge.append(bus)

        # Counter
        if len(Bridge)!=0:
            for i in range(len(Bridge)):
                Bridge[i].time+=1
                if Bridge[i].time==bridge_length:
                    sum=sum-Bridge[i].weight
                    Bridge.remove(Bridge[i])
                    

    return realtime

if __name__ == '__main__':
    bridge_length=2
    weight=10
    truck_weights=[7,4,5,6]
    print(solution(bridge_length,weight,truck_weights))