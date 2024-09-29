from src.widget import mask_account_card, get_date

number = ""
print("Введите тип и номер карты или введите счет:")
user_card_or_score = input()
print(mask_account_card(user_card_or_score))

print("Введите дату:")
user_date = input()
print(get_date(user_date))
