import streamlit as st

def le_trieur():
    st.markdown("""
    ## Le trieur
    Niveau 1: algorithme de tri  
    Niveau 2: tri spécialisé selon la typologie de la liste  
    """)

def le_miroir():
    st.markdown("""
    ## Le miroir
    Niveau 1: inverser des mots  
    Niveau 2: inverser des phrases  
    """)

def le_poete():
    st.markdown("""
    ## Le poète 
    créer des mots qui sonnent bien, evoluer en créateur de phrases, puis de poemes
    """)

def l_investisseur():
    st.markdown("""
    ## L'investisseur
    Formule des intérets composés
    """)
    
def l_oeil_d_horus():
    st.markdown("""
    ## L'oeil d'Horus
    Trouver la couleur majoritaire d'une image
    """)

def le_surfeur():
    st.markdown("""
    ## Le surfeur
    ploter des vagues, surface 3d
    """)
def les_lapins():
    st.markdown("""
    ## Les lapins 
    proie prédateur, equation différentielle et graphe 2d
    """)
    
def le_statisticien():
    st.markdown("""
    ## Le statisticien
    statistiques de base, evoluer en calcul de la p value
    """)

def le_philosophe():
    st.markdown("""
    ## Le philosophe
    Génerateur des citations philosophiques
    """)

def la_chaleur():
    st.markdown("""
    ## La chaleur
    Calculs autour de la diffusion de la chaleur 
    """)
    
def l_eau():
    st.markdown("""
    ## L'eau
    simulation de l'ecoulement de l'eau, équation de stokes 
    """)
    
def les_voitures():
    st.markdown("""
    ## Les voitures
    modélisation des circulations de voitures, mathématiques appliquées
    """)
    
def la_foret():
    st.markdown("""
    ## La forêt
    Modélisation de la croissance d'une forêt
    """)

def kratos():
    st.markdown("""
    ## Kratos
    Défis autours des chaines de caractères 
    """)
def matrix():
    st.markdown("""
    ## Matrix
    Défis autours des matrices
    """)

def vcs():
    st.markdown("""
    ## VCS
    lire un fichier csv/excel, premieres colonnes et lignes en DataFrame
    """)

def regression():
    st.markdown("""
    ## Régression
    Niveau 1: Regression linéaire
    Niveau 2: Regression multi-variables
    """)
    
challenges = [
    {
        "name": "Le miroir",
        "container": le_miroir
    },
    {
        "name": "Le trieur",
        "container": le_trieur
    },
    {
        "name": "Le poète",
        "container": le_poete
    },
    {
        "name": "L'investisseur",
        "container": l_investisseur
    },
    {
        "name": "L'oeil d'Horus",
        "container": l_oeil_d_horus
    },
    {
        "name": "Le surfeur",
        "container": le_surfeur
    },
    {
        "name": "Les lapins",
        "container": les_lapins
    },
    {
        "name": "Le statisticien",
        "container": le_statisticien
    },
    {
        "name": "Le philosophe",
        "container": le_philosophe
    },
    {
        "name": "La chaleur",
        "container": la_chaleur
    },
    {
        "name": "L'eau",
        "container": l_eau
    },
    {
        "name": "Les voitures",
        "container": les_voitures
    },
    {
        "name": "La forêt",
        "container": la_foret
    },
    {
        "name": "Kratos",
        "container": kratos
    },
    {
        "name": "Matrix",
        "container": matrix
    },
    {
        "name": "VCS",
        "container": vcs
    },
    {
        "name": "Régression",
        "container": regression
    }
]
