import customtkinter as ctk

class UsernamePage(ctk.CTkFrame):
    def __init__(self, master, on_next):
        super().__init__(master)
        self.configure(fg_color="#000000")
        self.on_next = on_next
        
        self.center_frame = ctk.CTkFrame(self, fg_color="#000000", width=450)
        self.center_frame.pack(expand=True, fill="y", pady=20)
        
        # 🎮 Progress Tracker: Screen 2 Active
        self.tracker_frame = ctk.CTkFrame(self.center_frame, fg_color="transparent")
        self.tracker_frame.pack(pady=(10, 40))
        ctk.CTkLabel(self.tracker_frame, text="🟣 Start", font=("Segoe UI", 13), text_color="#B026FF").pack(side="left", padx=10)
        ctk.CTkLabel(self.tracker_frame, text="━━━━━━━━━━", font=("Segoe UI", 12), text_color="#B026FF").pack(side="left")
        ctk.CTkLabel(self.tracker_frame, text="🟣 Discover", font=("Segoe UI", 13, "bold"), text_color="#B026FF").pack(side="left", padx=10)
        ctk.CTkLabel(self.tracker_frame, text="──────────", font=("Segoe UI", 12), text_color="#222222").pack(side="left")
        ctk.CTkLabel(self.tracker_frame, text="🏆 Future", font=("Segoe UI", 13), text_color="#444444").pack(side="left", padx=10)

        self.lbl_sub = ctk.CTkLabel(self.center_frame, text="Before we meet your AI companion...", font=("Segoe UI", 16), text_color="#B026FF")
        self.lbl_sub.pack()
        
        # Personalized Question
        self.lbl_main = ctk.CTkLabel(self.center_frame, text="What should Byte call you?", font=("Segoe UI", 26, "bold"), text_color="#B026FF")
        self.lbl_main.pack(pady=(10, 30))

        self.entry = ctk.CTkEntry(
            self.center_frame, 
            placeholder_text="Enter your name...",
            placeholder_text_color="#441166",
            font=("Segoe UI", 16),
            fg_color="#000000", 
            border_color="#B026FF", 
            text_color="#B026FF",
            border_width=2,
            corner_radius=8,
            width=280,
            height=45,
            justify="center"
        )
        self.entry.pack(pady=20)
        
        self.btn_next = ctk.CTkButton(
            self.center_frame, 
            text="Continue →", 
            font=("Segoe UI", 15, "bold"),
            hover_color="#000000",
            fg_color="#000000", 
            border_color="#B026FF", 
            border_width=2, 
            text_color="#B026FF",
            corner_radius=8,
            width=220,
            height=45,
            command=self.submit
        )
        self.btn_next.pack(pady=(15, 0))
        self.btn_next.bind("<Enter>", lambda e: self.btn_next.configure(border_color="#D685FF", text_color="#D685FF"))
        self.btn_next.bind("<Leave>", lambda e: self.btn_next.configure(border_color="#B026FF", text_color="#B026FF"))

    def submit(self):
        username = self.entry.get().strip()
        if username:
            self.on_next(username)