per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}

Vklad = int(input ("Ведите сумму депозита: "))

TKB = float(per_cent['ТКБ'])*Vklad/100
SKB = float(per_cent['СКБ'])*Vklad/100
VTB = float(per_cent['ВТБ'])*Vklad/100
SBER = float(per_cent['СБЕР'])*Vklad/100

Deposit = [TKB, SKB, VTB, SBER]
print (Deposit)

print ("Максимальная сумма, которую вы можете заработать", max(Deposit))
