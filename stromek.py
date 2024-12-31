def  vykresli_stromek(vyska):
    for i  in range(vyska):
        mezery = " " * (vyska - i -1)
        hvezdicky = "*" * (2 * i - 1)
        print(mezery + hvezdicky)
    
    for _ in range(2):
        print(" " * (vyska - 1) + "/")

try:
    vyska = int(input("Zadejte výšku stromu: "))
    if vyska > 0:
        vykresli_stromek(vyska)
    else:
        print("výška musí být v kladných číslech: ")
except ValueError:
    print("prosím zadej celé číslo")


print("Krásné a Veselé Vánoce")