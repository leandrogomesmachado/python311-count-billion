import time

start_time = time.time()

for i in range(1, 1000000001):
    pass

end_time = time.time()
elapsed_time = end_time - start_time

print("Contagem concluída.")
print("Tempo decorrido usando Loop For: ", elapsed_time, "segundos.")