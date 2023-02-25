import psutil
import requests
import time
#Устанавливаем лимит
limit_memori = 200

while True:
    result = psutil.virtual_memory().used / 1024 / 1024
    print(f"Проверка на результат {result}")

    # Если потребление памяти превышает result то отправляем на Http
    if result > limit_memori:
        response = requests.post('http://api.github.com', data={'memory_usage': result})
        print(response.text)
    else:
        print(f"{result} < {limit_memori}")
    time.sleep(25)