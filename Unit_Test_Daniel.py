import Student
import testData
import unittest

#Unit test for getPercentage based on testData
class TestStudent(unittest.TestCase):
    def test_getPercentage(self):
        #expected outcomes of getPercentage function
        testPercentageValues = [0.8, 1, 0.86, 0.9366666666666666, 0.93, 0.93, 0.97, 0.93]
        assignments = [] #data being used to test expected outcomes
        for assignmentX in testData.ASSIGNMENTS:
            assignments.append(Student.Assignment(**assignmentX)) 
        for i, assignment in enumerate(assignments):
            self.assertEqual(assignment.getPercentage(), testPercentageValues[i])
    def test_Grading(self):
        assignmentsarray = []
        for assignmentX in testData.ASSIGNMENTS:
            assignmentsarray.append(Student.Assignment(**assignmentX))
        testStudentX = Student.Student(name=testData.MATTHEW_POGUE["name"], ID=testData.MATTHEW_POGUE["ID"])
        testStudentX.addAssignment(assignmentsarray)
        self.assertEqual(testStudentX.getGrade(), 0.92416666666666666666666666666667)
        self.assertEqual(testStudentX.getLetterGrade(), "A") 
    def test_Events(self):
        eventsarray = []
        testStudentX = Student.Student(name=testData.MATTHEW_POGUE["name"], ID=testData.MATTHEW_POGUE["ID"])
        for eventX in testData.EVENTS:
            eventsarray.append(Student.Event(**eventX))
        testStudentX.addEvent(eventsarray)
        self.assertEqual(testStudentX.countEvents(), 9)
        self.assertEqual(testStudentX.countEventOfType(eventType="meeting"), 2)       

if __name__ == "__main__":
    unittest.main()