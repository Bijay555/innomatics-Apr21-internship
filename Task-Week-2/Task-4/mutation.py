def mutate_string(string, position, character):
    l=list(string)
    l[position]=character
    m=''.join(l)
    return m