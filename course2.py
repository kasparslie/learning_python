# text = "X-DSPAM-Confidence:    0.8475"

# str = text.find(":")
# print(str)

# extc = text[str+1:]
# print(extc)

# num = float(extc)
# print(num)

# # Use words.txt as the file name
# fname = input("Enter file name: ")
# fhandle = open(fname)
# for line in fhandle:
#     line = line.upper().rstrip()
#     print(line)

# # Use the file name mbox-short.txt as the file name
# fname = input("Enter file name: ")
# fh = open(fname)
# count = 0
# average = 0
# for line in fh:
#     if not line.startswith("X-DSPAM-Confidence:") : continue
#     average += float(line[20:-1].strip())
#     count = count + 1
#     print(line)
    
# print("Average spam confidence:", (average/count))

# fname = input("Enter file name: ")
# fh = open(fname)
# lst = list()
# for line in fh:
#     txt = line.rstrip().split()
#     # print(txt)
#     for wrd in txt:
#         # print(wrd)
#         if wrd in lst:
#           continue
#         else:
#             lst.append(wrd)
# lst.sort()
# print(lst)

# fname = input("Enter file name: ")
# fname = "mbox-short.txt"
# icount = 0
# fh = open(fname)

# for line in fh:
#     line = line.rstrip()
#     if not line.startswith('From '):
#         continue
#     words = line.split()
#     print(words[1])
#     icount +=1




# print("There were", icount, "lines in the file with From as the first word")

# stuff = dict()
# print(stuff['candy'])

# stuff = dict()
# print(stuff.get('candy',-1))


# Python Dictionaries and Files

name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)
senders = dict()
newList = list()
for line in handle:
    if not line.startswith('From '):continue
    line = line.split()
    newList.append(line[1])
print(newList)

for email in newList:
    senders[email] = senders.get(email,0) +1
# print(senders)

statWord = None
statCount= None
for word,count in senders.items():
    if statCount is None or count > statCount:
        statCount = count
        statWord  = word

print(statWord, statCount)