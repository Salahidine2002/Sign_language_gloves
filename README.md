Probablement vous savez déjà l’objectif du projet et la description, je vais juste vous présenter mon travail jusqu’à maintenant qui peut vous aider.

Prototype :
Afin d’avoir un suivi des mouvements de la main dans l’espace j’ai utilisé un accéléromètre 9 axes qui comporte à la fois un accéléromètre, un gyroscope et un magnétomètre,
ce capteur peut communiquer soit avec un protocole I2C soit avec un protocole SPI, personnellement j’utilise l’I2C car c’est plus simple à brancher
(pourtant le SPI est plus rapide en termes de vitesse de transmission). De plus j’ai ajouté des résistances variables fixées sur les doigts pour mesurer les déformations, 
ces résistances sont montées chacune dans un montage diviseur de tension, et les tensions dans leurs bornes sont liées aux entrées du CAN (convertisseur analogique numerique) 
qui va envoyer leurs valeurs au Raspberry avec un bus de donnée qui suit le protocole I2C aussi. Les deux modules sont connectés au meme bus I2C mais chacun a son adresse.
Pour traiter toutes ces donnees j’ai utilisé une Raspberry pi zéro. Je n’ai pas utilisé un Arduino simple car la recognition des gestes nécessite l’implémentation d’un modèle IA.

Software :
Afin de se connecter avec la Raspberry il y a deux methode principales soit avec CMD soit avec une interface comme VNC, pour commencer il suffit d’utiliser VNC.
Telecharger le ici : https://www.realvnc.com/en/connect/download/viewer/
J’ai configuré la carte pour se connecter automatiquement à point d’accès sans fil du PC, pour ne pas perdre le temps dans le changement de la configuration
(il faut modifier des fichiers dans la carte SD) vous pouvez juste utiliser le point d’accès de votre pc en modifiant l’identifiant et le mot de passe :
    -	Identifiant : Salah  (avec S majuscule)
    -	Mot de passe : 12345678
    -	Bande passante : 2,4 GHz
Connecter la carte au chargeur (attention ce n’est pas le port au milieu), lancer votre point d’accès avec les coordonnées au-dessus, normalement la carte va se connecter apres
2min ou moins (verifier en cherchant les appareils connectes à votre reseau). Après qu’elle se connecte, lancer VNC, copier l’adresse IP du carte connectée
(vous pouvez la trouver dans les paramètres de votre point d’accès) et la coller dans la barre de recherche dans vnc, une fenetre s’ouvert pour écrire l’I et le mot de passe :
    -	Id : pi
    -	Mot de passe : sign-cs
Et voila le bureau de votre mini pc s’ouvre. Accéder à l’explorateur des fichiers, sous le répertoire pi, vous trouver mon programme principal de lecture et d’enregistrement 
des donnees fournis par les capteurs. Essayer d’exécuter ce programme (s’il y a une erreur de connexion d’un capteur veuillez fixer tous les fils et relancer le programme).
Les donnees afficher dans le terminal pendant l’exécution sont respectivement les 4 tensions mesurées des résistances variables, les composantes d’accélération suivant 3 axes,
les vitesses de rotations suivant 3 axes et du champs magnétique suivant 3 axes (totale de 13 variables).

