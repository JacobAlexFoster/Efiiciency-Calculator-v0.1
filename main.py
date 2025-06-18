print("Which two parts of the equation do you know?")
print("Efficiency = EFF")
print("Useful Energy Output = UE")
print("Total Energy Input = TE")
print("Useful Power Output = UP")
print("Total Power Input = TP")

x = input("First known variable (EFF/UE/TE/UP/TP): ").strip().upper()
y = input("Second known variable (EFF/UE/TE/UP/TP): ").strip().upper()

if x == "UE" and y == "TE":
    UE = float(input("Useful Energy Output (J): "))
    TE = float(input("Total Energy Input (J): "))
    EFF = (UE / TE) * 100
    print(f"Efficiency: {EFF:.2f}%")

elif x == "UP" and y == "TP":
    UP = float(input("Useful Power Output (W): "))
    TP = float(input("Total Power Input (W): "))
    EFF = (UP / TP) * 100
    print(f"Efficiency: {EFF:.2f}%")

elif x == "EFF" and y == "TE":
    EFF = float(input("Efficiency (%): "))
    TE = float(input("Total Energy Input (J): "))
    UE = (EFF / 100) * TE
    print(f"Useful Energy Output: {UE:.2f} Joules")

elif x == "EFF" and y == "TP":
    EFF = float(input("Efficiency (%): "))
    TP = float(input("Total Power Input (W): "))
    UP = (EFF / 100) * TP
    print(f"Useful Power Output: {UP:.2f} Watts")

elif x == "EFF" and y == "UE":
    EFF = float(input("Efficiency (%): "))
    UE = float(input("Useful Energy Output (J): "))
    print("Invalid input. Please enter EFF, UE, TE, UP, or TP.")
