class Transaction:
    def __init__(self, name, description, value_transaction, type_transaction, account):
        self.__name = name
        self.__description = description
        self.__value_transaction = value_transaction
        self.__type_transaction = type_transaction
        self.__account = account

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def description(self):
        return self.__description

    @description.setter
    def description(self, description):
        self.__description = description

    @property
    def value_transaction(self):
        return self.__value_transaction

    @value_transaction.setter
    def value_transaction(self, value_transaction):
        self.__value_transaction = value_transaction

    @property
    def type_transaction(self):
        return self.__type_transaction

    @type_transaction.setter
    def type_transaction(self, type_transaction):
        self.__type_transaction = type_transaction

    @property
    def account(self):
        return self.__account

    @account.setter
    def account(self, account):
        self.__account = account





