import os
import speedtest
import random
os.system('clear')
print('HO SpeedTest v1.1\nBy ArSiFoX')
test = speedtest.Speedtest()
print('Загрузка списка серверов...')
test.get_servers()
print('Выбор лучшего сервера...')
best = test.get_best_server()
print(f"Найден: {best['sponsor']}")
print('Идёт тестирование скорости...')
print('0%')
download_result = test.download()
print(str(random.randint(20,50))+'%')
upload_result = test.upload()
ping_result = test.results.ping
print('100%')
print('Сбор результатов...')
download = round(download_result/1024/1024/8, 2)
upload = round(upload_result/1024/1024/8, 2)
ping = round(ping_result, 2)
print('Скачивание: '+str(download)+' МБ/сек')
print('Загрузка: '+str(upload)+' МБ/сек')
print('Пинг: '+str(ping)+' мс')
