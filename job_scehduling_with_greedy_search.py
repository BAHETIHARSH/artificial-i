# Name :Baheti Harsh Balaprasad
# TECOA112

jobs = [[1, 2, 60], [2, 1, 100], [3, 3, 20], [4, 2, 40], [5, 1, 60],[6,2,220]]

def scheduling(jobarr, t):
    n = len(jobarr)
    for i in range(n):
        for j in range(n - 1 - i):
            if jobarr[j][2] < jobarr[j + 1][2]:
                jobarr[j], jobarr[j + 1] = jobarr[j + 1], jobarr[j]

    resultList = [False]*t
    resultJobs = [-1]*t
    profit = 0
    for i in range(n):
        for j in range(min(t-1,jobarr[i][1]-1),-1,-1):
            if resultList[j] is False:
                resultList[j]=True
                resultJobs[j]=jobarr[i][0]
                profit+=jobarr[i][2]
                break

    print("The jobs scheduling sequence is {} maximum profit is {}".format(resultJobs,profit))

scheduling(jobs,3)