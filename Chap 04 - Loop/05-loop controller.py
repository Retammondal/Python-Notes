## BREAK 
# Ultimate kill switch...immediately destroys the loop, skips all remianing cycles

## CONTINUE
# It's like skip the current loop not entire; stops the current cycle
# And skips any code below it......


for i in range(1,10):
  if i == 5:
    break               # It will break the loop here, and skip below parts also..
  print(i)

print()

for i in range(1,10):
  if i == 5:
    continue            # IT will not close the loop just skip this loop cycle
  print(i)              # skip the below parts also ...

print()

for i in range(1,10):
  print(i)              # IT will print all b/c continue only skips below portions..
  if i == 5:
    continue  # IT will not close the loop just skip this loop cycle
