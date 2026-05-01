################
#Formulaire.py
################
import tkinter as tk  # Importation de la bibliothèque tkinter pour l'interface graphique
# FENÊTRE PRINCIPALE
root = tk.Tk()
root.title("Formulaire Étudiant") # Titre de la fenêtre
#root.geometry("600x500") # Taille fixe de la fenêtre 
root.state("zoomed")   # plein écran (Windows)
root.configure(bg="#e0f7fa")  # Couleur de fond bleu clair
root.configure(cursor="pirate")  # Curseur pirate

# TITRE PRINCIPAL AVEC COULEURS head
frame_titre = tk.Frame(root, bg="#e0f7fa") # Cadre pour le titre
frame_titre.pack(pady=20) # Espacement vertical

# Chaque lettre avec sa couleur
tk.Label(frame_titre, text="OF", font=("Helvetica", 32, "bold"), fg="green", bg="#e0f7fa").pack(side="left")
tk.Label(frame_titre, text="PP", font=("Helvetica", 32, "bold"), fg="blue", bg="#e0f7fa").pack(side="left")
tk.Label(frame_titre, text="T", font=("Helvetica", 32, "bold"), fg="gray", bg="#e0f7fa").pack(side="left") 

# PARTIE POUR LA FORMULAIRE body
frame_form = tk.Frame(root, bg="#e0f7fa", padx=20, pady=20) # Cadre pour le formulaire
frame_form.pack(pady=10) # Espacement vertical

# --- Nom complet ---
tk.Label(frame_form, text="Nom complet :", bg="#e0f7fa", font=("Arial", 12)).grid(row=0, column=0, sticky="w", pady=5) # Label pour le nom
entry_nom = tk.Entry(frame_form, width=40) # Entry pour le nom
entry_nom.grid(row=0, column=1, pady=5) # Placement dans la grille

# --- Type de formation ---
tk.Label(frame_form, text="Type de formation :", bg="#e0f7fa", font=("Arial", 12)).grid(row=1, column=0, sticky="w", pady=5)
frame_radios = tk.Frame(frame_form, bg="#e0f7fa")
frame_radios.grid(row=1, column=1, pady=5, sticky="w")
var_formation = tk.StringVar()
tk.Radiobutton(frame_radios, text="DD", variable=var_formation, value="DD", bg="#e0f7fa").pack(side="left", padx=5) # Bouton radio DD
tk.Radiobutton(frame_radios, text="ID", variable=var_formation, value="ID", bg="#e0f7fa").pack(side="left", padx=5) # Bouton radio ID

# --- Adresse email ---
tk.Label(frame_form, text="Adresse email :", bg="#e0f7fa", font=("Arial", 12)).grid(row=2, column=0, sticky="w", pady=5) # Label pour l'email
entry_email = tk.Entry(frame_form, width=40) 
entry_email.grid(row=2, column=1, pady=5) 

# --- Établissement ---
tk.Label(frame_form, text="Établissement :", bg="#e0f7fa", font=("Arial", 12)).grid(row=3, column=0, sticky="w", pady=5)
entry_etablissement = tk.Entry(frame_form, width=40)
entry_etablissement.grid(row=3, column=1, pady=5)

# --- Commentaire ---
tk.Label(frame_form, text="Commentaire :", bg="#e0f7fa", font=("Arial", 12)).grid(row=4, column=0, sticky="nw", pady=5)
text_commentaire = tk.Text(frame_form, width=30, height=5)
text_commentaire.grid(row=4, column=1, pady=5)

# BOUTONS   footer
btn_envoyer = tk.Button(root, text="Envoyer", width=15, bg="#00ccff", fg="white")# Bouton envoyer
btn_envoyer.pack(pady=10) # Espacement vertical
btn_reset = tk.Button(root, text="Réinitialiser", width=15, bg="#ff6666", fg="white")# Bouton réinitialiser
btn_reset.pack(pady=5) # Espacement vertical

# LANCER LA FENÊTRE PRINCIPALE
root.mainloop() # Lancer la boucle principale de l'interface graphique