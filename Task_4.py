"""
В файле хранятся данные с сайта IMDB. Скопированные
данные хранятся в файле ./data5/ r.list.
Откройте и прочитайте файл(если его нет
необходимо вывести ошибку).
Найдите ТОП250 фильмов и извлеките заголовки.
Программа создает 3 файла  top250_movies.txt –
названия файлов, ratings.txt – гистограмма рейтингов,
years.txt – гистограмма годов.
"""
try:
    with open("r.list", encoding="ISO-8859-1") as file:
        full_text = [line.strip() for line in file]
        clear_text = full_text[28:278]  # Необходимые строки
        text = [line.split() for line in clear_text]

        for element in text:
            position = element[3:-1]
            full_name = ' '.join(position)
            with open('top250_movies.txt', 'a') as top_250:
                top_250.write(full_name + "\n")

        for element in text:
            position = element[-1].strip('()/I')
            with open('years.txt', 'a') as years:
                years.write(position + "\n")

        for element in text:
            position = element[2]
            with open('ratings.txt', 'a') as ratings:
                ratings.write(position + "\n")

except:
    print('Упс!')
