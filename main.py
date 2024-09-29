from src.masks import get_mask_card_number, get_mask_account

print("Введите номер карты в виде числа:")
user_card_number = input()
print(get_mask_card_number(user_card_number))

print("Введите номер счета в виде числа:")
user_account = input()
print(get_mask_account(user_account))
