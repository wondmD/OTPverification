from twilio.rest import Client
import random
from tkinter import *
from tkinter import messagebox
import config
  
class otp_verifier(Tk):
    def __init__(self):
        super().__init__()
        self.geometry("600x600")
        self.resizable(False, False)
        self.n = random.randint(100000,999999)
        self.client = Client(config.ACCOUNT_SID, config.AUTH_TOKEN)
        self.client.messages.create(to="", from_="", body=str(self.n))

    def Labels(self):
        self.c = Canvas(self, bg="white", width=400, height=280)
        self.c.place(x=100,y=90)

        self.Login_Title = Label(self, text="OTP Verification",  font="bold, 20", bg="white")
        self.Login_Title.place(x=210,y=90)
    def Entry(self):
        self.User_name=Text(self, borderwidth=2, wrap="word", width=29, height=2)
        self.User_name.place(x=190, y=160)
    def Buttons(self):
        self.submitButtonImage=PhotoImage(file="submit.png")
        self.submitButton=Button(self,image=self.submitButtonImage,command=self.checkOTP, border=0)
        self.submitButton.place(x=208, y=400)

        self.resendOTPImage = PhotoImage("resend.png")
        self.resendOTP = Button(self, image=self.resendOTPImage,command=self.resendOTP, border=0)
        self.resendOTP.place(x=208,y=400)
    def resendOTP(self):
        self.n = random.randint(100000,999999)
        self.client=Client(config.ACCOUNT_SID, config.AUTH_TOKEN)
        self.client.messages.create(to="", from_="", body=str(self.n))
    def checkOTP(self):
        try :
            self.userInput = int(self.User_name.get(1.0, "end-1c"))
            if self.userInput==self.n:
                messagebox.showinfo("showinfo", "Login Succuss")
                self.n="done"
            elif self.n =="done":
                messagebox.showinfo("showinfo", "already verified")
            else :
                messagebox.showinfo("showinfo", "wrong OTP")
        except :
            messagebox.showinfo("showinfo", "invalid OTP")
 


if __name__=="__main__":
    window = otp_verifier()
    window.Labels()
    window.Entry()
    window.Buttons()
    window.mainloop()
           
