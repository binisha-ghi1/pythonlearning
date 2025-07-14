# Simple Stop Watch : Start and stop a timer.  

import time
print("Simple Stopwatch")
print("Press ENTER to start")
input()  # Wait for user to press Enter to start

start_time = time.time()  # Record start time
print("Timer started... Press ENTER to stop")
input()  # Wait for user to press Enter to stop

end_time = time.time()  # Record end time
elapsed_time = end_time - start_time  # Calculate time difference

print(f"Elapsed Time: {round(elapsed_time, 2)} seconds")

