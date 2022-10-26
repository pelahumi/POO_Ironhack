from VikingsClasses import Soldier, Saxon, Viking, War

def lanzador():
    pelayo = Viking("Pelayo", 150, 200)
    ruben = Viking("Ruben", 100, 120)

    flecha = Saxon(100, 130)
    german = Saxon(50, 75)

    guerra = War()

    guerra.addSaxon(flecha)
    guerra.addSaxon(german)

    guerra.addViking(pelayo)
    guerra.addViking(ruben)

    print(guerra.vikingAttack())
    print(guerra.saxonAttack())
    print(guerra.showStatus())


