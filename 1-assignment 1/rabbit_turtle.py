print("*** Rabbit & Turtle ***")
d, Vr, Vt, Vf = map(int, input("Enter Input : ").split())

# frequency of times (sec)
time = d / (Vt - Vr)

# insect fly distance it's going being on!!
distance = time * Vf

print(f"{distance:.2f}")