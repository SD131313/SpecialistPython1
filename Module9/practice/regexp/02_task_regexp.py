# Дан текст в котором упоминаются IP-адреса.
# Пример текста:
text = 'Все публичные сервера и сайты в сети Интернет используют "белые" IP-адреса (например, сайт google.com — 172.217.22.14,
DNS-сервер Google — 8.8.8.8, сайт yandex.ru — 213.180.204.11, DNS-сервер Яндекс.DNS — 77.88.8.8). 
Все публичные IP-адреса в сети Интернет уникальны и не могут повторяться'
result1 = re.findall(r'\d+[.]\d+[.]\d+[.]\d+', test)
print(result1)
# Найдите все упоминаемые IP.
# Точно известно, что все IP-адреса в тексте являются корректными, т.е. не будут встречаться адреса вида 900.400.18.56

