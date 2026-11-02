
# calls website list as in UML diagram
class WebsiteList:
    def __init__(self):
        self.website = []  # list to store website

    def add_website(self, website):
        self.website.append(website)  # ,ethod to add website

    def get_website(self):
        return self.website   # method to get list of website

    def remove_website(self, website):
        self.website.remove(website)   # method to remove particular website

    def get_count(self):
        return len(self.website)  # method to get number of website stored in the list

class Website(WebsiteList):   # class website which is inheriting website list
    def __init__(self, name, url):
        super().__init__()
        self.name = name
        self.url = url

    def get_name(self):  # method to get name of website
        return self.name

    def get_url(self):  # method to get url of website
        
        return self.url
