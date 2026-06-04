from address import Address
from mailing import Mailing

to_address = Address("123456", "Москва", "Ленина", "10", "5")
from_address = Address("654321", "Санкт-Петербург", "Садовая", "25", "12")

my_mailing = Mailing(to_address, from_address, cost=500, track="TRACK565345")

print(f"Отправление {my_mailing.track} из "
      f"{my_mailing.from_address.index}, {my_mailing.from_address.city},"
      f" {my_mailing.from_address.street}, {my_mailing.from_address.house}-"
      f"{my_mailing.from_address.apartment} "
      f"в {my_mailing.to_address.index}, {my_mailing.to_address.city}, "
      f"{my_mailing.to_address.street}, {my_mailing.to_address.house} - "
      f"{my_mailing.to_address.apartment}. Стоимость {my_mailing.cost} рублей")
