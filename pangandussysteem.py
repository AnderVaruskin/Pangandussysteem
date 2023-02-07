# Vanemklass (Pärandaja klass)
class User():  # Kasutaja klass, millesse peab sisestama kõik vajalikud andmed
    def __init__(self, name, age, gender):  # Meetod __init__ kasutab kolme argumenti: nimi, vanus ja sugu
        self.name = name
        self.age = age
        self.gender = gender

    def show_details(self):  # Funktsioon näitamaks kasutaja detaile
        # Kuvab kasutajale tema andmed
        print("Personal Details")
        print("")
        print("Name ", self.name)
        print("Age ", self.age)
        print("Gender ", self.gender)


# Tütarklass (Pärandav klass)
class Bank(User):  # Võtab kasutajaklassi meetodi (__init__)
    def __init__(self, name, age, gender):
        super().__init__(name, age, gender)  # Funktsioon super lähtestab panga eksemplari
        self.balance = 0  # Määrab uue konto arve algseks väärtuseks 0

    def deposit(self, amount):  # Vajab kahte argumenti self ning amount(summa), tähistab kontole pandud summat
        self.amount = amount
        self.balance = self.balance + self.amount
        print("Account balance has been updated: €",
              self.balance)  # Näitab peale sisestamist, et kontojääk on sisestatud ning uut kontojääki

    def withdraw(self, amount):  # Funktsioon mis väljastab kasutajale valitud summa
        self.amount = amount
        if self.amount > self.balance:  # Juhul kui kontosumma on väiksem kui väljavõetav summa prindib see veateate ning kontojäägi
            print("Insufficient Funds | Balance Available: €", self.balance)
        else:
            self.balance = self.balance - self.amount  # Eemaldab kontojäägist väljavõetava summa
            print("Account balance has been updated: €",
                  self.balance)  # Näitab, et raha on väljastatud ja uut kontojääki

    def view_balance(self):  # Näitab kasutajale kontosummat
        self.show_details()
        print("Account Balance: €", self.balance)  # Prindib kontosumma

# Johan = User(Johan, 21,Male) #Tekitab kasutaja Johan


# Johan.show_details() #Näitab tehtud kasutaja detaile

# Johan = Bank(Johan, 20,Male) #Tekitab pangakonto

# Johan.name #Otsib nime "Johan"

# Johan.age #Otsib kasutaja Johan nime

# Johan.gender #Otsib Johan'i sugu

# Johan.deposit(100) #Lisab Johan'i kontole raha

# Johan.withdraw (75) #Eemaldab Johan'i kontolt raha

# Johan.view_balance() #Näitab johani kontojääki

# Johan.show_details() #Näitab johani konto detaile
