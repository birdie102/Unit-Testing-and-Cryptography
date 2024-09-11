# Read the instructions to see what you need to do here!

alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def vig_encode(text, keyword):
  temp = ""
  for i in range(len(text)):
    letter = text[i]
    if letter in alpha:
      var = alpha.index(letter) + alpha.index(keyword[i % len(keyword)])
      if var > len(alpha) - 1:
        var = (var - 26) % var
      temp += alpha[var]
  return temp


def vig_decode(text, keyword):
  temp = ""
  for i in range(len(text)):
    letter = text[i]
    if letter in alpha:
      var = alpha.index(letter) - alpha.index(keyword[i % len(keyword)])
      if var > len(alpha):
        var = (var - 26) % var
      temp += alpha[var]
  return temp


test = "THEQUICKBROWNFOXJUMPEDOVERTHELAZYDOG"
vig_key = "TEST"
enc = vig_encode(test, vig_key)
dec = vig_decode(enc, vig_key)
print(enc)
print(dec)
# If this worked, dec should be the same as test!