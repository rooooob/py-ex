# 6 kyu
import re
def song_decoder(song):
    p = r'WUB'
    return " ".join(re.sub(p, ' ', song).split()) # con join(string.split()) removemos todos los
        # espacios innecesarios 

print(song_decoder("AWUBBWUBC"))
print(song_decoder("AWUBWUBWUBBWUBWUBWUBC")) # no puede tener espacios dobles
print(song_decoder("WUBAWUBBWUBCWUB")) # ni en el comienzo o el final

# https://www.delftstack.com/es/howto/python/how-to-remove-whitespace-in-a-string/