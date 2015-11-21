from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now
import csv

# Create your models here.
prog_data = []

with open('./data/input_programmes.csv' , 'r') as csvfile :
	reader = csv.reader(csvfile, delimiter = ',')
	try:
		for row in reader :
			prog_data.append(row)
	except :
		print('Error in loading file!')		

class PublicQuerysManager(models.Manager):	#for all the models(public field - is_public
	def get_queryset(self):
		q_set = super(PublicQuerysManager, self).get_queryset()
		return q_set.filter(is_public=False)

#details for each candidate
class Candidate(models.Model):
	progs = [''] * len(prog_data)
	BRANCH_CHOICES =()
	for x in range(len(progs)):
		BRANCH_CHOICES = ((prog_data[x][0], prog_data[x][0]),) + BRANCH_CHOICES
	BRANCH_CHOICES = BRANCH_CHOICES[::-1]
	CATEGORY_CHOICES =(('GE','GE'),	('OBC','OBC'), ('SC','SC'),	('ST','ST'),)
	
	roll_no = models.CharField('Roll No',max_length=20, default='15xxxxxxx')
	u_name = models.CharField('Your Name',max_length=30, default='Name')
	p_branch = models.CharField('Present Branch', max_length=30,choices=BRANCH_CHOICES, default=prog_data[0][0] )
	cpi = models.DecimalField('CPI',max_digits=5,decimal_places=2,default=10.0)
	cat = models.CharField('Your Category', max_length=30, choices=CATEGORY_CHOICES, default='GE')
	is_public = models.BooleanField('Public', default=False)
	
	owner = models.ForeignKey(User, verbose_name='owner', related_name='candidates')
	date_created = models.DateTimeField('Date Created')
	date_updated = models.DateTimeField('Date Updated')
	
	objects = models.Manager()
	public = PublicQuerysManager()

	class Meta:
		verbose_name = 'candidate'
		verbose_name_plural = 'candidates'

	def __str__(self):
		return '%s' % (self.roll_no)

	def save(self, *args, **kwargs):
		if not self.id:
			self.date_created = now()
		self.date_updated = now()
		
		super(Candidate, self).save(*args, **kwargs)


# for each preference(supports dynamic list feature)
class Branches(models.Model):
	progs = [''] * len(prog_data)
	BRANCH_CHOICES =()
	for x in range(len(progs)):
		BRANCH_CHOICES = ((prog_data[x][0], prog_data[x][0]),) + BRANCH_CHOICES
	BRANCH_CHOICES = BRANCH_CHOICES[::-1]

	name = models.CharField( 'Name',max_length=30,choices=BRANCH_CHOICES, default="None")
	is_public = models.BooleanField('Public', default=False)
	date_created = models.DateTimeField('Date Created')
	date_updated = models.DateTimeField('Date Updated')
	owner = models.ForeignKey(User, verbose_name='owner', related_name='branches')

	objects = models.Manager()
	public = PublicQuerysManager()

	class Meta:
		verbose_name = 'branch'
		verbose_name_plural = 'branches'
		ordering = ['date_created']

	def __str__(self):
		return '%s' % (self.name)

	def save(self, *args, **kwargs):
		if not self.id:
			self.date_created = now()
		self.date_updated = now()
		super(Branches, self).save(*args, **kwargs)

#import/export compatible model (max 17 preferences-IIT B model :P)
class ImportCandidate(models.Model):
	progs = [''] * len(prog_data)
	BRANCH_CHOICES =()
	for x in range(len(progs)):
		BRANCH_CHOICES = ((prog_data[x][0], prog_data[x][0]),) + BRANCH_CHOICES
	BRANCH_CHOICES = BRANCH_CHOICES[::-1]
	CATEGORY_CHOICES =(('GE','GE'),	('OBC','OBC'), ('SC','SC'),	('ST','ST'),)
	
	roll_no = models.CharField('Roll No',max_length=20, default='15xxxxxxx')
	u_name = models.CharField('Your Name',max_length=30, default='Name')
	p_branch = models.CharField('Present Branch', max_length=150,choices=BRANCH_CHOICES, default=prog_data[0][0] )
	cpi = models.DecimalField('CPI',max_digits=5,decimal_places=2,default=10.0)
	cat = models.CharField('Your Category', max_length=30, choices=CATEGORY_CHOICES, default='GE')
	is_public = models.BooleanField('Public', default=False)
	
	pref0=models.CharField( 'Name',max_length=15,choices=BRANCH_CHOICES, default="")
	pref1=models.CharField( 'Name',max_length=15,choices=BRANCH_CHOICES, default="")
	pref2=models.CharField( 'Name',max_length=15,choices=BRANCH_CHOICES, default="")
	pref3=models.CharField( 'Name',max_length=15,choices=BRANCH_CHOICES, default="")
	pref4=models.CharField( 'Name',max_length=15,choices=BRANCH_CHOICES, default="")
	pref5=models.CharField( 'Name',max_length=15,choices=BRANCH_CHOICES, default="")
	pref6=models.CharField( 'Name',max_length=15,choices=BRANCH_CHOICES, default="")
	pref7=models.CharField( 'Name',max_length=15,choices=BRANCH_CHOICES, default="")
	pref8=models.CharField( 'Name',max_length=15,choices=BRANCH_CHOICES, default="")
	pref9=models.CharField( 'Name',max_length=15,choices=BRANCH_CHOICES, default="")
	pref10=models.CharField( 'Name',max_length=15,choices=BRANCH_CHOICES, default="")
	pref11=models.CharField( 'Name',max_length=15,choices=BRANCH_CHOICES, default="")
	pref12=models.CharField( 'Name',max_length=15,choices=BRANCH_CHOICES, default="")
	pref13=models.CharField( 'Name',max_length=15,choices=BRANCH_CHOICES, default="")
	pref14=models.CharField( 'Name',max_length=15,choices=BRANCH_CHOICES, default="")
	pref15=models.CharField( 'Name',max_length=15,choices=BRANCH_CHOICES, default="")
	pref16=models.CharField( 'Name',max_length=15,choices=BRANCH_CHOICES, default="")

	
	objects = models.Manager()
	public = PublicQuerysManager()

	class Meta:
		verbose_name = 'icandidate'
		verbose_name_plural = 'icandidates'

	def __str__(self):
		return '%s' % (self.roll_no)



