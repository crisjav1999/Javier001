A=int(input("Valor de su compra"))
B=(A*(12/100))+A
print("Precio +IVA",B)
if B>200:
   print("valor con descuento",(B-(B*(2/100))))
   print("valor del ahorro",(B*(2/100)))
   print("total a pagar",(B-(B*(2/100))))
else:
    print("total a pagar",B)
