'''
Given two library versions of an executable: for example, “10.1.1.3”
and “10.1.1.9” or “10” and “10.1”. Find out which one is more recent?
Strings can be empty also.
'''
def latestVersion(S1, S2):
    L1 = S1.split('.')
    L2 = S2.split('.')
    if len(L1) < len(L2):
        for _ in range(len(L2)-len(L1)):
            L1.append('0')
    else:
        for _ in range(len(L1)-len(L2)):
            L2.append('0')
    n = len(L1)
    flag = 0
    for i in range(n):
        if L1[i] > L2[i]:
            flag = 1
            break
        elif L2[i] > L1[i]:
            flag = 2
            break
    if flag == 0:
        print(S1+" version is same as "+S2)
    elif flag == 1:
        print(S1+" version is latest than "+S2)
    else:
        print(S2+" version is latest than "+S1)

latestVersion("10.1.1.3","10.1.1.9")
latestVersion("10","10.1")
latestVersion("","10")
latestVersion("10.1.1","10.1.1.1")
latestVersion("11.1.1.1","10.1.1.9")
latestVersion("10.1.1","10.1.1.0")

'''
// Output //
10.1.1.9 version is latest than 10.1.1.3
10.1 version is latest than 10
10 version is latest than 
10.1.1.1 version is latest than 10.1.1
11.1.1.1 version is latest than 10.1.1.9
10.1.1 version is same as 10.1.1.0
'''