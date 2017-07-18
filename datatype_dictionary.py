
my_dict = {}
""" dictionary is an asociative array of key value pair """

characters = {
  "bob":"the builder",
  "mario":"the gamer",
  "turbo":"the rider"
}

#to check whether a key ("bob" in our case) exists in our dictionary characters do
"alice" in characters #returns False as alice does not exist in our dictionary characters

#to retrieve all the keys use `keys()` method
characters.keys()

characters.values()

val = list(characters.values())

#another way to create a dictionary

profile = dict(name="bob",age=27,gender="male")
""" same as 
  profile = {
    "name":"bob",
    "age":27,
    "gender":"male"
  }
"""



