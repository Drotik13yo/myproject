import random
klas25a = ["Daan A.", "Abdul", "Yaroslav", "Beam", "Luo Xi", "Dima", "Damiën", "Matthew", "Winay", "Jarrod", "Mohammad", "Jaimy", "Maurizio", "Jay-Quan", "Safa", "Kiyara", "Marouf", "Annemare", "Semen", "Ajay", "Bert", "Rogier", "Daan V.", "Kateryna"]
a =  int(input("How much people you need?"))
b = int(input("How much groups you need?"))
for i in range(b): 
    groep = [random.sample(klas25a, a) for i in range(b)]
    print(groep)