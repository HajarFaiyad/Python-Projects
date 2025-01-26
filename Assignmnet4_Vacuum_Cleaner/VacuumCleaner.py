# In this project there are other ways/methods to print all the features of a vacuum cleaner (including thoese for both classes)
# Like for example we can create a getVacuum() function, which returns the assigned value for each parameter in the class
#                          and a getCleaner() function, which retuens all the assigned values for the parameters (the 6 of them)
# Then we can create the objects (for example, obj1) and use print(obj1.getCleaner())
# There are other ways as well for which we can implement this project. 
#       For example, we can neglect the usage of the getVacuum(), or in my project showVacuum().

# first called vacuum class
class Vacuum:
    # The vacuum class has three parameters  
     # type: can be one of two: Dry or wet.
     # watt: can be one of three: 1000w, 600w or 300w
     # bag: A string value. can be one of two: yes or no

    #defining the vacuum class overriding constructor
    def __init__(self, Type, Watt, Bag):  # here we include the main 3 parameters of the vacuum class
        self.Type = Type
        self.Watt = str(Watt) + "w"  # i need to typpecst the watt variable to convert it from int to str
        self.Bag = Bag

    # showVacuum function to print and show the elements/features of the vacuum class
    def showVacuum(self):
        print(f'Vacuum Type: {self.Type}  Vacuum Watt: {self.Watt} Vacuum Bag:  {self.Bag}' )


# second class called Cleaner extends/inherits the Vacuum class
class Cleaner(Vacuum):

    # The cleaner class has three parameters  
     # brand: Name of brand. can be one of four: Singer, rainbow, vestel, or beko
     # cord: A boolean value for With or without cord. 
     # colour: Can be one of four: Grey, black, navy or red.

    #overriding Cleaner class constructor
    def __init__(self, Type, Watt, Bag, Brand, Cord, Colour):  # here we include the main 3 parameters of the cleaner class, and 3 parameters of the vacuum class 
        super().__init__(Type, Watt, Bag) # used to include the 3 parameters from the vacuum class
        self.Brand = Brand 
        self.Cord = Cord
        self.Colour = Colour


    #showCleanerV1 and showCleanerV2 functions to print and show the elements/features of the cleaner class
    # both functions produce the same output through using diferent methods
    def showCleanerV1(self):
        print(f'Vacuum Type: {self.Type}  Vacuum Watt: {self.Watt} Vacuum Bag: {self.Bag}   Cleaner Brand: {self.Brand}  Cleaner Cord: {self.Cord}  Cleaner Colour: {self.Colour}')

    #version 2 used the showVacuum() method from the vacuum class
    def showCleanerV2(self):
        print( f' {self.showVacuum()}  Cleaner Brand: {self.Brand}  Cleaner Cord: {self.Cord}  Cleaner Colour: {self.Colour}')

#Testing 
# Creating the four different vacuum cleaners, and printing all the related information

VacuumCleaner1 = Cleaner("Dry", 1000, "yes", "rainbow", True, "red")    #obj 1
VacuumCleaner2 = Cleaner("Wet", 300, "no" , "Singer", False, "black")   #obj 2
VacuumCleaner3 = Cleaner("Dry", 600,  "yes", "Beko", True, "gey" )      #obj 3
VacuumCleaner4 = Cleaner("Wet", 1000, "no", "vestel", False, "navy")    #obj 4

# To print the features of each vacuum cleaner I use showCleaner() method...
# Ps.: there are two versions in which I can print all the features from the two classes 
# I prefer using version 1.

#For VC (Vacuum Cleaner) 1:- 
VacuumCleaner1.showCleanerV1() 
#VacuumCleaner1.showCleanerV2()

#For VC (Vacuum Cleaner) 2:- 
VacuumCleaner2.showCleanerV1() 
#VacuumCleaner2.showCleanerV2()

#For VC (Vacuum Cleaner) 3:- 
VacuumCleaner3.showCleanerV1() 
#VacuumCleaner3.showCleanerV2()

#For VC (Vacuum Cleaner) 4:- 
VacuumCleaner4.showCleanerV1() 
#VacuumCleaner4.showCleanerV2()