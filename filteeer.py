#learning the filter functions
l1=[num for num in range(1,21)]
# l2=list(filter(lambda num:num%2==0,l1))
# print(l2)
import time
import subprocess
l2=filter(lambda num:num%2==0,l1)
for num in l1:
    print(num)
    time.sleep(1)
    subprocess.run(["clear"])
