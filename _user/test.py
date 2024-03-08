from user import User
import unittest
import os


# Create a new user
def test_create_user():
    user1 = User(username='slliks23', fullname='Skills Nwokolo', email='skills66@gmail.com', password='test123')
    result1 = user1.create_user()

    print(result1)

# Edit an existing user
def test_edit_user():
    user2 = User(username='slliks4')
    result = user2.edit_user(user_id=3)
    print(result)


# Delete an existing user
def test_delete_user():
    user3 = User()
    result = user3.delete_user(user_id=4)
    print(result)


def test_len_str():
    user = User()
    print(user.__len__())


# Main function to run the tests
if __name__ == "__main__":
    test_create_user()
    # test_edit_user()
    # test_delete_user()
    test_len_str()

# class TestUser(unittest.TestCase):
#
#     def setUp(self):
#         self.user = User(username='testuser', email='test@example.com', password='test')
#
#     def tearDown(self):
#         # Clean up the database file after each test
#         if os.path.exists(User.DATABASE):
#             os.remove(User.DATABASE)
#
#     def test_create_user(self):
#         response = self.user.create_user()
#         self.assertEqual(response['status'], '200')
#         self.assertEqual(response['user']['username'], 'testuser')
#         self.assertEqual(response['user']['email'], 'test@example.com')
#         self.assertEqual(response['user']['password'], 'test')
#
#     def test_edit_user(self):
#         self.user.create_user()  # Create a user for editing
#         response = self.user.edit_user(user_id=1)
#         self.assertEqual(response['status'], '200')
#         self.assertEqual(response['user']['username'], 'testuser')
#         self.assertEqual(response['user']['email'], 'test@example.com')
#         self.assertEqual(response['user']['password'], 'test')
#
#     def test_delete_user(self):
#         self.user.create_user()  # Create a user for deletion
#         response = self.user.delete_user(user_id=1)
#         self.assertEqual(response['status'], '200')
#
#     def test_load_save_users(self):
#         # Check if load and save operations work correctly
#         self.user.create_user()
#         users = self.user.load_users()
#         self.assertEqual(len(users), 1)
#         self.assertEqual(users[0]['username'], 'testuser')
#         self.assertEqual(users[0]['email'], 'test@example.com')
#         self.assertEqual(users[0]['password'], 'test')
#
#         # Edit and delete a user, then check if the database is empty
#         self.user.edit_user(user_id=1)
#         self.user.delete_user(user_id=1)
#         self.assertEqual(len(self.user.load_users()), 0)
#
#
# if __name__ == '__main__':
#     unittest.main()
