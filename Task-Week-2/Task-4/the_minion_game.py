def minion_game(string):
    # your code goes here
    vowel='AEIOU'
    kevin=0
    stuart=0
    s=len(string)
    for i in range(0,s):
        if string[i] in vowel:
            kevin += (s-i)
        else:
            stuart += s-i
    
    if kevin>stuart:
        print('Kevin',kevin)
    elif stuart>kevin:
        print('Stuart',stuart)
    else:
        print('Draw')            
    

if __name__ == '__main__':
    s = input()
    minion_game(s)