import time
from threading import Thread


def write_words(word_count, file_name):
    with open(file_name, 'w', encoding='utf-8') as f:
        for i in range(1, word_count + 1):
            f.write(f'Какое-то слово № {i}\n')
            time.sleep(0.1)

    print(f'Завершилась запись в файл {file_name}')


# Последовательные вызовы функции
start_time = time.time()

for count, name in [(10, 'example1.txt'), (30, 'example2.txt'), (200, 'example3.txt'), (100, 'example4.txt')]:
    write_words(count, name)

end_time = time.time()
print(f'\nВремя последовательного выполнения: {end_time - start_time:.2f} секунд\n')

# Параллельные вызовы функции с использованием потоков
threads = []

for count, name in [(10, 'example5.txt'), (30, 'example6.txt'), (200, 'example7.txt'), (100, 'example8.txt')]:
    thread = Thread(target=write_words, args=(count, name))
    threads.append(thread)

start_time = time.time()

for t in threads:
    t.start()

for t in threads:
    t.join()

end_time = time.time()
print(f'\nВремя параллельного выполнения: {end_time - start_time:.2f} секунд\n')