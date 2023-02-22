# MedNet
 Brief solo du 15/02 au 22/02

Voici le contexte du projet : 

L’objectif étant de prouver les compétences techniques de notre start-up et de faire adhérer le corps médical au projet DATA Health HUB. Dans un souci d’accessibilité aux données, le POC se fera avec les données publiques du dataset MedNist.

Nous partons d’une application existante développée par les équipes du CHRU, un algorithme développé via Pytorch qui propose déjà de beaux résultats ,L'application sera développée en flask et permet de classifier sa radiographie.

Voici les missions attendues :
-Implémenter un modèle de classification ( Transfert Learning) avec Keras /TensorFlow
-Amélioration du modèle MedNet ( Pytorch) : Un modèle de DeepLearning a été élaboré. Il utilise un réseau de neurones afin de pouvoir classer les images médicales dans ces 6 catégories. Le modèle a obtenu un taux de 99% de prédictions correctes ce qui est un bon score.
-Création d'une interface et Evolution fonctionnelle : * L’application comprend 2 pages. L’application permet de sélectionner un fichier image et de le télécharger :Puis elle permet d’obtenir sa classification. Les informations affichées sont « ID » qui correspond au numéro allant de 1 à 6 de la classe et « Class » qui correspond au nom de la classe. L'application sera déployée via AzureWebapp. L'interface pourra se faire avec Flask et /ou Streamlit

BONUS Il vous est demandé de pouvoir sélectionner un, plusieurs ou tous les fichiers d’un dossier, de le ou les télécharger et de prédire la classification.

Sur ce repository, il est possible de retrouver les documents suivants :
- la deuxième partie du brief, visant à améliorer le modèle MedNet via Pytorch (l'objectif étant de faire 15 erreurs ou moins)
- le dossier interface, réalisé avec Flask

/!\ le nombre de données étant trop volumineux, cela n'a pas été mis sur ce repository. Il est cependant possible de retrouver cela sur le google drive de la promotion (concernant la partie 1) et sur le git originel du projet MedNet (pour la partie 2)

Voici les liens pour les autres documents qui n'ont pas été mis sur ce repository :
- diagramme de Gantt : https://docs.google.com/spreadsheets/d/1OFr589xARsjoV8--c1W6EFCYbe34yvyK1EnYOeRwxlI/edit#gid=0
- notebook de la partie 1, réalisé sur Google Collab :https://colab.research.google.com/drive/1NEl4-d3LQt79uNiWapI7yKQotTruHV8G

Pour utiliser l'interface Flask :
- créer un environnement virtuel avec les librairies Pytorch, matplotlib, numpy, PIL
- ouvrer le fichier interface.py et lancer le script
- cliquer sur le lien localhost qui s'affiche dans le terminal
- il est possible de faire des prédictions !
