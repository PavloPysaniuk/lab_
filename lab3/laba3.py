

numbers = [1, 5, 3, 7, 4, 6, 2, 8, 9]  # ������� �������� �����

for i, num1 in enumerate(numbers):
    for j, num2 in enumerate(numbers[i+1:]):  # �������� ������ � ���������� ��������
        if num1 + num2 == 10:
            print(num1, num2)