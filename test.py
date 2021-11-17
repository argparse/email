def foo(my_list):
    for i in my_list:
        if i%2 == 1:
            print(i)
        else:
            break
    else:
        print(float('inf'))

print(foo([3,1,1,2,8,4,1]))

