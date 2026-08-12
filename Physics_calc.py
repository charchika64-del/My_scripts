def take_mass():
    mass = float(input("Enter mass of object: (in kg) "))
    return mass
def take_velocity():
    velocity = float(input("Enter velocity: (in m/s) "))
    return velocity
    
def force():
        #Storing return value
        m=take_mass()
        a = float(input("Enter acceleration of object:(in m/s²) "))
        f = m*a
        print("Force is", f ,"N")

def momentum():
        v = take_velocity()
        M = take_mass()
        p = M*v
        print("Momentum is ",p, "kg.m/sec")

def kinetic_energy():
        v = take_velocity()
        M = take_mass()
        sq= v**2
        ke=0.5*M*sq
        print("K.E. is", ke ,"joules")

def potential_energy():
        M = take_mass()
        g = float(input("Type 8 to take g as 10m/s² or  9 to take as 9.8m/s²: "))
        if g == 8:
                g=10
        else:
                g=9.8
        h = float(input("Enter height: (in metre) "))
        W=M*g*h
        print("P.E. is", W ,"joules")

def work():
        F = float(input("Enter force: (in N) "))
        s = float(input("Enter dispacement: (in metre) "))
        W=F*s
        print("Work done is", W ,"joules")

print("""Type the following numbers -
             1 to calculate force
             2 to calculate momentum
             3 to calculate kinetic energy
             4 to calculate potential energy
             5 to calculate work""")

print("NOTE: There should be no unit while entering quantities. Units  are set.")

while True:
        num = float(input("Enter the number: "))
        if num==1:
                force()
        elif num==2:
                momentum()
        elif num==3:
                kinetic_energy()
        elif num==4:
                potential_energy()
        elif num==5:
                work()
        else:
                print("Enter a valid number")
