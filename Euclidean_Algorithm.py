print("\nGCD or HCF of 2 numbers using EUCLID'S ALGORITHM\n")
try:
  A = a = int(input("value of A:"))
  B = b = int(input("value of B:"))
except:
  print("\nEnter a valid integer")
  exit()
c = 1
if a < b:
  a, b = b, a
print("\nEUCLID'S ALGORITHM STEPS\n")
while 1:
  if b == 0:
    print("\nGCD/HCF of", A, "and", B, "=", a)
    print("LCM", A * B / a)
    break
  print("Step", c, ":", a, "=", b, "*", a // b, "+", a % b)
  t = b
  b = a % b
  a = t
  c += 1
exit()
