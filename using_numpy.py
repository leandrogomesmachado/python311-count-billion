import numpy as np
import time

start_time = time.time()

count_array = np.arange(1, 1000000001)
count = np.size(count_array)

end_time = time.time()
elapsed_time = end_time - start_time

print("Contagem concluída.")
print("Tempo decorrido usando NumPy: ", elapsed_time, "segundos.")
