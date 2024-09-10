# Read the instructions to see what you need to do here!

alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def vig_encode(text, keyword):
  temp = ""
  num = 0
  for i in range(len(text)):
    letter = text[i]
    if letter in alpha:
      var = alpha.index(letter) + alpha.index(keyword[num])
      if var > 25:
        var = (var - 26) % var
      temp += alpha[var]
      num += 1
      if num >= len(keyword):
        num = 0
  return temp


def vig_decode(text, keyword):
  temp = ""
  num = 3
  for i in range(len(text)):
    letter = text[i]
    if letter in alpha:
      var = alpha.index(letter) - alpha.index(keyword[num])
      if len(alpha) < var:
        var = (var + 26) % var
      temp += alpha[var]
      num -= 1
      if num <= 0:
        num = 3
  return temp


test = "THEQUICKBROWNFOXJUMPEDOVERTHELAZYDOG"
vig_key = "TEST"
enc = vig_encode(test, vig_key)
dec = vig_decode(enc, vig_key)
print(enc)
print(dec)
# If this worked, dec should be the same as test!