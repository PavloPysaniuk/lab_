while True:
    file_path = input("Введіть шлях до файлу: ")
    
    try:
        with open(file_path, "r") as f:
            lines = f.readlines()
    except FileNotFoundError:
        print("Файл не знайдено")
        continue
    
    num_lines = len(lines)
    num_empty_lines = 0
    num_z_lines = 0
    num_z_chars = 0
    num_and_lines = 0
    
    for line in lines:
        if not line.strip():
            num_empty_lines += 1
        
        if "z" in line:
            num_z_lines += 1
            num_z_chars += line.count("z")
        
        if "and" in line:
            num_and_lines += 1
    
    print("Кількість рядків:", num_lines)
    print("Кількість порожніх рядків:", num_empty_lines)
    print("Кількість рядків з літерою 'z':", num_z_lines)
    print("Кількість літер 'z' у файлі:", num_z_chars)
    print("Кількість рядків з групою символів 'and':", num_and_lines)
    
    choice = input("Аналізувати ще один файл? (y/n) ")
    
    if choice.lower() != "y":
        break
