from smartphone import Smartphone

catalog = []

catalog.append(Smartphone("Apple", "iPhone 15", "+79001112233"))
catalog.append(Smartphone("Samsung", "Galaxy S24", "+79112223344"))
catalog.append(Smartphone("Google", "Pixel 8", "+79223334455"))
catalog.append(Smartphone("Xiaomi", "14 Pro", "+79334445566"))
catalog.append(Smartphone("Huawei", "P60 Pro", "+79445556677"))

for phone in catalog:
    print(f"{phone.brand} - {phone.model}. {phone.phone_number}")
