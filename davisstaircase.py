def stepPerms(n):
    if (n == 1 or n == 0):
        return 1
    elif (n ==2):
        return 2
    else:
        return stepPerms(n-3) + stepPerms(n-2) + stepPerms(n-1) 