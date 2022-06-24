password = 1234
input_password = 2134

if password == input_password:
    print("password correct, are you sure you want to launch the nuclear missiles?")
    descision = "no"
    if descision == "yes":
        print("missiles launched")
    else:
        print("launch cancelled")
else:
    print("password incorrect")
