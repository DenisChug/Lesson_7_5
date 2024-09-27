import os, time
def file_info(directory):

    for root, dirs, files in os.walk(directory):
        for file in files:
            os.chdir(root)
            filepath = os.path.join(directory)
            filetime = os.path.getmtime(file)
            formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(filetime))
            file_size = os.path.getsize(file)
            parent_dir = os.path.dirname(root)
            print(
                f'Обнаружен файл: {file}, Путь: {filepath}, Размер: {file_size} байт, Время изменения: '
                f'{formatted_time}, Родительская директория: {parent_dir}')




file_info(r'C:\Users\DXCom\Lesson\Lesson_7_5\Lesson_7_5')