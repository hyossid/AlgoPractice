



def solution(triangle):
    dp=[0]*500
    index=0
    for i,sublst in enumerate(triangle):
        if i==0:
            dp[0]=sublst[0]
            index += 1
            continue
        for j, value in enumerate(sublst):
            if j==0:    #  레벨에서 첫값은 항상 바로 위에있는놈이고, 차이는
                dp[index]=dp[index-len(sublst)+1]+value
            elif j==len(sublst)-1:
                dp[index]=dp[index-len(sublst)]+value
            else:
                dp[index]=max(dp[index-len(sublst)+1],dp[index-len(sublst)])+value
            index+=1

    b=len(triangle[-1])
    for i in


if __name__ == '__main__':
