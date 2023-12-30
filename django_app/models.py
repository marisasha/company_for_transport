from django.db import models

class Transports(models.Model):  # таблица
    title = models.CharField(
            db_index=False,
            primary_key=False,
            unique=False,
            editable=True,
            blank=True,
            null=False,
            default="",
            verbose_name="Наименование",
            max_length=100,
        )
        
    price = models.CharField(
            db_index=False,
            primary_key=False,
            unique=False,
            editable=True,
            blank=True,
            null=False,
            default="",
            verbose_name="Имя",
            max_length=300,
        )
    

    def __str__(self):
        return f"<User ({self.id}) имя:{self.name} жалоба: {self.report_text}/>"
    
    def id_(self):
        return self.id
