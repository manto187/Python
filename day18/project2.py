import time 

input("press enter to start stopwatch...")
start = time.time()

input("press enter to stop stopwatch...")
end = time.time()

elapsed = end-start
print("time elapsed: ", round(elapsed, 2), "seconds")