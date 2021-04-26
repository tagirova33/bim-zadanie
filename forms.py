from django import forms
from django.forms import ModelForm
from .models import *
from multiupload.fields import MultiFileField

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ('email',)

class LinearForm(ModelForm):
    class Meta:
        model = Linear
        fields = '__all__'
        widgets = {
            'techobespech_spravochnik': forms.CheckboxSelectMultiple(),
        }
 
        
class LinearFormFile(ModelForm):
    class Meta:
        model = LinearData
        fields = ['document']
        widgets = {
            'document': forms.FileInput(attrs={'multiple': True}),
        }
    

class CivilForm(ModelForm):
    class Meta:
        model = Citizen
        fields = '__all__'

        
class CivilFormFile(ModelForm):
    class Meta:
        model = CitizenData
        fields = ['document']
        widgets = {
            'document': forms.FileInput(attrs={'multiple': True}),
        }

class IndustrialForm(ModelForm):
    class Meta:
        model = Industrial
        fields = '__all__'

        
class IndustrialFormFile(ModelForm):
    class Meta:
        model = IndustrialData
        fields = ['document']
        widgets = {
            'document': forms.FileInput(attrs={'multiple': True}),
        }

STAGES = (
  ('Инженерные изыскания и проектирование',(
    ('1.1','Выпуск проектной документации на основе ЦИМ'),
    ('1.2','Пространственная междисциплинарная координация и выявление коллизий (3D-координация)'),
    ('1.3','Подсчет объемов работ и оценка сметной стоимости (BIM 5D)'),
  )
   ),
  ('Строительство',(
    ('2.1','Пространственная временная координация и выявление коллизий (4D-координация)'),
    ('2.2','Визуализация процесса строительства (BIM 4D)'),
    ('2.3','Исполнительная модель «как построено»'),
  )
   ),
  ('Эксплуатация', (
    ('3.1', 'Управление эксплуатацией зданий и сооружений'),
    ('3.2', 'Информационное моделирование существующего объекта «как есть»'),
  )
   )
)

class BimUseForm(forms.Form):
    stage = forms.MultipleChoiceField(label = "BIM-USE", widget=forms.CheckboxSelectMultiple, choices=STAGES)

OKS = (('Linear','Линейный объект'),
       ('Citizen','Непроизводственный объект'),
       ('Industrial','Производственный объект'))

class OKSForm(forms.Form):
    oks = forms.ChoiceField(label = "ОКС",
        widget=forms.RadioSelect, choices=OKS)

class HintForm(forms.Form):
    comment = forms.CharField(label='в соответствие с таблицей КСИ СЖЦ / LCS 8)стадия жизненного цикла объектов капитального строительства;')
    comment2 = forms.CharField(label='или альтернативные определения:3.2 строительство: Создание зданий, строений, сооружений (в том числе на месте сносимых объектов капитального строительства) (пункт 13 статьи 1 [2]). ')
    comment3 = forms.CharField(label='3')
    comment4= forms.CharField(label='4')
    comment5= forms.CharField(label='5')
    comment6= forms.CharField(label='6')
    comment7= forms.CharField(label='7')
    comment8= forms.CharField(label='8')
    comment9= forms.CharField(label='9')
    comment10= forms.CharField(label='10')
    comment11= forms.CharField(label='11')
    comment12= forms.CharField(label='12')
    comment13= forms.CharField(label='13')
