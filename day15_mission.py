
pokemons = [{"피카츄": 200}, {"라이츄": 150}, {"파이리": 90}, {"꼬부기": 50}, {"이상해씨": 30}]

def insert_pokemon(name, hp):

   for i in range(len(pokemons)):
      for value in pokemons[i].values():
         continue
      if value <= hp:
         idx = i
         break
      elif i == len(pokemons)-1:
         idx = len(pokemons)

   pokemons.append(None)
   for i in range(len(pokemons)-1, idx , -1):
      pokemons[i] = pokemons[i-1]
      pokemons[i-1] = None
   pokemons[idx] = {name: hp}

   print(pokemons)


if __name__ == "__main__":
   name = str(input("추가할 포켓몬 : "))
   hp = int(input("체력 : "))
   insert_pokemon(name, hp)



