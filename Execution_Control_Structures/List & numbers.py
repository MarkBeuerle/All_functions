invoer = "5-9-7-1-7-8-3-2-4-8-7-9"
invoer_lst = invoer.split('-')
invoer_lst.sort()
print("Gesorteerde list van ints: " + str(invoer_lst))
print("Grootste getal: " + str(max(invoer_lst)) + " en Kleinste getal: " + str(min(invoer_lst)))
totaal = 0
for x in invoer_lst:
    totaal += int(x)

print("Aantal getallen: " + str(len(invoer_lst)) + " en Som van de getallen: " + str(totaal))
aantal = 0
per_een = 0
for y in invoer_lst:
    aantal += int(y)
    per_een += 1

gemiddelde = (aantal / per_een)
print("Gemiddelde: " + str(gemiddelde))