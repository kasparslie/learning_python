text = "X-DSPAM-Confidence:    0.8475"

str = text.find(":")
print(str)

extc = text[str+1:]
print(extc)

num = float(extc)
print(num)