Largura_Garagem = float(input("Qual a largura da garagem em metros? "))
Profundidade_Garagem = float(input("Qual a profundidade da garagem em metros? "))

Area_Garagem = Largura_Garagem * Profundidade_Garagem

Largura_Terreno = float(input("Qual a largura do terreno em metros? "))
Profundidade_Terreno = float(input("Qual a profundidade do terreno em metros? "))

Area_Terreno = Largura_Terreno * Profundidade_Terreno

Percentual = ((Area_Garagem) / (Area_Terreno)) * 100
print("Percentual da ocupação: ", Percentual)

Zona=input("Entre com a zona de localização: Sul=S, Norte-N, Leste=L e Oeste=W: ")

print("Imóvel localizado na zona: ", Zona)
print("Percentual de ocupação: ", Percentual)

if Zona=="N" and Percentual <= 25:
    print("Projeto atende norma de zoneamento do plano diretor")

elif Zona=="L" or Zona=="W" and Percentual<=30:
    print("Projeto atende norma de zoneamento do plano diretor")

elif Zona=="S" and Percentual<=40:
    print("Projeto atende norma de zoneamento do plano diretor")

else:
    print("REVISAR MEDIDAS. Projeto NÃO atende norma do plano diretor")
    

