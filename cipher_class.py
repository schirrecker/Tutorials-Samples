class CaesarCipher(object):
    def __init__(self, shift):
        self.shift = shift

    def encode(self, str):
        res = ""
        new_str = str.upper()
        for l in new_str:
            x = ord(l) + self.shift
            if x > 90:
                x = 65 - (90 - x)
            res += chr(x)
        return res

    def decode(self, str):
        res = ""
        for l in str:
            x = ord(l) - self.shift
            if x < 65:
                x = 90 - (64 - x)
            res += chr(x)
        return res
    
c = CaesarCipher(5)
c.encode('Codewars')
c.decode('BFKKQJX')

