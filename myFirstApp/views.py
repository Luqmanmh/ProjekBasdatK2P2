from django.shortcuts import render, redirect
from .models import employee, child, parent, toy, equipment, supply

#view
def index(request):
    return render(request, 'index.html')

def inner(request):
    return render(request, 'inner.html')

def regch(request):
    return render(request, 'regch.html')

def children(request):
    ch_in = child.objects.filter(in_con = "Ya").order_by("child_id")
    query = request.GET.get('q', '')
    results = []

    if query:
        results = child.objects.filter(child_name__icontains=query)
    else :
        results = child.objects.all().order_by("child_id")

    table1 = []

    for i in results:
        employees = employee.objects.get(employee_id=i.care_taker_id)
        childs = child.objects.get(child_id=i.child_id)
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
    return render(request, 'children.html', {'query': query, 'results': results, 'table2': table2, 'table1': table1})

def employees(request):
    em_dt = employee.objects.all().order_by("employee_id")
    context = {
        "em_dt": em_dt,
    }
    return render(request, 'employee.html', context)

def logistics(request):
    toy_dt = toy.objects.all().order_by("toy_id")
    eq_dt = equipment.objects.all().order_by("equipment_id")
    sp_dt = supply.objects.all().order_by("supply_id")

    tablet = []
    for i in toy_dt:
        employees = employee.objects.get(employee_id=i.resp_id)
        toys = toy.objects.get(toy_id=i.toy_id)
        toyarr = {
            'employees':employees,
            'toys': toys,
        }
        tablet.append(toyarr)

    tablee = []
    for i in eq_dt:
        employees = employee.objects.get(employee_id=i.resp_id)
        eqs = equipment.objects.get(equipment_id=i.equipment_id)
        eqarr = {
            'employees':employees,
            'eqs':eqs,
        }
        tablee.append(eqarr)

    tables = []
    for i in sp_dt:
        employees = employee.objects.get(employee_id=i.resp_id)
        sps = supply.objects.get(supply_id=i.supply_id)
        sparr = {
            'employees': employees,
            'sps': sps,
        }
        tables.append(sparr)

    context = {
        "toy_dt": tablet,
        "eq_dt": tablee,
        "sp_dt": tables,
    }
    return render(request, 'logistics.html', context)

def parents(request):
    pr_dt = parent.objects.all().order_by("parent_id").values()
    context = {
        "pr_dt": pr_dt,
    }
    return render(request, 'parent.html', context)

def add_child(request):
    em = employee.objects.filter(employee_department = "Pengasuh")
    pr = parent.objects.all()
    context = {
        "pr":pr,
        "em": em
    }
    return render(request, 'add_kid.html', context)

def add_parent(request):
    return render(request, 'add_parent.html')

def add_employee(request):
    return render(request, 'add_employee.html')

def add_item(request):
    em = employee.objects.filter(employee_department = "Logistik")
    context = {
        "em":em
    }
    return render(request, 'add_item.html', context)

def add_supply(request):
    em = employee.objects.filter(employee_department = "Logistik")
    context = {
        "em":em
    }
    return render(request, 'add_supply.html', context)

def add_toy(request):
    em = employee.objects.filter(employee_department = "Logistik")
    context = {
        "em":em
    }
    return render(request, 'add_toy.html', context)

def parent_1(request, ch_id):
    ch = child.objects.get(child_id = ch_id)
    pr_1 = parent.objects.get(parent_id = ch.parent_id)
    context = {
        "ch":ch,
        "pr": pr_1,
    }
    return render(request, 'parentone.html', context)


#add
def push_add_item(request):
    eqid = request.POST['itemid']
    eqname = request.POST['itemname']
    eqcon = request.POST['itemcon']
    eqresp = request.POST['itemresp']

    eq = equipment(equipment_id = eqid, equipment_name = eqname, resp_id = eqresp, equipment_con = eqcon)
    eq.save()

    return redirect('/logistics')

def push_add_toy(request):
    toyid = request.POST['toyid']
    toyname = request.POST['toyname']
    toyresp = request.POST['toyresp']
    toycon = request.POST['toycon']
    
    itoy = toy(toy_id = toyid, toy_name = toyname, toy_con = toycon, resp_id = toyresp)
    itoy.save()

    return redirect('/logistics')

def push_add_supply(request):
    suppid = request.POST['suppid']
    suppname = request.POST['suppname']
    suppamt = request.POST['suppamt']
    suppresp = request.POST['suppresp']

    supp = supply(supply_id = suppid, supply_name = suppname, supply_amt = suppamt, resp_id = suppresp)
    supp.save()

    return redirect('/logistics')

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

def deleteeq(request, eq_id):

    eq = equipment.objects.get(equipment_id = eq_id)
    eq.delete()

    return redirect('/logistics')

def deletetoy(request, toy_id):

    toys = toy.objects.get(toy_id = toy_id)
    toys.delete()

    return redirect('/logistics')

def deletesupp(request, supp_id):

    supp = supply.objects.get(supply_id = supp_id)
    supp.delete()

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

def edit_eq(request, eq_id):
    eq = equipment.objects.get(equipment_id = eq_id)
    em = employee.objects.filter(employee_department = "Logistik")
    context = {
        'eq': eq,
        "em":em
    }

    return render(request, "edit_item.html", context)
def push_edit_eq(request):
    eqid = request.POST['itemid']
    new_eqname = request.POST['itemname']
    new_eqcon = request.POST['itemcon']
    new_eqresp = request.POST['itemresp']

    eq = equipment.objects.get(equipment_id = eqid)
    eq.equipment_name = new_eqname
    eq.equipment_con = new_eqcon
    eq.resp_id = new_eqresp
    eq.save()

    return redirect('/logistics')

def edit_toy(request, toy_id):
    toys = toy.objects.get(toy_id = toy_id)
    em = employee.objects.filter(employee_department = "Logistik")
    context = {
        'toy': toys,
        "em":em
    }

    return render(request, "edit_toy.html", context)
def push_edit_toy(request):
    toyid = request.POST['toyid']
    new_toyname = request.POST['toyname']
    new_toycon = request.POST['toycon']
    new_toyresp = request.POST['toyresp']

    toys = toy.objects.get(toy_id = toyid)
    toys.toy_name = new_toyname
    toys.toy_con = new_toycon
    toys.resp_id = new_toyresp
    toys.save()

    return redirect('/logistics')

def edit_supp(request, supp_id):
    supp = supply.objects.get(supply_id = supp_id)
    em = employee.objects.filter(employee_department = "Logistik")
    context = {
        'sp': supp,
        "em": em
    }

    return render(request, "edit_supply.html", context)
def push_edit_supp(request):
    suppid = request.POST['suppid']
    new_suppname = request.POST['suppname']
    new_suppamt = request.POST['suppamt']
    new_suppresp = request.POST['suppresp']

    sp = supply.objects.get(supply_id = suppid)
    sp.supply_name = new_suppname
    sp.supply_amt = new_suppamt
    sp.resp_id = new_suppresp
    sp.save()

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
    

def res_att(request):
    new_incon = request.POST['kidatt']

    children = child.objects.all()
    for ch in children:
        ch.in_con = new_incon
        ch.save()

    return redirect('/children')
    
    


