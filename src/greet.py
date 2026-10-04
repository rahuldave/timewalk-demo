def greet( name,excited = False ):
    return 'Hello, '+name+( '!' if excited else '.' )

def shout(name):  return greet(name,excited = True).upper()
