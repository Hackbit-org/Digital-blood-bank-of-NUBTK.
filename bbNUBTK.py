import pyfiglet

#All the data of the blood group members is here : 
# B+ Blood group list and number:
b_plusdoner = ["Sakil Hasan Saikat\nNumber-01790371317", "Chandro Shakor\nNumber-01966461327", "Mesba\nNumber-01978517018", "Emon\nNumber-01581552003", "RaFi\nNumber-22-07-2023", "Shahin\nNumber-01911090326"]

# B- blood group list and number:
b_minusdoner = ["Sakib Hasan Ruhin\nNumber-01947277883"]

# A+ Blood group list and number:
a_plusdoner = ["Payel\nNumber-01960377184", "Md Sajjad\nNumber-01972326308", "Feroz\nNumber-01741872518", "Lamisha\nNumber-01619800243"]

# A- Blood group list and number:
a_minusdoner = ["No data\nNumber-0"]

# O+ Blood group list and number:
o_plusdoner = ["Lamiya\nNumber-01725151076", "RS Ratul\nNumber-01406042181", "Mahabub\nNumber-01961872289", "Himel\nNumber-01928169446", "Ayon\nNumber-01780938835", "RAJORSHI\nNumber-01886944908", "Shuvro Dev\nNumber-01791996398", "Tåhmìd\nNumber-01913-147372"]

# O- Blood group list and number:
o_minusdoner = ["Shuvo\nNumber-01735-597662", "Rakesh\nNumber-01912935690"]

# AB+ Blood group list and number:
ab_plusdoner = ["Rifat\nNumber-01765570335"]

# AB- Blood group list and number:
ab_minusdoner = ["No data\nNumber-0"]

while True:

    print("This tool is made by: fb.com/0xSaikat and is available at http://hackbit.dao:")
    hackbit_text = pyfiglet.figlet_format("NUBTK Blood Bank!", font="slant")
    print(hackbit_text)
    
    print("Welcome to the Blood Bank of NUBTK.\n")
    print("Which blood group you need? Press the Number- ")
    print("1. A+")
    print("2. A-")
    print("3. B+")
    print("4. B-")
    print("5. O+")
    print("6. O-")
    print("7. AB+")
    print("8. AB-\n")

    data = int(input("Enter a Number:  "))

    if data == 1:
        for a_pluse in a_plusdoner:
            print(a_pluse)
    elif data == 2:
        for a_minus in a_minusdoner:
            print(a_minus)
    elif data == 3:
        for b_plus in b_plusdoner:
            print(b_plus)
    elif data == 4:
        for b_min in b_minusdoner:
            print(b_min)
    elif data == 5:
        for o_plus in o_plusdoner:
            print(o_plus)
    elif data == 6:
        for o_min in o_minusdoner:
            print(o_min)
    elif data == 7:
        for ab_pluse in ab_plusdoner:
            print(ab_pluse)
    elif data == 8:
        for ab_min in ab_minusdoner:
            print(ab_min)

    Continue = input("Enter 'Y' to search again or enter any other key to exit: ")

    if Continue.lower() != "y":
        break

print("Thank you for using this tool!")





