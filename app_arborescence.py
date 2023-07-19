# Selectionner le fichier à traiter :
import streamlit as st
import os
import pandas as pd
import re

st.sidebar.title('Choix de l\'outil')
bou_app=st.sidebar.radio("", ('Acceuil','Récupération de données','Traitement'))

if bou_app=='Acceuil': # ----------------------------------------------------------------------------------------------------------
    
    st.write('# Application Hiérarchie de dossier')
    st.write('Made by Gressier Kyllian')
    
if bou_app=='Récupération de données': # ------------------------------------------------------------------------------------------
    def get_file_paths(start_path):
        file_paths = []
        for root, dirs, files in os.walk(start_path):
            for file in files:
                file_paths.append(os.path.join(root, file))
        return file_paths

    def main():
        st.write("## Application de récupération des chemins de fichiers")

        # Demande à l'utilisateur de saisir le début du chemin
        start_path = st.text_input("Entrez le début du chemin:", "...")

        # Vérifie si le chemin est valide
        if not os.path.exists(start_path):
            st.error("Le chemin spécifié n'existe pas.")
            return

        # Bouton pour récupérer les chemins des fichiers
        if st.checkbox("Récupérer les chemins"):
            file_paths = get_file_paths(start_path)
            st.success(f"Nombre total de fichiers trouvés: {len(file_paths)}")
            st.write("Tableau des chemins :")
            df = pd.DataFrame(file_paths, columns=['Chemins'])
            df = df['Chemins'].apply(lambda x: pd.Series(x.split('\\')))
            # Renommer les colonnes avec des numéros
            df.columns = range(1, len(df.columns)+1)
            st.write(df)
            if st.button("Télécharger le fichier CSV"):
                df.to_csv(r'C:\Users\kyllian.gressier\OneDrive - EKIUM\Bureau'+'\Output_'+start_path.replace(':','_').replace('\\','_')+'.csv' ,sep=';' ,index=False)

    main()
        

if bou_app=='Traitement': # -------------------------------------------------------------------------------------------------------
    st.write('## Vérification de l\'arborescence')
    file = st.file_uploader('Veuiller déposer les données à verifier', accept_multiple_files=False)
    if st.checkbox('Lancer l\'analyse'):
        df=pd.read_csv(file,sep=',',dtype=str)
        df.columns=[i for i in range(1, len(df.columns) + 1)] # pour que les noms de col soient des chiffres


        # Traitement col 2 : récup les variables

        if len(df[2].drop_duplicates())==1:
            list_=df[2].drop_duplicates().str.split('_')[0]
            palier = list_[0]
            site = list_[1]
            tranche = list_[2]
            batiment = list_[3]

        # Traitement col 3
        st.write('### Premier 4 fichiers :')
        list_=list(df[3].drop_duplicates())
        verif3=['LFD','SourcesDiv','Photos','Documents']
        result_4fichier=True
        for ele in verif3: # verification des élémnts normalement présent
            if ele not in list_:
                st.write('Elements manquants : ', ele)
                result_4fichier=False
        for ele in list_: # Verification d'éléments en trop
            if ele not in verif3:
                st.write('3/ Elements en trop : ', ele)
                result_4fichier=False
        if result_4fichier:
            st.write('Noms des 4 fichiers conforme')

        # Traitement col 4 : LFD :
        st.write('### Fichier LFD :')
        
            # traitement LFDbatplancher
        list_=df[4].loc[(df[3]=='LFD')].drop_duplicates()
        result_LFDBat=True
        for ele in list_:
            if ele.startswith('LFD'+batiment.lower()) and re.search(r"\d{2}$", ele): # verif si ~(LFD+bat et fini par 2 chiffres)
                pass
            else:
                st.write('Fichier ', ele, ' non conforme')
                st.write(df.loc[df[4]==ele])
                result_LFDBat=False
        if result_LFDBat:
            st.write('##### Fichier LDFBatPlancher conforme :')
            
            # traitement dans fichiers LFDbatplancher
        for ele in list_:
            ele_in_LFDBatPlancher=list(df[5].loc[df[4]==ele].drop_duplicates())
            list_C=[]
            for ele2 in ele_in_LFDBatPlancher:
                if (ele2.startswith(palier+'_'+site+'_'+tranche+'_'+batiment+'_'+ele[-2:]+'_')) and (ele2.endswith('.lfd')):
                    list_C.append(ele2)
                if (ele2.startswith(palier+'_'+site+'_'+tranche+'_'+batiment+'_'+ele[-2:]+'_')) and (ele2.endswith('.lfm')):
                    list_C.append(ele2)
                if ele2 in ['points','pngs','config','Resource']: # resoucre avec ou sans 's'?
                    list_C.append(ele2)
            if len(list(set(ele_in_LFDBatPlancher)-set(list_C)))!=0: # Si y a des elements qui diffèrent de la normale renvoyer la liste
                st.write('Dans ',ele,': Elément(s) non conforme -->',set(ele_in_LFDBatPlancher)-set(list_C))
        









































# streamlit run "C:\Users\kyllian.gressier\OneDrive - EKIUM\Bureau\doc EKIUM\Demandes autres\Da-6-Mathias-arborescence-noms-fichiers\app_arborescence.py"
