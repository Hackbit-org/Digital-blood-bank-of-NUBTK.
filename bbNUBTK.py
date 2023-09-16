import pyfiglet

print("This tools made by: fb.com/0xSaikat and a tools of http://hackbit.dao :  ")
hackbit_text = pyfiglet.figlet_format("NUBTK Blood Bank!", font="slant")
print(hackbit_text)

#B+ Blood group list :

b_plusdoner = "Sakil Hasan Saikat\nNumber-01790371317\n"
b_plusdoner1 = "Chandro Shakor\nNumber-01966461327\n"
b_plusdoner2 = "Mesba\nNumber-01978517018\n"
b_plusdoner3 = "Emon\nNumber-01581552003\n"
b_plusdoner4 = "RaFi\nNumber-22-07-2023\n"
b_plusdoner5 = "Shahin\nNumber-01911090326\n"


#B- blood group list :
b_minusdoner = "Sakib Hasan Ruhin\nNumber-01947277883\n"


#A+ Blood group list :

a_plusdoner = "Payel\nNumber-01960377184\n"
a_plusdoner1 = "Md Sajjad\nNumber-01972326308\n"
a_plusdoner2 = "Feroz\nNumber-01741872518\n"
a_plusdoner3 = "Lamisha\nNumber-01619800243\n"


#A- Blood group list
a_minusdoner = "No data\nNumber-0\n"


#O+ Blood group list :

o_plusdoner = "Lamiya\nNumber-01725151076\n"
o_plusdoner1 = "RS Ratul\nNumber-01406042181\n"
o_plusdoner2 = "Mahabub\nNumber-01961872289\n"
o_plusdoner3 = "Himel\nNumber-01928169446\n"
o_plusdoner4 = "Ayon\nNumber-01780938835\n"
o_plusdoner5 = "RAJORSHI\nNumber-01886944908\n"
o_plusdoner6 = "Shuvro Dev\nNumber-01791996398\n"
o_plusdoner7 = "Tåhmìd\nNumber-01913-147372\n"


#O- Blood group list :

o_minusdoner = "Shuvo\nNumber-01735-597662\n"
o_minusdoner1 = "Rakesh\nNumber-01912935690\n"


#AB+ Blood group list :

ab_plusdoner = "Rifat\nNumber-01765570335\n"


#AB- Blood group list :

ab_minusdoner = "No data\nNumber-0\n"


print("Welcome to the Blood Bank of NUBTK.\n")
print("If you want A+ blood then press- 1")
print("If you want A- blood then press- 2")
print("If you want B+ blood then press- 3")
print("If you want B- blood then press- 4")
print("If you want O+ blood then press- 5")
print("If you want O- blood then press- 6")
print("If you want AB+ blood then press- 7")
print("If you want AB- blood then press- 8\n")



data = int (input("Enter a Number: "))

if data==1:
    print(a_plusdoner, a_plusdoner1, a_plusdoner2, a_plusdoner3)

if data==2:
    print(a_minusdoner)

if data==3:
    print(b_plusdoner, b_plusdoner1, b_plusdoner2, b_plusdoner3, b_plusdoner4, b_plusdoner5)

if data==4:
    print(b_minusdoner)

if data==5:
    print(o_plusdoner, o_plusdoner1, o_plusdoner2, o_plusdoner3, o_plusdoner4, o_plusdoner5, o_plusdoner6, o_plusdoner7)

if data==6:
    print(o_minusdoner, o_minusdoner1)

if data==7:
    print(ab_plusdoner)

if data==8:
    print(ab_minusdoner)

print("Thank you for usein this tools!")





