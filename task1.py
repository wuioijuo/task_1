A = {8, 10, 11, 13, 14, 15, 17, 18, 21, 23, 24, 25, 27, 29, 32, 33, 36, 39, 40}
B = {1, 2, 3, 6, 7, 8, 12, 14, 16, 18, 20, 21, 24, 26, 27, 29, 30, 32, 38, 40}
C = {3, 8, 9, 10, 13, 14, 16, 17, 22, 26, 27, 30, 31, 32, 33, 35, 38, 39}
D = {1, 2, 3, 5, 6, 7, 8, 9, 10, 13, 14, 21, 22, 23, 26, 28, 29, 30, 32, 33, 36, 37, 38}

print('Исходные множества:')
print(f'A = {A}')
print(f'B = {B}')
print(f'C = {C}')
print(f'D = {D}')
print()

# Вычисление первого выражения: ((B ∪ C) ∆ ((C ∪ A) ∆ D)) \ ((C ∩ A) ∪ (C ∩ B))
print('Вычисление ((B ∪ C) ∆ ((C ∪ A) ∆ D)) \ ((C ∩ A) ∪ (C ∩ B)):')

# шаг 1: B ∪ C
step_1 = B.union(C)
print(f'B ∪ C = {step_1}')

# шаг 2: C ∪ A
step_2 = C.union(A)
print(f'C ∪ A = {step_2}')

# шаг 3: (C ∪ A) ∆ D
step_3 = step_2 ^ D
print(f'(C ∪ A) ∆ D = {step_3}')

# шаг 4: (B ∪ C) ∆ ((C ∪ A) ∆ D)
step_4 = step_1 ^ step_3
print(f'(B ∪ C) ∆ ((C ∪ A) ∆ D) = {step_4}')

# шаг 5: C ∩ A
step_5 = C & A
print(f'C ∩ A = {sorted(step_5)}')

# шаг 6: C ∩ B
step_6 = C & B
print(f'C ∩ B = {sorted(step_6)}')

# шаг 7: (C ∩ A) ∪ (C ∩ B)
step_7 = step_5.union(step_6)
print(f'(C ∩ A) ∪ (C ∩ B) = {sorted(step_7)}')

# шаг 8: ((B ∪ C) ∆ ((C ∪ A) ∆ D)) \ ((C ∩ A) ∪ (C ∩ B))
result_1 = step_4 - step_7
print(f'Результат первого выражения = {sorted(result_1)}')
print()

# Вычисление второго выражения: ((D \ B) ∪ C) ∩ (((C ∪ B) ∩ A ∩ D) ∆ ((C ∪ D) ∩ (A ∪ B)))
print('Вычисление ((D \ B) ∪ C) ∩ (((C ∪ B) ∩ A ∩ D) ∆ ((C ∪ D) ∩ (A ∪ B))):')

# шаг 1: D \ B
step1 = D - B
print(f'D \ B = {sorted(step1)}')

# шаг 2: (D \ B) ∪ C
step2 = step1.union(C)
print(f'(D \ B) ∪ C = {sorted(step2)}')

# шаг3: C ∪ B
step3 = C.union(B)
print(f'C ∪ B = {sorted(step3)}')

# шаг 4: (C ∪ B) ∩ A ∩ D
step4 = step3 & A & D
print(f'(C ∪ B) ∩ A ∩ D = {sorted(step4)}')

# шаг 5: C ∪ D
step5 = C.union(D)
print(f'C ∪ D = {sorted(step5)}')

# шаг 6: A ∪ B
step6 = A.union(B)
print(f'A ∪ B = {sorted(step6)}')

# шаг 7: (C ∪ D) ∩ (A ∪ B)
step7 = step5 & step6
print(f'(C ∪ D) ∩ (A ∪ B) = {sorted(step7)}')

# шаг 8: ((C ∪ B) ∩ A ∩ D) ∆ ((C ∪ D) ∩ (A ∪ B))
step8 = step4 ^ step7
print(f'((C ∪ B) ∩ A ∩ D) ∆ ((C ∪ D) ∩ (A ∪ B)) = {sorted(step8)}')

# шаг 9: ((D \ B) ∪ C) ∩ (((C ∪ B) ∩ A ∩ D) ∆ ((C ∪ D) ∩ (A ∪ B)))
result_2 = step2 & step8
print(f'Результат второго выражения = {sorted(result_2)}')
print()

# Результаты двух выражений:
print('Результаты двух выражений:')
print(f'1.((B ∪ C) ∆ ((C ∪ A) ∆ D)) \ ((C ∩ A) ∪ (C ∩ B)) = {sorted(result_1)}')
print(f'2.((D \ B) ∪ C) ∩ (((C ∪ B) ∩ A ∩ D) ∆ ((C ∪ D) ∩ (A ∪ B))) = {sorted(result_2)}')