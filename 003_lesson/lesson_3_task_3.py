from address import Address
from mailing import Mailing

# Создаем экземпляры класса Address для отправителя и получателя
from_address = Address("625000", "Тюмень", "Ленина", "76", "3")
to_address = Address("625019", "Тюмень", "Республики", "155", "48")

# Создаем экземпляр класса Mailing
mailing = Mailing(to_address, from_address, 500, 62510022025)

# Выводим информацию об отправлении
print(mailing)
