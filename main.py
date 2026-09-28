import math

def calculate_room_area(coords):
    """Вычисляет точную площадь любого многоугольника по координатам углов (Формула Гаусса)"""
    n = len(coords)
    area = 0.0
    for i in range(n):
        j = (i + 1) % n
        area += coords[i][0] * coords[j][1]
        area -= coords[j][0] * coords[i][1]
    return abs(area) / 2.0

def main():
    print("--- УМНЫЙ КАЛЬКУЛЯТОР ПЛИТКИ ДЛЯ СЛОЖНЫХ СТЕН ---")
    print("Инструкция: встаньте в любой угол и идите по часовой стрелке вдоль стен.")

    # 1. Стартовые настройки
    coordinates = [[0.0, 0.0]]
    current_x = 0.0
    current_y = 0.0

    try:
        first_wall = float(input("\n[Шаг 1] Измерьте ПЕРВУЮ стену от угла (в метрах): "))
    except ValueError:
        print("Ошибка! Введите число")
        return

    current_y += first_wall
    coordinates.append([current_x, current_y])

    current_direction = 0

    print("\nОтлично! Теперь вы стоите на первом углу.")
    print("Идите дальше по кругу. На каждом углу говорите, куда повернули.")
    print("Когда вернетесь к самому первому углу, введите слово 'СТОП'.")

    # Направления для шагов:
    # После первойстены мы гарантированно идем ВПРАВО
    # Будем чередовать движение по горизонтали (X) и вертикали (Y)
    is_horizontal = True
    sign_x = 1
    sign_y = -1

    step = 2
    while True:
        turn = input(f"\n[Шаг {step}] Куда поворачивает стена? (1 - направо / 2 - налево) или СТОП: ").strip().lower()

        if turn == "stop" or turn == "стоп":
            break

        if turn not in ["1", "2"]:
            print("Ошибка! Напишите слово '1', '2' или 'стоп'")
            continue

        try:
            lenght = float(input("Длина этой стены в метрах: "))
        except ValueError:
            print("Ошибка! Введите число (например, 2.5 или 1)")
            continue

        if is_horizontal:
            current_x += lenght * sign_x
            if turn == "1":
                sign_y = -sign_y if sign_x == 1 else sign_y
            else:
                sign_y = -sign_y if sign_x == 1 else -sign_y
            is_horizontal = False
        else:
            current_y += lenght * sign_y
            if turn == "1":
                sign_x = sign_x if sign_y == 1 else sign_x
            else:
                sign_x = -sign_x if sign_y == 1 else sign_x
            is_horizontal = True

        coordinates.append([current_x, current_y])
        step += 1

    # 2. Вычисление площадей
    room_area = calculate_room_area(coordinates)
    print(f"\n Точная площадь комнаты: {room_area:.2f} кв.м.")

    # 3. Ввод параметров плитки (в сантиметрах)
    print("\n--- РАЗМЕР ПЛИТКИ ---")
    tile_width = float(input("Введите ШИРИНУ плитки (в см): ")) / 100.0 # переводим в метры
    tile_height = float(input("Введите ДЛИНУ плитки (в см): ")) /100.0 # переводим в метры

    tile_area = tile_width * tile_height

    # 4. Финальный расчет с запасом на подрезку (10%)
    pure_tiles_count = room_area / tile_area
    final_count = math.ceil(pure_tiles_count * 1.10) # Округляем в большую сторону до целой плитки

    print("\n================ РЕЗУЛЬТАТ РАСЧЕТА ===============")
    print(f"Площадь одной плитки: {tile_area} кв.м.")
    print(f"Чистое количество плитки без подрезки: {pure_tiles_count:.1f} шт.")
    print(f"Итого к покупке (с учетом 10% на подрезку сложных углов): {final_count} шт.")
    print("=================================================")
if __name__ == "__main__":
    main()

























































