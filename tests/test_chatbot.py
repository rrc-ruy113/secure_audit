"""
Description: Testing chatbot.py
Author: Ronald Uy
Date: October 24, 2024
Usage:
"""

import unittest
from unittest.mock import patch
from src.chatbot import get_account, get_amount, get_balance, make_deposit, user_selection
from src.chatbot import VALID_TASKS, ACCOUNTS

class TestChatbot(unittest.TestCase):
    
# TEST 1    
    def test_valid_account_number(self):
        with patch("builtins.input") as mock_input:
            '''
            Tests the get_account function to see if a valid account number is entered.
            
            Raises:
                ValueError: Raises an error if input does not match from ACCOUNTS.
            '''
            # Arrange
            'mocks input values that are prompted for the function'      
            mock_input.side_effect = ["123456"]
            expected = 123456
            # Act
            actual = get_account()
        
            # Assert
            self.assertEqual(expected, actual)

# Test 2            
    def test_data_non_numberic(self):
        with patch('builtins.input') as mock_input:
            '''
            Tests the get_account function to verify a ValueError is used when using a non-number input.
            
            Raises:
                ValueError: Account number must be a numberical input.
            '''
            # Arrange
            mock_input.side_effect = ['non_number_data']
            expected = f'{ValueError}: Account Number must be a whole number.'
            
            # Act & Assert
            # Using actual is useful when you need to validate a function’s output. Since we are wanting to test to fail, actual is not needed.
            with self.assertRaises(ValueError) as context:
                get_account()
                self.assertEqual(str(context.exception), 'Expected error message')

# Test 3                
    def test_account_not_exist(self):
        with patch('builtins.input') as mock_input:
            '''
            Tests the get_account function to verify a ValueError is raised when using a numberical input but does not exist in the ACCOUNTS dictionary.
            
            Raises:
                ValueError: Account number does not exist.
            '''
            # Arrange
            mock_input.side_effect = ['112233']
            expected = f'{ValueError}: Account number does not exist'
            
            # Act and Arrange
            with self.assertRaises(ValueError) as context:
                get_account()
                self.assertEqual(str(context.exception), 'Expected error message')

# Test 4                
    def test_get_amount_valid_amount(self):
        with patch('builtins.input') as mock_input:
            '''
            Tests the get_amount function to verify user inputs a valid input. A float is proper input
            
            Raises:
                ValueError is raised if it is not a float or not greater than 0.
            '''
            # Arrange
            # mock input of 500.01 is used for testing
            mock_input.side_effect = [500.01]
            expected = 500.01
            
            # Act
            actual = get_amount()
            
            # Assert
            self.assertEqual(expected, actual)
            
# Test 5            
    def test_get_amount_non_numberic(self):
        with patch('builtins.input') as mock_input:
            '''
            Tests get_amount function to verify if a ValueError is raised when using a non numberic input.
            
            Raises:
                ValueError: Is raised if it does not match correct message.
            '''
            
            # Arrange
            mock_input.side_effect = ['non_number_data']
            expected = f'{ValueError}: Invalid amount. Amount must be numeric'
            
            # Act & Arrange
            with self.assertRaises(ValueError) as context:
                get_amount()
                self.assertEqual(float(context.exception), 'Expected error message')
                
# Test 6                
    def test_get_amount_negative_input(self):
        with patch('builtins.input') as mock_input:
            '''
            Tests the get_amount function to verify if a ValueError is raised when using a number less than 0.
            
            Raises:
                ValueError: message was incorrect
            '''
            
            # Arrange
            mock_input.side_effect = [0]
            expected = f'{ValueError}: Invalid Amount. Please enter a positive number.'
            
            # Act and Arrange
            with self.assertRaises(ValueError) as context:
                get_amount()
                self.assertEqual(float(context.exception), 'Expected error message')
                
# Test 7                
    def test_get_balance_correct_value_returned(self):
        '''
        Tests get_balance function to verify if the correct message is displayed when entering a valid account number.
        
        Raises:
            ValueError: is raised if account does not exist in ACCOUNTS.
        '''
        # Arrange
        account = 123456
        expected = 'Your current balance for account 123456 is $1,000.00'
        
        # Act
        actual = get_balance(account)
        
        # Assert
        self.assertEqual(expected, actual)
        
# Test 8        
    def test_get_balance_account_invalid(self):
        with patch('builtins.input') as mock_input:
            '''
            Tests the get_balance function to verify a ValueError is raised with proper messaging when invalid input is entered.
            
            Raises:
                AssertionError: Account number does not exist
            
            '''
            
            # Arrange
            mock_input.side_effect = [112233]
            expected = f'{ValueError}: Account number does not exist'
            
            # Act and Arrange
            with self.assertRaises(ValueError) as context:
                get_account()
                self.assertRaises(str(context.exception), 'Expected Error Message')

# Test 9
    def test_valid_deposit(self):
        '''
        Tests make_deposit function to verify if the balance updates correctly and message is correct
        
        Raises:
            If message does not match the expected message
        '''
        # Arrange
        # Setup a valid account number to deposit a valid transaction amount
        # We setup a intial value to dictionary as to not impact other tests that update this dictionary
        account = 123456
        amount = 1500.01
        ACCOUNTS[account]['balance'] = 1000
        expected = 'Your current balance for account 123456 is $2,500.01'
        
        # Act
        # make_deposit method is used to update our balance
        make_deposit(account, amount)
        actual = get_balance(account)
        
        # Assert
        self.assertEqual(actual, expected)

# Test 10                
    def test_make_deposit_valid_account_value(self):
        with patch('builtins.input') as mock_input:
            '''
            Tests the make_deposit function to verify if the balance is properly raised with balance and correct message.
            
            Raises:
                AssertionError: If message does not match with expected message.
            '''
            # Arrange
            # A valid account number is to be used
            # A deposit greater than 0 is used.
            # Set up value in this dictionary to not affect other tests in dictionary.
            account = 123456
            amount = 1500.01
            ACCOUNTS[account]['balance'] = 1000.0
            # balance = ACCOUNTS[account]['balance'] + amount
            # expected = f'Account balance of {balance:,.2f}'
            expected = f'You have made a deposit of $1,500.01 to account 123456'
            
            # Act
            # We call account and amount in our make_deposit function.
            actual = make_deposit(account, amount)
            
            # Asset
            # Verify that the message output matches with actual and expected.
            self.assertEqual(expected, actual)
            
# Test 11
    def test_account_does_not_exist(self):
        '''
        Tests make_deposit() function that verifities a ValueError is raised when account does not exist
        
        Raises:
            ValueError: If account does not exist
        '''
        # Arrange
        # Setting up invalid account number with valid transaction amount
        account = 112233
        amount = 1500.01
        expected = 'Account does not exist'
        
        # Act and Assert
        with self.assertRaises(ValueError) as context:
            make_deposit(account, amount)
            self.assertEqual(str(context.exception), expected)
            
# Test 12
    def test_invalid_amount_deposit(self):
        '''
        Writes a test for make_deposit() when an amount is less or equal to zero
        
        Raises:
            ValueError: when amount is less than or equal to zero
        '''
        
        # Arrange
        # Sets up account and transactions amount
        # We expect a return or amount and transaction amount
        account = 123456
        amount = -50.01
        expected = 'Invalid Amount. Amount must be positive'
        
        # Act and Assert
        # Verify value error is raised when a non-positive transaction is used
        # Verify ValueError if account does not exist in the ACCOUNTS dictionary.
        with self.assertRaises(ValueError) as context:
            make_deposit(account, amount)
            self.assertEqual(str(context.exception), expected)
            
# Test 13            
    def test_verifies_user_selection_lowercase(self):
        '''
        Test for user_selection() function that verifies if user inputs uppercase or lowercase selection.
        
        Raises:
            AssertionError: If mock selection is not reutned the same.
        
        '''
        with patch('builtins.input') as mock_input:
            
            # Arrange
            # mock input of balance in lowercase.
            # Result should return the same as it is a valid choice.
            mock_input.side_effect = ['balance']
            expected = 'balance'
            
            # Act
            actual = user_selection()
            
            # Assert
            # Return of the function and expect and verify to be the same
            self.assertEqual(expected, actual)
            
# Test 14            
    def test_verifies_user_uppercase_mixed(self):
        '''
        Tests the user_selection function to verify if an uppercase valid input is to be returned.
        
        Raises:
            AssertionError: If mock input does not reutrn our valid choice regardless of case sensitivity.
        '''
        with patch('builtins.input') as mock_input:
            
            # Arrange
            # We mock input whether uppercase deposit is a valid choice.
            # Our expected should give a valid response regardless of case sensitivity.
            mock_input.side_effect = ['DEPOSIT']
            expected = 'deposit'
            
            # Act
            actual = user_selection()
            
            # Assert
            # We compare expected and actual to be valid.
            self.assertEqual(expected, actual)
            
# Test 15            
    def test_verify_invalid_selection_error(self):
        '''
        Test user_selection function to verify if a ValueError is raised when using an invalid selection.
        '''
        with patch('builtins.input') as mock_input:
            
            # Arrange
            # We mock an input of 'invalid_selection'
            # Expected should return a invalid task. As it is not either deposit, balance, nor exit.
            mock_input.side_effect = ['invalid_selection']
            expected = 'Invalid task. Please choose balance, deposit, or exit.'
            
            # Act and Assert
            with self.assertRaises(ValueError) as context:
                user_selection()
                self.assertEqual(str(context.exception), expected)