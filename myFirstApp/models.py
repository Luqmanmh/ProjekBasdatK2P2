from django.db import models

class employee(models.Model):
    DP_DT = [("Pengasuh", "Pengasuh"), ("Logistik", "Logistik")]
    gender = [("P", "P"), ("L", "L")]
    employee_id = models.CharField(max_length=7, primary_key=True)
    employee_name = models.CharField(max_length=200)
    employee_birth = models.DateField()
    employee_gender = models.CharField(max_length=2, choices=gender)
    employee_address = models.TextField()
    employee_phone = models.CharField(max_length=14)
    employee_department = models.CharField(max_length=12, choices=DP_DT)

class toy(models.Model):
    con = [("Buruk", "Buruk"), ("Baik", "Baik")]
    toy_id = models.CharField(max_length=7, primary_key=True)
    toy_name = models.CharField(max_length=100)
    toy_con = models.CharField(max_length=5, choices=con)
    resp = models.ForeignKey(employee, null=True, on_delete=models.SET_NULL)

    class Meta:
        managed = True


class equipment(models.Model):
    con = [("Buruk", "Buruk"), ("Baik", "Baik")]
    equipment_id = models.CharField(max_length=7, primary_key=True)
    equipment_name = models.CharField(max_length=100)
    equipment_con = models.CharField(max_length=5, choices=con)
    resp = models.ForeignKey(employee, null=True, on_delete=models.SET_NULL)

    class Meta:
        managed = True


class supply(models.Model):
    supply_id = models.CharField(max_length=7, primary_key=True)
    supply_name = models.CharField(max_length=100)
    supply_amt = models.CharField(max_length=100)
    resp = models.ForeignKey(employee, null=True, on_delete=models.SET_NULL)

    class Meta:
        managed = True


class parent(models.Model):
    parent_id = models.CharField(max_length=7, primary_key=True)
    f_name = models.CharField(max_length=200, null=True)
    m_name = models.CharField(max_length=200, null=True)
    f_phone = models.CharField(max_length=14, null=True)
    m_phone = models.CharField(max_length=14, null=True)
    parent_address = models.TextField()

class child(models.Model):
    gender = [("P", "P"), ("L", "L")]
    con = [("Ya", "Ya"), ("Tidak", "Tidak")]
    child_id = models.CharField(max_length=7, primary_key=True)
    child_name = models.CharField(max_length=200)
    child_gender = models.CharField(max_length=2, choices=gender)
    child_birth = models.DateField()
    disease = models.TextField(null=True)
    in_time = models.TimeField()
    out_time = models.TimeField()
    in_con = models.CharField(max_length=6, choices=con)
    parent = models.ForeignKey(parent, on_delete=models.CASCADE)
    care_taker = models.ForeignKey(employee, null=True, on_delete=models.SET_NULL)

    class Meta:
        managed = True

