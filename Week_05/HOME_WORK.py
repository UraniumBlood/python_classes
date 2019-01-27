#NO. 1
# n = int(input("Enter no."))
# if n == 0:
#     print("It is equal to 0")
#
# elif n > 0:
#     print("It is a positive no.")
#
# else:
#     print("It is a negative no.")

# NO. 2
# n = int(input("Enter no."))
#
# if n%2 == 0:
#     print("Even")
#
# else:
#     print("odd")

#NO. 3

#2,3,5,7,11,13,17,19


y = int(input("enter"))
list_prime=[2,3,5,7,11,13,17,19]
count = 0g
bool = 0
while count<=7:
    n = int(list_prime[int(count)])
    print(n)
    if y % n == 0:
        bool = 1
    count = count + 1

if bool == 1:
    print("composite")
else:
    print("prime")



