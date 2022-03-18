###~~~~~~~~~~~ A ~~~~~~~~~~~###
def read_line(n, file):
    try:
        count = 0 
        with open(file) as f:
            lines = f.readlines()
            for i in lines:
                count = count + 1
        if type(n) != int:
            return "invalid input detected"
        elif n > count:
            ret = "Line " + str(n) + " doesn't exist"
            return(ret)
        else:
            return lines[n-1] 
    except:
          return "file not found"
      
###~~~~~~~~~~~ B ~~~~~~~~~~~###
def longest_words(file):
    import re
    try:
        data = open(file, 'r')
        lines = [re.split('\W', line) for line in data]
        words = []
        for i in lines:
            for j in i:
                if not j.isalpha():
                    continue
                words.append(j)
        longest = []
        for i in range(5):
            longest.append(max(words, key=len))
            words.remove(max(words, key=len))
        return longest
    except FileNotFoundError:
        return "File not found"

    
    
   