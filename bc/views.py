from django.shortcuts import render, render_to_response, get_object_or_404, redirect
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import BranchForm, CandidateForm 
from .models import *
import csv

# Create your views here.

def branch_list(request):
	branches = Branches.public.all()
	candidates = Candidate.public.all()
	context = {'branches':branches, 'candidates': candidates, 'edit': False}
	return render(request, 'bc/branch_list.html', context)		

def branch_user(request, username):
	user = get_object_or_404(User, username=username)
	if request.user == user:
		branches = Branches.public.filter(owner=request.user)
		candidates = Candidate.public.filter(owner=request.user)
	context = {'branches': branches, 'candidates':candidates ,'owner':user, 'edit': True}
	return render(request, 'bc/branch_user.html', context)

@login_required		
def branch_create(request):
	if request.method == 'POST':
		form = BranchForm(data = request.POST)
		data=request.POST
		if form.is_valid():
			if not Branches.objects.all().filter(name = data['name'], owner = request.user).exists():
				form.save(owner=request.user)
		return redirect('bc_branch_user', username=request.user.username)
	else:
		form = BranchForm()
	return render(request, 'bc/form.html',{'form':form,'create':True,'isBranch':True})

@login_required
def branch_edit(request, pk):
	branch = get_object_or_404(Branches, pk=pk)
	if branch.owner != request.user and not request.user.is_superuser:
		raise PermissionDenied
	if request.method == 'POST':
		form = BranchForm(instance=branch, data=request.POST)
		if form.is_valid():
			data = request.POST
			_branches = Branches.objects.all()
			flag=False	
			for _branch in _branches:
				if _branch.name == data['name'] and _branch.owner==branch.owner:
					flag=True
			if not flag:
				form.save() 

			return redirect('bc_branch_user', username=request.user.username)
	else:
		form=BranchForm(instance=branch)		
	return render(request,'bc/form.html',{'form':form, 'create':False,'branch':branch,'isBranch':True})		

@login_required
def branch_delete(request, pk):
	branch = get_object_or_404(Branches,pk=pk)
	if branch.owner != request.user:
		raise PermissionDenied
	branch.delete()
	return redirect('bc_branch_user',username=request.user.username)

@login_required		
def candidate_create(request):
	print(request.POST)
	if request.method == 'POST':
		form = CandidateForm(data = request.POST)
		print(request.POST)
		data=request.POST
		if form.is_valid():
			if not Candidate.objects.all().filter(owner = request.user).exists():
				form.save(owner=request.user)
		return redirect('bc_branch_user', username=request.user.username)
	else:
		form = CandidateForm()
	return render(request, 'bc/form.html',{'form':form,'create':True,'isBranch':False})

@login_required
def candidate_edit(request, pk):
	candidate = get_object_or_404(Candidate, pk=pk)
	if candidate.owner != request.user and not request.user.is_superuser:
		raise PermissionDenied
	if request.method == 'POST':
		form = CandidateForm(instance=candidate, data=request.POST)
		if form.is_valid():
			form.save()
			return redirect('bc_branch_user', username=request.user.username)
	else:
		form=CandidateForm(instance=candidate)		
	return render(request,'bc/form.html',{'form':form, 'create':False,'candidate':candidate,'isBranch':False})		

@login_required
def branch_export(request):
	branches = Branches.public.all()
	candidates = Candidate.public.all()
	icandidates = ImportCandidate.public.all()

	#fill uop database with data in the forms filled in with details of students
	for candidate in candidates:
		_pref=[]
		for branch in branches:
			if candidate.owner == branch.owner :
				_pref.append(branch.name)
		start = len(_pref)
		for j in range(start,17):
			_pref.append('')
		Created=ImportCandidate.objects.get_or_create(roll_no=candidate.roll_no,u_name=candidate.u_name,p_branch=candidate.p_branch,cpi=candidate.cpi,cat=candidate.cat, pref0=_pref[0],
					pref1=_pref[1],pref2=_pref[2],pref3=_pref[3],pref4=_pref[4],pref5=_pref[5],pref6=_pref[6],pref7=_pref[7],pref8=_pref[8],pref9=_pref[9],
					pref10=_pref[10],pref11=_pref[11],pref12=_pref[12],pref13=_pref[13],pref14=_pref[14],pref15=_pref[15],pref16=_pref[16])
	#read from file
	with open( './input_options.csv','w') as CSVfile: 
		CSVwriter = csv.writer(CSVfile)
		for icandidate in icandidates:
			CSVrowList=[icandidate.roll_no, icandidate.u_name, icandidate.p_branch, icandidate.cpi, icandidate.cat, icandidate.pref0,
					icandidate.pref1, icandidate.pref2, icandidate.pref3, icandidate.pref4, icandidate.pref5, icandidate.pref6, icandidate.pref7, icandidate.pref8, icandidate.pref9,
					icandidate.pref10, icandidate.pref11, icandidate.pref12, icandidate.pref13, icandidate.pref14, icandidate.pref15, icandidate.pref16]
			CSVwriter.writerow(CSVrowList)
	
	#Class to send the details together in context	
	class Student:
		rollno=''
		name=''
		pBranch=''
		fBranch=''

	studentList=[]	
	with open('allotment.csv', 'r') as CSVfile :
		reader = csv.reader(CSVfile, delimiter = ',')
		for read in reader:
			student=Student()
			student.rollno=(read[0])
			student.name=(read[1])
			student.pBranch=(read[2])
			student.fBranch=(read[3])
			studentList.append(student)


	branches = Branches.public.all()
	candidates = Candidate.public.all()
	icandidates = ImportCandidate.public.all()
	context = {'branches':branches, 'candidates': candidates, 'studentList':studentList}
	return render(request, 'bc/branch_change.html', context)	

@login_required
def branch_import(request):	
	branches = Branches.public.all()
	candidates = Candidate.public.all()
	icandidates = ImportCandidate.public.all()
	for branch in branches:
		branch.delete()
	for candidate in candidates:
		candidate.delete()	
	for icandidate in icandidates:
		icandidate.delete()	

	with open('./input_options.csv' , 'r') as CSVfile :
		reader = csv.reader(CSVfile, delimiter = ',')
		try:
			for line in reader :
				_rollno=line[0]
				_name=line[1]
				_original_branch=line[2]
				_cpi=float(line[3])
				_category=line[4]
				_pref=line[5:]
				start = len(_pref)
				for j in range(start,17):
					_pref.append('')
				Created=ImportCandidate.objects.get_or_create(roll_no = _rollno,u_name=_name,p_branch=_original_branch,cpi=_cpi,cat=_category, pref0=_pref[0],
					pref1=_pref[1],pref2=_pref[2],pref3=_pref[3],pref4=_pref[4],pref5=_pref[5],pref6=_pref[6],pref7=_pref[7],pref8=_pref[8],pref9=_pref[9],
					pref10=_pref[10],pref11=_pref[11],pref12=_pref[12],pref13=_pref[13],pref14=_pref[14],pref15=_pref[15],pref16=_pref[16])
		except:
			print("Error in importing!!!")
	
	branch_change_algorithm()
		
	context = {'branches':branches}
	return render(request, 'bc/branch_list.html', context)	

	branches = Branches.public.all()
	candidates = Candidate.public.all()
	icandidates = ImportCandidate.public.all()
	context = {'branches':branches, 'candidates': candidates}
	return render(request, 'bc/branch_list.html', context)	

@login_required
def branch_algorithm(request):
	
	branch_change_algorithm()
	
	branches = Branches.public.all()
	candidates = Candidate.public.all()
	context = {'branches':branches, 'candidates': candidates}
	return render(request, 'bc/branch_list.html', context)

############################################### ALGORITHM ##################################################

import math

def branch_change_algorithm():	
	preferenceList={}	#{RollNo : [Branch1,...]}
	studentBranch={}	#{RollNo : [CurrentBranch,FinalBranch]}
	studentDetail={}			#{RollNo : [Name,CPI]}
	studentCurrentPreference={}		#{RollNo : index-in-PreferenceList}	
	ineligible=[]
	ineligibleDetail={}

	CPIList=[]			#[[CPI,Rollno]...]

	branchDetail={}     #{Branch:[Current Strengh,Lower Limit, Upper Limit]}
	branchOriginalDetail={}	#{Branch:[ Sanctioned Strength, Original Strength]}
	rejectedList={}  	#{Branch:[[RollNo,CPI],...]}
	acceptedList={}		#{Branch:[[RollNo,CPI],...]}

	beta=1.10
	alpha=0.75

	fileHandleIn=open('./input_programmes.csv', 'r')
	while True:
		l=fileHandleIn.readline();
		if l=='':
			break
		l.rstrip('\r\n')	
		l.rstrip(',')
		l=l.split(',')
		lower=math.ceil(alpha*int(l[1]))
		upper=beta*int(l[1])
		if (upper*10)%10>=5:
			upper=math.floor(upper)+1
		else:
			upper=math.floor(upper)	
		branchDetail[l[0]]=[int(l[2]), lower , upper]
		branchOriginalDetail[l[0]]=[l[1],str(int(l[2]))]
		rejectedList[l[0]]=[]
		acceptedList[l[0]]=[]
	fileHandleIn.close()
	
	fileHandleIn=open('./input_options.csv', 'r')
	ll=fileHandleIn.readlines();
	
	for i in range(len(ll)):
		ll[i]=ll[i].rstrip('\n')
		ll[i]=ll[i].rstrip(',')
		ll[i]=ll[i].split(',')
		
		if ((ll[i][4]=="GE" or ll[i][4]=="OBC") and float(ll[i][3])>=8.0) or (ll[i][4]!="GE" and ll[i][4]!="OBC" and float(ll[i][3])>=7.0) :
			if ll[i][0] in preferenceList:
				del preferenceList[ll[i][0]]
				preferenceList[ll[i][0]]= list()
				preferenceList[ll[i][0]].extend(ll[i][5:])
				while 'None' in preferenceList[ll[i][0]]:
					preferenceList[ll[i][0]].remove('None')
				while '' in preferenceList[ll[i][0]]:
					preferenceList[ll[i][0]].remove('')
			else:
				preferenceList[ll[i][0]]=ll[i][5:]	
				studentBranch[ll[i][0]]=[ll[i][2],ll[i][2]]
				studentDetail[ll[i][0]]=[ll[i][1],float(ll[i][3])]
				studentCurrentPreference[ll[i][0]]=0;
				CPIList.append([float(ll[i][3]),ll[i][0]])
				while 'None' in preferenceList[ll[i][0]]:
					preferenceList[ll[i][0]].remove('None')
				while '' in preferenceList[ll[i][0]]:
					preferenceList[ll[i][0]].remove('')
		else:
			if not ll[i][0] in ineligible:
				ineligible.append(ll[i][0])
			ineligibleDetail[ll[i][0]]=[ll[i][1],ll[i][2]]	

	CPIList[0:] = sorted(CPIList[0:] , key=(lambda l: -1*(l[0])))	
	
	CPIList_unchanged=[]
	CPIList_unchanged=CPIList[0:]
	fileHandleIn.close()

	##### Algorithm begins #####
	# iterate over the preferences of the candidates, picked in order of their CPI. If someone gets his first preference he
	# is removed from the queue and "finalised". Otherwise we keep on iterating untill the list becomes empty or there are no more changes!
	#-i.e. saturation is reached (saturation boolean just for that!) 	
	saturation=False
	while not saturation and len(CPIList)!=0:
		saturation=True # set to False if any changes occur
		i=0
		while i < len(CPIList):
			_student=CPIList[i]
			i+=1
			_rollno=_student[1]
			_cpi=_student[0] 
			_finalBranch=preferenceList[_rollno][studentCurrentPreference[_rollno]]
			_currentBranch=studentBranch[_rollno][1]
			
			flag=False
			if _cpi>=9.00:			#can neglect alpha condition
				flag=True
			elif branchDetail[_currentBranch][0]-1 >= branchDetail[_currentBranch][1]: #alpha condition	
				flag=True
			else:
				for cpiInList in CPIList_unchanged:			#someone with equal in source branch gets a branch change
					if cpiInList[0]==_cpi:
						rollNoInList=cpiInList[1]
						branchInList=studentBranch[rollNoInList]
						if branchInList[0]!=branchInList[1] and studentBranch[_rollno][0]==branchInList[0] and _rollno!=rollNoInList:
							flag=True
							break
				_acceptedList=acceptedList[_finalBranch]
				j=0
				while j<len(_acceptedList):		#someone with less or equal CPI is accepted
					rNo=_acceptedList[j]
					if studentDetail[rNo][1]<=_cpi:
						flag=True
						break
					j+=1
				
				'''studentCurrentPreference[rNo]=0
					_acceptedList.remove(rNo)
					branchDetail[studentBranch[rNo][0]][0]+=1
					branchDetail[_finalBranch][0]-=1	
					print("rejected")
					j-=1					 
				j+=1
				'''
			if flag:
				flag=False 		# Check other conditions	
				_acceptedList=acceptedList[_finalBranch]
				j=0
				while j < len(_acceptedList):		#someone with equal CPI is accepted
					rNo=_acceptedList[j]
					if studentDetail[rNo][1]==_cpi:
						flag=True
						#print("others with same cpi")
						break
					j+=1	
				if not flag:
					if branchDetail[_finalBranch][0]+1<=branchDetail[_finalBranch][2]:	# someone with >= cpi is rejected
						_rejectedList=rejectedList[_finalBranch]
						flag=True
						j=0
						while j<len(_rejectedList):
							rNo=_rejectedList[j]
							if studentDetail[rNo][1]>_cpi:
								flag=False
								break			
							j+=1	
			#Finally allotted or rejected...
			if flag:
				j=studentCurrentPreference[_rollno]
				_preferenceList=preferenceList[_rollno]
				for k in range(j,len(_preferenceList)):
					_branch=_preferenceList[k]
					if _rollno in rejectedList[_branch]:
						rejectedList[_branch].remove(_rollno)
						#print("rejected")
				try:
					acceptedList[_currentBranch].remove(_rollno)
				except:
					pass
				branchDetail[_currentBranch][0]-=1
				studentBranch[_rollno][1]=_finalBranch
				branchDetail[_finalBranch][0]+=1						 
				acceptedList[_finalBranch].append(_rollno)
				preferenceList[_rollno]=preferenceList[_rollno][:j]
				studentCurrentPreference[_rollno]=0
				if j==0:
					CPIList.remove(_student)
					i-=1
				saturation=False
			elif studentCurrentPreference[_rollno]<len(preferenceList[_rollno])-1:
				if not _rollno in rejectedList[_finalBranch]:
					rejectedList[_finalBranch].append(_rollno)
				studentCurrentPreference[_rollno]+=1
				i-=1
			else:
				if not _rollno in rejectedList[_finalBranch]:
					rejectedList[_finalBranch].append(_rollno)
				studentCurrentPreference[_rollno]=0	
		
	
	##### Allotment  ####
	fileHandleOut=open('allotment.csv','w')

	_finalRoll=[rollno for rollno in studentBranch]
	_finalRoll.extend(ineligible)
	_finalRoll.sort()
	for i in range(len(_finalRoll)):
		rollno=_finalRoll[i]
		if rollno in studentBranch:
			if studentBranch[rollno][0]==studentBranch[rollno][1]:
				fileHandleOut.write(rollno+','+studentDetail[rollno][0]+','+studentBranch[rollno][0]+',Branch Unchanged\r\n')
			else:
				fileHandleOut.write(rollno+','+studentDetail[rollno][0]+','+studentBranch[rollno][0]+','+studentBranch[rollno][1]+'\r\n')
		else:
			fileHandleOut.write(rollno+','+ineligibleDetail[rollno][0]+','+ineligibleDetail[rollno][1]+',Ineligible\r\n')	
	fileHandleOut.close()		
	#### Output_stats ###		
	fileHandleOut=open('output_stats.csv','w')
	listOfBranch=[branch for branch in branchDetail]
	listOfBranch.sort()

	fileHandleOut.write("Program,CutOff,Sanctioned Strength,Original Strength,Final Strength\n")
	for branch in listOfBranch:
		cutoff=10.0
		for rollNo in acceptedList[branch]:
			cutoff=min(cutoff,studentDetail[rollNo][1])	
		if acceptedList[branch]==[]:
			fileHandleOut.write(branch+',NA,'+branchOriginalDetail[branch][0]+','+branchOriginalDetail[branch][1]+','+repr(branchDetail[branch][0])+'\r\n')
		else:
			fileHandleOut.write(branch+','+str(cutoff)+','+branchOriginalDetail[branch][0]+','+branchOriginalDetail[branch][1]+','+repr(branchDetail[branch][0])+'\r\n')			
	fileHandleOut.close()	
	

