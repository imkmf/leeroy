from django.db import models

class Server(models.Model):
  name = models.CharField(max_length=100)
  url = models.CharField(max_length=100)
  port = models.IntegerField(max_length=5, default=80)
  private = models.BooleanField(default=False)
  username = models.CharField(max_length=50, blank=True)
  password = models.CharField(max_length=30, blank=True)
  def __unicode__(self):
    return self.name
  def set_password(self, raw_password):
    import random
    algo = 'sha1'
    salt = get_hexdigest(algo, str(random.random()), str(random.random()))[:5]
    hsh = get_hexdigest(algo, salt, raw_password)
    self.password = '%s$%s$%s' % (algo, salt, hsh)
