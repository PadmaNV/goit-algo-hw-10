import pulp

"""Компанія виробляє продукти А і Б. 
Для виробництва одиниці 

продукту А потрібно 5 годин на машині №1 та 3 години на машині №2. 

Для продукту Б — 2 години на машині №1 та 2 години на машині №2. 

Максимально доступний час роботи машини №1 — 80 
годин, а машини №2 — 40 годин. Прибуток від продажу одиниці продукту А становить $50,
а від продукту Б — $40.



Умови завдання:

"Лимонад" виготовляється з "Води", "Цукру" та "Лимонного соку".
"Фруктовий сік" виготовляється з "Фруктового пюре" та "Води".

Обмеження ресурсів: 100 од. "Води", 50 од. "Цукру", 30 од. "Лимонного соку" та 40 од. "Фруктового пюре".

Виробництво одиниці "Лимонаду" вимагає 2 од. "Води", 1 од. "Цукру" та 1 од. "Лимонного соку".
Виробництво одиниці "Фруктового соку" вимагає 2 од. "Фруктового пюре" та 1 од. "Води".
"""

# Ініціалізація моделі
model = pulp.LpProblem("Maximize Profit", pulp.LpMaximize)

# Визначення змінних
A = pulp.LpVariable('Limonad', lowBound=0, cat='Integer')  # Кількість продукту А
B = pulp.LpVariable('Juice', lowBound=0,  cat='Integer')  # Кількість продукту Б

# Функція цілі (Максимізація прибутку)
model += A + B, "Quality"

# Додавання обмежень
model += 2 * A + B <= 100  # Обмеження Вода
model += A <= 50  # Обмеження Цукор
model += A <= 30  # Обмеження Цукор
model += 2 * B <= 30  # Обмеження Цукор


# Розв'язання моделі
model.solve()

# Вивід результатів
print("Оптимальне виробництво Лимонаду в кількості:", A.varValue)
print("             та Фруктового соку в кількості:", B.varValue)