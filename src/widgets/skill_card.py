import customtkinter as ctk


class SkillCard(ctk.CTkFrame):

    def __init__(self, master, skill_data, command=None):
        super().__init__(master)

        self.skill_data = skill_data
        self.command = command
        self.configure(
        corner_radius=18,
        border_width=2,
        border_color="#7B2CBF",
        fg_color="#151126",
        cursor="hand2"
)       
        self.configure(
             width=700,
            height=150
)

        self.pack_propagate(False)
        self.icon = ctk.CTkLabel(
    self,
    text=skill_data["icon"],
    font=("Segoe UI Emoji", 36)
)

        self.icon.pack(
    anchor="w",
    padx=20,
    pady=(15, 0)
)
        self.title = ctk.CTkLabel(
    self,
    text=skill_data["name"],
    font=("Poppins", 22, "bold")
)

        self.title.pack(anchor="w", padx=20)
        self.description = ctk.CTkLabel(
    self,
    text=skill_data["description"],
    font=("Poppins", 14),
    justify="left"
)

        self.description.pack(anchor="w", padx=20)
        self.info = ctk.CTkLabel(
    self,
    text=f'{skill_data["difficulty"]}     ⏳ {skill_data["duration"]}',
    font=("Poppins", 13)
)

        self.info.pack(anchor="w", padx=20, pady=(5, 15))