# Generic Program Template


# operators <,>,==,<=,>=,!=
# data types
#   Tuple_1 = (1,15,3) a list that cannot be changed
#   List_1 = [1,15,3] append, pop, insert, sort, extend
#   Dictionary_1 = {"Joe":"Joe Blow","Jim":"Jim Crow"}

# Import Stuff Here



# Define Stuff Here

something_else=0 # Top level variable can be used as global

def myfunction(something):
    global something_else # referance variable outside function
    something_else = something * 7
    
    return something

class Some_item(): #Capatilize Classes
    ''' This is a docstring for this class '''
    def __init__(self,shape,height,width,depth):
        self.height = height
        self.width = width
        self.depth = depth
        
    def volume(self):# this is a method inside a class
        self.volume = self.height * self.width * self.depth
        return self.volume
        



def main(): # The actual main program
    print("Main Running")
    print(myfunction(23))
    print(something_else)
    cube = Some_item("cube",3,3,3)
    box = Some_item("box",1,2,3)
    print(cube.height * cube.width * cube.depth)
    print('Cube volume=',cube.volume())
    print('Box volume=',box.volume())


if __name__ == "__main__":
    # If this is being run stand-alone then execute otherwise it is being
    # imported and the importing program will use the modules it needs
    main() # Invoke the program

    
