import unittest
from package1.login import Login 
from package1.signup import SignUp
from package2.payment1 import Payment
from package2.payment2 import UPI_Payment

#Tests are loaded
test1=unittest.TestLoader().loadTestsFromTestCase(Login)
test2=unittest.TestLoader().loadTestsFromTestCase(SignUp)
test3=unittest.TestLoader().loadTestsFromTestCase(Payment)
test4=unittest.TestLoader().loadTestsFromTestCase(UPI_Payment)

#If we don't want to run every tests then,we need to make test suits.
#Test Suit
sanityTestsuit=unittest.TestSuite([test1,test4])
unittest.TextTestRunner().run(sanityTestsuit) #Running the Test Suit