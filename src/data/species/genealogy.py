"""
Gestion de l'arbre généalogique des organismes
"""
import json
import os
from datetime import datetime

class Genealogy:
    def __init__(self):
        self.species = {}  # Dictionnaire pour stocker tous les organismes
        
        # Créer le dossier data/species s'il n'existe pas
        self.data_dir = os.path.join('src', 'data', 'species')
        os.makedirs(self.data_dir, exist_ok=True)
        
        # Chemin du fichier de sauvegarde
        self.save_file = os.path.join(self.data_dir, 'genealogy.json')
        
        # Charger les données existantes si elles existent
        self.load_data()
    
    def load_data(self):
        """Charge les données existantes depuis le fichier JSON"""
        if os.path.exists(self.save_file):
            try:
                with open(self.save_file, 'r') as f:
                    data = json.load(f)
                    self.species = data.get('species', {})
            except Exception as e:
                print(f"Erreur lors du chargement des données: {e}")
                self.species = {}
    
    def save_data(self):
        """Sauvegarde les données dans le fichier JSON"""
        try:
            with open(self.save_file, 'w') as f:
                json.dump({
                    'species': self.species
                }, f, indent=2)
        except Exception as e:
            print(f"Erreur lors de la sauvegarde des données: {e}")
    
    def add_organism(self, organism, parent_id=None):
        """Ajoute un nouvel organisme à l'arbre généalogique"""
        # Utiliser l'ID de l'organisme comme clé dans la généalogie
        organism_id = organism.id
        
        # Vérifier si l'organisme existe déjà
        if organism_id in self.species:
            return organism_id
        
        # Créer l'entrée pour l'organisme
        self.species[organism_id] = {
            'id': organism_id,
            'parent_id': organism.parent_id,
            'color': organism.color,
            'birth_time': datetime.now().isoformat(),
            'children': []
        }
        
        # Ajouter l'organisme comme enfant de son parent
        if organism.parent_id is not None:
            # S'assurer que le parent existe
            if organism.parent_id not in self.species:
                self.species[organism.parent_id] = {
                    'id': organism.parent_id,
                    'parent_id': None,  # On ne connaît pas le parent du parent
                    'color': [0, 0, 0],  # Couleur par défaut
                    'birth_time': datetime.now().isoformat(),
                    'children': []
                }
            # Ajouter l'enfant à la liste des enfants du parent
            if organism_id not in self.species[organism.parent_id]['children']:
                self.species[organism.parent_id]['children'].append(organism_id)
        
        # Sauvegarder les données
        self.save_data()
        
        return organism_id
    
    def get_organism_info(self, organism_id):
        """Récupère les informations d'un organisme"""
        return self.species.get(str(organism_id))
    
    def get_family_tree(self, organism_id):
        """Récupère l'arbre généalogique complet d'un organisme"""
        def build_tree(org_id, tree=None):
            if tree is None:
                tree = {}
            
            org = self.species.get(str(org_id))
            if org:
                tree[org_id] = {
                    'info': org,
                    'children': {}
                }
                for child_id in org['children']:
                    build_tree(child_id, tree[org_id]['children'])
            
            return tree
        
        return build_tree(organism_id)
    
    def export_to_dot(self, filename='genealogy.dot'):
        """Exporte l'arbre généalogique au format DOT pour Graphviz"""
        with open(filename, 'w') as f:
            f.write('digraph Genealogy {\n')
            f.write('    node [shape=box, style=filled];\n')
            
            # Écrire les nœuds
            for org_id, org in self.species.items():
                color = f"#{org['color'][0]:02x}{org['color'][1]:02x}{org['color'][2]:02x}"
                f.write(f'    {org_id} [label="{org_id}", fillcolor="{color}"];\n')
            
            # Écrire les relations
            for org_id, org in self.species.items():
                for child_id in org['children']:
                    f.write(f'    {org_id} -> {child_id};\n')
            
            f.write('}\n')
        
        return filename 