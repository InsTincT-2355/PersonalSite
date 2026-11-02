class Homework:
    def __init__(self, description="", completed=False):
        self.description = description
        self.completed = completed
        
        
        
    def __str__(self):
        completed_str = ""
        if self.completed == True:
            completed_str = "Done ! "
        return self.description + completed_str
    
    
    
class HomeworkList:
    def __init__(self, name):
        self.name = name
        self.__homeworkList = []
        
    def addHomework(self, homework):
        self.__homeworkList.append(homework)
        
    def getHomework(self, number):
        index = number - 1
        homework = self.__homeworkList[index]
        return homework
    
    def removeHomework(self, homework):
        self.__homeworkList.remove(homework)
        
        
    def getCount(self):
        return len(self.__homeworkList)
    
    
    
    def __iter__(self):
        self.__index = -1
        return self
    
    def __next__(self):
        if self.__index >= len(self.__homeworkList) -1:
            raise StopIteration()
        self.__index +=1
        homework = self.__homeworkList[self.__index]
        return homework
    
    def __str__(self):
        homeworkList.str = ""
        for homework in self.__homeworkList:
            homeworkList_str += str(homework) + " | "
        homeworkList_str = homeworkList_str[:-3]
        return homeworkList_str