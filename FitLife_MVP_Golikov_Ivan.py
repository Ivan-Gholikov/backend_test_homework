# Начинаю писать данные пользователя
user_name = input("Добрый день, как Вас зовут? ")
user_age = int(input("Сколько Вам лет? "))
user_weight = float(input("Какой у Вас вес в кг? "))  # Следующим запрашиваю вес и рост
user_height_cm = float(input("Какой у вас рост в см? "))
user_height_m = user_height_cm / 100  # Перевод в метры

bmi = user_weight / (user_height_m ** 2)  # Расчёт индекса массы тела
bmi_rounded = round(bmi, 1)  # Создаю переменную, которая будет считать до одного знака после запятой
water_ml = user_weight * 30  # Расчёт нормы воды в миллилитрах
water_l = water_ml / 1000  # Перевод в литры

print(f"Отчёт для пользователя: {user_name}, возраст: {user_age}")
print(f"Твой индекс массы тела: {bmi_rounded}")
print(f"Рекомендуемая норма воды: {water_l:.1f} л в день")
print("Расчёт окончен. Будьте здоровы!")