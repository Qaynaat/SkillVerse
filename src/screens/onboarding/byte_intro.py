import customtkinter as ctk
from core.career_database import CareerDatabase



class ByteIntroPage(ctk.CTkFrame):
    def __init__(self, master, username, on_next):
        super().__init__(master)
        self.configure(fg_color="#000000")
        self.on_next = on_next
        
        self.center_frame = ctk.CTkFrame(self, fg_color="#000000", width=450)
        self.center_frame.pack(expand=True, fill="y", pady=20)
        
        # 🎮 Progress Tracker: Full Active Path Achieved
        self.tracker_frame = ctk.CTkFrame(self.center_frame, fg_color="transparent")
        self.tracker_frame.pack(pady=(10, 30))
        ctk.CTkLabel(self.tracker_frame, text="🟣 Start", font=("Segoe UI", 13), text_color="#B026FF").pack(side="left", padx=10)
        ctk.CTkLabel(self.tracker_frame, text="━━━━━━━━━━", font=("Segoe UI", 12), text_color="#B026FF").pack(side="left")
        ctk.CTkLabel(self.tracker_frame, text="🟣 Discover", font=("Segoe UI", 13), text_color="#B026FF").pack(side="left", padx=10)
        ctk.CTkLabel(self.tracker_frame, text="━━━━━━━━━━", font=("Segoe UI", 12), text_color="#B026FF").pack(side="left")
        ctk.CTkLabel(self.tracker_frame, text="🟣 Future", font=("Segoe UI", 13, "bold"), text_color="#B026FF").pack(side="left", padx=10)

        self.lbl_bot = ctk.CTkLabel(self.center_frame, text="🤖", font=("Segoe UI", 64), text_color="#B026FF")
        self.lbl_bot.pack(pady=(10, 15))

        self.lbl_greet = ctk.CTkLabel(self.center_frame, text=f"Hi {username}!", font=("Segoe UI", 26, "bold"), text_color="#B026FF")
        self.lbl_greet.pack()
        
        self.lbl_identity = ctk.CTkLabel(self.center_frame, text="I'm Byte, your AI companion.", font=("Segoe UI", 16, "italic"), text_color="#B026FF")
        self.lbl_identity.pack(pady=(5, 20))

        intro_text = (
            "I won't tell you what to become.\n\n"
            "I'm here to help you unpack your strengths\n"
            "and map a journey you actually care about."
        )
        self.lbl_dialog = ctk.CTkLabel(self.center_frame, text=intro_text, font=("Segoe UI", 15), text_color="#B026FF", justify="center")
        self.lbl_dialog.pack(pady=15)

        # Anti-school UX Action Text Update
        self.btn_quiz = ctk.CTkButton(
            self.center_frame, 
            text="Begin Your Journey →", 
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
        self.btn_quiz.pack(pady=(25, 10))
        self.btn_quiz.bind("<Enter>", lambda e: self.btn_quiz.configure(border_color="#D685FF", text_color="#D685FF"))
        self.btn_quiz.bind("<Leave>", lambda e: self.btn_quiz.configure(border_color="#B026FF", text_color="#B026FF"))