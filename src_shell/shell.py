from myfunction import *
class MyPrompt(Cmd):

    def do_date(self, args):
        """print the local time.
Name                              Category  Synopsis
----                              --------  --------
Get-Date                          Cmdlet    Gets the current date and time.
Set-Date                          Cmdlet    Changes the system time on the computer to a time that you specify.
Update-List                       Cmdlet    Adds items to and removes items from a property value that contains a co...
Update-TypeData                   Cmdlet    Updates the current extended type configuration by reloading the *.types...
Update-FormatData                 Cmdlet    Updates the formatting data in the current session.


"""
        localtime = time.asctime( time.localtime(time.time()) )
        print(localtime)

    def do_exit(self, args):
        """
NAME
    Exit-PSSession

SYNOPSIS
    Ends an interactive session with a remote computer.


SYNTAX
    Exit-PSSession [<CommonParameters>]


DESCRIPTION
    The Exit-PSSession cmdlet ends interactive sessions that you started by using Enter-PSSession.

    You can also use the Exit keyword to end an interactive session. The effect is the same as using Exit-PSSession.

"""
        raise SystemExit
    def do_pwd(self,args):
        """
NAME
    Get-Location

SYNOPSIS
    Gets information about the current working location.


SYNTAX
    Get-Location [-PSDrive <string[]>] [-PSProvider <string[]>] [-UseTransaction] [<CommonParameters>]

    Get-Location [-Stack] [-StackName <string[]>] [-UseTransaction] [<CommonParameters>]


DESCRIPTION
    The Get-Location cmdlet gets an object that represents the current directory, much like the pwd (print working dire
    ctory) command.

    When you move between Windows PowerShell drives, Windows PowerShell retains your location in each drive. You can us
    e Get-Location to find your location in each drive.

    You can also use Get-Location to get the current directory at run time and use it in functions and scripts, such as
     in a function that displays the current directory in the Windows PowerShell prompt.

    If you use the Push-Location cmdlet to add locations to a path stack, you can use the Stack parameter of Get-Locati
    on to display the current stack.

        pwd [OPTION]...

        -L -P -help --version 
        """
        
        print(os.getcwd())
    def do_ls(self,args):
           
        """ NAME
    Get-ChildItem

SYNOPSIS
    Gets the items and child items in one or more specified locations.


SYNTAX
    Get-ChildItem [[-Path] <string[]>] [[-Filter] <string>] [-Exclude <string[]>] [-Force] [-Include <string[]>] [-Name
    ] [-Recurse] [-UseTransaction] [<CommonParameters>]

    Get-ChildItem [-LiteralPath] <string[]> [[-Filter] <string>] [-Exclude <string[]>] [-Force] [-Include <string[]>] [
    -Name] [-Recurse] [-UseTransaction] [<CommonParameters>]


DESCRIPTION
    The Get-ChildItem cmdlet gets the items in one or more specified locations. If the item is a container, it gets the
     items inside the container, known as child items. You can use the Recurse parameter to get items in all child cont
    ainers.

    A location can be a file system location, such as a directory, or a location exposed by another provider, such as a
     registry hive or a certificate store. """
        destdir = os.getcwd()
        files = [ f for f in os.listdir(destdir)]
        for i in files:
            print(i,end=" ")
        print()    
    def do_man(self,args):
        if(args=='ls'):
            print(self.do_ls.__doc__)
        if(args=='pwd'):
            print(self.do_pwd.__doc__)
        if(args=='date'):
            print(self.do_date.__doc__)
        if(args=='exit'):
            print(self.do_exit.__doc__)
        if(args=='kmod'):
            print(self.do_kmod.__doc__)
        if(args=='mkdir'):
            print(self.do_mkdir.__doc__)
        if(args=='rm'):
            print(self.do_rm.__doc__)
    def do_kmod(self,args):
        "it will show how many modules are under help function"
        print(help("modules"))
    def do_mkdir(self,args):
        """
NAME
    New-Item

SYNOPSIS
    Creates a new item.


SYNTAX
    New-Item [-Path] <string[]> [-Credential <PSCredential>] [-Force] [-ItemType <string>] [-Value <Object>] [-Confirm]
     [-WhatIf] [-UseTransaction] [<CommonParameters>]

    New-Item -Name <string> [[-Path] <string[]>] [-Credential <PSCredential>] [-Force] [-ItemType <string>] [-Value <Ob
    ject>] [-Confirm] [-WhatIf] [-UseTransaction] [<CommonParameters>]


DESCRIPTION
    The New-Item cmdlet creates a new item and sets its value. The types of items that can be created depend upon the l
    ocation of the item. For example, in the file system, New-Item is used to create files and folders. In the registry
    , New-Item creates registry keys and entries.

    New-Item can also set the value of the items that it creates. For example, when creating a new file, New-Item can a
    dd initial content to the file."""
        w=os.getcwd()+str("\\")+str(args)
        if not os.path.exists(w):
            os.makedirs(w)
    def do_rm(self,args):
        """
NAME
    Remove-Item

SYNOPSIS
    Deletes the specified items.


SYNTAX
    Remove-Item [-LiteralPath] <string[]> [-Credential <PSCredential>] [-Exclude <string[]>] [-Filter <string>] [-Force
    ] [-Include <string[]>] [-Recurse] [-Confirm] [-WhatIf] [-UseTransaction] [<CommonParameters>]

    Remove-Item [-Path] <string[]> [-Credential <PSCredential>] [-Exclude <string[]>] [-Filter <string>] [-Force] [-Inc
    lude <string[]>] [-Recurse] [-Confirm] [-WhatIf] [-UseTransaction] [<CommonParameters>]


DESCRIPTION
    The Remove-Item cmdlet deletes one or more items. Because it is supported by many providers, it can delete many dif
    ferent types of items, including files, directories, registry keys, variables, aliases, and functions.
"""
        w=os.getcwd()+str("\\")+str(args)
        if not os.path.exists(w):
            os.rmdir(w)
    def do_clear(self,args):
        os.system('cls')
        
if __name__ == '__main__':
    
    prompt = MyPrompt()
    print("")
    print(">BASH/LINUX")
    print(">@admin : Adarsh Kumar")
    print(">@ver:1")
    print("___________________________________________")
    print("")
    prompt.prompt = '$ '
    prompt.cmdloop('')
