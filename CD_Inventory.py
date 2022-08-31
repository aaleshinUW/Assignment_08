#------------------------------------------#
# Title: CD_Inventory.py
# Desc: Assignnment 08 - Working with classes
# Change Log: (Who, When, What)
# DBiesinger, 2030-Jan-01, created file
# DBiesinger, 2030-Jan-01, added pseudocode to complete assignment 08
# aaleshin, 2022-Aug-30, Modified File; Replaced Pseudocode with Code.
#------------------------------------------#

# -- DATA -- #
strFileName = 'cdInventory.txt'
lstOfCDObjects = []

class CD:
    """Stores data about a CD:

    properties:
        cd_id: (int) with CD ID
        cd_title: (string) with the title of the CD
        cd_artist: (string) with the artist of the CD
    methods:

    """
    # TODone Add Code to the CD 
    # -- Fields -- #
    # -- Constructor -- #
    def __init__(self, ID, title, artist):
        """Constructor for the CD class"""
        # -- Attributes -- #
        self.__cd_id = ID
        self.__cd_title = title
        self.__cd_artist = artist
    
    @property    
    def cd_id(self):
        """Getter for CD ID"""
        return self.__cd_id
    
    @property
    def cd_title(self):
        """Getter for CD Title"""
        return self.__cd_title
    
    @property
    def cd_artist(self):
        """Getter for CD Artist"""
        return self.__cd_artist    
    
    @cd_id.setter
    def cd_id(self, value):
        """Setter for CD ID"""
        if str(value).isnumeric():
            self.__cd_id = value
        else:
            raise Exception('The ID has to be an Integer!')
                
    @cd_title.setter
    def cd_title(self, value):
        """Setter for CD Title"""
        if str(value).isnumeric():
            raise Exception('The Title has to be a String!') 
        else:
            self.__cd_title = value
    
    @cd_artist.setter
    def cd_artist(self, value):
        """Setter for CD Artist"""
        if str(value).isnumeric():
            raise Exception('The Artist has to be a String!') 
        else:
            self.__cd_artist = value

    # -- Methods -- #

# -- PROCESSING -- #
class FileIO:
    """Processes data to and from file:

    properties:

    methods:
        save_inventory(file_name, lst_Inventory): -> None
        load_inventory(file_name): -> (a list of CD objects)

    """
    # -- Fields -- #
    # -- Constructor -- #
        # -- Attributes -- #
    # -- Methods -- #
    # TODone Add code to process data from a file
    @staticmethod
    def load_inventory(file_name):
        """Loads the inventory from file
        
        Args:
            file_name: (string) The name of the file to be opened
            
        Returns:
            None
        """
        lstOfCDObjects.clear()
        try:
            with open(file_name) as f:
                lines = f.readlines()
            for line in lines:
                cd = CD(0, '', '')
                data = line.strip().split(',')
                cd.cd_id = int(data[0])
                cd.cd_title = data[1]
                cd.cd_artist = data[2]
                lstOfCDObjects.append(cd)
        except FileNotFoundError:
            print('Text file does not exist!')
        except EOFError:
            print('The file is empty!')            
    # TODone Add code to process data to a file
    @staticmethod
    def save_inventory(file_name, lst_Inventory):
        """Saves the inventory to file
        
        Args:
            file_name: (string) The name of the file to be opened
            lst_Inventory: (list) The list containing the CD objects
            
        Returns:
            None
        """
        try:
            with open(file_name, 'w') as f:
                for cd in lst_Inventory:
                    f.write(str(cd.cd_id) + ',' + cd.cd_title + ',' + cd.cd_artist + '\n')
        except Exception:
            print('There was a general error!')
      # -- PRESENTATION (Input/Output) -- #
class IO:

    """Handling Input / Output"""

    @staticmethod
    def print_menu():
        """Displays a menu of choices to the user

        Args:
            None.

        Returns:
            None.
        """

        print('Menu\n\n[l] load Inventory from file\n[a] Add CD\n[i] Display Current Inventory')
        print('[s] Save Inventory to file\n[x] exit\n')

    @staticmethod
    def menu_choice():
        """Gets user input for menu selection

        Args:
            None.

        Returns:
            choice (string): a lower case sting of the users input out of the choices l, a, i, s or x

        """
        choice = ' '
        while choice not in ['l', 'a', 'i', 's', 'x']:
            choice = input('Which operation would you like to perform? [l, a, i, s or x]: ').lower().strip()
        print()  # Add extra space for layout
        return choice

    @staticmethod
    def show_inventory(lstInventory):
        """Displays current inventory table


        Args:
            lstInventory (list of strings) that holds the data during runtime.

        Returns:
            None.

        """
        print('======= The Current Inventory: =======')
        print('ID\tCD Title (by: Artist)\n')
        for row in lstInventory:
            print('{}\t{} (by:{})'.format(str(row.cd_id), row.cd_title, row.cd_artist))
        print('======================================')

    @staticmethod
    def get_CD():
        """Gets user input for CD ID, Title and Artist.
        
        Args:
            None.
            
        Returns:
            Returns the CD ID as a string.
            Returns the CD Title as a string.
            Returns the CD Artist as as string.
        """
        try:
            ID = input('Enter ID: ').strip()
        except ValueError:
            print('ID is not an integer!')                 
        Title = input('What is the CD\'s title? ').strip()
        Artist = input('What is the Artist\'s name? ').strip()

        return ID, Title, Artist

# -- Main Body of Script -- #
# TODone Add Code to the main body
# Load data from file into a list of CD objects on script start

try:
    FileIO.load_inventory(strFileName)
except FileNotFoundError:
    print('Text file does not exist!')
except EOFError:
    print('The file is empty!')

while True:
    # Display menu to user
    IO.print_menu()
    strChoice = IO.menu_choice()
    # let user exit program   
    if strChoice == 'x':
        break
    # show user current inventory
    elif strChoice == 'i':
        IO.show_inventory(lstOfCDObjects)
        continue  # start loop back at top.    
    # let user add data to the inventory
    elif strChoice == 'a':
        # 3.3.1 Ask user for new ID, CD Title and Artist
        strID, strTitle, strArtist = IO.get_CD()
        # 3.3.2 Add item to the table
        cd = CD(0, '', '')
        cd.cd_id = int(strID)
        cd.cd_title = strTitle
        cd.cd_artist = strArtist
        lstOfCDObjects.append(cd)
        continue  # start loop back at top.
    # let user save inventory to file
    elif strChoice == 's':
        # 3.6.1 Display current inventory and ask user for confirmation to save
        IO.show_inventory(lstOfCDObjects)
        strYesNo = input('Save this inventory to file? [y/n] ').strip().lower()
        # 3.6.2 Process choice
        if strYesNo == 'y':
            # 3.6.2.1 save data
            FileIO.save_inventory(strFileName, lstOfCDObjects)
        else:
            input('The inventory was NOT saved to file. Press [ENTER] to return to the menu.')
        continue  # start loop back at top.    
    # let user load inventory from file
    elif strChoice == 'l':
        print('WARNING: If you continue, all unsaved data will be lost and the Inventory re-loaded from file.')
        strYesNo = input('type \'yes\' to continue and reload from file. otherwise reload will be canceled ')
        if strYesNo.lower() == 'yes':
            print('reloading...')
            FileIO.load_inventory(strFileName)
            IO.show_inventory(lstOfCDObjects)
        else:
            input('canceling... Inventory data NOT reloaded. Press [ENTER] to continue to the menu.')
            IO.show_inventory(lstOfCDObjects)
        continue  # start loop back at top.
    else:
        print('General Error')