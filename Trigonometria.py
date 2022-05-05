import math
import sys
import os
import subprocess
def results(catAd, catOp, hip):
    print('~=' * 30)
    print(f'Hipotenusa: {round(hip,2)} ou √{round(hip**2,2)}\nCateto Oposto: {round(catOp,2)} ou √{round(catOp**2,2)}\nCateto Adjacente: {round(catAd,2)} ou √{round(catAd**2,2)}')
    print(f'\nValor do ângulo α: {round(((math.asin(catOp/hip))*180)/math.pi,2)}°\nValor do ângulo β: {round(((math.asin(catAd/hip))*180)/math.pi,2)}°')
    print('~=' * 30)
    print('\n')

while True:
    resp = str(input("Observações:\n— Digite 'r' antes do número para simbolizar raíz quadrada\n— Digite '0' para finalizar\nDigite o Cateto Oposto, Adjascente e Hipotenusa, Respectivamente (Ex: 3 4 xx): "))
    if (resp == "0"):
        print ("Tenha um bom dia!")
        exit()
    elif resp=="":
        print ("Nenhum valor inserido!\n")
        continue
    resp2 = resp.split(" ")
    if len(resp2) < 3:
        print("Não foram inseridos todos os dados necessários!\n")
        continue
    for i in range(len(resp2)):
        if resp2[i] == "0":
            print("Não é possível existir um valor número, tente outro valor!\n")
            sys.stdout.flush()
            subprocess.call([sys.executable, os.path.realpath(__file__)] + sys.argv[1:])
        if resp2[i] == "xx" or resp2[i] == "yy" or resp2[i] == "zz":
            resp2[i] = "0"
        if resp2[i][0] == "r":
            resp2[i] = resp2[i].replace("r","")
            resp2[i] = math.sqrt(float(resp2[i]))
        for j in range(len(resp2[i])):
            if resp2[i][j] == ",":
                resp2[i] = resp2[i].replace(",",".")
    resp3 = [float(i) for i in resp2]
    catOp = resp3[0]; catAd = resp3[1]; hip = resp3[2]
    
    if catOp!=0 and catAd!=0 and hip!=0:
        print("Todos os valores já foram inseridos, nenhuma operação necessária!\n")
        continue
    elif catOp!=0 and catAd!=0 and hip==0:
        hip = math.sqrt(catOp**2 + catAd**2)
        teta = ((math.asin(catOp/hip))*180)/math.pi
    elif catOp!=0 and catAd==0 and hip!=0:
        catAd = math.sqrt(hip**2 - catOp**2)
    elif catOp==0 and catAd!=0 and hip!=0:
        catOp = math.sqrt(hip**2 - catAd**2)
    elif catOp==0 and catAd==0 and hip==0:
        print("Nenhum valor inserido!\n")
        continue

    elif catOp!=0 and catAd==0 and hip==0:
        ang = float(input("Digite o ângulo oposto (α) ao Cateto Oposto: "))
        arc = (ang*math.pi)/180
        catAd = catOp/math.tan(arc); hip = math.sqrt(catOp**2 + catAd**2)
    elif catOp==0 and catAd!=0 and hip==0:
        ang = float(input("Digite o ângulo oposto (α) ao Cateto Oposto: "))
        arc = (ang*math.pi)/180
        catOp = catAd*math.tan(arc); hip = catAd/math.cos(arc)
    elif catOp==0 and catAd==0 and hip!=0:
        ang = float(input("Digite o ângulo oposto (α) ao Cateto Oposto: "))
        arc = (ang*math.pi)/180
        catOp = hip*math.sin(arc); catAd = hip*math.cos(arc)
    results(catAd, catOp, hip)