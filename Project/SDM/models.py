from django.db import models

class Trainer(models.Model):
    name = models.CharField(max_length=100)
    qualification = models.CharField(max_length=100)
    experience_years = models.PositiveIntegerField()

    def __str__(self):
        return f"Shri. {self.name}, {self.qualification}, {self.experience_years} yrs Experience"

class Topic(models.Model):
    name = models.CharField(max_length=100)
    duration_days = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.name} ({self.duration_days} days)"

class Course(models.Model):
    title = models.CharField(max_length=40)
    duration = models.PositiveIntegerField()
    mobile_number_1 = models.CharField(max_length=10)
    mobile_number_2 = models.CharField(max_length=10)
    trainer = models.ForeignKey(Trainer, on_delete=models.CASCADE)
    topics = models.ManyToManyField(Topic)
    fee = models.PositiveIntegerField()

    def __str__(self):
        return self.title

class Batch(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name
    
class Student(models.Model):
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    email = models.EmailField(max_length=60)
    country_code = models.CharField(max_length=5, default="+91")
    mobile_number = models.CharField(max_length=10)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    batch = models.ForeignKey(Batch, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
