from django.shortcuts import render
from . import core
from django.http import HttpResponse
import pandas as pd

# Create your views here.
def index(req):
    context = {}
    return render(req, 'polls/index.html', context)

def puResult(req):
    conn = core.create_connection()
    if req.method == 'POST':
        pu_name = req.POST.get('polling_unit_name')
        sql = ''
        if core.validate_pu(pu_name):
            sql = f"SELECT polling_unit.polling_unit_name, announced_pu_results.party_abbreviation, announced_pu_results.party_score FROM announced_pu_results INNER JOIN polling_unit ON announced_pu_results.polling_unit_uniqueid=polling_unit.uniqueid WHERE polling_unit.polling_unit_name='{pu_name}'"

            with conn:
                csr = conn.cursor()
                csr.execute(sql)
                result = csr.fetchall()
                pu_res_df = pd.DataFrame(list(result), columns=['Polling_Unit_Name', 'Party', 'Party_score'])
                csr.close()
                return render(req, 'polls/puresult.html', {'pu_res_df': pu_res_df})
        
        return HttpResponse('Invalid Polling Unit Name')
    
    return render(req, 'polls/puresult.html')


def lgaResult(req):
    # Create a connection
    conn = core.create_connection()

    lga_name = str(input()).strip()
    sql = ''
    if core.validate_lga(lga_name): 
        sql =f"SELECT lga.lga_name, polling_unit.polling_unit_name, sum(announced_pu_results.party_score) FROM companydb.polling_unit INNER JOIN lga on polling_unit.lga_id=lga.lga_id LEFT JOIN announced_pu_results on polling_unit.uniqueid=announced_pu_results.polling_unit_uniqueid WHERE lga_name='{lga_name}' GROUP BY polling_unit_name;"

    with conn:
        with conn.cursor() as csr :
            csr.execute(sql)
            result = csr.fetchall()        
            df = pd.DataFrame(list(result), columns=['lga', 'Polling Unit Name', 'Sum'])
            
    lgs = lgas = ['Aniocha North', 'Aniocha - South', 'Ethiope East', 'Ethiope West', 'Ika North - East', 'Ika - South', 'Isoko North', 'Isoko South', 'Ndokwa East', 'Ndokwa West', 'Okpe', 'Oshimili - North', 'Oshimili - South', 'Patani', 'Sapele', 'Udu', 'Ughelli North', 'Ughelli South', 'Ukwuani', 'Uvwie', 'Bomadi', 'Burutu', 'Warri North', 'Warri South', 'Warri South West']
    return render(req, 'polls/lgaresult.html', {'df': df, 'lgas': lgas})

def newResult(req):
    return render(req, 'polls/newresult.html', {})