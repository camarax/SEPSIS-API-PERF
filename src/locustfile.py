from locust import HttpUser, task

class ProjectPerfTest(HttpUser):
    
    @task
    def health(self):
        # Tester la charge lorsque les utilisateurs ping l'api.
        headers = {'Content-Type': 'application/json',"Authorization":"lesecret"}
        self.client.get("http://127.0.0.1:5000/health",headers=headers)

    @task
    def predict_one(self):
        # Tester la charge lorsque les utilisateurs effectue des prédictions avec une ligne à la fois
        headers = {'Content-Type': 'application/json',"Authorization":"lesecret"}

        data = {
            "PRG" : 8,
            "PL" : 183,
            "PR" : 64,
            "SK" : 0,
            "TS" : 0,
            "M11" : 23.3,
            "BD2" : 0.672,
            "Age" : 32,
            "Insurance" : 1
        }
        self.client.post("http://127.0.0.1:5000/predict", json=data, headers=headers)

    # @task
    # def predict_all(self):
    #     # Tester la charge lorsque les utilisateurs effectue des prédiction avec plusieurs lignes en même temps
    #     headers = {'Content-Type': 'application/json',"Authorization":"lesecret"}
    #     data = {}
    #     self.client.get("http://127.0.0.1:5000/health", json=data, headers=headers)

    