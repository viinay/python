


characters = {
  "bob":"the builder",
  "mario":"the gamer",
  "turbo":"the rider",
  "alice":"the builder"
}

builders = list(characters.values())

for builder in builders:
  num = builders.count()
  print "there are {} builder(s) in characters dict".format(num)
  

for builder in set(builders):
  num = builders.count()
  print "there are {} builder(s) in characters dict".format(num)
