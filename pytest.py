def double_char(str:str) -> str:
   '''Using a given string, it returns a different string

    Args:
        str: the given string

    Returns:
        a string where every character from the given string is repeated twice
    '''
   new_str = ""
   for i in range (len(str)):
      new_str += str[i] + str[i]
   return new_str


def count_hi(str:str) -> int:
    '''Counts the number of "hi" in a string

    Args:
        str: a given string
    
    Returns:
        the number of "hi" in the string
    '''
    count = 0
    for i in range(len(str)-1):
        if str[i:i+2] == "hi":
            count += 1
    return count

def cat_dog(str:str) -> bool:
    '''Counts the number of "cat" and "dog" in a string

    Args:
        str: a given string
    
    Returns:
        True if the number of "cat" is equal to the number of "dog". False if not
    '''
    count_cat = 0
    count_dog = 0
    for i in range (len(str)-1):
        if str[i:i+3] == "cat":
            count_cat += 1
        if str[i:i+3] == "dog":
            count_dog += 1
    return count_cat == count_dog

def count_code(str:str) -> int:
    '''Counts the number of "code" in a string; however, the third letter can be different

    Args:
        str: a given string
    
    Returns:
        the number of "code" or anything with only the third letter different
    '''
    count = 0
    for i in range (len(str)-1):
        if str[i:i+2] == "co" and str[i+3] == "e":
            count += 1
    return count

def xyz_there(str:str) -> bool:
    '''Sees if there is a "xyz" in the string

    Args:
        str: a given string
    
    Returns:
        True if there is a "xyz". False if there is no "xyz" or if the "xyz" is preceeded by a "."
    '''
    for i in range (len(str)-1):
        if str[i] != "." and str[i+1:i+4] == "xyz":
            return True
        elif str[0:3] == "xyz":
            return True
    return False
    
    
    
 #Tests
 from main import double_char
from main import count_hi
from main import cat_dog
from main import count_code
from main import xyz_there

def test_double_char():
    assert double_char('The') == 'TThhee'	
    assert double_char('AAbb') == 'AAAAbbbb'	
    assert double_char('Hi-There') == 'HHii--TThheerree'	
    assert double_char('Word!') == 'WWoorrdd!!'	

def test_count_hi():
    assert count_hi('abc hi ho') == 1	
    assert count_hi('ABChi hi') == 2	
    assert count_hi('hihi') == 2	
    assert count_hi('hiHIhi') == 2

def test_cat_dog():
    assert cat_dog('catdog') == True	
    assert cat_dog('catcat') == False
    assert cat_dog('1cat1cadodog') == True	
    assert cat_dog('catxxdogxxxdog') == False	

def test_count_code():
    assert count_code('aaacodebbb') == 1
    assert count_code('codexxcode') == 2	
    assert count_code('cozexxcope') == 2	
    assert count_code('cozfxxcope') == 1

def test_xyz_there():
    assert xyz_there('abcxyz') == True	
    assert xyz_there('abc.xyz') == False	
    assert xyz_there('xyz.abc') == True	
    assert xyz_there('abcxy') == False
