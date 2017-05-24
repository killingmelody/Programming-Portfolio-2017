import getpass

class PoemGenerator:

    def getWords(self):
        n1 = input("Enter a noun: ")
        adj1 = input("Enter an adjective: ")
        v1 = input("Enter a verb ending in 'ing': ")
        n2 = input("Enter another noun: ")
        adj2 = input("Enter another adjective: ")
        v2 = input("Enter another verb ending in 'ing': ")
        self.n1 = n1 + " "
        self.adj1 = adj1 + " "
        self.v1 = v1 + " "
        self.n2 = n2 + " "
        self.adj2 = adj2 + " "
        self.v2 = v2 + " "
        self.wordList = [n1,adj1,v1,n2,adj2,v2]

    def title(self):
        title = input("Now, title your masterpiece!\n: ")
        name = getpass.getuser()
        self.title = title + " by " + name
        
