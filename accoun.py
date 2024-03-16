from MyPackage import account
from MyPackage.account import Account


def main():
    A = Account (" 3564758 " , 30)
    print(A.deposit(500))
    print(A.withdraw(300))
    print(A.display())
main()