from django.db import models


class Analysis(models.Model):
    """
    Modelo que representa un análisis de CV realizado por el sistema
    """

    POSITION_CHOICES = [
        ('backend', 'Backend Developer'),
        ('frontend', 'Frontend Developer'),
        ('fullstack', 'Fullstack Developer'),
        ('data', 'Data Analyst'),
        ('qa', 'QA Tester'),
        ('other', 'Otro'),
    ]

    cv_file = models.FileField(upload_to='cvs/')
    target_position = models.CharField(
        max_length=50,
        choices=POSITION_CHOICES
    )

    # Resultado de la IA (se completará en fases posteriores)
    result_json = models.JSONField(null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"CV para {self.get_target_position_display()} - {self.created_at:%d/%m/%Y}"
