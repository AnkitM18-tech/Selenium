import unittest

class Login(unittest.TestCase):
    def test_Login_with_FB(self):
        print("Log In with FaceBook")

    def test_Login_with_Insta(self):
        print("Log In with InstaGram")

    def test_Login_with_GitHub(self):
        print("Log In with GitHub")

if __name__=="__main__":
    unittest.main()