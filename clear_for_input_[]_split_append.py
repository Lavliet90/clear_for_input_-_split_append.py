# Write a function modify_list (l) that takes a list of integers as input,
# removes all odd values from it, and divides even ones by two.
# The function should not return anything, it only needs to change the passed list


def modify_list(l):
    mod=[]
    for z in l:
        if z%2==0:
            mod.append(z//2)
    l.clear()
    l+=mod
    return



