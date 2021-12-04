print("Hello world!")
nam = input("Who are you?")
print("Welcome", nam)

hrs = input("Enter Hours:")
rte = input("Enter Rate:")
h = float(hrs)
r = float(rte)
if h <= 40:
    print(h * r)
elif h > 40:
    print((40 * r) + ((h-40)* (r * 1.5)))

score = input("Enter Score: ")
x = float(score)
if x >=0.9:
    print("A")
elif x >= 0.8:
    print("B")
elif x >= 0.7:
    print("C")
elif x >= 0.6:
    print("D")
elif x < 0.6:
    print("F")
else:
    print("you are fucked")


def computepay(h, r):
    
    a=0
 
    if float(h) > 40:
        a = (40 * r) + ((h-40)* (r * 1.5))
    elif float(h) == 40:
        a = (h * r)

    return a

hrs = input("Enter Hours:")
rte = input("Enter Rate")
p = computepay(float(hrs), float(rte))
print("Pay", p)

zork = 0
for thing in [9, 41, 12, 3, 74, 15] :
    zork = zork + thing
print('After', zork)

smallest_so_far = -1
for the_num in [9, 41, 12, 3, 74, 15] :
   if the_num < smallest_so_far :
      smallest_so_far = the_num
print(smallest_so_far)


largest = None
smallest = None
while True:
    inp = input("Enter a number: ")
    if inp == "done":
        break
    # print(inp)
    try:
        num=int(inp)
       
        if largest is None:
            largest=num
        elif largest<num:
            largest=num
        if smallest is None:
            smallest=num
        elif smallest>num:
            smallest=num
    except:
        print("Invalid input, please try again")
        continue


print("Maximum is", largest)
print("Minimum is", smallest)

