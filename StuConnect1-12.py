# -*- coding: utf-8 -*-
"""
Created on Wed May 27 16:28:11 2026

@author: dieru

123
"""

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
LILA_HELL = "#EDE9FF"
WEISS     = "#FFFFFF"
GRAU_BG   = "#F0F0F0"
GRAU_BG2  = "#F8F8F8"
GRAU_TEXT = "#666666"
SCHWARZ   = "#1A1A1A"
GRUEN     = "#27AE60"

# ══════════════════════════════════════════════════════════════
# NAVIGATION – Onboarding
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

def von6b_zu7():
    frame6b.pack_forget()
    zeige_menu(frame7)

# ══════════════════════════════════════════════════════════════
# NAVIGATION – Menü
# ══════════════════════════════════════════════════════════════
alle_menu_frames = []

def zeige_menu(naechster):
    for f in alle_menu_frames:
        f.pack_forget()
    naechster.pack(fill="both", expand=True)

def zu_home():
    zeige_menu(frame7)

def zu_suche():
    zeige_menu(frame8)

def zu_chat():
    zeige_menu(frame11)

def zu_profil():
    zeige_menu(frame12)

def von8_zu9():
    zeige_menu(frame9)

def von9_zu8():
    zeige_menu(frame8)

def von9_zu10():
    zeige_menu(frame10)

def von10_zu9():
    zeige_menu(frame9)

def zeige_chat_mit(name):
    chat_name_label.config(text="👤  " + name)
    zeige_menu(frame11b)

def von11b_zu11():
    zeige_menu(frame11)

def zu_einstellungen():
    zeige_menu(frame12b)

def von12b_zu12():
    zeige_menu(frame12)

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
# HILFSFUNKTION: Menüleiste
# ══════════════════════════════════════════════════════════════
def erstelle_nav(eltern, aktiv_name):
    eltern.aktiv_name = aktiv_name
    tk.Frame(eltern, bg=GRAU_BG, height=1).pack(side="bottom", fill="x")
    nav = tk.Frame(eltern, bg=WEISS)
    nav.pack(side="bottom", fill="x", pady=6)
    punkte = [
        ("🏠", "Home",   zu_home),
        ("🔍", "Suche",  zu_suche),
        ("💬", "Chat",   zu_chat),
        ("👤", "Profil", zu_profil)
    ]
    for symbol, name, funktion in punkte:
        farbe_fg = LILA if name == aktiv_name else GRAU_TEXT
        btn_frame = tk.Frame(nav, bg=WEISS)
        btn_frame.pack(side="left", expand=True)
        tk.Button(btn_frame, text=symbol + chr(10) + name,
                  command=funktion,
                  bg=WEISS, fg=farbe_fg,
                  font=("Helvetica", 9),
                  relief="flat", bd=0,
                  cursor="hand2").pack(expand=True)

# ══════════════════════════════════════════════════════════════
# FRAME 1 – Willkommen
# ══════════════════════════════════════════════════════════════
frame1 = tk.Frame(window, bg=WEISS)
frame1.pack(fill="both", expand=True)

logo_frame = tk.Frame(frame1, bg=WEISS, height=160)
logo_frame.pack(fill="x")
logo_frame.pack_propagate(False)
tk.Frame(logo_frame, bg=WEISS, height=40).pack()
ttk.Label(logo_frame, text="🎓", font=("Helvetica", 52),
          background=WEISS, foreground=LILA).pack()
ttk.Label(logo_frame, text="StuConnect", font=("Helvetica", 24, "bold"),
          background=WEISS, foreground=LILA).pack()

inhalt1 = tk.Frame(frame1, bg=WEISS)
inhalt1.pack(fill="x", padx=30, pady=(20, 0))
ttk.Label(inhalt1, text="Nachhilfe von Studierenden\nfür Studierende.",
          font=("Helvetica", 16, "bold"), background=WEISS,
          foreground=SCHWARZ, justify="center").pack(pady=(0, 6))
ttk.Label(inhalt1, text="Für LMU, TUM und HM.",
          font=("Helvetica", 11), background=WEISS,
          foreground=GRAU_TEXT, justify="center").pack()

dots1 = tk.Frame(frame1, bg=WEISS)
dots1.pack(pady=16)
for i in range(4):
    tk.Label(dots1, bg=LILA if i == 0 else GRAU_BG,
             width=3 if i == 0 else 1, height=1).pack(side="left", padx=3, ipady=3)

tk.Button(frame1, text="Mit Uni-E-Mail anmelden", command=von1_zu2,
          bg=LILA, fg=WEISS, font=("Helvetica", 13, "bold"),
          relief="flat", cursor="hand2", pady=14, bd=0).pack(fill="x", padx=30, pady=(8, 0))
ttk.Label(frame1, text="✓  Nur für Studierende – sicher und verifiziert",
          font=("Helvetica", 10), background=WEISS,
          foreground=GRAU_TEXT).pack(pady=(12, 0))

# ══════════════════════════════════════════════════════════════
# FRAME 2 – Uni-E-Mail
# ══════════════════════════════════════════════════════════════
frame2 = tk.Frame(window, bg=WEISS)

tk.Button(frame2, text="←", command=von2_zu1, bg=WEISS, fg=SCHWARZ,
          font=("Helvetica", 18), relief="flat", bd=0,
          cursor="hand2").pack(anchor="w", padx=20, pady=(50, 0))
tk.Label(frame2, text="✉", font=("Helvetica", 52),
         bg=WEISS, fg=LILA).pack(pady=(30, 0))
ttk.Label(frame2, text="Deine Uni-E-Mail", font=("Helvetica", 20, "bold"),
          background=WEISS, foreground=SCHWARZ).pack(pady=(20, 6))
ttk.Label(frame2, text="Wir prüfen deine Berechtigung.",
          font=("Helvetica", 11), background=WEISS, foreground=GRAU_TEXT).pack()

email_entry = tk.Entry(frame2, font=("Helvetica", 12),
                       relief="solid", bd=1, fg=GRAU_TEXT)
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

tk.Button(frame2, text="Weiter", command=von2_zu3,
          bg=LILA, fg=WEISS, font=("Helvetica", 13, "bold"),
          relief="flat", cursor="hand2", pady=14, bd=0).pack(fill="x", padx=30, pady=(20, 0))
ttk.Label(frame2, text="🔒  Wir verwenden deine E-Mail\n       nur zur Verifizierung.",
          font=("Helvetica", 10), background=WEISS,
          foreground=GRAU_TEXT, justify="left").pack(pady=(16, 0))

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

studiengang_frame3 = tk.Frame(frame3, bg=WEISS)
studiengang_frame3.pack(fill="x", padx=30, pady=(24, 0))
ttk.Label(studiengang_frame3, text="Studiengang", font=("Helvetica", 12),
          background=WEISS, foreground=SCHWARZ).pack(anchor="w", pady=(0, 8))
studiengang_var3 = tk.StringVar(value="Studiengang wählen")
ttk.Combobox(studiengang_frame3, textvariable=studiengang_var3,
             values=["Studiengang wählen", "BWL", "Informatik", "Wirtschaftsinformatik",
                     "Medizin", "Jura", "Psychologie", "Maschinenbau", "Architektur"],
             state="readonly", font=("Helvetica", 12)).pack(fill="x", ipady=6)

tk.Button(frame3, text="Weiter", command=von3_zu4,
          bg=LILA, fg=WEISS, font=("Helvetica", 13, "bold"),
          relief="flat", cursor="hand2", pady=14, bd=0).pack(fill="x", padx=30, pady=(40, 0))

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

tk.Button(frame4, text="Weiter", command=von4_zu5,
          bg=LILA, fg=WEISS, font=("Helvetica", 13, "bold"),
          relief="flat", cursor="hand2", pady=14, bd=0).pack(fill="x", padx=30, pady=(40, 0))

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

tk.Button(frame5, text="Weiter", command=von5_zu6,
          bg=LILA, fg=WEISS, font=("Helvetica", 13, "bold"),
          relief="flat", cursor="hand2", pady=14, bd=0).pack(fill="x", padx=30, pady=(40, 0))

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

tk.Button(frame6, text="Weiter", command=von6_zu6b,
          bg=LILA, fg=WEISS, font=("Helvetica", 13, "bold"),
          relief="flat", cursor="hand2", pady=14, bd=0).pack(fill="x", padx=30, pady=(40, 0))

# ══════════════════════════════════════════════════════════════
# FRAME 6b – Hurra!
# ══════════════════════════════════════════════════════════════
frame6b = tk.Frame(window, bg=WEISS)

tk.Frame(frame6b, bg=WEISS, height=120).pack()
ttk.Label(frame6b, text="🎉", font=("Helvetica", 70), background=WEISS).pack()
ttk.Label(frame6b, text="Hurra!", font=("Helvetica", 28, "bold"),
          background=WEISS, foreground=LILA).pack(pady=(20, 10))
ttk.Label(frame6b, text="Du bist jetzt startklar!",
          font=("Helvetica", 16), background=WEISS, foreground=SCHWARZ).pack()
ttk.Label(frame6b, text="Finde jetzt Studierende\ndie dir helfen können.",
          font=("Helvetica", 12), background=WEISS,
          foreground=GRAU_TEXT, justify="center").pack(pady=(10, 0))
tk.Frame(frame6b, bg=WEISS, height=80).pack()
tk.Button(frame6b, text="Zur Startseite", command=von6b_zu7,
          bg=LILA, fg=WEISS, font=("Helvetica", 13, "bold"),
          relief="flat", cursor="hand2", pady=14, bd=0).pack(fill="x", padx=30)

# ══════════════════════════════════════════════════════════════
# FRAME 7 – Home
# ══════════════════════════════════════════════════════════════
frame7 = tk.Frame(window, bg=WEISS)
alle_menu_frames.append(frame7)
erstelle_nav(frame7, "Home")

inhalt7 = tk.Frame(frame7, bg=WEISS)
inhalt7.pack(fill="both", expand=True, padx=20, pady=(20, 0))

kopf7 = tk.Frame(inhalt7, bg=WEISS)
kopf7.pack(fill="x", pady=(0, 16))
ttk.Label(kopf7, text="StuConnect", font=("Helvetica", 18, "bold"),
          background=WEISS, foreground=LILA).pack(side="left")
ttk.Label(kopf7, text="🔔", font=("Helvetica", 18), background=WEISS).pack(side="right")

ttk.Label(inhalt7, text="Anfragen für dich", font=("Helvetica", 13, "bold"),
          background=WEISS, foreground=SCHWARZ).pack(anchor="w", pady=(0, 8))
ttk.Label(inhalt7, text="Noch keine Anfragen vorhanden.",
          font=("Helvetica", 11), background=WEISS,
          foreground=GRAU_TEXT).pack(anchor="w", pady=(10, 0))

# ══════════════════════════════════════════════════════════════
# FRAME 8 – Suche
# ══════════════════════════════════════════════════════════════
frame8 = tk.Frame(window, bg=WEISS)
alle_menu_frames.append(frame8)
erstelle_nav(frame8, "Suche")

inhalt8 = tk.Frame(frame8, bg=WEISS)
inhalt8.pack(fill="both", expand=True, padx=20, pady=(20, 0))

kopf8 = tk.Frame(inhalt8, bg=WEISS)
kopf8.pack(fill="x", pady=(0, 12))
ttk.Label(kopf8, text="Suche", font=("Helvetica", 18, "bold"),
          background=WEISS, foreground=SCHWARZ).pack(side="left")

# Filter-Popup
filter_popup = tk.Frame(frame8, bg=WEISS, relief="solid", bd=1)

filter_sichtbar = tk.BooleanVar(value=False)

def toggle_filter():
    if filter_sichtbar.get():
        filter_popup.place_forget()
        filter_sichtbar.set(False)
    else:
        filter_popup.place(x=180, y=70, width=200, height=300)
        filter_popup.lift()
        filter_sichtbar.set(True)

tk.Button(kopf8, text="⚙ Filter", command=toggle_filter,
          bg=LILA_HELL, fg=LILA, font=("Helvetica", 10, "bold"),
          relief="flat", bd=0, cursor="hand2", padx=8, pady=4).pack(side="right")

# Suchfeld
such_entry = tk.Entry(inhalt8, font=("Helvetica", 12),
                      relief="solid", bd=1, fg=GRAU_TEXT)
such_entry.insert(0, "🔍  Fach oder Thema suchen")
such_entry.pack(fill="x", ipady=8, pady=(0, 16))

def such_click(event):
    if such_entry.get() == "🔍  Fach oder Thema suchen":
        such_entry.delete(0, "end")
        such_entry.config(fg=SCHWARZ)

def such_leave(event):
    if such_entry.get() == "":
        such_entry.insert(0, "🔍  Fach oder Thema suchen")
        such_entry.config(fg=GRAU_TEXT)

such_entry.bind("<FocusIn>", such_click)
such_entry.bind("<FocusOut>", such_leave)

ttk.Label(inhalt8, text="Suchergebnisse erscheinen hier...",
          font=("Helvetica", 11), background=WEISS,
          foreground=GRAU_TEXT).pack(anchor="w", pady=(10, 0))

# Filter-Popup Inhalt
ttk.Label(filter_popup, text="Filter", font=("Helvetica", 12, "bold"),
          background=WEISS, foreground=SCHWARZ).pack(anchor="w", padx=10, pady=(8, 4))

tk.Frame(filter_popup, bg=GRAU_BG, height=1).pack(fill="x")

# Fach
ttk.Label(filter_popup, text="Fach", font=("Helvetica", 10),
          background=WEISS, foreground=GRAU_TEXT).pack(anchor="w", padx=10, pady=(6, 2))
fach_var = tk.StringVar(value="Alle Fächer")
ttk.Combobox(filter_popup, textvariable=fach_var,
             values=["Alle Fächer", "BWL", "Informatik", "Mathematik",
                     "Buchhaltung", "Kostenrechnung", "Statistik"],
             state="readonly", font=("Helvetica", 10)).pack(fill="x", padx=10)

# Region
ttk.Label(filter_popup, text="Region", font=("Helvetica", 10),
          background=WEISS, foreground=GRAU_TEXT).pack(anchor="w", padx=10, pady=(6, 2))
region_var = tk.StringVar(value="Alle Regionen")
ttk.Combobox(filter_popup, textvariable=region_var,
             values=["Alle Regionen", "München", "Online", "Augsburg", "Nürnberg"],
             state="readonly", font=("Helvetica", 10)).pack(fill="x", padx=10)

# Geschlecht
ttk.Label(filter_popup, text="Geschlecht", font=("Helvetica", 10),
          background=WEISS, foreground=GRAU_TEXT).pack(anchor="w", padx=10, pady=(6, 2))
geschlecht_var = tk.StringVar(value="Egal")
geschlecht_frame = tk.Frame(filter_popup, bg=WEISS)
geschlecht_frame.pack(fill="x", padx=10)
for g in ["Egal", "Männlich", "Weiblich"]:
    tk.Radiobutton(geschlecht_frame, text=g, variable=geschlecht_var, value=g,
                   bg=WEISS, fg=SCHWARZ, font=("Helvetica", 10),
                   activebackground=WEISS, cursor="hand2").pack(side="left")

# Umkreis
ttk.Label(filter_popup, text="Umkreis", font=("Helvetica", 10),
          background=WEISS, foreground=GRAU_TEXT).pack(anchor="w", padx=10, pady=(6, 2))
umkreis_var = tk.StringVar(value="Egal")
ttk.Combobox(filter_popup, textvariable=umkreis_var,
             values=["Egal", "5 km", "10 km", "25 km", "50 km", "Nur Online"],
             state="readonly", font=("Helvetica", 10)).pack(fill="x", padx=10)

tk.Button(filter_popup, text="Anwenden", command=toggle_filter,
          bg=LILA, fg=WEISS, font=("Helvetica", 10, "bold"),
          relief="flat", bd=0, cursor="hand2", pady=6).pack(fill="x", padx=10, pady=8)

# ══════════════════════════════════════════════════════════════
# FRAME 9 – Anbieterprofil
# ══════════════════════════════════════════════════════════════
frame9 = tk.Frame(window, bg=WEISS)
alle_menu_frames.append(frame9)
frame9.aktiv_name = "Suche"

kopf9 = tk.Frame(frame9, bg=WEISS)
kopf9.pack(fill="x", padx=20, pady=(30, 0))
tk.Button(kopf9, text="←", command=von9_zu8, bg=WEISS, fg=SCHWARZ,
          font=("Helvetica", 18), relief="flat", bd=0, cursor="hand2").pack(side="left")

inhalt9 = tk.Frame(frame9, bg=WEISS)
inhalt9.pack(fill="both", expand=True, padx=20, pady=(16, 0))

ttk.Label(inhalt9, text="👤", font=("Helvetica", 40), background=WEISS).pack()
ttk.Label(inhalt9, text="Anna M.", font=("Helvetica", 18, "bold"),
          background=WEISS, foreground=SCHWARZ).pack(pady=(6, 2))
ttk.Label(inhalt9, text="⭐ 4.8  (23 Bewertungen)",
          font=("Helvetica", 11), background=WEISS, foreground=SCHWARZ).pack()
ttk.Label(inhalt9, text="BWL – 2. Semester an der TUM",
          font=("Helvetica", 10), background=WEISS, foreground=GRAU_TEXT).pack(pady=(2, 12))
ttk.Label(inhalt9, text="Über mich", font=("Helvetica", 12, "bold"),
          background=WEISS, foreground=SCHWARZ).pack(anchor="w")
ttk.Label(inhalt9,
          text="Ich helfe dir gerne bei Buchungssätzen,\nJahresabschluss und Bilanzierung.",
          font=("Helvetica", 10), background=WEISS,
          foreground=GRAU_TEXT, justify="left").pack(anchor="w", pady=(4, 12))

for bezeichnung, wert in [("Fach", "Bilanzierung (1.–2. Sem.)"),
                            ("Preis", "15 €/Stunde"),
                            ("Unterricht", "Online oder München"),
                            ("Sprache", "Deutsch")]:
    zeile = tk.Frame(inhalt9, bg=WEISS)
    zeile.pack(fill="x", pady=2)
    ttk.Label(zeile, text=bezeichnung, font=("Helvetica", 10),
              background=WEISS, foreground=GRAU_TEXT, width=12).pack(side="left")
    ttk.Label(zeile, text=wert, font=("Helvetica", 10),
              background=WEISS, foreground=SCHWARZ).pack(side="left")

tk.Button(frame9, text="Anfrage senden", command=von9_zu10,
          bg=LILA, fg=WEISS, font=("Helvetica", 13, "bold"),
          relief="flat", cursor="hand2", pady=14, bd=0).pack(fill="x", padx=20, pady=(20, 10))

# ══════════════════════════════════════════════════════════════
# FRAME 10 – Anfrage senden
# ══════════════════════════════════════════════════════════════
frame10 = tk.Frame(window, bg=WEISS)
alle_menu_frames.append(frame10)
frame10.aktiv_name = "Suche"

kopf10 = tk.Frame(frame10, bg=WEISS)
kopf10.pack(fill="x", padx=20, pady=(30, 0))
tk.Button(kopf10, text="←", command=von10_zu9, bg=WEISS, fg=SCHWARZ,
          font=("Helvetica", 18), relief="flat", bd=0, cursor="hand2").pack(side="left")

inhalt10 = tk.Frame(frame10, bg=WEISS)
inhalt10.pack(fill="both", expand=True, padx=20, pady=(16, 0))

ttk.Label(inhalt10, text="Anfrage an Anna M.", font=("Helvetica", 18, "bold"),
          background=WEISS, foreground=SCHWARZ).pack(anchor="w", pady=(0, 16))
ttk.Label(inhalt10, text="Deine Nachricht (optional)",
          font=("Helvetica", 11), background=WEISS, foreground=SCHWARZ).pack(anchor="w")

nachricht_entry = tk.Text(inhalt10, font=("Helvetica", 11),
                           relief="solid", bd=1, height=5, fg=GRAU_TEXT)
nachricht_entry.insert("1.0", "Schreibe hier deine Nachricht...")
nachricht_entry.pack(fill="x", pady=(6, 16))

for bezeichnung in ["Vorschlag", "Datum", "Uhrzeit", "Dauer"]:
    zeile = tk.Frame(inhalt10, bg=WEISS)
    zeile.pack(fill="x", pady=4)
    ttk.Label(zeile, text=bezeichnung, font=("Helvetica", 11),
              background=WEISS, foreground=SCHWARZ, width=10).pack(side="left")
    ttk.Label(zeile, text="–", font=("Helvetica", 11),
              background=WEISS, foreground=GRAU_TEXT).pack(side="left")

tk.Button(frame10, text="Anfrage senden", command=zu_home,
          bg=LILA, fg=WEISS, font=("Helvetica", 13, "bold"),
          relief="flat", cursor="hand2", pady=14, bd=0).pack(fill="x", padx=20, pady=(20, 10))

# ══════════════════════════════════════════════════════════════
# FRAME 11 – Chat-Liste
# ══════════════════════════════════════════════════════════════
frame11 = tk.Frame(window, bg=WEISS)
alle_menu_frames.append(frame11)
erstelle_nav(frame11, "Chat")

inhalt11 = tk.Frame(frame11, bg=WEISS)
inhalt11.pack(fill="both", expand=True, padx=20, pady=(20, 0))

ttk.Label(inhalt11, text="Chats", font=("Helvetica", 18, "bold"),
          background=WEISS, foreground=SCHWARZ).pack(anchor="w", pady=(0, 16))

chat_kontakte = ["Anna M.", "Lukas S.", "Sarah K."]
for kontakt in chat_kontakte:
    karte = tk.Frame(inhalt11, bg=GRAU_BG2, cursor="hand2")
    karte.pack(fill="x", pady=(0, 8))
    karte_inhalt = tk.Frame(karte, bg=GRAU_BG2)
    karte_inhalt.pack(fill="x", padx=12, pady=10)
    ttk.Label(karte_inhalt, text="👤  " + kontakt, font=("Helvetica", 12, "bold"),
              background=GRAU_BG2, foreground=SCHWARZ).pack(side="left")
    ttk.Label(karte_inhalt, text="›", font=("Helvetica", 16),
              background=GRAU_BG2, foreground=GRAU_TEXT).pack(side="right")
    karte.bind("<Button-1>", lambda e, n=kontakt: zeige_chat_mit(n))
    karte_inhalt.bind("<Button-1>", lambda e, n=kontakt: zeige_chat_mit(n))

# ══════════════════════════════════════════════════════════════
# FRAME 11b – Einzel-Chat
# ══════════════════════════════════════════════════════════════
frame11b = tk.Frame(window, bg=WEISS)
alle_menu_frames.append(frame11b)
frame11b.aktiv_name = "Chat"

kopf11b = tk.Frame(frame11b, bg=WEISS)
kopf11b.pack(fill="x", padx=20, pady=(20, 0))
tk.Button(kopf11b, text="←", command=von11b_zu11, bg=WEISS, fg=SCHWARZ,
          font=("Helvetica", 18), relief="flat", bd=0, cursor="hand2").pack(side="left")
chat_name_label = ttk.Label(kopf11b, text="", font=("Helvetica", 13, "bold"),
                              background=WEISS, foreground=SCHWARZ)
chat_name_label.pack(side="left", padx=10)

nachrichten_frame = tk.Frame(frame11b, bg=WEISS)
nachrichten_frame.pack(fill="both", expand=True, padx=20, pady=(12, 0))
ttk.Label(nachrichten_frame, text="Noch keine Nachrichten. Schreib etwas!",
          font=("Helvetica", 11), background=WEISS,
          foreground=GRAU_TEXT).pack(anchor="w", pady=(20, 0))

eingabe11b = tk.Frame(frame11b, bg=WEISS)
eingabe11b.pack(fill="x", padx=20, pady=10)
tk.Entry(eingabe11b, font=("Helvetica", 11), relief="solid", bd=1,
         fg=GRAU_TEXT).pack(side="left", fill="x", expand=True, ipady=8, padx=(0, 8))
tk.Button(eingabe11b, text="➤", bg=LILA, fg=WEISS,
          font=("Helvetica", 12), relief="flat", bd=0,
          padx=12, pady=6).pack(side="left")

# ══════════════════════════════════════════════════════════════
# FRAME 12 – Profil
# ══════════════════════════════════════════════════════════════
frame12 = tk.Frame(window, bg=WEISS)
alle_menu_frames.append(frame12)
erstelle_nav(frame12, "Profil")

inhalt12 = tk.Frame(frame12, bg=WEISS)
inhalt12.pack(fill="both", expand=True, padx=20, pady=(20, 0))

avatar12 = tk.Frame(inhalt12, bg=LILA_HELL, width=80, height=80)
avatar12.pack(pady=(10, 0))
avatar12.pack_propagate(False)
ttk.Label(avatar12, text="👤", font=("Helvetica", 30),
          background=LILA_HELL, foreground=LILA).pack(expand=True)

ttk.Label(inhalt12, text="Mein Profil", font=("Helvetica", 16, "bold"),
          background=WEISS, foreground=SCHWARZ).pack(pady=(10, 2))
ttk.Label(inhalt12, text="Verwalte dein Profil und deine Einstellungen.",
          font=("Helvetica", 10), background=WEISS,
          foreground=GRAU_TEXT).pack(pady=(2, 16))

tk.Frame(inhalt12, bg=GRAU_BG, height=1).pack(fill="x", pady=(0, 10))

profil_punkte = [
    ("📋", "Meine Angebote",  None),
    ("📩", "Meine Anfragen",  None),
    ("⭐", "Bewertungen",     None),
    ("⚙",  "Einstellungen",  zu_einstellungen),
]

for symbol, text, funktion in profil_punkte:
    zeile = tk.Frame(inhalt12, bg=WEISS, cursor="hand2")
    zeile.pack(fill="x", pady=8)
    ttk.Label(zeile, text=symbol + "  " + text, font=("Helvetica", 12),
              background=WEISS, foreground=SCHWARZ).pack(side="left")
    ttk.Label(zeile, text="›", font=("Helvetica", 14),
              background=WEISS, foreground=GRAU_TEXT).pack(side="right")
    if funktion:
        zeile.bind("<Button-1>", lambda e, f=funktion: f())

# ══════════════════════════════════════════════════════════════
# FRAME 12b – Einstellungen
# ══════════════════════════════════════════════════════════════
frame12b = tk.Frame(window, bg=WEISS)
alle_menu_frames.append(frame12b)
frame12b.aktiv_name = "Profil"

kopf12b = tk.Frame(frame12b, bg=WEISS)
kopf12b.pack(fill="x", padx=20, pady=(30, 0))
tk.Button(kopf12b, text="←", command=von12b_zu12, bg=WEISS, fg=SCHWARZ,
          font=("Helvetica", 18), relief="flat", bd=0, cursor="hand2").pack(side="left")
ttk.Label(kopf12b, text="Einstellungen", font=("Helvetica", 16, "bold"),
          background=WEISS, foreground=SCHWARZ).pack(side="left", padx=12)

inhalt12b = tk.Frame(frame12b, bg=WEISS)
inhalt12b.pack(fill="both", expand=True, padx=20, pady=(20, 0))

# Name
ttk.Label(inhalt12b, text="Dein Name", font=("Helvetica", 11),
          background=WEISS, foreground=GRAU_TEXT).pack(anchor="w", pady=(0, 4))
name_entry = tk.Entry(inhalt12b, font=("Helvetica", 12), relief="solid", bd=1)
name_entry.pack(fill="x", ipady=8, pady=(0, 14))

# Uni
ttk.Label(inhalt12b, text="Deine Universität", font=("Helvetica", 11),
          background=WEISS, foreground=GRAU_TEXT).pack(anchor="w", pady=(0, 4))
uni_var = tk.StringVar(value="Universität wählen")
ttk.Combobox(inhalt12b, textvariable=uni_var,
             values=["Universität wählen", "LMU München", "TU München", "HM München",
                     "Uni Augsburg", "FAU Erlangen-Nürnberg"],
             state="readonly", font=("Helvetica", 12)).pack(fill="x", ipady=6, pady=(0, 14))

# Studiengang
ttk.Label(inhalt12b, text="Studiengang", font=("Helvetica", 11),
          background=WEISS, foreground=GRAU_TEXT).pack(anchor="w", pady=(0, 4))
studiengang_einstell_var = tk.StringVar(value="Studiengang wählen")
ttk.Combobox(inhalt12b, textvariable=studiengang_einstell_var,
             values=["Studiengang wählen", "BWL", "Informatik", "Wirtschaftsinformatik",
                     "Medizin", "Jura", "Psychologie", "Maschinenbau", "Architektur"],
             state="readonly", font=("Helvetica", 12)).pack(fill="x", ipady=6, pady=(0, 14))

# Semester
ttk.Label(inhalt12b, text="Semester", font=("Helvetica", 11),
          background=WEISS, foreground=GRAU_TEXT).pack(anchor="w", pady=(0, 4))
semester_einstell_var = tk.StringVar(value="Semester wählen")
ttk.Combobox(inhalt12b, textvariable=semester_einstell_var,
             values=["Semester wählen", "1. Semester", "2. Semester", "3. Semester",
                     "4. Semester", "5. Semester", "6. Semester",
                     "7. Semester", "8. Semester"],
             state="readonly", font=("Helvetica", 12)).pack(fill="x", ipady=6, pady=(0, 14))

# Ich bin
ttk.Label(inhalt12b, text="Ich bin...", font=("Helvetica", 11),
          background=WEISS, foreground=GRAU_TEXT).pack(anchor="w", pady=(0, 4))
rolle_var = tk.StringVar(value="Suchend")
rolle_frame = tk.Frame(inhalt12b, bg=WEISS)
rolle_frame.pack(fill="x", pady=(0, 14))
for rolle in ["Suchend", "Anbietend", "Beides"]:
    tk.Radiobutton(rolle_frame, text=rolle, variable=rolle_var, value=rolle,
                   bg=WEISS, fg=SCHWARZ, font=("Helvetica", 11),
                   activebackground=WEISS, cursor="hand2").pack(side="left", padx=(0, 12))

def speichern():
    print("Name:", name_entry.get())
    print("Uni:", uni_var.get())
    print("Studiengang:", studiengang_einstell_var.get())
    print("Semester:", semester_einstell_var.get())
    print("Rolle:", rolle_var.get())
    von12b_zu12()

tk.Button(frame12b, text="Speichern", command=speichern,
          bg=LILA, fg=WEISS, font=("Helvetica", 13, "bold"),
          relief="flat", cursor="hand2", pady=14, bd=0).pack(fill="x", padx=20, pady=(10, 0))

# ── Start ──────────────────────────────────────────────────────
window.mainloop()
