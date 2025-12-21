
math_students = {"Анна", "Борис", "Виктор", "Дарья", "Елена"}
physics_students = {"Виктор", "Георгий", "Дарья", "Иван", "Ксения"}
cs_students = {"Анна", "Виктор", "Елена", "Иван", "Мария"}

third_year = math_students & physics_students & cs_students
print(f"Во всех трех множествах: {third_year}")

one_math = math_students - physics_students - cs_students
print(f"Посещали только математику: {one_math}")

two = (math_students & physics_students) | (math_students & cs_students) | (physics_students & cs_students)
print(f"Те кто есть только в двух множествах: {two}")

one_raz = math_students | physics_students | cs_students
print(f"Уникальные студенты: {one_raz}")

