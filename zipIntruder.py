import zipfile as z

class zipVictim:
    """
    A Class that helps to perform different attacks to a zip file and handle/evaluate the results. Must set a zipfile object when created.

    Paramenters:
        found: A boolean object set to true when the file is cracked or false when the craking process failed. By default set to false.
        password: A string object containing the password string when the file is cracked. By default set to an empty string.
        file: containg the zipfile object referred when the zipVictim object was created.
        extracted_file_list: A list object containing a list of all the files within cracked zip file. By default set to an empty list.

    Methods:
        wordlistAttack: A method that performs a wordlist based attack (see its own __doc__ fot further info).

    Raises:
        See each method __doc__ Raises section.
    """

    def __init__(self,file):
        self.found = False
        self.password = ''
        self.file = file
        self.extracted_file_list = []

    def wordlistAttack(self,wordlist_path,wordlist_separator = '\n',print_mode = False):
        """
        A wordlist based attack.

        Args:
            wordlist_path = String object with wordlist path.
            wordlist_separator = string object with the dictionary separator. By default set to new line (\n).
            print_mode = boolean value that determines if the password tryouts will be printed at the screen (recommended to be used only at the console screen). By default set to false.

        Returns:
            Returns true when the file is cracked, and false on failure.

        Raises:
            Any default python or zipfile error, except RuntimeError when attempeting to crack the file (avoiding Bad Password zipfile module error).
        """

        oFile = self.file
        oDict = open(wordlist_path)
        lList = oDict.read().split(wordlist_separator)

        for iInc in range(len(lList)):
            
            try:
                sPass = lList[iInc]
                
                if print_mode:
                    print("Attempt %s of %s, password: %s" % (iInc,len(lList),sPass),end='\r')
                    
                oFile.extractall(pwd=sPass.encode())
                oDict.close()

                self.extracted_file_list = oFile.namelist()
                self.password = sPass
                self.found = True

                return self.found
                
            except RuntimeError:
                pass

        return self.found
    
if __name__ == '__main__':

    # Wordlist Attack use example
    file = z.ZipFile('data.zip')
    wordlist_path = 'list.txt'

    s = zipVictim(file)
    if s.wordlistAttack(wordlist_path):
        print("Cracked! Password %s" % s.password)
    else:
        print("Failed! Try another wordlist")
        


    
