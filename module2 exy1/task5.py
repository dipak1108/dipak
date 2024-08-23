print('Give mass in talents ,pounds ,lots ')
talents = float(input('first give talents : '))
pounds = float(input('Then give pounds:'))
lots = float(input('Then give lots:'))

lotsInGrams = 13.3
poundsInGrams = 32 * lotsInGrams
talentsInGrams = 20 * poundsInGrams

mass = talents * talentsInGrams + pounds * poundsInGrams  + lots *lotsInGrams


kg = int(mass / 1000)

grams = mass % 1000

print('The weight in modern units:')
print(f'{kg} kilograms and {grams:.2f} grams')