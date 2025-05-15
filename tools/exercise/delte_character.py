def delete_characters(string1: str, string2: str) -> None:
    """ return two string with the intersetion """
    
    
    out1 = [s1 for s1 in string1 if s1 not in string1]
    out2 = [s2 for s2 in string2 if s2 not in string1]
            
    print(out1,"\n",out2)


def main():
    
    string1 = "WReKneQMedÑinaF"
    string2 = "XReneZMedCiDnaP" 
    
    delete_characters(string1, string2)
    


main()