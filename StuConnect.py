import tkinter as tk
from tkinter import ttk

# ── Fenster erstellen ──────────────────────────────────────────
window = tk.Tk()
window.title("StuConnect")
window.geometry("390x780")
window.resizable(False, False)
window.configure(bg="#FFFFFF")

# ── Farben ─────────────────────────────────────────────────────
LILA      = "#5B4FCF"
WEISS     = "#FFFFFF"
GRAU_BG   = "#F0F0F0"
GRAU_TEXT = "#666666"
SCHWARZ   = "#1A1A1A"

# ══════════════════════════════════════════════════════════════
# NAVIGATION
# ══════════════════════════════════════════════════════════════
def zeige(aktuell, naechster):
    aktuell.pack_forget()
    naechster.pack(fill="both", expand=True)

def von1_zu2():
    zeige(frame1, frame2)

def von2_zu1():
    zeige(frame2, frame1)

def von2_zu3():
    zeige(frame2, frame3)

def von3_zu2():
    zeige(frame3, frame2)

def von3_zu4():
    zeige(frame3, frame4)

def von4_zu3():
    zeige(frame4, frame3)

def von4_zu5():
    zeige(frame4, frame5)

def von5_zu4():
    zeige(frame5, frame4)

def von5_zu6():
    zeige(frame5, frame6)

def von6_zu5():
    zeige(frame6, frame5)

def von6_zu6b():
    zeige(frame6, frame6b)

def von6b_zu6():
    zeige(frame6b, frame6)

def von6b_zu7():
    zeige(frame6b, frame7)

# ══════════════════════════════════════════════════════════════
# HILFSFUNKTION: Fortschritts-Punkte
# ══════════════════════════════════════════════════════════════
def erstelle_kopf(eltern, aktiver_dot, zurueck_funktion):
    kopf = tk.Frame(eltern, bg=WEISS)
    kopf.pack(fill="x", padx=20, pady=(50, 0))
    tk.Button(kopf, text="←", command=zurueck_funktion, bg=WEISS, fg=SCHWARZ,
              font=("Helvetica", 18), relief="flat", bd=0, cursor="hand2").pack(side="left")
    dots = tk.Frame(kopf, bg=WEISS)
    dots.pack(side="left", padx=(70, 0))
    for i in range(4):
        farbe = LILA if i == aktiver_dot else GRAU_BG
        tk.Label(dots, bg=farbe, width=3 if i == aktiver_dot else 1, height=1).pack(side="left", padx=3, ipady=3)

# ══════════════════════════════════════════════════════════════
# FRAME 1 – Willkommen
# ══════════════════════════════════════════════════════════════
frame1 = tk.Frame(window, bg=WEISS)
frame1.pack(fill="both", expand=True)

logo_frame = tk.Frame(frame1, bg=WEISS, height=160)
logo_frame.pack(fill="x")
logo_frame.pack_propagate(False)
tk.Frame(logo_frame, bg=WEISS, height=40).pack()
ttk.Label(logo_frame, text="🎓", font=("Helvetica", 52), background=WEISS, foreground=LILA).pack()
ttk.Label(logo_frame, text="StuConnect", font=("Helvetica", 24, "bold"), background=WEISS, foreground=LILA).pack()

inhalt = tk.Frame(frame1, bg=WEISS)
inhalt.pack(fill="x", padx=30, pady=(20, 0))
ttk.Label(inhalt, text="Nachhilfe von Studierenden\nfür Studierende.", font=("Helvetica", 16, "bold"),
          background=WEISS, foreground=SCHWARZ, justify="center").pack(pady=(0, 6))

tk.Button(frame1, text="Mit Uni-E-Mail anmelden", command=von1_zu2,
          bg=LILA, fg=WEISS, font=("Helvetica", 13, "bold"), relief="flat",
          cursor="hand2", pady=14, bd=0).pack(fill="x", padx=30, pady=(8, 0))

ttk.Label(frame1, text="✓  Nur für Studierende – sicher und verifiziert",
          font=("Helvetica", 10), background=WEISS, foreground=GRAU_TEXT).pack(pady=(12, 0))

# ══════════════════════════════════════════════════════════════
# FRAME 2 – Uni-E-Mail eingeben
# ══════════════════════════════════════════════════════════════
frame2 = tk.Frame(window, bg=WEISS)

tk.Button(frame2, text="←", command=von2_zu1, bg=WEISS, fg=SCHWARZ,
          font=("Helvetica", 18), relief="flat", bd=0, cursor="hand2").pack(anchor="w", padx=20, pady=(50, 0))

tk.Label(frame2, text="✉", font=("Helvetica", 52), bg=WEISS, fg=LILA).pack(pady=(30, 0))

ttk.Label(frame2, text="Deine Uni-E-Mail", font=("Helvetica", 20, "bold"),
          background=WEISS, foreground=SCHWARZ).pack(pady=(20, 6))
ttk.Label(frame2, text="Wir prüfen deine Berechtigung.", font=("Helvetica", 11),
          background=WEISS, foreground=GRAU_TEXT).pack()

email_entry = tk.Entry(frame2, font=("Helvetica", 12), relief="solid", bd=1, fg=GRAU_TEXT)
email_entry.insert(0, "name@uni-muenchen.de")
email_entry.pack(fill="x", padx=30, ipady=10, pady=(30, 0))

def email_click(event):
    if email_entry.get() == "name@uni-muenchen.de":
        email_entry.delete(0, "end")
        email_entry.config(fg=SCHWARZ)

def email_leave(event):
    if email_entry.get() == "":
        email_entry.insert(0, "name@uni-muenchen.de")
        email_entry.config(fg=GRAU_TEXT)

email_entry.bind("<FocusIn>", email_click)
email_entry.bind("<FocusOut>", email_leave)

tk.Button(frame2, text="Weiter", command=von2_zu3, bg=LILA, fg=WEISS,
          font=("Helvetica", 13, "bold"), relief="flat", cursor="hand2", pady=14, bd=0).pack(fill="x", padx=30, pady=(20, 0))

ttk.Label(frame2, text="🔒  Wir verwenden deine E-Mail\n       nur zur Verifizierung.",
          font=("Helvetica", 10), background=WEISS, foreground=GRAU_TEXT, justify="left").pack(pady=(16, 0))

# ══════════════════════════════════════════════════════════════
# FRAME 3 – Abschluss
# ══════════════════════════════════════════════════════════════
frame3 = tk.Frame(window, bg=WEISS)

erstelle_kopf(frame3, 0, von3_zu2)

ttk.Label(frame3, text="Dein Abschluss", font=("Helvetica", 22, "bold"),
          background=WEISS, foreground=SCHWARZ).pack(pady=(40, 20))

abschluss_frame = tk.Frame(frame3, bg=WEISS)
abschluss_frame.pack(fill="x", padx=30)
ttk.Label(abschluss_frame, text="Abschluss", font=("Helvetica", 12),
          background=WEISS, foreground=SCHWARZ).pack(anchor="w", pady=(0, 8))

auswahl_frame = tk.Frame(abschluss_frame, bg=WEISS)
auswahl_frame.pack(fill="x")

abschluss_var = tk.StringVar(value="Bachelor")

def setze_bachelor():
    abschluss_var.set("Bachelor")
    bachelor_btn.config(bg=LILA, fg=WEISS)
    master_btn.config(bg=GRAU_BG, fg=SCHWARZ)

def setze_master():
    abschluss_var.set("Master")
    master_btn.config(bg=LILA, fg=WEISS)
    bachelor_btn.config(bg=GRAU_BG, fg=SCHWARZ)

bachelor_btn = tk.Button(auswahl_frame, text="Bachelor", command=setze_bachelor,
                         bg=LILA, fg=WEISS, font=("Helvetica", 12, "bold"),
                         relief="flat", bd=0, cursor="hand2", pady=10, width=12)
bachelor_btn.pack(side="left", padx=(0, 8))

master_btn = tk.Button(auswahl_frame, text="Master", command=setze_master,
                       bg=GRAU_BG, fg=SCHWARZ, font=("Helvetica", 12, "bold"),
                       relief="flat", bd=0, cursor="hand2", pady=10, width=12)
master_btn.pack(side="left")

tk.Button(frame3, text="Weiter", command=von3_zu4, bg=LILA, fg=WEISS,
          font=("Helvetica", 13, "bold"), relief="flat", cursor="hand2", pady=14, bd=0).pack(fill="x", padx=30, pady=(40, 0))

# ══════════════════════════════════════════════════════════════
# FRAME 4 – Fakultät
# ══════════════════════════════════════════════════════════════
frame4 = tk.Frame(window, bg=WEISS)

erstelle_kopf(frame4, 1, von4_zu3)

ttk.Label(frame4, text="Deine Fakultät", font=("Helvetica", 22, "bold"),
          background=WEISS, foreground=SCHWARZ).pack(pady=(40, 20))

fakultaet_frame = tk.Frame(frame4, bg=WEISS)
fakultaet_frame.pack(fill="x", padx=30)

fakultaet_var = tk.StringVar(value="Fakultät wählen")
ttk.Combobox(fakultaet_frame, textvariable=fakultaet_var,
             values=["Fakultät wählen", "Wirtschaftswissenschaften", "Informatik",
                     "Medizin", "Jura", "Sozialwissenschaften",
                     "Naturwissenschaften", "Ingenieurwissenschaften", "Architektur"],
             state="readonly", font=("Helvetica", 12)).pack(fill="x", ipady=6)

tk.Button(frame4, text="Weiter", command=von4_zu5, bg=LILA, fg=WEISS,
          font=("Helvetica", 13, "bold"), relief="flat", cursor="hand2", pady=14, bd=0).pack(fill="x", padx=30, pady=(40, 0))

# ══════════════════════════════════════════════════════════════
# FRAME 5 – Welcher Studiengang?
# ══════════════════════════════════════════════════════════════
frame5 = tk.Frame(window, bg=WEISS)

erstelle_kopf(frame5, 2, von5_zu4)

ttk.Label(frame5, text="Welcher Studiengang?", font=("Helvetica", 22, "bold"),
          background=WEISS, foreground=SCHWARZ).pack(pady=(40, 20))

studiengang_frame5 = tk.Frame(frame5, bg=WEISS)
studiengang_frame5.pack(fill="x", padx=30)

studiengang_var5 = tk.StringVar(value="Studiengang eingeben oder wählen")
ttk.Combobox(studiengang_frame5, textvariable=studiengang_var5,
             values=["Studiengang eingeben oder wählen", "BWL", "Informatik",
                     "Wirtschaftsinformatik", "Medizin", "Jura",
                     "Psychologie", "Maschinenbau", "Architektur"],
             font=("Helvetica", 12)).pack(fill="x", ipady=6)

tk.Button(frame5, text="Weiter", command=von5_zu6, bg=LILA, fg=WEISS,
          font=("Helvetica", 13, "bold"), relief="flat", cursor="hand2", pady=14, bd=0).pack(fill="x", padx=30, pady=(40, 0))

# ══════════════════════════════════════════════════════════════
# FRAME 6 – Welches Semester?
# ══════════════════════════════════════════════════════════════
frame6 = tk.Frame(window, bg=WEISS)

erstelle_kopf(frame6, 3, von6_zu5)

ttk.Label(frame6, text="Welches Semester?", font=("Helvetica", 22, "bold"),
          background=WEISS, foreground=SCHWARZ).pack(pady=(40, 20))

semester_frame = tk.Frame(frame6, bg=WEISS)
semester_frame.pack(fill="x", padx=30)

semester_var = tk.StringVar(value="Semester wählen")
ttk.Combobox(semester_frame, textvariable=semester_var,
             values=["Semester wählen", "1. Semester", "2. Semester", "3. Semester",
                     "4. Semester", "5. Semester", "6. Semester",
                     "7. Semester", "8. Semester"],
             state="readonly", font=("Helvetica", 12)).pack(fill="x", ipady=6)

def abschliessen():
    print("Registrierung abgeschlossen!")
    print("Abschluss:", abschluss_var.get())
    print("Studiengang:", studiengang_var3.get())
    print("Fakultät:", fakultaet_var.get())
    print("Semester:", semester_var.get())

tk.Button(frame6, text="Weiter", command=von6_zu6b, bg=LILA, fg=WEISS,
          font=("Helvetica", 13, "bold"), relief="flat", cursor="hand2", pady=14, bd=0).pack(fill="x", padx=30, pady=(40, 0))

# ══════════════════════════════════════════════════════════════
# FRAME 6b – Hurra!
# ══════════════════════════════════════════════════════════════
frame6b = tk.Frame(window, bg=WEISS)

tk.Frame(frame6b, bg=WEISS, height=120).pack()

ttk.Label(frame6b, text="🎉", font=("Helvetica", 70),
          background=WEISS).pack()

ttk.Label(frame6b, text="Hurra!", font=("Helvetica", 28, "bold"),
          background=WEISS, foreground=LILA).pack(pady=(20, 10))

ttk.Label(frame6b, text="Du bist jetzt startklar!",
          font=("Helvetica", 16), background=WEISS,
          foreground=SCHWARZ).pack()

ttk.Label(frame6b, text="Finde jetzt Studierende\ndie dir helfen können.",
          font=("Helvetica", 12), background=WEISS,
          foreground=GRAU_TEXT, justify="center").pack(pady=(10, 0))

tk.Frame(frame6b, bg=WEISS, height=80).pack()

tk.Button(frame6b, text="Zur Startseite", command=von6b_zu7,
          bg=LILA, fg=WEISS, font=("Helvetica", 13, "bold"),
          relief="flat", cursor="hand2", pady=14, bd=0).pack(fill="x", padx=30)



# ── Fenster anzeigen ──────────────────────────────────────────
window.mainloop()
