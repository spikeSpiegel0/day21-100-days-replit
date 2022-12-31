print("Math Game!")
print()
print()
multi = int(input("Name your multiples: "))
print()
count = 0
for i in range(1,11):
  print(i, "x", multi, "=")
  answer = int(input())
  if answer == i * multi:
    print("Nice!")
    print()
    count += 1
  else:
    print("Nope! Correct answer is", i * multi)
    print()
print()
print("...")
print()
print("You scored", count, "out of 10")
if count == 10:
  print("Mkaay, ser gut! You got 10 out of 10")