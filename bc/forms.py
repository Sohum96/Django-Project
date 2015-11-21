from django.forms import ModelForm
from django import forms
from .models import *
from decimal import *
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit

verificationData = {}
with open('./data/input_verification_data.csv','r') as csvfile:
	reader = csv.reader(csvfile, delimiter=',')
	for row in reader:
		verificationData[row[0]]=Decimal(row[1])

# to fill up preferences
class BranchForm(forms.ModelForm):
	class Meta:
		model = Branches
		exclude = ('date_created', 'date_updated', 'owner', 'is_public')
	'''def __init__(self, *args, *kwargs):
		super(BranchForm, self).__init__(*args,**kwargs)
		self.helper=FormHelper()
		self.helper.form_class='form-horizontal'
		self.helper.label_class='col-lg-4'
		self.helper.field_class ='col-lg-8'
	'''	
	def save(self, commit=True, owner=None):
		if not self.instance.pk:
			if not owner:
				raise TypeError("Owner is required to create an Account.")
			self.instance.owner = owner	
		return super(BranchForm, self).save(commit)

#to fill up other details and validate them (clean over ridden)
class CandidateForm(forms.ModelForm):
	class Meta:
		model = Candidate
		exclude = ('owner','is_public','date_created','date_updated')
	'''def __init__(self, *args, **kwargs):
		super(CandidateForm, self).__init__(*args,**kwargs)
		self.helper=FormHelper()
		self.helper.form_class='form-horizontal'
		self.helper.label_class='col-lg-4'
		self.helper.field_class ='col-lg-8'
	'''	

	def save(self, commit=True, owner=None):
		if not self.instance.pk:
			if not owner:
				raise TypeError("Owner is required to create an Account.")
			self.instance.owner = owner
		return super(CandidateForm, self).save(commit) 
	def clean(self):
		cleaned_data = super(CandidateForm,self).clean()
		roll_no = cleaned_data.get('roll_no')
		cpi = cleaned_data.get('cpi')
		if roll_no:
			roll_len = len(roll_no)
			if roll_no not in verificationData.keys():
				raise forms.ValidationError("No such Roll number present")
			if ((roll_no[0] != '1') or (roll_no[1] != '5') or (roll_len != 9)):
				raise forms.ValidationError("Roll number should start with '15' and must be 9 digits long")
		if cpi:
			if(cpi>10 or cpi<0):
				raise forms.ValidationError("CPI should be between 0 and 10")
			if roll_no:
				if verificationData[roll_no]-cpi<0.01 and verificationData[roll_no]-cpi>-0.01:
					pass
				else:
					raise forms.ValidationError("Please enter valid CPI")		
					

# import compatible candidate form ("may be" used for authentication)
'''
class ImportCandidateForm(ModelForm):
	class Meta:
		model = ImportCandidate
		exclude = ('is_public',)
	
	def clean(self):
		cleaned_data = super(ImportCandidateForm,self).clean()
		roll_no = cleaned_data.get('roll_no')
		cpi = cleaned_data.get('cpi')
		roll_len = len(roll_no)
		if roll_no:
			if ((roll_no[0] != '1') or (roll_no[1] != '5') or (roll_len != 9)):
				raise forms.ValidationError("Roll number should start with '15' and must be 9 digits long")
		if cpi:
			if(cpi>10 or cpi<0):
				raise forms.ValidationError("CPI should be between 0 and 10")		
'''