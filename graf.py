import matplotlib.pyplot as plt
import lots_db

lots = lots_db.select_all()

data = {}
count = {}
price = {}

for lot in lots:
    if lot[2] in data.keys():
        data[lot[2]] += lot[3]
    else:
        data.update({lot[2]: lot[3]})
    if lot[2] in count.keys():
        count[lot[2]] += 1
    else:
        count.update({lot[2]: 1})

print(data, count)

for key, item in data.items():
    price[key] = item / count[key]

print(price)

fig = plt.figure()   # Создание объекта Figure
for key, items in price.items():
    plt.scatter(key, items)   # scatter - метод для нанесения маркера в точке (1.0, 1.0)

plt.show()