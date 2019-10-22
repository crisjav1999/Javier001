A=int(input("Ingresar numero X"))
B=int(input("Ingresar numero Y"))
C=int(input("Ingresar numero Z"))

if A>B and A>C:
    print("el numero mayor es",A)
elif B>A and B>C:
    print("el numero mayor es",B)
else:
    print("el numero mayor es",C)
