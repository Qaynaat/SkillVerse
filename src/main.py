import customtkinter as ctk
# Sahi class name import karein jo aapne onboarding.py mein rakha hai
from ui.onboarding import SkillVerseApp

ctk.set_appearance_mode("Dark")

# SkillVerseApp ko instantiate karein
app = SkillVerseApp()
app.mainloop()