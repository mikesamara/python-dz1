# Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S журавликов. 
# Сколько журавликов сделал каждый ребенок, если известно,
# что Петя и Сережа сделали одинаковое количество журавликов, 
# а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?

# *Пример:*

# 6 -> 1  4  1
# 24 -> 4  16  4
#     60 -> 10  40  10

s = int (input("Введите количество журавликов, которые сделали дети:"))
rez = s/6
c = rez*4
print(f"Петя и сережа сделали {rez} журавликов")
print(f"Света сделала {c} журавликов")