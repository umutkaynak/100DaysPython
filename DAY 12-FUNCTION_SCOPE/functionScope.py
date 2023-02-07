################### Scope ####################

enemies = 1

def increase_enemies():
  enemies = 2
  print(f"içerideki düşmanlar  function: {enemies}")

increase_enemies()
print(f"dışarıdaki düşmanlar function: {enemies}")  


#local scope# -YEREL KAPSAM-
def iksir_icmek():
  iksirGucu=2
  print(iksirGucu)
  
iksir_icmek()

print(iksir_icmek) #kapsam içerisinde olmadığından dışında kullanmaya çalışırsak hata ile karşılaşırız

#global Scope# - KÜRESEL KAPSAM-

playerHealth=10

def drink_potion():
  potipnStrength=2
  print(playerHealth)
drink_potion()
print(playerHealth)


#block scope# -BLOK KAPSAM-

gameLevel=3
def create_enemy():
  enemies=["SKELETON","ZOMBIE","ALIEN"]
  if gameLevel<5:
    newEnemy=enemies[0]

    print(newEnemy)

create_enemy()


#global bir değişken nasıl değiştirilir

enemy="zombie"

def increase_enemy():
  enemy="skleleton"
  print(f"içerideki düşman {enemy}")

increase_enemy()
print(f"dışarıdaki düşman {enemy}")

enemies = 1

def increase_enemies():
  global enemies
  enemies +=1
  print(f"içerideki düşmanlar  function: {enemies}")

increase_enemies()
print(f"dışarıdaki düşmanlar function: {enemies}")  

