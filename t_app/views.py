from django.shortcuts import render,redirect
from .models import *
from itertools import combinations
from django.contrib.auth.models import auth
from django.contrib.auth import login
# Create your views here.
def home(request):
    team=Team.objects.all()
    return  render(request,"home.html",{"len":len(team)})

def registration(request):
    if request.method=="POST":
        name=request.POST["name"]
        manager=request.POST["manager"]
        coach=request.POST['coach']
        contact=request.POST['contact']
        players=request.POST.getlist('pname[]')
        team=Team(name=name,manager=manager,coach=coach,contact=contact)
        team.save()
        for i in players:
            player=Players(team=team,name=i)
            player.save()
        return redirect('home')
    
    return render(request,'register.html')


def team(request):
    team=Team.objects.all()
    return render(request,'team.html',{"team":team,"len":len(team)})

def team_details(request,id):
    team=Team.objects.get(id=id)
    players=Players.objects.filter(team=id)
    all_team=Team.objects.all()
    team_list=[i.name for i in all_team]
    groupA=team_list[:5]
    groupB=team_list[5:]
    
    # Generate combinations of 2 items
    A = list(combinations(groupA, 2))
    B=list(combinations(groupB,2))

    #match scheduling
    try:
        fix_list=[A[3],A[7],B[3],B[7],A[9],A[4],B[9],B[4],A[1],A[5],B[1],B[5],A[2],A[6],B[2],B[6],A[8],A[0],B[8],B[0]]
    except:
        fix_list=[]    
    dates=["30-9-2023","30-9-2023",'1-10-2023','1-10-2023','2-10-2023','2-10-2023','3-10-2023','3-10-2023','4-10-2023','4-10-2023','5-10-2023','5-10-2023','6-10-2023','6-10-2023','7-10-2023','7-10-2023','8-10-2023','8-10-2023','9-10-2023','9-10-2023']
    times=["5:30 PM","7:30 PM"]*10
    venue=["KOZHIKODE","KANNUR","MALAPPURAM","THRISSUR","PALAKKADU"]*4
    zipped_lists = list(zip(fix_list,dates,times,venue))

    return render(request,'team_detail.html',{"player":players,"team":team,"len":len(all_team),"fix":zipped_lists})

def fixture(request):
    all_team=Team.objects.all()
    team_list=[i.name for i in all_team]
    groupA=team_list[:5]
    groupB=team_list[5:]
    
    # Generate combinations of 2 items
    A = list(combinations(groupA, 2))
    B=list(combinations(groupB,2))

    #match scheduling
    try:
        fix_list=[A[3],A[7],B[3],B[7],A[9],A[4],B[9],B[4],A[1],A[5],B[1],B[5],A[2],A[6],B[2],B[6],A[8],A[0],B[8],B[0]]
    except:
        fix_list=[]   
    dates=["30-9-2023","30-9-2023",'1-10-2023','1-10-2023','2-10-2023','2-10-2023','3-10-2023','3-10-2023','4-10-2023','4-10-2023','5-10-2023','5-10-2023','6-10-2023','6-10-2023','7-10-2023','7-10-2023','8-10-2023','8-10-2023','9-10-2023','9-10-2023']
    times=["5:30 PM","7:30 PM"]*10
    venue=["KOZHIKODE","KANNUR","MALAPPURAM","THRISSUR","PALAKKADU"]*4
    zipped_lists = list(zip(fix_list,dates,times,venue))
    context={
        "len":len(all_team),
        "A":groupA,
        "B":groupB,
        "fix":zipped_lists
    }
    return render(request,'fixture.html',context)

def login_view(request):
    team=Team.objects.all()
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            if user.is_staff:
                login(request,user)
                return redirect('admin_home')
            else:
                return redirect('login_view')  
        else:
            return redirect('login_view')    
    return render(request,'login.html',{"len":len(team)})

def admin_home(request):
    all_team=Team.objects.all()
    team_list=[i.name for i in all_team]
    groupA=team_list[:5]
    groupB=team_list[5:]
    
    # Generate combinations of 2 items
    A = list(combinations(groupA, 2))
    B=list(combinations(groupB,2))
    try:
        fix_list=[A[3],A[7],B[3],B[7],A[9],A[4],B[9],B[4],A[1],A[5],B[1],B[5],A[2],A[6],B[2],B[6],A[8],A[0],B[8],B[0]]
    except:
        fix_list=[]
    scores=Score.objects.all()
    return render(request,'admin_home.html',{"len":len(all_team),"fix":fix_list,"score":scores})

def score(request):
    if request.method=="POST":
        score=request.POST['scores']
        match_no=request.POST['match_no']
        if Score.objects.filter(match_no=match_no).exists():
            scores=Score.objects.get(match_no=match_no)
            scores.match_no=match_no
            scores.score=score
            scores.save()
            return redirect('admin_home')
            
        else:
            score=Score(match_no=match_no,score=score)
            score.save()
            print("successs")
            return redirect('admin_home')