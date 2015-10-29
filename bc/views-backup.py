from django.shortcuts import render, render_to_response, get_object_or_404, redirect
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from .forms import BranchForm, QueryForm 
from .models import Branches, Query

import csv
# Create your views here.
'''
def login_user(request):
	state = "Please log in above ..."
	username=password=''
	if request.POST:
		username = request.POST.get('username')
		password = request.POST.get('password')

		user = authenticate(username=username,password=password)

		if user is not None:
			if user.is_active:
				login(request, user)
				state = "You're successfully logged in!"
				return render(request, 'bc/branch_user.html', context)
			else:
				state = "Your account is not active, please contact the site admin!"
		else:
			state = "Your username and/or password were incorrect!"	
	return render_to_response('auth.html',{'state':state, 'username':username})
'''
prog_data = []
with open('./bc/input_programmes.csv' , 'r') as csvfile :
	reader = csv.reader(csvfile, delimiter = ',')
	for row in reader :
		prog_data.append(row)

def branch_list(request):
	branches = Branches.public.all()
	context = {'branches':branches}
	return render(request, 'bc/branch_list.html', context)		

def branch_user(request, username):
	user = get_object_or_404(User, username=username)
	if request.user == user:
		branches = Branches.public.filter(owner=request.user)
	context = {'branches': branches, 'owner':user}
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
	return render(request, 'bc/form.html',{'form':form,'create':True})

@login_required
def branch_edit(request, pk):
	branch = get_object_or_404(Branches, pk=pk)
	if branch.owner != request.user and not request.user.is_superuser:
		raise PermissionDenied
	if request.method == 'POST':
		form = BranchForm(instance=branch, data=request.POST)
		if form.is_valid():
			form.save()
			return redirect('bc_branch_user', username=request.user.username)
	else:
		form=BranchForm(instance=branch)		
	return render(request,'bc/form.html',{'form':form, 'create':False,'branch':branch})		

@login_required
def branch_delete(request, pk):
	branch = get_object_or_404(Branches,pk=pk)
	if branch.owner != request.user:
		raise PermissionDenied
	branch.delete()
	return redirect('bc_branch_user',username=request.user.username)

@login_required
def branch_export():
	x=1
@login_required
def branch_import():	
	x=1
@login_required
def branch_algorithm():	
	x=1
'''	
def main(request)

def user_loggedin(request, username):
	user = get_object_or_404(User, username=username)
	if request.user == user:
'''