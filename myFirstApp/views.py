from django.shortcuts import render, redirect
from .models import employee, child, parent, consumable, nonconsumable

#view
def index(request):
    return render(request, 'index.html')

def inner(request):
    return render(request, 'inner.html')

def regch(request):
    return render(request, 'regch.html')

def children(request):
    ch_in = child.objects.filter(in_con = "Ya").order_by("child_id")
    emp= employee.objects.all()
    query = request.GET.get('q', '')
    results = []

    if query:
        results = child.objects.filter(child_name__icontains=query)
    else :
        results = child.objects.all().order_by("child_id")

    table1 = []

    for i in results:
        childs = child.objects.get(child_id=i.child_id)
        employees = employee.objects.get(employee_id=i.care_taker_id)      
        
        childarr1 = {
            'employees': employees,
            'childs': childs,
        }
        table1.append(childarr1)

    table2 = []

    for i in ch_in:
        employees = employee.objects.get(employee_id=i.care_taker_id)
        childs = child.objects.get(child_id=i.child_id)
        childsarr2 = {
            'employees': employees,
            'childs': childs,
        }
        table2.append(childsarr2)
    context ={
        'query': query,
        'results': results,
        'table2': table2,
        'table1': table1
    }
    return render(request, 'children.html', context)

def employees(request):
    em_dt = employee.objects.all().order_by("employee_id")
    context = {
        "em_dt": em_dt,
    }
    return render(request, 'employee.html', context)

def logistics(request):
    fd_dt = consumable.objects.filter(con_kind = "Food")
    med_dt = consumable.objects.filter(con_kind = "Med")
    utl_dt = consumable.objects.filter(con_kind = "Util")

    tablef = []
    for i in fd_dt:
        employees = employee.objects.get(employee_id=i.resp_id)
        food = consumable.objects.get(con_id=i.con_id)
        foodarr = {
            'emps':employees,
            'foods': food,
        }
        tablef.append(foodarr)

    tablem = []
    for i in med_dt:
        employees = employee.objects.get(employee_id=i.resp_id)
        meds = consumable.objects.get(con_id=i.con_id)
        eqarr = {
            'emps':employees,
            'meds':meds,
        }
        tablem.append(eqarr)

    tableu = []
    for i in utl_dt:
        employees = employee.objects.get(employee_id=i.resp_id)
        utls = consumable.objects.get(con_id=i.con_id)
        sparr = {
            'emps': employees,
            'utils': utls,
        }
        tableu.append(sparr)

    frn_dt = nonconsumable.objects.filter(nocon_kind = "Furn")
    toy_dt = nonconsumable.objects.filter(nocon_kind = "Toy")

    tabler = []
    for i in frn_dt:
        employees = employee.objects.get(employee_id=i.resp_id)
        frns = nonconsumable.objects.get(nocon_id=i.nocon_id)
        frnarr = {
            'emps': employees,
            'furns': frns,
        }
        tabler.append(frnarr)
    
    tablet = []
    for i in toy_dt:
        employees = employee.objects.get(employee_id=i.resp_id)
        toys = nonconsumable.objects.get(nocon_id=i.nocon_id)
        toyarr = {
            'emps': employees,
            'toys': toys,
        }
        tablet.append(toyarr)

    context = {
        "med" : tablem,
        "util" : tableu,
        "food" : tablef,
        "furn" : tabler,
        "toy" : tablet,
    }
    return render(request, 'logistics.html', context)

def parents(request):
    pr_dt = parent.objects.all().order_by("parent_id").values()
    context = {
        "pr_dt": pr_dt,
    }
    return render(request, 'parent.html', context)

def parent_1(request, ch_id):
    ch = child.objects.get(child_id = ch_id)
    pr_1 = parent.objects.get(parent_id = ch.parent_id)
    context = {
        "ch":ch,
        "pr": pr_1,
    }
    return render(request, 'parentone.html', context)


#add
def add_con(request):
    em = employee.objects.filter(employee_department = "Logistik")
    context = {
        "em":em
    }
    return render(request, 'add_consumable.html', context)
def push_add_con(request):
    conid = request.POST['conid']
    conname = request.POST['conname']
    conamt = request.POST['conamt']
    conkind = request.POST['conkind']
    conresp = request.POST['conresp']

    con = consumable(con_id = conid, con_name = conname, con_amt = conamt, con_kind = conkind, resp_id = conresp )
    con.save()

    return redirect('/logistics')

def add_nocon(request):
    em = employee.objects.filter(employee_department = "Logistik")
    context = {
        "em":em
    }
    return render(request, 'add_nonconsumable.html', context)
def push_add_nocon(request):
    noconid = request.POST['noconid']
    noconname = request.POST['noconname']
    noconcon = request.POST['noconcon']
    noconkind = request.POST['noconkind']
    noconresp = request.POST['noconresp']

    nocon = nonconsumable(nocon_id = noconid, nocon_name = noconname, nocon_con = noconcon, nocon_kind = noconkind, resp_id = noconresp )
    nocon.save()

    return redirect('/logistics')

def add_employee(request):
    return render(request, 'add_employee.html')
def push_add_employee(request):
    empid = request.POST['empid']
    empname = request.POST['empname']
    empbd = request.POST['empage']
    empgend = request.POST['empgend']
    empaddr = request.POST['empaddr']
    empph = request.POST['empph']
    empdp = request.POST['empdp']

    emp = employee(employee_id = empid, employee_name = empname, employee_birth = empbd, employee_address = empaddr, employee_phone = empph, employee_gender = empgend, employee_department = empdp)
    emp.save()

    return redirect('/employee')

def add_child(request):
    em = employee.objects.filter(employee_department = "Pengasuh")
    pr = parent.objects.all()
    context = {
        "pr":pr,
        "em": em
    }
    return render(request, 'add_kid.html', context)
def push_add_kid(request):
    kidid = request.POST['kidid']
    kidname = request.POST['kidname']
    kidbd = request.POST['kidage']
    kidgend = request.POST['kidgend']
    kidill = request.POST['kidill']
    kidpr = request.POST['prid']
    kidcr = request.POST['empid']
    kiddr = request.POST['droptime']
    kidpk = request.POST['picktime']
    kidatt = request.POST['kidatt']

    kid = child(child_id = kidid, child_name = kidname, child_gender = kidgend, disease = kidill, child_birth = kidbd, in_time = kiddr, out_time = kidpk, parent_id = kidpr, care_taker_id = kidcr, in_con = kidatt)
    kid.save()

    return redirect('/children')

def add_parent(request):
    return render(request, 'add_parent.html')
def push_add_parent(request):
    prid = request.POST['prid']
    prmname = request.POST['prmname']
    prmph = request.POST['prmph']
    prfname = request.POST['prfname']
    prfph = request.POST['prfph']
    praddr = request.POST['praddr']

    pr = parent(parent_id = prid, f_name = prfname, m_name = prmname, f_phone = prfph, m_phone = prmph, parent_address = praddr)
    pr.save()

    return redirect('/parent')


#delete
def deletech(request, child_id):

    kid = child.objects.get(child_id = child_id)
    kid.delete()

    return redirect('/children')

def deletepr(request, parent_id):

    pr = parent.objects.get(parent_id = parent_id)
    pr.delete()

    return redirect('/parent')

def deleteem(request, em_id):

    emp = employee.objects.get(employee_id = em_id)
    emp.delete()

    return redirect('/employee')

def deletecon(request, con_id):

    con = consumable.objects.get(con_id = con_id)
    con.delete()

    return redirect('/logistics')

def deletenocon(request, nocon_id):

    nocon = nonconsumable.objects.get(nocon_id = nocon_id)
    nocon.delete()

    return redirect('/logistics')


#edit
def edit_pr(request, parent_id):
    pr_1 = parent.objects.get(parent_id = parent_id)
    context = {
        "pr_1": pr_1
    }
    return render(request, 'edit_parent.html', context)
def push_edit_pr(request):
    prid = request.POST['prid']
    new_prmname = request.POST['prmname']
    new_prmph = request.POST['prmph']
    new_prfname = request.POST['prfname']
    new_prfph = request.POST['prfph']
    new_praddr = request.POST['praddr']

    pr = parent.objects.get(parent_id = prid)
    pr.f_name = new_prfname
    pr.m_name = new_prmname
    pr.f_phone = new_prfph
    pr.m_phone = new_prmph
    pr.parent_address = new_praddr
    pr.save()

    return redirect('/parent')

def edit_em(request, em_id):
    em = employee.objects.get(employee_id = em_id)
    context = {
        "em": em
    }
    return render(request, 'edit_employee.html', context)
def push_edit_em(request):
    emid = request.POST['empid']
    new_emname = request.POST['empname']
    new_embd = request.POST['empage']
    new_emgend = request.POST['empgend']
    new_emaddr = request.POST['empaddr']
    new_emph = request.POST['empph']
    new_empdp = request.POST['empdp']

    em = employee.objects.get(employee_id = emid)
    em.employee_name = new_emname
    em.employee_birth = new_embd
    em.employee_address = new_emaddr
    em.employee_phone = new_emph
    em.employee_gender = new_emgend
    em.employee_department = new_empdp
    em.save()

    return redirect('/employee')

def edit_kid(request, ch_id):
    ch = child.objects.get(child_id = ch_id)
    em = employee.objects.filter(employee_department = "Pengasuh")
    pr = parent.objects.all()
    context = {
        "ch": ch,
        "em": em,
        "pr": pr
    }
    return render(request, 'edit_kid.html', context)
def push_edit_kid(request):
    kidid = request.POST['kidid']
    new_kidname = request.POST['kidname']
    new_kidbd = request.POST['kidage']
    new_kidgend = request.POST['kidgend']
    new_kidill = request.POST['kidill']
    new_prid = request.POST['prid']
    new_emid = request.POST['empid']
    new_dtime = request.POST['droptime']
    new_ptime = request.POST['picktime']

    ch = child.objects.get(child_id = kidid)
    ch.child_name = new_kidname
    ch.child_birth = new_kidbd
    ch.child_gender = new_kidgend
    ch.disease = new_kidill
    ch.parent_id = new_prid
    ch.care_taker_id = new_emid
    ch.in_time = new_dtime
    ch.out_time = new_ptime
    ch.save()

    return redirect('/children')

def edit_con(request, con_id):
    con = consumable.objects.get(con_id = con_id)
    em = employee.objects.filter(employee_department = "Logistik")
    context = {
        "con": con,
        "em": em
    }

    return render(request, "edit_consumable.html", context)
def push_edit_con(request):
    conid = request.POST['conid']
    new_conname = request.POST['conname']
    new_conamt = request.POST['conamt']
    new_conresp = request.POST['conresp']
    new_conkind = request.POST['conkind']

    con = consumable.objects.get(con_id = conid)
    con.con_name = new_conname
    con.con_amt = new_conamt
    con.con_kind = new_conkind
    con.resp_id = new_conresp
    
    con.save()

    return redirect('/logistics')

def edit_nocon(request, nocon_id):
    nocon = nonconsumable.objects.get(nocon_id = nocon_id)
    em = employee.objects.filter(employee_department = "Logistik")
    context = {
        "nocon": nocon,
        "em": em
    }

    return render(request, "edit_nonconsumable.html", context)
def push_edit_nocon(request):
    noconid = request.POST['noconid']
    new_noconname = request.POST['noconname']
    new_noconcon = request.POST['noconcon']
    new_noconresp = request.POST['noconresp']
    new_noconkind = request.POST['noconkind']

    nocon = nonconsumable.objects.get(nocon_id = noconid)
    nocon.con_name = new_noconname
    nocon.con_amt = new_noconcon
    nocon.con_kind = new_noconkind
    nocon.resp_id = new_noconresp
    
    nocon.save()

    return redirect('/logistics')

def att_kid(request, ch_id):
    ch = child.objects.get(child_id = ch_id)
    context = {
        "ch": ch
    }
    return render(request, 'attendance.html', context)
def push_att_kid(request):
    kidid = request.POST['kidid']
    new_dtime = request.POST['droptime']
    new_ptime = request.POST['picktime']
    new_incon = request.POST['kidatt']

    ch = child.objects.get(child_id = kidid)
    ch.in_time = new_dtime
    ch.out_time = new_ptime
    ch.in_con = new_incon
    ch.save()

    return redirect('/children')
    

#reset attendance
def res_att(request):
    new_incon = request.POST['kidatt']

    children = child.objects.all()
    for ch in children:
        ch.in_con = new_incon
        ch.save()

    return redirect('/children')
    
    


