import pandas as pd

# Шаг 1: Загрузка данных из CSV файла
file_path = r"C:\Users\IMOE001\Documents\GitHub\Pandasmy\csvfile\World-happiness-report-2024.csv"  # Путь к вашему CSV файлу
df = pd.read_csv(file_path)

# Шаг 2: Вывод первых 5 строк данных
print("Первые 5 строк данных:")
print(df.head())

# Шаг 3: Вывод информации о данных
print("\nИнформация о данных:")
print(df.info())

# Шаг 4: Вывод статистического описания данных
print("\nСтатистическое описание данных:")
print(df.describe())


