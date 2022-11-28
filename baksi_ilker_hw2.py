from typing import Tuple,Dict,List, Pattern
import re
answerKey : List[str] = []
average: float
studentDictonary: Dict[Tuple[str,str],int] = {}
answerPattern: Pattern[str] = re.compile(r"[a-e]{10}")
answerList: List[str] = []

def main() -> None:
    inputAnswerKey()
    inputAnswer()
    calculateAverage()
    print("Student Dictionary:\r\n",studentDictonary)
    print("Average: %.2f" % average)
    printStudentsAboveAvg()
    searchStudent()

def inputAnswerList(inputPlaceHolder:str) -> List[str]:
    global answerList
    answers = (input(inputPlaceHolder)).lower()
    if re.fullmatch(answerPattern,answers):
        for answer in answers[::]:
            answerList += answer
    else:
        print("Please enter a valid key!")
        answerList = []
        inputAnswerList(inputPlaceHolder)
    return answerList
    
def inputAnswerKey()-> None:
    global answerKey
    answerKey = inputAnswerList("Enter answer key: ")
    
def inputAnswer()->None:
    global studentDictonary,answerList
    choice:str = "Initial value"
    for _ in range(5):
        correctCount: int = 0
        answerList = []
        firstName:str = (input("Enter name: ")).lower()
        lastName:str = (input ("Enter last name: ")).lower()
        name : Tuple[str,str] = (firstName,lastName)
        
        if name in studentDictonary.keys():
            print("The exact name and surname already exists.")
            choice = (input("Write 'yes' to enter answers of the student to overwrite the information .\r\nOtherwise, please write 'no' to be able to enter a new name-surname combination:")).lower()
            while choice.lower() !=  "yes" and choice.lower() != "no":
                choice = input("Please input a valid choice:")
        if choice.lower() == "yes":
            print("Grade is successfully overwritten.")
        while choice.lower() == "no":
            print("You need to enter new name and surname.")
            firstName = (input("Enter name: ")).lower()
            lastName = (input ("Enter last name: ")).lower()
            name = (firstName,lastName)
            if name not in studentDictonary.keys():
                choice = "Invalid value"
        answerList = inputAnswerList("Enter answers: ")
        for x in range(10):
            if (answerList[x] == answerKey[x]):
                correctCount += 1
        studentDictonary[name] = correctCount * 10
def calculateAverage()->None:
    global average
    gradeSum:int = 0
    for key in studentDictonary.keys():
        gradeSum += studentDictonary[key]
    average = gradeSum / len(studentDictonary)
def printStudentsAboveAvg() -> None:
    for key in studentDictonary.keys():
        if studentDictonary[key] > average:
            printableName = key[1][0:1].upper()+ key[1][1:]+ ", " + key[0][0:1].upper() + ". "
            print("Name:  ",printableName,"Score:  ","%.2f" % studentDictonary[key])
def searchStudent() -> None:
    firstNameList : List[str] = []
    lastNameList: List[str] = []
    isValid: bool = False
    indexes: List[int] = []
    studentName = (input("Who are you searching for? ")).lower()
    namesList: List[Tuple[str,str]] =  list(studentDictonary.keys())
    for person in namesList:
        firstNameList.append(person[0])
        lastNameList.append(person[1])
    for person in namesList:
        if studentName in firstNameList:
            if indexes != [i for i, student in enumerate(firstNameList) if student == studentName]:
                isValid = True
                indexes = [i for i, student in enumerate(firstNameList) if student == studentName]
        if studentName in lastNameList:
            if indexes != [i for i, student in enumerate(lastNameList) if student == studentName]:
                isValid = True
                indexes = [i for i, student in enumerate(lastNameList) if student == studentName]
    if not isValid:
        print("Invalid input! Please input a student first name or last name.")
        searchStudent()
    else:
        for index in indexes:
            print(firstNameList[index] , lastNameList[index] , "received" , studentDictonary[(firstNameList[index],lastNameList[index])])

main()

