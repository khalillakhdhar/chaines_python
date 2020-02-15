s = "hey python! c'est quoi une chaine?"
print("longueur est s = %d" % len(s))

print("la premiere occurence de c = %d" % s.index("c"))

print("c se répéte %d fois" % s.count("c"))

print("Les cinques premier caractéres sont '%s'" % s[:5]) # Commence de 5
print("The les cinque prochain sont '%s'" % s[5:10]) # 5 à 10
print("The le treizième caractére est '%s'" % s[12])  # seulement 12
#print("The characters with odd index are '%s'" %s[1::2]) #(0-based indexing)
print("les cinqs dernier sont '%s'" % s[-5:]) # 5th-from-last to end

# Convert everything to uppercase
print("La chaine majuscule devient: %s" % s.upper())

# Convert everything to lowercase
print("La chaine miniscule devient: %s" % s.lower())

# Check how a string starts
if s.startswith("Str"):
    print("phrase commence par 'Str'. Good!")
else:
    print("phrase ne  commence pas par 'Str'!")
# Check how a string ends
if s.endswith("chaine?"):
    print("la phrase finit par 'chaine!'. Good!")

# Split the string into three separate strings,
# each containing only a word
print("chaque mot sans espace: %s" % s.split(" "))
#convert first letter into capital
print(s.capitalize())
