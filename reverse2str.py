class StringReverser:
    @staticmethod
    def reverse_words(s:str)->str:
        return' '.join(s.split()[::-1])
if __name__== "__main__":
       s="hello world python"
reverser=StringReverser()
print(reverser.reverse_words(s))

