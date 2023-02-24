from packages.interface.main import Interface

# This is the entry point to the program. 
# The interface class whicg controls the others classes is instantiated here
if __name__ == '__main__':
    user = Interface()
    user.welcome()
