contagem_numero = 0
i = 0
while i < 5000000:
  i = i + 1
  if ((i % 2 == 0) and (i % 37 == 0) and (i % 49 == 0)):
      contagem_numero = contagem_numero + 1


print(contagem_numero)