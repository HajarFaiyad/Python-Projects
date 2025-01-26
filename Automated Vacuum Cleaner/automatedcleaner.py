import random

class AutomatedVacuumCleaner:
    #vacLoc: vacuum cleaner's location
    #aState: location A's state
    #bState: location A's state

    def __init__(self, vacLoc ,aState, bState):
        self.vacLoc = vacLoc
        self.aState = aState
        self.bState = bState

    def randomGenState(self):
        r = random.SystemRandom()
        vacLoc = random.choice(["A","B"])
        aState = random.randint(0,1)
        bState = random.randint(0,1)
        return self.aState, self.bState, self.vacLoc

    def run(self):
        vacLoc = self.vacLoc
        aState = self.aState
        bState = self.bState
# all cases:
# start at location A (clean:0): go to B check state if (clean:0): print "finish" and exit; if (dirty:1): clean and print "finish" and exit
# start at location A (dirty:1): clean and go to B check state if (clean:0): print "finish" and exit; if (dirty:1): clean and print "finish" and exit
# start at location B (clean:0): go to A check state if (clean:0): print "finish" and exit; if (dirty:1): clean and print "finish" and exit
# start at location B (dirty:1): clean and go to B check state if (clean:0): print "finish" and exit; if (dirty:1): clean and print "finish" and exit

        while True: 
            #location A and state is clean --> go right to location B
            if vacLoc == "A" and aState == 0:
                vacLoc == "B"
                print("I am at ", vacLoc)
                print("A is " , aState)
                print("B is " , bState)
                #check if B (clean:0): print "All clean" and exit
                if bState == 0:
                    print("I am at ", vacLoc)
                    print("A is " , aState)
                    print("B is " , bState)
                    print("All clean, going to sleep!")
                    break
                #if B is (dirty:1): clean and print "All clean" and exit
                elif bState == 1:
                    bState = "Clean"
                    print("I am at ", vacLoc)
                    print("A is " , aState)
                    print("B is " , bState)
                    print("All clean, going to sleep!")
                    break

            #location A and state is dirty --> clean and go right to location B
            elif vacLoc == "A" and aState == 1:
                aState = "Clean"
                vacLoc = "B"
                print("I am at ", vacLoc)
                print("A is " , aState)
                print("B is " , bState)
                #check if B (clean:0): print "All clean" and exit
                if bState == 0:
                    print("I am at ", vacLoc)
                    print("A is " , aState)
                    print("B is " , bState)
                    print("All clean, going to sleep!")
                    break
                #if B is (dirty:1): clean and print "All clean" and exit
                elif bState == 1:
                    bState = "Clean"
                    print("I am at ", vacLoc)
                    print("A is " , aState)
                    print("B is " , bState)
                    print("All clean, going to sleep!")
                    break

            #location B and state is clean --> go left to location A
            elif vacLoc == "B" and aState == 0:
                vacLoc == "A"
                print("I am at ", vacLoc)
                print("A is " , aState)
                print("B is " , bState)
                #check if A (clean:0): print "All clean" and exit
                if aState == 0:
                    print("I am at ", vacLoc)
                    print("A is " , aState)
                    print("B is " , bState)
                    print("All clean, going to sleep!")
                    break
                #if A is (dirty:1): clean and print "All clean" and exit
                elif aState == 1:
                    aState = "Clean"
                    print("I am at ", vacLoc)
                    print("A is " , aState)
                    print("B is " , bState)
                    print("All clean, going to sleep!")
                    break

            #location B and state is dirty --> clean and go left to location A
            elif vacLoc == "B" and aState == 1:
                bState = "Clean"
                vacLoc = "A"
                print("I am at ", vacLoc)
                print("A is " , aState)
                print("B is " , bState)
                #check if A (clean:0): print "All clean" and exit
                if aState == 0:
                    print("I am at ", vacLoc)
                    print("A is " , aState)
                    print("B is " , bState)
                    print("All clean, going to sleep!")
                    break
                #if A is (dirty:1): clean and print "All clean" and exit
                elif aState == 1:
                    aState = "Clean"
                    print("I am at ", vacLoc)
                    print("A is " , aState)
                    print("B is " , bState)
                    print("All clean, going to sleep!")
                    break

myVacuum = AutomatedVacuumCleaner() 
myVacuum.run() 
print(myVacuum.randomGenState())
