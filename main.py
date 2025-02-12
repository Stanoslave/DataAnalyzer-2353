Так, звичайно. Ось приклад програми, яка виконує основну обробку даних - завантаження CSV-файлу, очищення даних, аналіз і виведення деяких статистик:

```python
# імпортуємо необхідні бібліотеки
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# завантажуємо дані з CSV-файлу
def load_data(file_name):
    data = pd.read_csv(file_name)
    return data

# очищуємо дані від пропущених значень
def clean_data(data):
    data = data.dropna()
    return data

# визначаємо середнє значення
def calc_mean(data, column_name):
    mean_val = data[column_name].mean()
    return mean_val

# визначаємо медіану
def calc_median(data, column_name):
    median_val = data[column_name].median()
    return median_val

# визначаємо моду
def calc_mode(data, column_name):
    mode_val = data[column_name].mode()[0]
    return mode_val

# виводимо основні статистики для кожного стовпця
def print_stats(data, columns):
    for column in columns:
        print(f"Column: {column}")
        print(f"Mean: {calc_mean(data, column)}")
        print(f"Median: {calc_median(data, column)}")
        print(f"Mode: {calc_mode(data, column)}")
        print("\n")

# виводимо графіки для кожного стовпця
def plot_data(data, columns):
    for column in columns:
        plt.figure(figsize=(10,5))
        sns.histplot(data[column], bins=30, kde=True)
        plt.title(f'Distribution of {column}')
        plt.show()

# основна програма
def main():
    # завантажуємо дані
    data = load_data('data.csv')

    # очищуємо дані
    data = clean_data(data)

    # виводимо статистику
    columns = ['Column1', 'Column2', 'Column3']  # замініть на імена ваших стовпців
    print_stats(data, columns)

    # побудова графіків
    plot_data(data, columns)

if __name__ == "__main__":
    main()
```

Цей код зчитує CSV-файл, обробляє пропущені значення, обчислює та виводить основні статистичні показники (середнє, медіана, мода) для кожного стовпця і показує гістограму розподілу для кожного стовпця. Будь ласка, замініть `'data.csv'` та `['Column1', 'Column2', 'Column3']` своїми значеннями.