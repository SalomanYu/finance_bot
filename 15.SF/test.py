a = """Подготовим к сдаче CFA – самого престижного и известного экзамена международного уровня в инвестиционной сфере.

Страница курса — {{URL}}

Программа курса
1. Количественные методы
Количественные методы. Часть 1 
Количественные методы. Часть 2

Длительность: 8 часов

2. Корпоративные финансы
Корпоративные финансы. Часть 1
Корпоративные финансы. Часть 2

Длительность: 8 часов

3. Акции
Акции. Часть 1
Акции. Часть 2

Длительность: 8 часов

4. Экономика
Экономика. Часть 1
Экономика. Часть 2

Длительность: 8 часов

Практика №1
Консультация № 1
Mock Exam №1

Длительность: 8 часов

5. Анализ финансовой отчетности
Анализ финансовой отчетности. Часть 1
Анализ финансовой отчетности. Часть 2

Длительность: 8 часов

6. Инструменты с фиксированной доходностью

Длительность: 4 часа

7. Альтернативные инвестиции

Длительность: 4 часа

8. Деривативы

Длительность: 4 часа

9. Управление портфелем

Управление портфелем

Длительность: 4 часа

10. Этические и профессиональные стандарты

Этические и профессиональные стандарты

Длительность: 4 часа

Практика:
Консультация № 2
Mock Exam № 2
Консультация № 3

Длительность: 9 часов
"""
import re

direction_pattern = 'Длительность: .*?\\n'
pattern = '\d{2}. .*?\\n|\d{1}. .*?\\n'

# new = re.sub('Длительность: .*?\\n', '', a).strip()

# res = re.split('\d{2}. .*?\\n|\d{1}. .*?\\n', a)
without_direction = re.sub(direction_pattern, '', a)
headers = re.findall(pattern, without_direction)
descriptions = re.split(pattern, without_direction)[1:]

data = []
for item in range(len(descriptions)):
    data.append({
        'name': headers[item].replace('\n', ''),
        'desc': descriptions[item].strip().replace('\n\n\n', ' | ').replace('\n', ' | ')
    })

print(data)