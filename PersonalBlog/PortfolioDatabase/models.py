from django.db import models

# Create your models here.

class Hobby(models.Model):
    hobby_name = models.CharField()
    hobby_desc = models.TextField()
    hobby_image = models.CharField(max_length = 500, default = "https://img.freepik.com/free-vector/speech-bubble-with-interrogation-sign-cloud-isolated-icon_18591-83281.jpg?semt=ais_user_personalization&w=740&q=80")


    def __str__(self):
        return self.hobby_name
    
class Portfolio(models.Model):
    port_name = models.CharField()
    port_desc = models.TextField()
    port_image = models.CharField(max_length = 500, default = "https://img.freepik.com/free-vector/speech-bubble-with-interrogation-sign-cloud-isolated-icon_18591-83281.jpg?semt=ais_user_personalization&w=740&q=80")

    def __str__(self):
        return self.port_name
    


