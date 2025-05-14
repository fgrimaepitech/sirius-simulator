"""
Script pour visualiser l'arbre généalogique des organismes
"""
import os
import subprocess
from genealogy import Genealogy

def visualize_genealogy():
    """Génère et affiche l'arbre généalogique"""
    # Définition des chemins
    data_dir = os.path.join('src', 'data', 'species')
    dot_file = os.path.join(data_dir, 'genealogy.dot')
    png_file = os.path.join(data_dir, 'genealogy.png')
    
    # Chargement des données
    genealogy = Genealogy()
    genealogy.load_data()
    
    # Export au format DOT
    genealogy.export_to_dot(dot_file)
    
    # Génération de l'image avec Graphviz
    try:
        subprocess.run(["dot", "-Tpng", dot_file, "-o", png_file])
        print(f"Arbre généalogique généré avec succès : {png_file}")
        
        # Ouverture de l'image
        if os.name == 'nt':  # Windows
            os.startfile(png_file)
        elif os.name == 'posix':  # macOS ou Linux
            subprocess.run(["open", png_file])
    except Exception as e:
        print(f"Erreur lors de la génération de l'image : {e}")
        print("Assurez-vous que Graphviz est installé sur votre système.")
        print("Installation :")
        print("- Windows : https://graphviz.org/download/")
        print("- macOS : brew install graphviz")
        print("- Linux : sudo apt-get install graphviz")

if __name__ == "__main__":
    visualize_genealogy() 