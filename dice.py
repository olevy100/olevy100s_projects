a = int(input("how many sides would you like to have on your dice"))
print (f'your die has {a} sides.')
print("rolling die...")
import time
time.sleep(2)

import numpy as np
print(f"you rolled {np.random.choice(range(1,a))}.")