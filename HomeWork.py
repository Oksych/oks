num_tickets = int(input("Введите количество билетов, которые вы хотите приобрести: "))

total_cost = 0
discount = 0

for i in range(num_tickets):
    age = int(input("Введите возраст посетителя: "))

    if age < 18:
        cost = 0
    elif 18 < age < 25:
        cost = 990
    else:
        cost = 1390

    total_cost += cost

    if num_tickets > 3:
        discount = total_cost * 0.1

total_cost -= discount
print("Сумма к оплате:", total_cost, "руб.")
