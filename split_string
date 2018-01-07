
string="Exemplo de uma frase, espero que funcione ......"


def split_string(string, splitlist):
    size=len(string)
    i=0
    words=[]
    word=""
    letter_check=0
    while i<size:
        if string[i] not in splitlist:
            word =word+string[i]    # if not split caracter keep forming word
            letter_check=1        # found letters
            
        if string[i] in splitlist:
            if letter_check==1:     #if letter found separate word
                words.append(word)
                word=""
                letter_check=0      #found a separation start over
        i=i+1                   #if not keep jumping separation caracters
    if letter_check==1: words.append(word)
    return words
            
        
    
    
    

print split_string(string,". ,!")
