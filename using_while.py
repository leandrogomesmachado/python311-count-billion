import time

start_time = time.time()

count = 1
while count <= 1000000000:
    count += 1

end_time = time.time()
elapsed_time = end_time - start_time

print("Contagem concluída.")
print("Tempo decorrido usando Loop While: ", elapsed_time, "segundos.")