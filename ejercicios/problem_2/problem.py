def length_of_last_word(s):
    ###first constraint
    if 1 <= len(s) <= 104:
        ###start problem
        s = s.strip()
        for i in range(1, len(s)):
            if s[-i] == " ":
                word = s[-i + 1:]
                return len(word)
    else:
        return "String length out of range"
        
length_of_last_word("Hello World")
length_of_last_word("   fly me   to   the moon  ")
length_of_last_word("luffy is still joyboy")
