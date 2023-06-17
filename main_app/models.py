from django.db import models

# Create your models here.

class Movie(models.Model):
  api_id = models.CharField(max_length=250)
  image = models.CharField(max_length=250)
  full_title = models.CharField(max_length=250)
  release_date = models.CharField(max_length=250)
  runtime_str = models.CharField(max_length=250)
  director = models.CharField(max_length=250)
  plot = models.CharField(max_length=250)
  stars = models.TextField(max_length=250)
  # Create a M:M relationship with Toy
  # toys is the Related Manager
#   toys = models.ManyToManyField(Toy)
  # add user_id FK column
#   user = models.ForeignKey(User, on_delete=models.CASCADE)

  # Changing this instance method
  # does not impact the database, therefore
  # no makemigrations is necessary
  def __str__(self):
    return f'{self.full_title} ({self.id})'

#   def get_absolute_url(self):
#     return reverse('detail', kwargs={'cat_id': self.id})

#   def fed_for_today(self):
#     return self.feeding_set.filter(date=date.today()).count() >= len(MEALS)