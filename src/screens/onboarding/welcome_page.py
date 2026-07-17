import customtkinter as ctk

class WelcomePage(ctk.CTkFrame):
    def __init__(self, master, on_next):
        super().__init__(master)
        self.configure(fg_color="#000000")
        self.on_next = on_next
        
        self.center_frame = ctk.CTkFrame(self, fg_color="#000000", width=450)
        self.center_frame.pack(expand=True, fill="y", pady=20)
        
        # 🎮 Progress Tracker: Screen 1 Active
        self.tracker_frame = ctk.CTkFrame(self.center_frame, fg_color="transparent")
        self.tracker_frame.pack(pady=(10, 20))
        
        ctk.CTkLabel(self.tracker_frame, text="🟣 Start", font=("Segoe UI", 13, "bold"), text_color="#B026FF").pack(side="left", padx=10)
        ctk.CTkLabel(self.tracker_frame, text="──────────", font=("Segoe UI", 12), text_color="#222222").pack(side="left")
        ctk.CTkLabel(self.tracker_frame, text="🎯 Discover", font=("Segoe UI", 13), text_color="#444444").pack(side="left", padx=10)
        ctk.CTkLabel(self.tracker_frame, text="──────────", font=("Segoe UI", 12), text_color="#222222").pack(side="left")
        ctk.CTkLabel(self.tracker_frame, text="🏆 Future", font=("Segoe UI", 13), text_color="#444444").pack(side="left", padx=10)

        self.lbl_logo = ctk.CTkLabel(self.center_frame, text="SkillVerse", font=("Segoe UI", 48, "bold"), text_color="#B026FF")
        self.lbl_logo.pack(pady=(10, 2))
        
        # New Tagline
        self.lbl_tagline = ctk.CTkLabel(self.center_frame, text="Discover Yourself. Build Your Future.", font=("Segoe UI", 16, "italic"), text_color="#B026FF")
        self.lbl_tagline.pack(pady=(0, 20))

        ctk.CTkLabel(self.center_frame, text="━━━━━━━━━━━━━━━━━━━━━━━━━━", font=("Segoe UI", 10), text_color="#B026FF").pack(pady=5)

        hook_text = (
            "Choosing a career isn't easy.\n\n"
            "Many students don't know where to start.\n"
            "Some follow pressure. Some follow trends.\n\n"
            "Let's discover what YOU truly enjoy."
        )
        self.lbl_hook = ctk.CTkLabel(self.center_frame, text=hook_text, font=("Segoe UI", 15), text_color="#B026FF", justify="center")
        self.lbl_hook.pack(pady=15)

        ctk.CTkLabel(self.center_frame, text="━━━━━━━━━━━━━━━━━━━━━━━━━━", font=("Segoe UI", 10), text_color="#B026FF") .pack(pady=5)

        # Let's Begin CTA with Glow Effect
        self.btn_begin = ctk.CTkButton(
            self.center_frame, 
            text="Let's Begin →", 
            font=("Segoe UI", 15, "bold"),
            hover_color="#000000",
            fg_color="#000000", 
            border_color="#B026FF",
            border_width=2,
            text_color="#B026FF",
            corner_radius=8,
            width=220,
            height=45,
            command=self.on_next
        )
        self.btn_begin.pack(pady=(25, 10))
        self.btn_begin.bind("<Enter>", lambda e: self.btn_begin.configure(border_color="#D685FF", text_color="#D685FF"))
        self.btn_begin.bind("<Leave>", lambda e: self.btn_begin.configure(border_color="#B026FF", text_color="#B026FF"))