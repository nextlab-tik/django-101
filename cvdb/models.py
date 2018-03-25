from django.db import models

class Skill(models.Model):
    name = models.CharField(max_length=20, unique=True, primary_key=True)

    def __str__(self):
        return self.name

class Person(models.Model):
    username = models.SlugField(max_length=40, unique=True)
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    photo = models.ImageField()

    email = models.EmailField()
    phone = models.CharField(max_length=12)
    website = models.URLField()
    twitter = models.SlugField(max_length=40)
    facebook = models.SlugField(max_length=40)
    github = models.SlugField(max_length=40)
    linkedin = models.SlugField(max_length=40)
    address = models.CharField(max_length=80)

    headline = models.CharField(max_length=80)
    summary = models.TextField(max_length=80)

    skills_proficiency = models.ManyToManyField(Skill, related_name="skills_proficiency")
    skills_familiar = models.ManyToManyField(Skill, related_name="skills_familiar")

    def __str__(self):
        return "{} {}".format(self.first_name, self.last_name)

class Experience(models.Model):
    cv = models.ForeignKey(Person, on_delete=models.CASCADE)
    title = models.CharField(max_length=80)
    company = models.CharField(max_length=40)
    description = models.TextField()
    started_at = models.DateField()
    ended_at = models.DateField(null=True, blank=True)

    def __str__(self):
        return "{} - {}".format(self.title, self.company)

class Education(models.Model):
    cv = models.ForeignKey(Person, on_delete=models.CASCADE)
    title = models.CharField(max_length=80)
    institute = models.CharField(max_length=40)
    started_at = models.DateField()
    ended_at = models.DateField()

    def __str__(self):
        return "{} - {}".format(self.title, self.institute)
