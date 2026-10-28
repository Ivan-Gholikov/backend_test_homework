# Начинаю писать данные пользователя
user_name = input("Добрый день, как Вас зовут?")
user_age = int(input("Сколько Вам лет?"))
# Следующим запрашиваю вес и рост
user_weight = float(input("Какой у Вас вес в кг?"))
user_height_cm = float(input("Какой у вас рост в см?"))
# Перевод в метры
user_height_m = user_height_cm / 100 

bmi = user_weight / (user_height_m ** 2) # расчет  индекса массы тела
#Создаю переменную которая будет считать до одного знака после запятой
bmi_rounded = round(bmi, 1)
# Рассчет нормы воды в миллилитрах
water_ml = user_weight * 30 
water_l = water_ml / 1000 # Перевод в литры

print("Отчет для пользователя:", user_name , (user_age))
print("Твой Индекс Массы Тела:", bmi_rounded)
print("Рекомендуемая норма воды:", water_l , "л. в день")
print("Расчет окончен. Будьте здоровы!")