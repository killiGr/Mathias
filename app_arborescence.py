# Selectionner le fichier à traiter :
import streamlit as st
import os
import pandas as pd
import re
import PIL as P

st.sidebar.title('Choix de l\'outil')
bou_app=st.sidebar.radio("", ('Acceuil','Traitement'))

if bou_app=='Acceuil': # ----------------------------------------------------------------------------------------------------------
    
    st.write('# Application Hiérarchie de dossier')
    st.write('Made by Gressier Kyllian')
    st.write('### Explication des différentes fonctions :')
    st.markdown(

"""**- premiers_fichiers() :** Cette fonction effectue une vérification sur les noms des 4 premier fichiers. Elle s'assure que certains éléments, tels que 'LFD', 'SourcesDiv', 'Photos', 'Documents', sont présents exactement une fois et qu'il n'y a pas d'éléments en trop. Elle renvoie une liste des fichiers à traiter par la suite.

**- fichier_LFD() :** Cette fonction effectue une vérification sur le fichier LFD.

Vérification du nom du bâtiment : Chaque fichier dans list_ est vérifié pour s'assurer que le nom du bâtiment commence par les lettres "LFD" suivie du nom du bâtiment en majuscules. Si ce n'est pas le cas, un avertissement est affiché indiquant que le nom du bâtiment n'est pas en majuscules.

Vérification du format des fichiers : Pour chaque fichier dans list_, il doit respecter les critères suivants :

Le nom du fichier doit commencer par "LFD" suivi du nom du bâtiment (en minuscules ou en majuscules).
Le nom du fichier doit être suivi de deux chiffres ou de l'abréviation "TT".
La longueur totale du nom de fichier doit être égale à la longueur de "LFD" + la longueur du nom du bâtiment + 2 caractères (chiffres ou "TT").
Sinon, le fichier est considéré non conforme.
Si tous les fichiers dans list_ satisfont les critères ci-dessus, la variable result_LFDBat est mise à True, et un message indiquant que les fichiers "LDFBatPlancher" sont conformes est affiché.

Traitement des fichiers dans le dossier "LFD" : Pour chaque fichier dans list_, on récupère les éléments (autres fichiers) contenus dans le dossier portant le nom de ce fichier. Ces éléments sont stockés dans la liste ele_in_LFDBatPlancher.

Vérification des éléments dans le dossier "LFD" : Pour chaque élément dans ele_in_LFDBatPlancher, on vérifie s'il correspond à certains critères :

S'il commence par une combinaison de "palier + site + tranche + nom du bâtiment + les deux derniers caractères du nom du fichier dans list_" suivi de "_" et se termine par ".lfd", alors il est ajouté à la liste list_C.
S'il commence de la même manière mais se termine par ".lfm", alors il est également ajouté à la liste list_C.
Si l'élément est l'un des suivants : 'points', 'pngs', 'config', 'Resource', il est également ajouté à la liste list_C.
Si la différence entre ele_in_LFDBatPlancher et list_C n'est pas vide, cela signifie qu'il y a des éléments non conformes dans le dossier "LFD". Un message est affiché pour signaler ces éléments non conformes.

**- fichier_Photos() :** Cette fonction traite les fichiers correspondant à 'Photos'.

Vérification du nombre d'éléments uniques dans le fichier "Photos". On vérifie si ce nombre est égal à 1 et si la valeur de l'unique élément est "JPG". Si ces deux conditions sont satisfaites, cela signifie que le dossier "Photos" contient un seul élément dont le nom est "JPG".

Si la vérification ci-dessus est réussie (un seul élément et vaut "JPG"), un message indiquant que le fichier JPG est conforme est affiché.

La liste list_ est créée en récupérant les éléments uniques dans le fichier "JPG". Cela donne une liste des noms de fichiers correspondant au format "JPG" dans le dossier "Photos".

La variable result_JPGBat est initialisée à True, et une boucle parcourt chaque fichier dans list_ pour vérifier s'il satisfait certains critères :

Le nom du fichier doit commencer par "JPG" suivi du nom du bâtiment (en minuscules ou en majuscules).
Le nom du fichier doit être suivi de deux chiffres ou de l'abréviation "TT".
La longueur totale du nom de fichier doit être égale à la longueur de "JPG" + la longueur du nom du bâtiment + 2 caractères (chiffres ou "TT").
Si ces conditions sont satisfaites, le fichier est considéré conforme et le traitement continue. Sinon, le fichier est considéré non conforme, et la variable result_JPGBat est mise à False.
Si tous les fichiers dans list_ satisfont les critères ci-dessus (c'est-à-dire result_JPGBat est True), un message est affiché indiquant que les fichiers "JPGBatPlancher" sont conformes.

Si la vérification initiale échoue (le nombre d'éléments uniques n'est pas égal à 1 ou l'unique élément n'est pas "JPG"), cela signifie que le dossier "Photos" n'est pas conforme, et un message est affiché pour indiquer que le contenu du dossier ne sera pas vérifié. Une liste des éléments présents dans le dossier "Photos" est également affichée.

**- fichier_Documents() :** Cette fonction traite les fichiers correspondant à 'Documents'. Elle vérifie la présence de dossiers dans les fichiers et s'assure que les fichiers 'Liste_livrable_informatique' et 'Tableau_recapitulatif' sont présents avec des noms conformes.

**- fichier_SourcesDiv() :** Cette fonction traite les fichiers correspondant à 'SourcesDiv'. Elle vérifie la présence d'éléments spécifiques dans les fichiers, tels que 'FormatJPG_color', 'FormatNeutreE57', etc. Elle signale les éléments manquants et les noms de fichiers non conformes."""
        
)
        

if bou_app=='Traitement': # -------------------------------------------------------------------------------------------------------
    st.write('## Vérification de l\'arborescence')
    file = st.file_uploader('Veuiller déposer les données à verifier', accept_multiple_files=False)
    
    # Fonctions : _________________________________________________________________

    def ligne():
        st.image(P.Image.open('photo_2.png'))
    
    
    def premiers_fichiers():
        # Traitement col 3
        st.markdown('## *Premier 4 fichiers :*')
        list_=list(df[3].drop_duplicates())
        verif3=['LFD','SourcesDiv','Photos','Documents']
        result_4fichier=True
        for ele in verif3: # verification des élémnts normalement présent
            if ele not in list_:
                st.write('Elements manquants : ', ele)
                result_4fichier=False
        for ele in list_: # Verification d'éléments en trop
            if ele not in verif3:
                st.write('Elements en trop : ', ele)
                result_4fichier=False
        if result_4fichier:
            st.write('Noms des 4 fichiers conforme')

        # Créer la liste des elements à verifier (si manquant ne pas verifier)
        fichiers_traiter = list(set(list_).intersection(verif3))
        return fichiers_traiter

    def fichier_LFD():
        # Traitement col 4 : LFD :
        st.markdown('## *Fichier LFD :*')

            # traitement LFDbatplancher
        list_=df[4].loc[(df[3]=='LFD')].drop_duplicates()
        
        for ele in list_:
            if ele[3:3+len(batiment)]!=batiment.upper():# verifier si batiment en majuscule
                st.markdown("<font color='red'>Warning :</font>"+' le batiment n\'est pas en majuscule ( {} )'.format(ele), unsafe_allow_html=True)
        
        result_LFDBat=True
        for ele in list_:
            if (ele.startswith('LFD'+batiment.lower()) or ele.startswith('LFD'+batiment.upper())) and len(ele)==len('LFD'+batiment+'00') and (re.search(r"\d{2}$", ele) or ele.endswith("TT")): # verif si ~(LFD+bat(upper ou lower) et fini par 2 chiffres ou 'TT' et taille noms = lfd+batiment+2 caractères)
                pass
            else:
                st.write('##### Fichier ', ele, ' non conforme. Son contenu ne sera pas entièrement verrifié.')
                st.write('Contenu de ',ele)
                st.write(df[5].loc[df[4]==ele].drop_duplicates())
                result_LFDBat=False
                
        if result_LFDBat:
            st.write('##### Fichiers LDFBatPlancher conforme')
            
            # traitement dans fichiers LFDbatplancher
        st.write('##### Test dans les fichiers "LFDbatplancher" : ')
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
                
                
    def fichier_Photos():
        st.markdown('## *Fichier Photos :*')
        if len(df[4].loc[df[3]=='Photos'].drop_duplicates())==1 and df[4].loc[df[3]=='Photos'].drop_duplicates().iloc[0]=='JPG': # Verifier si un seul élément et vaut 'JPG'
            st.write('##### Fichier JPG conforme')

            list_=df[5].loc[df[4]=='JPG'].drop_duplicates()
            result_JPGBat=True
            for ele in list_:
#                if ele.startswith('JPG'+batiment.lower()) and re.search(r"\d{2}$", ele): # verif si ~(JPG+bat et fini par 2 chiffres)
                if (ele.startswith('JPG'+batiment.lower()) or ele.startswith('JPG'+batiment.upper())) and len(ele)==len('JPG'+batiment+'00') and (re.search(r"\d{2}$", ele) or ele.endswith("TT")):
                    pass
                else:
                    st.write('##### Fichier ', ele, ' non conforme. Son contenu ne sera pas entièrement verrifié.')
                    st.write('Contenu de ',ele)
                    st.write(df.loc[df[5]==ele])
                    result_JPGBat=False
            if result_JPGBat:
                st.write('##### Fichiers JPGBatPlancher conforme')
        else:
            st.write('##### Fichier JPG non conforme (Le contenu du fichier Photos ne sera donc pas verrifié)')
            st.write('Contenu du fichier Photos : ', list(df[4].loc[df[3]=='Photos'].drop_duplicates()))
            
    def fichier_Documents():
        st.markdown('## *Fichier Documents :*')
        st.write('#### Test de présence de dossiers :')
        ele_in_Documents=list(df[4].loc[df[3]=='Documents'].drop_duplicates())
        list_doc=[]
        for ele2 in ele_in_Documents:
            if '.' not in ele2: # test de présence de dossiers dans Documents
                list_doc.append(ele2)
        if list_doc: # si non vide
            st.write('##### Test non conforme : il n\'y a pas que des fichiers')
            st.write('Liste des dossiers contenus dans "Documents" : ')
            st.write(list_doc)
        else:
            st.write('Test conforme')
            
        st.write('#### Test de présence des fichiers  "Liste_livrable_informatique" et "Tableau_recapitulatif" : ')
        list_C=[]
        for ele2 in ele_in_Documents:
            if (ele2.startswith('Tableau_recapitulatif'+'_'+palier+'_'+site+'_'+tranche+'_'+batiment+'_')) and (ele2.endswith('.xlsx')):
                list_C.append(ele2)
            if (ele2.startswith('Liste_livrable_informatique'+'_'+palier+'_'+site+'_'+tranche+'_'+batiment+'_')) and (ele2.endswith('.xlsx')):
                list_C.append(ele2)
        if len(list_C)==2:
            st.write('##### Fichier Documents Conforme')
            if len(ele_in_Documents)!=2:
                st.write('Liste des éléments dans "Documents" : ',ele_in_Documents)
        elif len(list_C)==1:
            st.write('##### Test non conforme :')
            if list_C[0].startswith('Tableau_recapitulatif'):
                st.write('Fichier "Liste_livrable_informatique" manquant')
            if list_C[0].startswith('Liste_livrable_informatique'):    
                st.write('Fichier "Tableau_recapitulatif" manquant')
            st.write('Liste des fichiers contenus dans "Documents" : ')
            st.write(list(set(ele_in_Documents)-set(list_doc)))
        else: 
            st.write('##### Test non conforme :')
            st.write('Fichiers "Liste_livrable_informatique" et "Tableau_recapitulatif" manquants')
            st.write('Liste des fichiers contenus dans "Documents" : ')
            st.write(list(set(ele_in_Documents)-set(list_doc)))
            
    def fichier_SourcesDiv():
        st.markdown('## *Fichier SourcesDiv :*')
        
        list_=list(df[4].loc[df[3]=='SourcesDiv'].drop_duplicates())
        verif3=['FormatJPG_color','FormatNeutreE57','FormatProprietaire','FormatRealworks','FormatRMX','ZFC','FormatMySurvey']
        result_4fichier=True
        for ele in verif3: # verification des élémnts normalement présent
            if ele not in list_:
                st.write('Elements manquants : ', ele)
                result_4fichier=False
        for ele in list_: # Verification d'éléments en trop
            if ele not in verif3:
                st.write('Elements en trop : ', ele)
                result_4fichier=False
        if result_4fichier:
            st.write('Fichier "SourcesDiv" conforme')
            
        # FormatJPG_color
        list_2=list(df[5].loc[df[4]=='FormatJPG_color'])
        list_C=[]
        for ele2 in list_2:
            if (ele2.startswith(palier+'_'+site+'_'+tranche+'_'+batiment+'_')) and (ele2.endswith('.jpg')):
                list_C.append(ele2)
        if len(list(set(list_2)-set(list_C)))!=0:
            st.write('##### Fichier "FormatJPG_color" non conforme')
            st.write('Les fichiers suivants sont mal renomés')
            st.write(list(set(list_2)-set(list_C)))
        else: 
            st.write('##### Fichier "FormatJPG_color" conforme')
            
        # FormatNeutreE57
        list_2=list(df[5].loc[df[4]=='FormatNeutreE57'])
        list_C=[]
        for ele2 in list_2:
            if (ele2.startswith(palier+'_'+site+'_'+tranche+'_'+batiment+'_')) and (ele2.endswith('.e57')):
                list_C.append(ele2)
        if len(list(set(list_2)-set(list_C)))!=0:
            st.write('##### Fichier "FormatNeutreE57" non conforme')
            st.write('Les fichiers suivants sont mal renomés')
            st.write(list(set(list_2)-set(list_C)))
        else: 
            st.write('##### Fichier "FormatNeutreE57" conforme')
            
        # FormatProprietaire
        st.write('##### Traitement "FormatProprietaire" en développement')
            
    # Analyse : _______________________________________________________________________________________
    
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
            
        ligne()
        fichier_traiter=premiers_fichiers()
        ligne()
        
        if 'LFD' in fichier_traiter:
            fichier_LFD()
            ligne()
        
        if 'SourcesDiv' in fichier_traiter:   
            fichier_SourcesDiv()
            ligne()
            
        if 'Photos' in fichier_traiter:
            fichier_Photos()
            ligne()
            
        if 'Documents' in fichier_traiter:
            fichier_Documents()
            ligne()
















# streamlit run "C:\Users\kyllian.gressier\OneDrive - EKIUM\Bureau\doc EKIUM\Demandes autres\Da-6-Mathias-arborescence-noms-fichiers\app_arborescence.py"
