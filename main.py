from datetime import date

place_name = "Гора Эльбрус"
altitude = 5642
visit_date = date(2026, 7, 20)
is_open = True

def get_visit_status(is_open):
    if is_open:
        return "Место открыто для посещения"
    return "Место временно закрыто"

print(f"Туристическое место: {place_name}")
print(f"Высота: {altitude} м")
print(f"Дата посещения: {visit_date}")
print(get_visit_status(is_open))