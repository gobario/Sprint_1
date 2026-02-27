line = '1h 45m,360s,25m,30m 120s,2h 60s'
line = line.replace(' ', ',').split(',')#разделил строку на список
result = 0 #здесь будет храниться результат
temporarily_result = 0 #временная переменная для подсчёта часов и секунд в минутах
for i in range(len(line)):
    if 'h' in line[i]:
        line[i] = line[i].replace('h', '')
        temporarily_result = int(line[i]) * 60
        result += temporarily_result
    if 'm' in line[i]:
        line[i] = line[i].replace('m', '')
        result += int(line[i])
    if 's' in line[i]:
        line[i] = line[i].replace('s', '')
        temporarily_result = int(line[i]) / 60
        result += temporarily_result

print(f'Всего минут в строке: {int(result)}.')