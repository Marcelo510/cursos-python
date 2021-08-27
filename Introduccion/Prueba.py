

medios = ["cheques", "bonos", "acciones", 1000, "transferencia"]
segundo = medios[1]

print(segundo[2])


print(medios[1][2])



medios = ["cheques", "bonos", "acciones", 1000, "transferencia"]
print(medios[1][2])

listavac = [1,2,3]
medios.append(listavac)
print(medios)

medios = ["cheques", "bonos", "acciones", 1000, "transferencia", []]

for medio in medios:
    if(type(medio) == int):
        print(str(medio)[0])
    elif(type(medio) == str):
        print(medio[0])
    else:
        print('Es otro tipo ->' + str(type(medio)))
    
    