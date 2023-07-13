# Tests de Performance de l'API

Ce projet contient des tests de performance pour l'API de prédiction du sepsis. Les tests sont réalisés à l'aide de l'outil de test de charge Locust.

## Installation

Pour exécuter les tests de performance, suivez les étapes suivantes :

1. Clonez ce dépôt de code sur votre machine locale.
2. Assurez-vous d'avoir Python 3.7 ou une version ultérieure installée.
3. Installez Locust en exécutant la commande suivante :
```bash
pip install -r requirements.txt
```

## Exécution des tests

Pour exécuter les tests de performance, suivez les étapes suivantes :

1. Ouvrez une fenêtre de terminal et naviguez vers le répertoire contenant le fichier **'locustfile.py'**.
2. Exécutez la commande suivante pour démarrer l'interface web de Locust :
```bash
locust --host=http://localhost:5000
```
3. Ouvrez votre navigateur et accédez à l'URL **'http://localhost:8089'**. Cela affichera l'interface web de Locust.
4. Configurez le nombre d'utilisateurs simulés, la charge, la période d'incubation, etc. sur l'interface web de Locust.
5. Cliquez sur le bouton "Start Swarming" pour démarrer les tests de performance.
6. Les résultats des tests seront affichés en temps réel sur l'interface web de Locust. Vous pourrez voir les statistiques de performance telles que le nombre de requêtes par seconde, le temps de réponse moyen, etc.

## Scénarios de test

Le fichier **'locustfile.py'** contient des scénarios de test de performance pour l'API. Actuellement, il y a deux tâches **('tasks')** définies :

- **'health'** : Cette tâche simule la charge lorsque les utilisateurs envoient une requête de vérification d'état **('/health')** à l'API.
- **'predict_one'** : Cette tâche simule la charge lorsque les utilisateurs effectuent des prédictions avec une ligne à la fois. Elle envoie une requête POST avec des données d'exemple à l'API.

Vous pouvez personnaliser les scénarios de test en modifiant le fichier **'locustfile.py'** selon vos besoins.

## Auteurs

Ce projet a été développé par **Aboubacar CAMARA**, **Aaricia DOMINGUEZ** et **Adrien ALVAREZ** dans le cadre du projet annuel de la classe M1IABD de l'école ESGI. Si vous avez des questions, veuillez nous contacter à l'adresse mail **aa-dz@hotmail.com**, **aboubacar.camara.abk@gmail.com** ou **adrienalvarezzpro@gmail.com**.
