saldo = 80 # 80
saldo_anterior = saldo # 80

saldo = saldo - 25 # 55
saldo = saldo + 10 # 65

print("Saldo anterior:", saldo_anterior) # 80
print("Saldo atual:", saldo) # 65

# 'saldo_anterior' mantém seu valor porque ele nunca foi alterado após a variável 'saldo' ser alterada.

saldo -= 15 # 50
print("Saldo anterior:", saldo_anterior) # 80
print("Saldo atual:", saldo) # 50
