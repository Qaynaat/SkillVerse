import customtkinter as ctk
from screens.onboarding.welcome_page import WelcomePage
from screens.onboarding.username_page import UsernamePage
from screens.onboarding.byte_intro import ByteIntroPage

class SkillVerseApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("SkillVerse")
        self.geometry("600x700")
        self.configure(fg_color="#000000")
        
        # Pehli screen load karein
        self.show_welcome()

    def clear_screen(self):
        # Purani screen ko delete karne ke liye
        for widget in self.winfo_children():
            widget.destroy()

    def show_welcome(self):
        self.clear_screen()
        # Next screen par jaane ke liye callback pass kar rahe hain
        page = WelcomePage(self, on_next=self.show_username)
        page.pack(fill="both", expand=True)

    def show_username(self):
        self.clear_screen()
        page = UsernamePage(self, on_next=self.show_byte_intro)
        page.pack(fill="both", expand=True)

    def show_byte_intro(self, username):
        self.clear_screen()
        page = ByteIntroPage(self, username=username, on_next=self.finish_onboarding)
        page.pack(fill="both", expand=True)

    def finish_onboarding(self):
        print("Onboarding Khatam! Ab dashboard khulega.")
        self.destroy()

if __name__ == "__main__":
    app = SkillVerseApp()
    app.mainloop()