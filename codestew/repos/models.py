from django.db import models

# Create your models here.
class Repo(models.Model):
    VCS_TYPE = (
            ('git', 'Git'),
            ('hg', 'Mercurial'),
            ('bzr', 'Bazaar'),
            ('svn', 'Subversion'),
            ('cvs', 'cvs'),
    )
    name = models.CharField(max_length=60)
    vcs = models.CharField(max_length=3, choices=VCS_TYPE)
    pub_date = models.DateTimeField('date published')
    url = models.URLField(verify_exists=True)

class CodestewUser(models.Model):
    username = models.CharField(max_length=20)
    paswdhash = models.CharField(max_length=80)
    email = models.EmailField()
    web = models.URLField()
    join_date = models.DateTimeField('date joined')

class Comment(models.Model):
    repo = models.ForeignKey(Repo)
    comment = models.TextField()
    pub_date = models.DateTimeField('date published')
    user = models.ForeignKey(CodestewUser)
