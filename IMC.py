#Code

#IMC = Peso / Altura2

weight = int(input("What is your current weight in pounds?:"))
if weight>150:
        print("Wow...thats a lot")
elif weight<150:
        print("Very good, stay healthy.")   
height = float(input ("What is your current height in ft?:"))

poundstokg = weight / 2.2046

fttom = height * 0.3048 

multiplicacion = fttom * fttom 

imc = int(poundstokg / multiplicacion)
print("You Have a corporal mass of:",imc)

if imc <18:
        print("You are underweight")
elif imc >=18 and imc <=24:
        print("You have a normal weight")
elif imc >=25 and imc <=29:
        print("You are overweight")
else:
        print("You are Obese")



















    