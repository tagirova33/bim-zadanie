from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView
from .forms import *
from docxtpl import DocxTemplate
from docx import Document
from django.http import FileResponse
import os
from docx2pdf import convert
from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives
import subprocess
from .models import *
import datetime


def manual(request):
    return render(request, 'manual.html')
#Функция для страницы с выбором ОКС и бим-юзов
def first(request):
    if request.method == "POST":
        oks = OKSForm(request.POST)
        bim = BimUseForm(request.POST)
        request.session['user'] = request.POST.get('oks')
        return redirect('first/second')
    else:
        oks = OKSForm()
        bim = BimUseForm()
    return render(request, 'first.html', context = {'oks': oks, 'bim':bim})
#Функция для работы с формами объектов ОКС
def second(request):
    if request.method == "POST":
        results = request.session['user']
        if results == "Linear":
            return lin(request)
        elif results == "Citizen":
            return cit(request)
        else:
            return indus(request)
    else:
        results = request.session['user']
        if results == "Linear":
            linear = LinearForm()
            linear_file = LinearFormFile()
            user = UserForm()
            return render(request, 'linear.html', context = {'user': user, 'linear': linear,'linear_file':linear_file})
        elif results == "Citizen":
            civil = CivilForm()
            civil_file = CivilFormFile()
            user = UserForm()
            return render(request, 'civil.html', context={'user': user,'civil': civil,'civil_file':civil_file})
        else:
            industrial = IndustrialForm()
            industrial_file = IndustrialFormFile()
            user = UserForm()
            return render(request, 'industrial.html', context={'user': user,'industr': industrial,'industrial_file':industrial_file})
   # return HttpResponse('<h1>Page not found</h1>')


def cit(request):
    civil = CivilForm(request.POST, request.FILES)
    civil_file = CivilFormFile(request.POST, request.FILES)
    user = UserForm(request.POST)
    files = request.FILES.getlist('document')
    print(civil.errors)
    if civil.is_valid() and user.is_valid():	
        email = user.cleaned_data.get('email')
        objectname = civil.cleaned_data.get('objectname')
        document = DocxTemplate(r"ТЗ_ГражданскийОбъект.docx")
        context = {'objectname': civil.cleaned_data.get('objectname'),
                   'date':datetime.date.today(),
                   'objectaddress': civil.cleaned_data.get('objectaddress'),
                   'osnovanie': civil.cleaned_data.get('osnovanie'),
                   'rekviziti_osnovanie': civil.cleaned_data.get('rekviziti_osnovanie'),
                   'zastroichik': civil.cleaned_data.get('zastroichik'),
                   'investor': civil.cleaned_data.get('investor'),
                   'projectorganization': civil.cleaned_data.get('projectorganization'),
                   'vidrabot': civil.cleaned_data.get('vidrabot'),
                   'finansirovanie': civil.cleaned_data.get('finansirovanie'),
                   'finansirovanie_rekviziti': civil.cleaned_data.get('finansirovanie_rekviziti'),
                   'techobespech' : civil.cleaned_data.get('techobespech'),
                   'techobespech' : civil.cleaned_data.get('techobespech'),
                   'techobespech_spravochnik' : civil.cleaned_data.get('techobespech_spravochnik'),
                   'techobespech_spravochnik_drugoe' : civil.cleaned_data.get('techobespech_spravochnik_drugoe'),
                   'etapistroitelsta': civil.cleaned_data.get('etapistroitelsta'),
                   'videlenie_etapov': civil.cleaned_data.get('videlenie_etapov'),
                   'start_date': civil.cleaned_data.get('start_date'),
                   'end_date': civil.cleaned_data.get('end_date'),
                   'techeconompokazatel': civil.cleaned_data.get('techeconompokazatel'),
                   'naznachenie': civil.cleaned_data.get('naznachenie'),
                   'prinadlezhnost': civil.cleaned_data.get('prinadlezhnost'),
                   'prinadlezhnost_text': civil.cleaned_data.get('prinadlezhnost_text'),
                   'opasnieyavlenia': civil.cleaned_data.get('opasnieyavlenia'),
                   'categoryzdanii': civil.cleaned_data.get('categoryzdanii'),
                   'stepenognya': civil.cleaned_data.get('stepenognya'),
                   'konstructive': civil.cleaned_data.get('konstructive'),
                   'functionalpozar': civil.cleaned_data.get('functionalpozar'),
                   'prebivanieludei': civil.cleaned_data.get('prebivanieludei'),
                   'urovenotvetstvennosti': civil.cleaned_data.get('urovenotvetstvennosti'),
                   'proektniireshenia': civil.cleaned_data.get('proektniireshenia'),
                   'inzhinerniziskania': civil.cleaned_data.get('inzhinerniziskania'),
                   'predelnstoimost': civil.cleaned_data.get('predelnstoimost'),
                   'istochnikfinans': civil.cleaned_data.get('istochnikfinans'),
                    #
                    'shema_plan_org': civil.cleaned_data.get('shema_plan_org'),
                    'shema_plan_org_RZO': civil.cleaned_data.get('shema_plan_org_RZO'),
                    'arh_hud_reshenia': civil.cleaned_data.get('arh_hud_reshenia'),
                    'technologich_reshenia': civil.cleaned_data.get('technologich_reshenia'),
                    'materiali': civil.cleaned_data.get('materiali'),
                    'stroitelnie_konstrukcii': civil.cleaned_data.get('stroitelnie_konstrukcii'),
                    'fundament': civil.cleaned_data.get('fundament'),
                    'steni_podvali_cokol': civil.cleaned_data.get('steni_podvali_cokol'),
                    'steni_naruzhn': civil.cleaned_data.get('steni_naruzhn'),
                    'steni_vnutr': civil.cleaned_data.get('steni_vnutr'),
                    'perekritia': civil.cleaned_data.get('perekritia'),
                    'colonni': civil.cleaned_data.get('colonni'),
                    'lestnici': civil.cleaned_data.get('lestnici'),
                    'poli': civil.cleaned_data.get('poli'),
                    'krovlya': civil.cleaned_data.get('krovlya'),
                    'vitrazhi': civil.cleaned_data.get('vitrazhi'),
                    'dveri': civil.cleaned_data.get('dveri'),
                    'otdelka_vnutr': civil.cleaned_data.get('otdelka_vnutr'),
                    'otdelka_naruzhn': civil.cleaned_data.get('otdelka_naruzhn'),
                    'bezopasnost': civil.cleaned_data.get('bezopasnost'),
                    'inzh_zashita': civil.cleaned_data.get('inzh_zashita'),
                    'otoplenie': civil.cleaned_data.get('otoplenie'),
                    'ventilyacia': civil.cleaned_data.get('ventilyacia'),
                    'vodoprovod': civil.cleaned_data.get('vodoprovod'),
                    'kanalizacia': civil.cleaned_data.get('kanalizacia'),
                    'electrosnabzhenie': civil.cleaned_data.get('electrosnabzhenie'),
                    'telefonizacia': civil.cleaned_data.get('telefonizacia'),
                    'radiofikacia': civil.cleaned_data.get('radiofikacia'),
                    'inthernet': civil.cleaned_data.get('inthernet'),
                    'televidenie': civil.cleaned_data.get('televidenie'),
                    'gazifikacia': civil.cleaned_data.get('gazifikacia'),
                    'avtomatizacia': civil.cleaned_data.get('avtomatizacia'),
                    'vodosnabzhenie': civil.cleaned_data.get('vodosnabzhenie'),
                    'vodootvedenie': civil.cleaned_data.get('vodootvedenie'),
                    'teplosnabzhenie': civil.cleaned_data.get('teplosnabzhenie'),
                    'electrosnabzhenie_naruzh': civil.cleaned_data.get('electrosnabzhenie_naruzh'),
                    'telefonizacia_naruzh': civil.cleaned_data.get('telefonizacia_naruzh'),
                    'radiofikacia_naruzh': civil.cleaned_data.get('radiofikacia_naruzh'),
                    'inthernet_naruzh': civil.cleaned_data.get('inthernet_naruzh'),
                    'televidenie_naruzh': civil.cleaned_data.get('televidenie_naruzh'),
                    'gazosnabzhenie': civil.cleaned_data.get('gazosnabzhenie'),
                    'inoe_naruzh': civil.cleaned_data.get('inoe_naruzh'),
                    #
                   'ohrana_okr_sredi': civil.cleaned_data.get('ohrana_okr_sredi'),
                   'obespeh_pozharn_bezop': civil.cleaned_data.get('obespeh_pozharn_bezop'),
                   'energy_effekt': civil.cleaned_data.get('energy_effekt'),
                   'energy_effekt': civil.cleaned_data.get('energy_effekt'),
                   'energy_effekt_klass': civil.cleaned_data.get('energy_effekt_klass'),
                   'energy_effekt_kharakteristika': civil.cleaned_data.get('energy_effekt_kharakteristika'),
                   'invalidi': civil.cleaned_data.get('invalidi'),
                   'inzh_teh_ykreplenie': civil.cleaned_data.get('inzh_teh_ykreplenie'),
                   'uslovia_prebivania': civil.cleaned_data.get('uslovia_prebivania'),
                   'technich_ekspluatacia': civil.cleaned_data.get('technich_ekspluatacia'),
                   'proekt_organizacii_str': civil.cleaned_data.get('proekt_organizacii_str'),
                   'snos_sohranenie': civil.cleaned_data.get('snos_sohranenie'),
                   'blagoustroistvo': civil.cleaned_data.get('blagoustroistvo'),
                   'vosstanovlenie': civil.cleaned_data.get('vosstanovlenie'),
                   'skladirovanie': civil.cleaned_data.get('skladirovanie'),
                   'nauchno_issled': civil.cleaned_data.get('nauchno_issled'),
                    #
                   'sostav_proektnoi_documentacii': civil.cleaned_data.get('sostav_proektnoi_documentacii'),
                   'smetnaya_documentacia': civil.cleaned_data.get('smetnaya_documentacia'),
                   'spec_tech_uslovia': civil.cleaned_data.get('spec_tech_uslovia'),
                   'standartizacia': civil.cleaned_data.get('standartizacia'),
                   'demonstacii': civil.cleaned_data.get('demonstacii'),
                   'inform_modelirovanie': civil.cleaned_data.get('inform_modelirovanie'),
                   'econom_effect_document': civil.cleaned_data.get('econom_effect_document'),
                   'rekviziti_ogradostroy_plan': civil.cleaned_data.get('rekviziti_ogradostroy_plan'),
                   'rekviziti_res_engineers': civil.cleaned_data.get('rekviziti_res_engineers'),
                   'rekviziti_technich_condition': civil.cleaned_data.get('rekviziti_technich_condition'),
                   'rekviziti_materiali_proekta_planirovki': civil.cleaned_data.get('rekviziti_materiali_proekta_planirovki'),
                   'rekviziti_reshenie_o_soglasovanii': civil.cleaned_data.get('rekviziti_reshenie_o_soglasovanii'),
                   'rekviziti_doc_polnomochiya': civil.cleaned_data.get('rekviziti_doc_polnomochiya'),
                   'rekviziti_other_documents': civil.cleaned_data.get('rekviziti_other_documents')                
                   }
        

        document.render(context)
        tz_path = "documents/" + objectname
        if not os.path.exists(tz_path):
            os.mkdir(tz_path)
        document.save("documents/%s/ТЗ_ГражданскийОбъект_%s.docx" % (objectname, objectname))
        civil_instance = civil.save(commit=False)
        civil_instance.save()
        user.save()
        for f in files:
                file_instance = CitizenData(document=f, civil=civil_instance)
                file_instance.save()
        path = "documents/%s/ТЗ_ГражданскийОбъект_%s.docx" % (objectname, objectname)
        subprocess.call("abiword --to=pdf '"+ path +"'", shell=True)  
        msg = EmailMultiAlternatives("Документы", "Ваш пакет документов", "bimcentre.info@gmail.com", [email])
        msg.attach_file("documents/%s/ТЗ_ГражданскийОбъект_%s.pdf" % (objectname, objectname))
        msg.send()
        return redirect('http://xn------5cdabbpnldcprfc4ag7bdhqdgn0ae1br.xn--p1ai:8080/feedback_page.php')
        #return HttpResponse("<h2>Ваш пакет документов успешно отправлен на {0}</h2>".format(email))


def indus(request):
    industrial = IndustrialForm(request.POST,request.FILES)
    industrial_file = IndustrialFormFile(request.POST, request.FILES)
    user = UserForm(request.POST)
    files = request.FILES.getlist('document')
    if industrial.is_valid()  and user.is_valid():
        email = user.cleaned_data.get('email')
        objectname = industrial.cleaned_data.get('objectname')
        document = DocxTemplate(r"ТЗ_ПроизводственныйОбъект.docx")
        context = {'objectname': industrial.cleaned_data.get('objectname'),
                   'date':datetime.date.today(),
                   'objectaddress': industrial.cleaned_data.get('objectaddress'),
                   'objectname': industrial.cleaned_data.get('objectname'),
                   'rekviziti_osnovanie': industrial.cleaned_data.get('rekviziti_osnovanie'),
                   'zastroichik': industrial.cleaned_data.get('zastroichik'),
                   'investor': industrial.cleaned_data.get('investor'),
                   'projectorganization': industrial.cleaned_data.get('projectorganization'),
                   'vidrabot': industrial.cleaned_data.get('vidrabot'),
                   'finansirovanie': industrial.cleaned_data.get('finansirovanie'),
                   'finansirovanie_rekviziti': industrial.cleaned_data.get('finansirovanie_rekviziti'),
                   'techobespech': industrial.cleaned_data.get('techobespech'),
                   'techobespech_spravochnik': industrial.cleaned_data.get('techobespech'),
                   'techobespech_spravochnik_drugoe': industrial.cleaned_data.get('techobespech_spravochnik_drugoe'),
                   'etapistroitelsta': industrial.cleaned_data.get('etapistroitelsta'),
                   'videlenie_etapov': industrial.cleaned_data.get('videlenie_etapov'),
                   'start_date': industrial.cleaned_data.get('start_date'),
                   'end_date': industrial.cleaned_data.get('end_date'),
                   'techeconompokazatel': industrial.cleaned_data.get('techeconompokazatel'),
                   'naznachenie': industrial.cleaned_data.get('naznachenie'),
                   'prinadlezhnost': industrial.cleaned_data.get('prinadlezhnost'),
                   'prinadlezhnost_text': industrial.cleaned_data.get('prinadlezhnost_text'),
                   'opasnieyavlenia': industrial.cleaned_data.get('opasnieyavlenia'),
                   'klassopasnosti': industrial.cleaned_data.get('klassopasnosti'),
                   'klassopasnosti_klass': industrial.cleaned_data.get('klassopasnosti_klass'),
                   'klassopasnosti_category': industrial.cleaned_data.get('klassopasnosti_category'),
                   'categoryzdanii': industrial.cleaned_data.get('categoryzdanii'),
                   'klassopasnosti': industrial.cleaned_data.get('klassopasnosti'),
                   'stepenognya': industrial.cleaned_data.get('stepenognya'),
                   'konstructive': industrial.cleaned_data.get('konstructive'),
                   'functionalpozar': industrial.cleaned_data.get('functionalpozar'),
                   'prebivanieludei': industrial.cleaned_data.get('prebivanieludei'),
                   'urovenotvetstvennosti': industrial.cleaned_data.get('urovenotvetstvennosti'),
                   'opasniobekt':industrial.cleaned_data.get('opasniobekt'),
                   'proektniireshenia': industrial.cleaned_data.get('proektniireshenia'),
                   'inzhinerniziskania': industrial.cleaned_data.get('inzhinerniziskania'),
                   'predelnstoimost': industrial.cleaned_data.get('predelnstoimost'),
                   'istochnikfinans': industrial.cleaned_data.get('istochnikfinans'),
                   #
                   'shema_plan_org': industrial.cleaned_data.get('shema_plan_org'),
                   'shema_plan_org_RZO': industrial.cleaned_data.get('shema_plan_org_RZO'),
                   'arh_hud_reshenia': industrial.cleaned_data.get('arh_hud_reshenia'),
                   'technologich_reshenia': industrial.cleaned_data.get('technologich_reshenia'),
                   'materiali': industrial.cleaned_data.get('materiali'),
                   'stroitelnie_konstrukcii': industrial.cleaned_data.get('stroitelnie_konstrukcii'),
                   'fundament': industrial.cleaned_data.get('fundament'),
                   'steni_podvali_cokol': industrial.cleaned_data.get('steni_podvali_cokol'),
                   'steni_naruzhn': industrial.cleaned_data.get('steni_naruzhn'),
                   'steni_vnutr': industrial.cleaned_data.get('steni_vnutr'),
                   'perekritia': industrial.cleaned_data.get('perekritia'),
                   'colonni': industrial.cleaned_data.get('colonni'),
                   'lestnici': industrial.cleaned_data.get('lestnici'),
                   'poli': industrial.cleaned_data.get('poli'),
                   'krovlya': industrial.cleaned_data.get('krovlya'),
                   'vitrazhi': industrial.cleaned_data.get('vitrazhi'),
                   'dveri': industrial.cleaned_data.get('dveri'),
                   'otdelka_vnutr': industrial.cleaned_data.get('otdelka_vnutr'),
                   'otdelka_naruzhn': industrial.cleaned_data.get('otdelka_naruzhn'),
                   'bezopasnost': industrial.cleaned_data.get('bezopasnost'),
                   'inzh_zashita': industrial.cleaned_data.get('inzh_zashita'),
                   'otoplenie': industrial.cleaned_data.get('otoplenie'),
                   'ventilyacia': industrial.cleaned_data.get('ventilyacia'),
                   'vodoprovod': industrial.cleaned_data.get('vodoprovod'),
                   'kanalizacia': industrial.cleaned_data.get('kanalizacia'),
                   'electrosnabzhenie': industrial.cleaned_data.get('electrosnabzhenie'),
                   'telefonizacia': industrial.cleaned_data.get('telefonizacia'),
                   'radiofikacia': industrial.cleaned_data.get('radiofikacia'),
                   'inthernet': industrial.cleaned_data.get('inthernet'),
                   'televidenie': industrial.cleaned_data.get('televidenie'),
                   'gazifikacia': industrial.cleaned_data.get('gazifikacia'),
                   'avtomatizacia': industrial.cleaned_data.get('avtomatizacia'),
                   'vodosnabzhenie': industrial.cleaned_data.get('vodosnabzhenie'),
                   'vodootvedenie': industrial.cleaned_data.get('vodootvedenie'),
                   'teplosnabzhenie': industrial.cleaned_data.get('teplosnabzhenie'),
                   'electrosnabzhenie_naruzh': industrial.cleaned_data.get('electrosnabzhenie_naruzh'),
                   'telefonizacia_naruzh': industrial.cleaned_data.get('telefonizacia_naruzh'),
                   'radiofikacia_naruzh': industrial.cleaned_data.get('radiofikacia_naruzh'),
                   'inthernet_naruzh': industrial.cleaned_data.get('inthernet_naruzh'),
                   'televidenie_naruzh': industrial.cleaned_data.get('televidenie_naruzh'),
                   'gazosnabzhenie': industrial.cleaned_data.get('gazosnabzhenie'),
                   'inoe_naruzh': industrial.cleaned_data.get('inoe_naruzh'),
                   #
                   'ohrana_okr_sredi': industrial.cleaned_data.get('ohrana_okr_sredi'),
                   'obespeh_pozharn_bezop': industrial.cleaned_data.get('obespeh_pozharn_bezop'),
                   'energy_effekt': industrial.cleaned_data.get('energy_effekt'),
                   'energy_effekt_klass': industrial.cleaned_data.get('energy_effekt_klass'),
                   'energy_effekt_kharakteristika': industrial.cleaned_data.get('energy_effekt_kharakteristika'),
                   'energy_effekt_rekviziti': industrial.cleaned_data.get('energy_effekt_rekviziti'),
                   'invalidi': industrial.cleaned_data.get('invalidi'),
                   'inzh_teh_ykreplenie': industrial.cleaned_data.get('inzh_teh_ykreplenie'),
                   'uslovia_prebivania': industrial.cleaned_data.get('uslovia_prebivania'),
                   'technich_ekspluatacia': industrial.cleaned_data.get('technich_ekspluatacia'),
                   'proekt_organizacii_str': industrial.cleaned_data.get('proekt_organizacii_str'),
                   'snos_sohranenie': industrial.cleaned_data.get('snos_sohranenie'),
                   'blagoustroistvo': industrial.cleaned_data.get('blagoustroistvo'),
                   'vosstanovlenie': industrial.cleaned_data.get('vosstanovlenie'),
                   'skladirovanie': industrial.cleaned_data.get('skladirovanie'),
                   'nauchno_issled': industrial.cleaned_data.get('nauchno_issled'),
                   #
                   'sostav_proektnoi_documentacii': industrial.cleaned_data.get('sostav_proektnoi_documentacii'),
                   'smetnaya_documentacia': industrial.cleaned_data.get('smetnaya_documentacia'),
                   'spec_tech_uslovia': industrial.cleaned_data.get('spec_tech_uslovia'),
                   'standartizacia': industrial.cleaned_data.get('standartizacia'),
                   'demonstacii': industrial.cleaned_data.get('demonstacii'),
                   'inform_modelirovanie': industrial.cleaned_data.get('inform_modelirovanie'),
                   'econom_effect_document': industrial.cleaned_data.get('econom_effect_document'),
                   'rekviziti_ogradostroy_plan': industrial.cleaned_data.get('rekviziti_ogradostroy_plan'),
                   'rekviziti_res_engineers': industrial.cleaned_data.get('rekviziti_res_engineers'),
                   'rekviziti_technich_condition': industrial.cleaned_data.get('rekviziti_technich_condition'),
                   'rekviziti_materiali_proekta_planirovki': industrial.cleaned_data.get('rekviziti_materiali_proekta_planirovki'),
                   'rekviziti_reshenie_o_soglasovanii': industrial.cleaned_data.get('rekviziti_reshenie_o_soglasovanii'),
                   'rekviziti_doc_polnomochiya': industrial.cleaned_data.get('rekviziti_doc_polnomochiya'),
                   'rekviziti_other_documents': industrial.cleaned_data.get('rekviziti_other_documents')
                   }

        document.render(context)
        tz_path = "documents/" + objectname
        if not os.path.exists(tz_path):
            os.mkdir(tz_path)
        document.save("documents/%s/ТЗ_ПроизводственныйОбъект_%s.docx" % (objectname, objectname))
        industrial_instance = industrial.save(commit=False)
        industrial_instance.save()
        user.save()
        for f in files:
                file_instance = IndustrialData(document=f, industrial=industrial_instance)
                file_instance.save()
        path = "documents/%s/ТЗ_ПроизводственныйОбъект_%s.docx" % (objectname, objectname)
        subprocess.call("abiword --to=pdf '"+ path +"'", shell=True)  
        msg = EmailMultiAlternatives("Документы", "Ваш пакет документов", "bimcentre.info@gmail.com", [email])
        msg.attach_file("documents/%s/ТЗ_ПроизводственныйОбъект_%s.pdf" % (objectname, objectname))
        msg.send()
        return redirect('http://xn------5cdabbpnldcprfc4ag7bdhqdgn0ae1br.xn--p1ai:8080/feedback_page.php')
        #return HttpResponse("<h2>Ваш пакет документов успешно отправлен на {0}</h2>".format(email))

def lin(request):
    linear = LinearForm(request.POST, request.FILES)
    linear_file = LinearFormFile(request.POST, request.FILES)
    user = UserForm(request.POST)
    files = request.FILES.getlist('document')
    if linear.is_valid() and user.is_valid():
        objectname = linear.cleaned_data.get('objectname')
        document = DocxTemplate(r"ТЗ_ЛинейныйОбъект.docx")
        email = user.cleaned_data.get('email')
        context = {'objectname': linear.cleaned_data.get('objectname'),
                           'date':datetime.date.today(),
                           'objectaddress': linear.cleaned_data.get('objectaddress'),
                           # Общие данные Пункты 1-10
                           'osnovanie': linear.cleaned_data.get('osnovanie'),
                           'rekviziti_osnovanie': linear.cleaned_data.get('rekviziti_osnovanie'),
                           'zastroichik': linear.cleaned_data.get('zastroichik'),
                           'investor': linear.cleaned_data.get('investor'),
                           'projectorganization': linear.cleaned_data.get('projectorganization'),
                           'vidrabot': linear.cleaned_data.get('vidrabot'),
                           'finansirovanie': linear.cleaned_data.get('finansirovanie'),
                           'finansirovanie_rekviziti': linear.cleaned_data.get('finansirovanie_rekviziti'),
                           'techobespech' : linear.cleaned_data.get('techobespech'),
                           'techobespech_spravochnik' : linear.cleaned_data.get('techobespech_spravochnik'),
                           'techobespech_spravochnik_drugoe' : linear.cleaned_data.get('techobespech_spravochnik_drugoe'),
                           'etapistroitelsta': linear.cleaned_data.get('etapistroitelsta'),
                           'videlenie_etapov': linear.cleaned_data.get('videlenie_etapov'),
                           'start_date': linear.cleaned_data.get('start_date'),
                           'end_date': linear.cleaned_data.get('end_date'),
                           'techeconompokazatel': linear.cleaned_data.get('techeconompokazatel'),
                           # Общие данные Пункты 11.1-11.7
                           'naznachenie': linear.cleaned_data.get('naznachenie'),
                           'prinadlezhnost': linear.cleaned_data.get('prinadlezhnost'),
                           'prinadlezhnost_text': linear.cleaned_data.get('prinadlezhnost_text'),
                           'opasnieyavlenia': linear.cleaned_data.get('opasnieyavlenia'),
                           'klassopasnosti': linear.cleaned_data.get('klassopasnosti'),
                           'klassopasnosti_klass': linear.cleaned_data.get('klassopasnosti_klass'),
                           'klassopasnosti_category': linear.cleaned_data.get('klassopasnosti_category'),
                           'categoryzdanii': linear.cleaned_data.get('categoryzdanii'),
                           'stepenognya': linear.cleaned_data.get('stepenognya'),
                           'konstructive': linear.cleaned_data.get('konstructive'),
                           'functionalpozar': linear.cleaned_data.get('functionalpozar'),
                           'urovenotvetstvennosti': linear.cleaned_data.get('urovenotvetstvennosti'),
                           # Общие данные Пункты 12-16
                           'opasniobekt':linear.cleaned_data.get('opasniobekt'),
                           'proektniireshenia': linear.cleaned_data.get('proektniireshenia'),
                           'inzhinerniziskania': linear.cleaned_data.get('inzhinerniziskania'),
                           'predelnstoimost': linear.cleaned_data.get('predelnstoimost'),
                           'istochnikfinans': linear.cleaned_data.get('istochnikfinans'),
                            #
                           'polosa_otvoda': linear.cleaned_data.get('polosa_otvoda'),
                            # Раздел 2 Пункт 21
                            'materiali': linear.cleaned_data.get('materiali'),
                            'stroitelnie_konstrukcii': linear.cleaned_data.get('stroitelnie_konstrukcii'),
                            'fundament': linear.cleaned_data.get('fundament'),
                            'steni_podvali_cokol': linear.cleaned_data.get('steni_podvali_cokol'),
                            'steni_naruzhn': linear.cleaned_data.get('steni_naruzhn'),
                            'steni_vnutr': linear.cleaned_data.get('steni_vnutr'),
                            'perekritia': linear.cleaned_data.get('perekritia'),
                            'colonni': linear.cleaned_data.get('colonni'),
                            'lestnici': linear.cleaned_data.get('lestnici'),
                            'poli': linear.cleaned_data.get('poli'),
                            'krovlya': linear.cleaned_data.get('krovlya'),
                            'vitrazhi': linear.cleaned_data.get('vitrazhi'),
                            'dveri': linear.cleaned_data.get('dveri'),
                            'otdelka_vnutr': linear.cleaned_data.get('otdelka_vnutr'),
                            'otdelka_naruzhn': linear.cleaned_data.get('otdelka_naruzhn'),
                            'bezopasnost': linear.cleaned_data.get('bezopasnost'),
                            'inzh_zashita': linear.cleaned_data.get('inzh_zashita'),
                            # Раздел 2 Пункты 22-23 ТОЛЬКО ДЛЯ ЛИНЕЙНЫХ ОБЪЕКТОВ
                           'technologich_reshenia_lin': linear.cleaned_data.get('technologich_reshenia_lin'),
                           'zdania_lin': linear.cleaned_data.get('zdania_lin'),
                            # Раздел 2 Пункты 24.1.1-24.1.11
                            'otoplenie': linear.cleaned_data.get('otoplenie'),
                            'ventilyacia': linear.cleaned_data.get('ventilyacia'),
                            'vodoprovod': linear.cleaned_data.get('vodoprovod'),
                            'kanalizacia': linear.cleaned_data.get('kanalizacia'),
                            'electrosnabzhenie': linear.cleaned_data.get('electrosnabzhenie'),
                            'telefonizacia': linear.cleaned_data.get('telefonizacia'),
                            'radiofikacia': linear.cleaned_data.get('radiofikacia'),
                            'inthernet': linear.cleaned_data.get('inthernet'),
                            'televidenie': linear.cleaned_data.get('televidenie'),
                            'gazifikacia': linear.cleaned_data.get('gazifikacia'),
                            'avtomatizacia': linear.cleaned_data.get('avtomatizacia'),
                             # Раздел 2 Пункты 24.2.1-24.1.10
                            'vodosnabzhenie': linear.cleaned_data.get('vodosnabzhenie'),
                            'vodootvedenie': linear.cleaned_data.get('vodootvedenie'),
                            'teplosnabzhenie': linear.cleaned_data.get('teplosnabzhenie'),
                            'electrosnabzhenie_naruzh': linear.cleaned_data.get('electrosnabzhenie_naruzh'),
                            'telefonizacia_naruzh': linear.cleaned_data.get('telefonizacia_naruzh'),
                            'radiofikacia_naruzh': linear.cleaned_data.get('radiofikacia_naruzh'),
                            'inthernet_naruzh': linear.cleaned_data.get('inthernet_naruzh'),
                            'televidenie_naruzh': linear.cleaned_data.get('televidenie_naruzh'),
                            'gazosnabzhenie': linear.cleaned_data.get('gazosnabzhenie'),
                            'inoe_naruzh': linear.cleaned_data.get('inoe_naruzh'),
                            # Раздел 2 Пункты 25-37
                           'ohrana_okr_sredi': linear.cleaned_data.get('ohrana_okr_sredi'),
                           'obespeh_pozharn_bezop': linear.cleaned_data.get('obespeh_pozharn_bezop'),
                           'energy_effekt': linear.cleaned_data.get('energy_effekt'),
                           'energy_effekt_klass': linear.cleaned_data.get('energy_effekt_klass'),
                           'energy_effekt_kharakteristika': linear.cleaned_data.get('energy_effekt_kharakteristika'),
                           'energy_effekt_rekviziti': linear.cleaned_data.get('energy_effekt_rekviziti'),
                           'invalidi': linear.cleaned_data.get('invalidi'),
                           'inzh_teh_ykreplenie': linear.cleaned_data.get('inzh_teh_ykreplenie'),
                           'uslovia_prebivania': linear.cleaned_data.get('uslovia_prebivania'),
                           'technich_ekspluatacia': linear.cleaned_data.get('technich_ekspluatacia'),
                           'proekt_organizacii_str': linear.cleaned_data.get('proekt_organizacii_str'),
                           'snos_sohranenie': linear.cleaned_data.get('snos_sohranenie'),
                           'blagoustroistvo': linear.cleaned_data.get('blagoustroistvo'),
                           'vosstanovlenie': linear.cleaned_data.get('vosstanovlenie'),
                           'skladirovanie': linear.cleaned_data.get('skladirovanie'),
                           'nauchno_issled': linear.cleaned_data.get('nauchno_issled'),
                           # Раздел 3 Пункты 38-45
                           'sostav_proektnoi_documentacii': linear.cleaned_data.get('sostav_proektnoi_documentacii'),
                           'sostav_proektnoi_documentacii_spravochnik': linear.cleaned_data.get('sostav_proektnoi_documentacii_spravochnik'),
                           'smetnaya_documentacia': linear.cleaned_data.get('smetnaya_documentacia'),
                           'spec_tech_uslovia': linear.cleaned_data.get('spec_tech_uslovia'),
                           'standartizacia': linear.cleaned_data.get('standartizacia'),
                           'demonstacii': linear.cleaned_data.get('demonstacii'),
                           'inform_modelirovanie': linear.cleaned_data.get('inform_modelirovanie'),
                           'econom_effect_document': linear.cleaned_data.get('econom_effect_document'),
                           'prochee': linear.cleaned_data.get('prochee'),
                           # Раздел 3 Пункты 46.1-46.7
                           'rekviziti_ogradostroy_plan': linear.cleaned_data.get('rekviziti_ogradostroy_plan'),
                           'rekviziti_res_engineers': linear.cleaned_data.get('rekviziti_res_engineers'),
                           'rekviziti_technich_condition': linear.cleaned_data.get('rekviziti_technich_condition'),
                           'rekviziti_materiali_proekta_planirovki': linear.cleaned_data.get('rekviziti_materiali_proekta_planirovki'),
                           'rekviziti_reshenie_o_soglasovanii': linear.cleaned_data.get('rekviziti_reshenie_o_soglasovanii'),
                           'rekviziti_doc_polnomochiya': linear.cleaned_data.get('rekviziti_doc_polnomochiya'),
                           'rekviziti_other_documents': linear.cleaned_data.get('rekviziti_other_documents')
                           }

        document.render(context)
        tz_path = "documents/" + objectname
        if not os.path.exists(tz_path):
            os.mkdir(tz_path)
        document.save("documents/%s/ТЗ_ЛинейныйОбъект_%s.docx" % (objectname, objectname))
        linear_instance = linear.save(commit=False)
        linear_instance.save()
        user.save()
        for f in files:
                file_instance = LinearData(document=f, linear=linear_instance)
                file_instance.save()
        path = "documents/%s/ТЗ_ЛинейныйОбъект_%s.docx" % (objectname, objectname)
        subprocess.call("abiword --to=pdf '"+ path +"'", shell=True) 
        msg = EmailMultiAlternatives("Документы", "Ваш пакет документов", "bimcentre.info@gmail.com", [email])
        msg.attach_file("documents/%s/ТЗ_ЛинейныйОбъект_%s.pdf" % (objectname, objectname))
        msg.send()
        return redirect('http://xn------5cdabbpnldcprfc4ag7bdhqdgn0ae1br.xn--p1ai:8080/feedback_page.php')
        #return HttpResponse("<h2>Ваш пакет документов успешно отправлен на {0}</h2>".format(email))
       