# A bank account starts with $100.

# Given a list of deposits and withdrawals, return the balance after every transaction.

def bank_account(transactions):

  balance = 100

  result = []
  for amount in transactions:
    balance += amount
    result.append(balance)

  return result

transactions = [20, -10, 15, -5]
print(bank_account(transactions))

# Time complexity : O(n)
# Space complexity: O(n)



