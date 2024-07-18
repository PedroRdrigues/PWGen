from tkinter import Tk
from tkinter import *


root = Tk()

# Classe de funções
class Funcs:
    # Função para puxar os valores de cada CheckBox.
    def getOptions(self):
        import string
        
        Num = self.iNum.get()
        UppercaseLetters = self.iUppercaseLetters.get()
        LowercaseLetters = self.iLowercaseLetters.get()
        Special = self.iSpecial.get()
        
        
        self.listChars = []
        if Num:
            self.listChars.append(string.digits)

        if UppercaseLetters:
            self.listChars.append(string.ascii_uppercase)

        if LowercaseLetters:
            self.listChars.append(string.ascii_lowercase)

        if Special:
            self.listChars.append(string.punctuation)

        self.createPassword()

    # Função para criar uma senha aleatória baseada nas opções selecionadas.
    def createPassword(self):
        from random import choice
        import pyperclip as pc

        self.clearLabel()
        try:
            pwList = []
            numChars = int(self.entryNumChars.get())

            if 6 <= numChars <= 16:
                for _ in range(numChars):
                    pwList.append(choice("".join(self.listChars)))
                
                password = "".join(pwList)
                response = f'sua senha: {password}'
                
                self.btClipboard = Button(self.frame1, text='Copiar Senha',
                                            command=pc.copy(password))
                self.btClipboard.place(relx=0.39, rely=0.85)
                
            else:
                response = 'O número de caracteres dever ser entre 6 e 16.'
            
        except Exception as err:
            response = 'não é possivel criar uma senha sem caracteres.'
            
            print(err)
        finally:
            self.lbReturn = Label(self.frame1,text=response,
                                    bg='#56a5fa')
            self.lbReturn.place(relx=0.02,rely=0.70)

    # Função para excluir a Label de retorno e o botão de cpipiar para a área de transferencia caso ela já exista.
    def clearLabel(self):
        try:
            self.lbReturn.destroy()
            self.btClipboard.destroy()
            
        except Exception as err:
            print(err)

# Classe principal que herda da classe de funções.
class App(Funcs):
    def __init__(self) -> None:
        self.root = root
        self.configMain()
        self.frames()
        self.widgets()
        self.root.mainloop()

    def configMain(self):
        self.root.title('PWGen')
        self.root.configure(background='#56a5fa')
        self.root.geometry("400x250")
        self.root.resizable(False,False)
    
    def frames(self):
        self.frame1 = Frame(
        self.root, bg='#56a5fa'
    )
        self.frame1.place(relx=0.02, rely=0.02, relwidth=0.96, relheight=0.96)


    def widgets(self):
        # label da seleção de caracteres
        self.lbOpcoesSenhas = Label(
            self.frame1,
            text='Selecione os caracteres que seram usados na sua senha:',
            bg='#56a5fa'
        )
        self.lbOpcoesSenhas.place(relx=0.02, rely=0.02)

        # CheckBox para cada tipo de caractere.
        self.iNum = IntVar() # CheckBox para Números
        self.numbers = Checkbutton(self.frame1, text = "Números",
                                variable=self.iNum, bg='#56a5fa')
        self.numbers.place(relx=0.02, rely=0.11)

        self.iUppercaseLetters = IntVar() # CheckBox para Letras maiúsculas
        self.UppercaseLetters = Checkbutton(self.frame1, text = "Letras Maiúsculas",
                                variable=self.iUppercaseLetters, bg='#56a5fa')
        self.UppercaseLetters.place(relx=0.5, rely=0.11)

        self.iLowercaseLetters = IntVar() # CheckBox para Letras minúsculas
        self.LowercaseLetters = Checkbutton(self.frame1, text = "Letras Minúsculas",
                                variable=self.iLowercaseLetters, bg='#56a5fa')
        self.LowercaseLetters.place(relx=0.5, rely=0.21)

        self.iSpecial = IntVar() # CheckBox para caracteres especiais
        self.specialCharacters = Checkbutton(self.frame1, text = "Carecteres especiais",
                                            variable=self.iSpecial, bg='#56a5fa')
        self.specialCharacters.place(relx=0.02, rely=0.21)

        # Label e entry da quantidade de caracteres por senha.
        self.lbNumChars = Label(self.frame1, text='Quantidade de cara caracteres: ', bg='#56a5fa')
        self.lbNumChars.place(relx=0.02,rely=0.35)

        self.entryNumChars = Entry(self.frame1)
        self.entryNumChars.place(relx=0.47,rely=0.359, width=35)
        
        # Botão para chamar as funções para gerar a senha.
        self.btCreate = Button(self.frame1, text='Gerar Senha', command=self.getOptions)
        self.btCreate.place(relx=0.39, rely=0.50)

App()

