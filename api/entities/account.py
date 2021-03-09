class Account:
    def __init__(self, name, description, balance, user):
        self.__name = name
        self.__description = description
        self.__balance = balance
        self.__user = user

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
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, balance):
        self.__balance = balance

    @property
    def user(self):
        return self.__user

    @user.setter
    def user(self, user):
        self.__user = user