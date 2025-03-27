def extras(agenda:tuple):
    i:int=0
    while (i<len(agenda)):
        nombre, correo, tel = agenda[i]
        i+=1
        yield nombre, correo, tel


if __name__ == '__main__':
    agenda=[]
    agenda.append(("Alison", "meneses0307@gmail.com", "2481968948"))
    agenda.append(("Dulce", "dulcencia2345@gmail.com", "2485673456"))
    agenda.append(("Alfredo", "josealfredo502@gmail.com", "2481312968"))
    agenda.append(("Brenda", "meneses0307@gmail.com", "2485673456"))
    agenda.append(("Cecilia", "ceciliaA0307@gmail.com", "2485673456"))
    agenda.append(("Juan", "juan879@gmail.com", "2485673456"))
    agenda.append(("Rubi", "rubi67@gmail.com", "2485673456"))
    agenda.append(("Nancy", "nancy234@gmail.com", "2485673456"))
    agenda.append(("Yessica", "yessVicuña@gmail.com", "2485673456"))

    for a,b,c in extras(agenda):
        print(f"nombre: {a}, correo: {b}, telefono: {c}")