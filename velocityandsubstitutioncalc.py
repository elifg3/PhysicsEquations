import time
print("Welcome to the velocity and displacement calculator")
time.sleep(1)
second=float(input("Please enter how long object hung in the air (second): "))
time.sleep(1)

deltatime=second/2
g=-9.8


LastVelocity=0 #object hungs in the air so the velocity is 0
DeltaVelocity=g*deltatime

FirstVelocity=DeltaVelocity*-1 #substractions erases each other
AverageVelocity=(LastVelocity+FirstVelocity)/2
d=AverageVelocity*deltatime

print(f"The substitution in the {deltatime}th second is {s:.2f}m which is maximum displacement in the whole movement of the object.")
print(f"The maximum velocity of the object whole time is {FirstVelocity:} m/s.")







