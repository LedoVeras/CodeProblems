vert = {
    "vertebrado": {
        "ave" : {
            "carnivoro" : "aguia",
            "onivoro" : "pomba"
            },
        "mamifero" : {
            "onivoro" : "homem",
            "herbivoro" : "voco"
        }
    },
    "invertebrado": {
        "inseto" : {
            "hematofago" : "pulga",
            "herbivoro" : "lagarta"
            },
        "anelideo" : {
            "hematofago" : "sanguessuga",
            "onivoro" : "minhoca"
        }
    }   
}

ve = input()
cl = input()
nu = input()

print(vert[ve][cl][nu])
