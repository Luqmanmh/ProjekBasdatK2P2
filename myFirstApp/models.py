from django.db import models
from datetime import date

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

class nonconsumable(models.Model):
    con = [("Buruk", "Buruk"), ("Baik", "Baik")]
    kind = [("Furn", "Furn"), ("Toy", "Toy")]
    nocon_id = models.CharField(max_length=7, primary_key=True)
    nocon_name = models.CharField(max_length=100)
    nocon_con = models.CharField(max_length=5, choices=con)
    nocon_kind = models.CharField(max_length=10, choices=kind)
    resp = models.ForeignKey(employee, null=True, on_delete=models.PROTECT)

class consumable(models.Model):
    kind = [("Food", "Food"), ("Med", "Med"), ("Util", "Util")]
    con_id = models.CharField(max_length=7, primary_key=True)
    con_name = models.CharField(max_length=100)
    con_amt = models.CharField(max_length=100)
    con_kind = models.CharField(max_length=10, choices=kind)
    resp = models.ForeignKey(employee, null=True, on_delete=models.PROTECT)

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
    care_taker = models.ForeignKey(employee, null=True, on_delete=models.PROTECT)

    class Meta:
        managed = True

    @property
    def age(self):
      if self.child_birth:
        today = date.today()
        age = today.year - self.child_birth.year - ((today.month, today.day) < (self.child_birth.month, self.child_birth.day))
        return age
      return None

