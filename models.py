from django.db import models
from django.forms import ModelForm
from multiselectfield import MultiSelectField

my_systems_firstwave = (('Электроснабжение', 'Электроснабжение'),
               ('Водоснабжение', 'Водоснабжение'),
               ('Теплоснабжение', 'Теплоснабжение'),
               ('Газоснабжение', 'Газоснабжение'),
               ('Водоотведение', 'Водоотведение'),
               ('Связь','Связь'),
               ('Другое','Другое')
         )

my_systems = (('Наземная система', 'Наземная система'),
               ('Стеновая система', 'Стеновая система'),
               ('Система перекрытий', 'Система перекрытий'),
               ('Система крыши', 'Система крыши'),
               ('Газовая и воздушная система', 'Газовая и воздушная система'),
               ('Водяная и жидкостная система','Водяная и жидкостная система'),
               ('Система дренажа и удаления отходов', 'Система дренажа и удаления отходов'),
               ('Система отопления и/или охлаждения', 'Система отопления и/или охлаждения'),
               ('Система вентиляции', 'Система вентиляции'),
               ('Система электроэнергии', 'Система электроэнергии'),
               ('Система автоматизации', 'Система автоматизации'),
               ('Информационная и коммуникационная система','Информационная и коммуникационная система'),
               ('Система транспортировки', 'Система транспортировки'),
               ('Система охраны и обеспечения безопасности', 'Система охраны и обеспечения безопасности'),
               ('Система освещения', 'Система освещения'),
               ('Железнодорожная система', 'Железнодорожная система'),
               ('Система обустройства', 'Система обустройства'),
               ('Система оснащения объектов транспорта', 'Система оснащения объектов транспорта'),
               ('Другое','Другое')
               )
osnovanie_choices = ( ('Федеральная программа', 'Федеральная целевая программа'),
                                          ('Программа развития субъекта Российской Федерации', 'Программа развития субъекта Российской Федерации'), 
                                          ('Комплексная программа развития муниципального образования', 'Комплексная программа развития муниципального образования'), 
                                          ('Ведомственная целевая программа','Ведомственная целевая программа'),
                                          ('Решение Президента Российской Федерации', 'Решение Президента Российской Федерации'), 
                                          ('Решение Правительства Российской Федерации', 'Решение Правительства Российской Федерации'), 
                                          ('Решение органов исполнительной власти субъектов Российской Федерации', 'Решение органов исполнительной власти субъектов Российской Федерации'), 
                                          ('Решение органов местности самоуправления в соответствии с их положениями','Решение органов местности самоуправления в соответствии с их положениями'),
                                          ('Решение застройщика', 'Решение застройщика'),
                                          ('Решение руководителя ЭО', 'Решение руководителя эксплуатирующей организации'),
                                          ('РосТехНадзор','Предписание территориальных органов РосТехНадзора'),
                                          ('Служба производственного контроля', 'Предложение службы производственного контроля по внедрению новых технологий или устранению нарушений'),
                                          ('Другое','Другое')
    )

class User(models.Model):
    email = models.EmailField(max_length=254, verbose_name = "Email")
    date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title

class Linear(models.Model):
    # Шапка
    objectname = models.TextField(max_length=500,
        verbose_name='Наименование объекта капитального строительства')
    objectaddress = models.TextField(max_length=500,
        verbose_name='Адрес объекта капитального строительства')
    # Общие данные Пункты 1-10
    osnovanie = models.CharField(choices=osnovanie_choices, max_length=300,
                                          verbose_name='Основание для проектирования')
    rekviziti_osnovanie = models.TextField(max_length=300,
                                 verbose_name='Реквизиты документа-основания')
    zastroichik = models.TextField(max_length=300,
                                   verbose_name='Застройщик(заказчик)')
    investor = models.TextField(max_length=300,
                                verbose_name='Инвестор (при наличии)', blank=True)
    projectorganization = models.TextField(max_length=300,
                                           verbose_name='Проектная организация')
    vidrabot = models.CharField(choices=[('Строительство', 'Строительство'), ('Реконструкция', 'Реконструкция'),
                                         ('Капитальный ремонт', 'Капитальный ремонт')], max_length=60,
                                verbose_name='Вид работ')
    finansirovanie = models.CharField(choices=[('ФБ', 'Федеральный бюджет'), ('РБ', 'Региональный бюджет'),
                                         ('МБ', 'Местный бюджет'), ('ВБ', 'Внебюджетные средства')], max_length=60,
                                verbose_name='Выбор источника финансирования строительства')
    finansirovanie_rekviziti = models.TextField(max_length=300,
                                      verbose_name='Источник финансирования строительства')
    techobespech = models.CharField(choices=[('Получение', 'Требуется разработка технических условий'), ('Продление', 'Требуется продление или актуализация технических условий'),
                                         ('Получены', 'Имеются актуальные технические условия')], max_length=60,
                                    verbose_name='Технические условия на подключение (присоединение) объекта к сетям инженерно-технического обеспечения (при наличии)')
    techobespech_spravochnik = MultiSelectField(choices = my_systems_firstwave, verbose_name='Перечень сетей инженерно-технического обеспечения')
    techobespech_spravochnik_drugoe = models.TextField(max_length=100, verbose_name='Другое', blank = True)
    etapistroitelsta = models.TextField(choices=[('Выделение не требуется', 'Выделение не требуется'), ('Проработать вопрос в ходе проектирования', 'Проработать вопрос в ходе проектирования'), ('Выделить этапы', 'Выделить этапы')],
                                    max_length=60,verbose_name='Требования к выделению этапов строительства объектов')
    videlenie_etapov = models.TextField(max_length=300,verbose_name='Выделение этапов', blank = True)
    start_date = models.TextField(max_length=300,verbose_name='Дата начала строительства объекта')
    end_date = models.TextField(max_length=300,verbose_name='Дата окончания строительства объекта')
    techeconompokazatel = models.TextField(max_length=500,
                                           verbose_name='Требования к основным технико-экономическим показателям объекта (площадь, объем, протяженность,  количество этажей, производственная мощность, пропускная способность, грузооборот, интенсивность движения и другие показатели)')
    # Общие данные Пункты 11.1-11.7
    naznachenie = models.CharField(max_length=100, verbose_name='Назначение')
    prinadlezhnost = models.CharField(choices=[('Да', 'Да'), ('Нет', 'Нет')], max_length=3,
                                      verbose_name='Принадлежность к объектам транспортной инфраструктуры и к другим объектам, функционально-технологические особенности которых влияют на их безопасность')
    prinadlezhnost_text = models.TextField(max_length=300,verbose_name='Вид объекта строительства', blank = True)
    opasnieyavlenia = models.CharField(choices=[('Да', 'Да'), ('Нет', 'Нет')], max_length=3,
                                       verbose_name='Возможность возникновения опасных природных процессов и явлений и техногенных воздействий на территории, на которой будет осуществляться строительство объекта')
    #klassopasnosti = models.CharField(choices=[('Нет', 'Нет'), ('I класс опасности', 'I класс опасности'), ('II класс опасности', 'II класс опасности'),('III класс опасности', 'III класс опасности'),('IV класс опасности', 'IV класс опасности')], max_length=30,
                                      #verbose_name='Принадлежность к опасным производственным объектам')
    klassopasnosti = models.CharField(choices=[('Не принадлежит', 'Не принадлежит'), ('Принадлежит', 'Принадлежит')], max_length=30,
                                      verbose_name='Принадлежность к опасным производственным объектам')
    klassopasnosti_klass = models.TextField(max_length=100, verbose_name='Класс опасного объекта', blank = True)
    klassopasnosti_category = models.TextField(max_length=100, verbose_name='Категория опасного объекта', blank = True)
     #klasspozharopastnosti = models.CharField(
     #    choices=[('(А) Повышенная взрывопожароопасность', '(А) Повышенная взрывопожароопасность'),
     #            ('(Б) Взрывопожароопасность', '(Б) Взрывопожароопасность'),
     #            ('(В1-В4) Пожароопасность', '(В1-В4) Пожароопасность'),
     #            ('(Г) Умеренная пожароопасность)', '(Г) Умеренная пожароопасность'),
     #            ('(Д) Пониженная пожароопасность', '(Д) Пониженная пожароопасность')], max_length=60,
     #   verbose_name='Пожарная и взрывопожарная опасность')
    categoryzdanii =  models.TextField(max_length=100, verbose_name='Категория зданий, сооружений, помещений по пожарной и взрывопожарной опасности')
    stepenognya =  models.TextField(max_length=100, verbose_name='Степень огнестойкости ')
    konstructive =  models.TextField(max_length=100, verbose_name='Класс конструктивной пожарной опасности ')
    functionalpozar =  models.TextField(max_length=100, verbose_name='Класс функциональной пожарной опасности')
    urovenotvetstvennosti = models.CharField(
        choices=[('Повышенный', 'Повышенный'), ('Нормальный', 'Нормальный'), ('Пониженный', 'Пониженный')],
        max_length=60,
        verbose_name='Уровень ответственности')
    # Общие данные Пункты 12-16
    opasniobekt = models.TextField(max_length=300,
                                           verbose_name='Требования о необходимости соответствия проектной документации обоснованию безопасности опасного производственного объекта', blank=True)
    proektniireshenia = models.TextField(max_length=300,
                                         verbose_name='Требования к качеству, конкурентоспособности, экологичности и энергоэффективности проектных решений')
    inzhinerniziskania = models.TextField(max_length=300,
                                          verbose_name='Необходимость выполнения инженерных изысканий для подготовки проектной документации')
    predelnstoimost = models.TextField(max_length=300,
                                       verbose_name='Предполагаемая (предельная) стоимость строительства объекта')
    istochnikfinans = models.TextField(max_length=300,
                                       verbose_name='Сведения об источниках финансирования строительства объекта')
    # Раздел 2 Пункты 17 - 20 ТОЛЬКО ДЛЯ НЕЛИНЕЙНЫЙ ОБЪЕКТОВ (ПРОИЗВОДСТВ И НЕПРОИЗВОДСТВ НАЗНАЧЕНИЯ)
    polosa_otvoda = models.TextField(max_length=300,
                                     verbose_name='Требования к проекту полосы отвода',
                                     blank=True)
    # Раздел 2 Пункт 21
    materiali = models.TextField(max_length=300,
                                 verbose_name='Порядок выбора и применения материалов, изделий, конструкций, оборудования и их согласования застройщиком',
                                 blank=True)
    stroitelnie_konstrukcii = models.TextField(max_length=300,
                                               verbose_name='Требования к строительным конструкциям',
                                               blank=True)
    fundament = models.TextField(max_length=300,
                                 verbose_name='Требования к фундаментам',
                                 blank=True)
    steni_podvali_cokol = models.TextField(max_length=300,
                                           verbose_name='Требования к стенам, подвалам и цокольному этажу',
                                           blank=True)
    steni_naruzhn = models.TextField(max_length=300,
                                     verbose_name='Требования к наружным стенам',
                                     blank=True)
    steni_vnutr = models.TextField(max_length=300,
                                   verbose_name='Требования к внутренним стенам и перегородкам',
                                   blank=True)
    perekritia = models.TextField(max_length=300,
                                  verbose_name='Требования к перекрытиям',
                                  blank=True)
    colonni = models.TextField(max_length=300,
                               verbose_name='Требования к колоннам, ригелям',
                               blank=True)
    lestnici = models.TextField(max_length=300,
                                verbose_name='Требования к лестницам',
                                blank=True)
    poli = models.TextField(max_length=300,
                            verbose_name='Требования к полам',
                            blank=True)
    krovlya = models.TextField(max_length=300,
                               verbose_name='Требования к кровле',
                               blank=True)
    vitrazhi = models.TextField(max_length=300,
                                verbose_name='Требования к витражам, окнам',
                                blank=True)
    dveri = models.TextField(max_length=300,
                             verbose_name='Требования к дверям',
                             blank=True)
    otdelka_vnutr = models.TextField(max_length=300,
                                     verbose_name='Требования к внутренней отделке',
                                     blank=True)
    otdelka_naruzhn = models.TextField(max_length=300,
                                       verbose_name='Требования к наружной отделке',
                                       blank=True)
    bezopasnost = models.TextField(max_length=300,
                                   verbose_name='Требования к обеспечению безопасности объекта при опасных природных процессах и явлениях и техногенных воздействиях',
                                   blank=True)
    inzh_zashita = models.TextField(max_length=300,
                                    verbose_name='Требования к инженерной защите территории объекта',
                                    blank=True)
    # Раздел 2 Пункты 22-23 ТОЛЬКО ДЛЯ ЛИНЕЙНЫХ ОБЪЕКТОВ
    technologich_reshenia_lin = models.TextField(max_length=300,
                                                 verbose_name='Требования	к	технологическим	и	конструктивным	решениям линейного объекта',
                                                 blank=True)
    zdania_lin = models.TextField(max_length=300,
                                  verbose_name='Требования к зданиям, строениям и сооружениям, входящим в инфраструктуру линейного объекта',
                                  blank=True)
    # Раздел 2 Пункты 24.1.1-24.1.11
    otoplenie = models.TextField(max_length=100,
                                 verbose_name='Отопление',
                                     blank=True)
    ventilyacia = models.TextField(max_length=100,
                                   verbose_name='Вентиляция',
                                     blank=True)
    vodoprovod = models.TextField(max_length=100,
                                  verbose_name='Водопровод',
                                     blank=True)
    kanalizacia = models.TextField(max_length=100,
                                   verbose_name='Канализация',
                                     blank=True)
    electrosnabzhenie = models.TextField(max_length=100,
                                         verbose_name='Электроснабжение',
                                     blank=True)
    telefonizacia = models.TextField(max_length=100,
                                     verbose_name='Телефонизация',
                                     blank=True)
    radiofikacia = models.TextField(max_length=100,
                                    verbose_name='Радиофикация',
                                     blank=True)
    inthernet = models.TextField(max_length=100,
                                 verbose_name='Информационно-телекоммуникационная сеть "Интернет"',
                                     blank=True)
    televidenie = models.TextField(max_length=100,
                                   verbose_name='Телевидение',
                                     blank=True)
    gazifikacia = models.TextField(max_length=100,
                                   verbose_name='Газификация',
                                     blank=True)
    avtomatizacia = models.TextField(max_length=100,
                                     verbose_name='Автоматизация и диспетчеризация',
                                     blank=True)
    # Раздел 2 Пункты 24.2.1-24.1.10
    vodosnabzhenie = models.TextField(max_length=100,
                                      verbose_name='Водоснабжение',
                                     blank=True)
    vodootvedenie = models.TextField(max_length=100,
                                     verbose_name='Водоотведение',
                                     blank=True)
    teplosnabzhenie = models.TextField(max_length=100,
                                       verbose_name='Теплоснабжение',
                                     blank=True)
    electrosnabzhenie_naruzh = models.TextField(max_length=100,
                                                verbose_name='Электроснабжение',
                                     blank=True)
    telefonizacia_naruzh = models.TextField(max_length=100,
                                            verbose_name='Телефонизация',
                                     blank=True)
    radiofikacia_naruzh = models.TextField(max_length=100,
                                           verbose_name='Радиофикация',
                                     blank=True)
    inthernet_naruzh = models.TextField(max_length=100,
                                        verbose_name='Информационно-телекоммуникационная сеть "Интернет"',
                                     blank=True)
    televidenie_naruzh = models.TextField(max_length=100,
                                          verbose_name='Телевидение',
                                     blank=True)
    gazosnabzhenie = models.TextField(max_length=100,
                                      verbose_name='Газоснабжение',
                                     blank=True)
    inoe_naruzh = models.TextField(max_length=100,
                                   verbose_name='Иные сети инженерно-технического обеспечения',
                                   blank=True)
    # Раздел 2 Пункты 25-37
    ohrana_okr_sredi = models.TextField(max_length=300,
                                        verbose_name='Требования к мероприятиям по охране окружающей среды',
                                     blank=True)
    obespeh_pozharn_bezop = models.TextField(max_length=300,
                                             verbose_name='Требования к мероприятиям по обеспечению пожарной безопасности',
                                     blank=True)
    energy_effekt = models.TextField(max_length=300,
                                     verbose_name='Требования к мероприятиям по обеспечению соблюдения требований энергетической эффективности и по оснащенности объекта приборами учета используемых энергетических ресурсов',
                                     blank=True)
    energy_effekt_klass = models.TextField(max_length=300,
                                             verbose_name='Класс энергетической эффективности',
                                     blank=True)
    energy_effekt_kharakteristika = models.TextField(max_length=300,
                                             verbose_name='Характеристика расхода тепловой энергии',
                                             blank=True)
    energy_effekt_rekviziti = models.TextField(max_length=300,
                                             verbose_name='Реквизиты энергетического паспорта(при наличии)',
                                             blank=True)
    invalidi = models.TextField(max_length=300,
                                verbose_name='Требования к мероприятиям по обеспечению доступа инвалидов к объекту',
                                     blank=True)
    inzh_teh_ykreplenie = models.TextField(max_length=300,
                                           verbose_name='Требования к инженерно-техническому укреплению объекта в целях обеспечения его антитеррористической защищенности',
                                     blank=True)
    uslovia_prebivania = models.TextField(max_length=300,
                                          verbose_name='Требования к соблюдению безопасных для здоровья человека условий проживания и пребывания в объекте и требования к соблюдению безопасного уровня воздействия объекта на окружающую среду',
                                     blank=True)
    technich_ekspluatacia = models.TextField(max_length=300,
                                             verbose_name='Требования к технической эксплуатации и техническому обслуживанию объекта',
                                     blank=True)
    proekt_organizacii_str = models.TextField(max_length=300,
                                              verbose_name='Требования к проекту организации строительства объекта',
                                     blank=True)
    snos_sohranenie = models.TextField(max_length=300,
                                       verbose_name='Обоснование необходимости сноса или сохранения зданий, сооружений, зеленых насаждений, а также переноса инженерных сетей и коммуникаций, расположенных на земельном участке, на котором планируется размещение объекта',
                                     blank=True)
    blagoustroistvo = models.TextField(max_length=300,
                                       verbose_name='Требования к решениям по благоустройству прилегающей территории, к малым архитектурным формам и к планировочной организации земельного участка, на котором планируется размещение объекта',
                                     blank=True)
    vosstanovlenie = models.TextField(max_length=300,
                                      verbose_name='Требования к разработке проекта восстановления (рекультивации) нарушенных земель или плодородного слоя',
                                      blank=True)
    skladirovanie = models.TextField(max_length=300,
                                     verbose_name='Требования к местам складирования излишков грунта и (или) мусора при строительстве и протяженность маршрута их доставки',
                                     blank=True)
    nauchno_issled = models.TextField(max_length=300,
                                      verbose_name='Требования к выполнению научно-исследовательских и опытно- конструкторских работ в процессе проектирования и строительства объекта',
                                      blank=True)

    # Раздел 3 Пункты 38-45
    sostav_proektnoi_documentacii_spravochnik = MultiSelectField(
        choices=[('1', 'Раздел 1 "Пояснительная записка" '),
                 ('2', 'Раздел 2 "Проект полосы отвода"'),
                 ('3', 'Раздел 3 "Технологические и конструктивные решения линейного объекта. Искусственные сооружения"'),
                 ('4', 'Раздел 4 "Здания, строения и сооружения, входящие в инфраструктуру линейного объекта"'),
                 ('5', 'Раздел 5 "Проект организации строительства"'),
                 ('6', 'Раздел 6 "Проект организации работ по сносу (демонтажу) линейного объекта"'),
                 ('7', 'Раздел 7 "Мероприятия по охране окружающей среды"'),
                 ('8', 'Раздел 8 "Мероприятия по обеспечению пожарной безопасности"'),
                 ('9', 'Раздел 9 "Смета на строительство"'),
                 ('10','Раздел 10 "Иная документация в случаях, предусмотренных федеральными законами"')],
        verbose_name='Выбор необходимых разделов проектной документации', blank=True)
    sostav_proektnoi_documentacii = models.TextField(max_length=300,
                                                     verbose_name='Иные требования к составу проектной документации, в том числе требования о разработке разделов проектной документации, наличие которых не является обязательным',
                                     blank=True)
    smetnaya_documentacia = models.TextField(max_length=300,
                                             verbose_name='Требования к подготовке сметной документации',
                                     blank=True)
    spec_tech_uslovia = models.TextField(max_length=300,
                                         verbose_name='Требования к разработке специальных технических условий',
                                     blank=True)
    standartizacia = models.TextField(max_length=300,
                                      verbose_name='Требования о применении при разработке проектной документации документов в области стандартизации, не включенных в перечень национальных стандартов и сводов правил',
                                      blank=True)
    demonstacii = models.TextField(max_length=300,
                                   verbose_name='Требования к выполнению демонстрационных материалов, макетов',
                                   blank=True)
    inform_modelirovanie = models.TextField(max_length=300,
                                            verbose_name='Требования о применении технологий информационного моделирования',
                                            blank=True)
    econom_effect_document = models.TextField(max_length=300,
                                              verbose_name='Требование о применении экономически эффективной проектной документации повторного использования',
                                     blank=True)
    prochee = models.TextField(max_length=300,
                               verbose_name='Прочие дополнительные требования и указания, конкретизирующие объем проектных работ',
                               blank=True)
    # Раздел 3 Пункты 46.1-46.7
    rekviziti_ogradostroy_plan = models.TextField(max_length=300, blank=True,
                                           verbose_name='Реквизиты документа "Градостроительный план земельного участка на котором планируется размещение объекта и (или) проект планировки территории  и проект межевания территории"')
    gradostroy_plan = models.FileField(
        verbose_name='',
        blank=True, upload_to='media/')
    rekviziti_res_engineers = models.TextField(max_length=300, blank=True,
                                                  verbose_name='Реквизиты документа "Результаты инженерных изысканий"')
    res_engineers = models.FileField(verbose_name='',
                                     blank=True, upload_to='media/')
    rekviziti_technich_condition = models.TextField(max_length=300, blank=True,
                                               verbose_name='Реквизиты документа "Технические условия на подключение объекта к сетям инженерно-технического обеспечения"')
    #technich_condition = models.FileField(
    #    verbose_name='',
    #    blank=True, upload_to='media/')
    rekviziti_materiali_proekta_planirovki = models.TextField(max_length=300, blank=True,
                                               verbose_name='Реквизиты документа "Имеющиеся материалы утвержденного проекта планировки участка строительства. Сведения о надземных и подземных инженерных сооружениях и коммуникациях"')
    materiali_proekta_planirovki = models.FileField(
        verbose_name='',
        blank=True, upload_to='media/')
    rekviziti_reshenie_o_soglasovanii = models.TextField(max_length=300, blank=True,
                                               verbose_name='Реквизиты документа "Решение о предварительном  согласовании  места размещения объекта"')
    reshenie_o_soglasovanii = models.FileField(
        verbose_name='',
        blank=True, upload_to='media/')
    rekviziti_doc_polnomochiya = models.TextField(max_length=300, blank=True,
                                               verbose_name='Реквизиты документа, подтверждающего полномочия лица, утверждающего задание на проектирование')
    doc_polnomochiya = models.FileField(
        verbose_name='',
        blank=True, upload_to='media/')
    rekviziti_other_documents = models.TextField(max_length=300, blank=True,
                                               verbose_name='Реквизиты иных документов и материалов, которые необходимо учесть в качестве исходных данных для проектирования')
    other_documents = models.FileField(
        verbose_name='',
        blank=True, upload_to='media/')

    def __str__(self):
        return self.title


class LinearData(models.Model):
    linear = models.ForeignKey(Linear, on_delete=models.CASCADE)
    document = models.FileField(verbose_name='',
        blank=True, upload_to='media/')

class Citizen(models.Model):
    # Шапка
    objectname = models.TextField(max_length=500,
        verbose_name='Наименование объекта капитального строительства')
    objectaddress = models.TextField(max_length=500,
        verbose_name='Адрес объекта капитального строительства')
    # Общие данные Пункты 1-10
    osnovanie = models.CharField(choices=osnovanie_choices, max_length=300,
                                          verbose_name='Основание для проектирования')
    rekviziti_osnovanie = models.TextField(max_length=300,
                                 verbose_name='Реквизиты документа-основания')
    zastroichik = models.TextField(max_length=300,
                                   verbose_name='Застройщик(заказчик)')
    investor = models.TextField(max_length=300,
                                verbose_name='Инвестор', blank=True)
    projectorganization = models.TextField(max_length=300,
                                           verbose_name='Проектная организация')
    vidrabot = models.CharField(choices=[('Строительство', 'Строительство'), ('Реконструкция', 'Реконструкция'),
                                         ('Капитальный ремонт', 'Капитальный ремонт')], max_length=60,
                                verbose_name='Вид работ')
    finansirovanie = models.CharField(choices=[('ФБ', 'Федеральный бюджет'), ('РБ', 'Региональный бюджет'),
                                         ('МБ', 'Местный бюджет'), ('ВБ', 'Внебюджетные средства')], max_length=60,
                                verbose_name='Выбор источника финансирования строительства')
    finansirovanie_rekviziti = models.TextField(max_length=300,
                                      verbose_name='Источник финансирования строительства')

    techobespech = models.TextField(max_length=300,
                                    verbose_name='Технические условия на подключение (присоединение) объекта к сетям инженерно-технического обеспечения (при наличии)',
                                    blank=True)
    techobespech_spravochnik = MultiSelectField(choices = my_systems_firstwave, verbose_name='Перечень сетей инженерно-технического обеспечения')
    techobespech_spravochnik_drugoe = models.TextField(max_length=100, verbose_name='Другое', blank = True)
    etapistroitelsta = models.TextField(choices=[('Выделение не требуется', 'Выделение не требуется'), ('Проработать вопрос в ходе проектирования', 'Проработать вопрос в ходе проектирования'), ('Выделить этапы', 'Выделить этапы')],
                                    max_length=60,verbose_name='Требования к выделению этапов строительства объектов')
    videlenie_etapov = models.TextField(max_length=300,verbose_name='Выделение этапов', blank = True)
    
    start_date = models.TextField(max_length=300,verbose_name='Дата начала строительства объекта')
    end_date = models.TextField(max_length=300,verbose_name='Дата окончания строительства объекта')
    techeconompokazatel = models.TextField(max_length=300,
                                           verbose_name='Требования к основным технико-экономическим показателям объекта (площадь, объем, протяженность,  количество этажей, производственная мощность, пропускная способность, грузооборот, интенсивность движения и другие показатели)')
    # Общие данные Пункты 11.1-11.7
    naznachenie = models.CharField(max_length=100, verbose_name='Назначение')
    prinadlezhnost = models.CharField(choices=[('Да', 'Да'), ('Нет', 'Нет')], max_length=3,
                                      verbose_name='Принадлежность к объектам транспортной инфраструктуры и к другим объектам, функционально-технологические особенности которых влияют на их безопасность')
    prinadlezhnost_text = models.TextField(max_length=300,verbose_name='Вид объекта строительства', blank = True)
    opasnieyavlenia = models.CharField(choices=[('Да', 'Да'), ('Нет', 'Нет')], max_length=3,
                                       verbose_name='Возможность возникновения опасных природных процессов и явлений и техногенных воздействий на территории, на которой будет осуществляться строительство объекта')
   
    categoryzdanii =  models.TextField(max_length=100, verbose_name='Категория зданий, сооружений, помещений по пожарной и взрывопожарной опасности')
    stepenognya =  models.TextField(max_length=100, verbose_name='Степень огнестойкости ')
    konstructive =  models.TextField(max_length=100, verbose_name='Класс конструктивной пожарной опасности ')
    functionalpozar =  models.TextField(max_length=100, verbose_name='Класс функциональной пожарной опасности')
    prebivanieludei = models.CharField(choices=[('Да', 'Да'), ('Нет', 'Нет')], max_length=3,
                                       verbose_name='Наличие помещений с постоянным пребыванием людей')
    urovenotvetstvennosti = models.CharField(
        choices=[('Повышенный', 'Повышенный'), ('Нормальный', 'Нормальный'), ('Пониженный', 'Пониженный')],
        max_length=60,
        verbose_name='Уровень ответственности')
    # Общие данные Пункты 12-16
    proektniireshenia = models.TextField(max_length=300,
                                         verbose_name='Требования к качеству, конкурентоспособности, экологичности и энергоэффективности проектных решений')
    inzhinerniziskania = models.TextField(max_length=300,
                                          verbose_name='Необходимость выполнения инженерных изысканий для подготовки проектной документации')
    predelnstoimost = models.TextField(max_length=300,
                                       verbose_name='Предполагаемая (предельная) стоимость строительства объекта')
    istochnikfinans = models.TextField(max_length=300,
                                       verbose_name='Сведения об источниках финансирования строительства объекта')
    # Раздел 2 Пункты 17 - 20 ТОЛЬКО ДЛЯ НЕЛИНЕЙНЫЙ ОБЪЕКТОВ (ПРОИЗВОДСТВ И НЕПРОИЗВОДСТВ НАЗНАЧЕНИЯ)
    shema_plan_org = models.TextField(max_length=300,
                                      verbose_name='Требования к схеме планировочной организации земельного участка',
                                      blank=True)
    shema_plan_org_RZO = models.CharField(
        choices=[('Пространство для пребывания людей', 'Пространство для пребывания людей'),
                 ('Пространство для ведения человеческой деятельности', 'Пространство для ведения человеческой деятельности'),
                 ('Пространство для хранения', 'Пространство для хранения'),
                 ('Пространство для технических систем', 'Пространство для технических систем'),
                 ('Пространство для связей между другими пространствами', 'Пространство для связей между другими пространствами'),
                 ('Пространство для движения транспорта', 'Пространство для движения транспорта'),
                 ('Пространство для физических процессов', 'Пространство для физических процессов'),
                 ('Пространство с неустановленным функциональным назначением', 'Пространство с неустановленным функциональным назначением'),
                 ('Территориальные зоны', 'Территориальные зоны')], max_length=60,
        verbose_name='Классификация земельного участка')
    
    arh_hud_reshenia = models.TextField(max_length=300,
                                        verbose_name='Требования к архитектурно-художественным решениям, включая требования к графическим материалам',
                                        blank=True)
    technologich_reshenia = models.TextField(max_length=300,
                                             verbose_name='Требования к технологическим решениям',
                                     blank=True)
    # Раздел 2 Пункты 21.1-21.17 Только для объектов производственного и непроизводственного назначения
    materiali = models.TextField(max_length=300,
                                 verbose_name='Порядок выбора и применения материалов, изделий, конструкций, оборудования и их согласования застройщиком',
                                 blank=True)
    stroitelnie_konstrukcii = models.TextField(max_length=300,
                                               verbose_name='Требования к строительным конструкциям',
                                               blank=True)
    fundament = models.TextField(max_length=300,
                                 verbose_name='Требования к фундаментам',
                                 blank=True)
    steni_podvali_cokol = models.TextField(max_length=300,
                                           verbose_name='Требования к стенам, подвалам и цокольному этажу',
                                           blank=True)
    steni_naruzhn = models.TextField(max_length=300,
                                     verbose_name='Требования к наружным стенам',
                                     blank=True)
    steni_vnutr = models.TextField(max_length=300,
                                   verbose_name='Требования к внутренним стенам и перегородкам',
                                   blank=True)
    perekritia = models.TextField(max_length=300,
                                  verbose_name='Требования к перекрытиям',
                                  blank=True)
    colonni = models.TextField(max_length=300,
                               verbose_name='Требования к колоннам, ригелям',
                               blank=True)
    lestnici = models.TextField(max_length=300,
                                verbose_name='Требования к лестницам',
                                blank=True)
    poli = models.TextField(max_length=300,
                            verbose_name='Требования к полам',
                            blank=True)
    krovlya = models.TextField(max_length=300,
                               verbose_name='Требования к кровле',
                               blank=True)
    vitrazhi = models.TextField(max_length=300,
                                verbose_name='Требования к витражам, окнам',
                                blank=True)
    dveri = models.TextField(max_length=300,
                             verbose_name='Требования к дверям',
                             blank=True)
    otdelka_vnutr = models.TextField(max_length=300,
                                     verbose_name='Требования к внутренней отделке',
                                     blank=True)
    otdelka_naruzhn = models.TextField(max_length=300,
                                       verbose_name='Требования к наружной отделке',
                                       blank=True)
    bezopasnost = models.TextField(max_length=300,
                                   verbose_name='Требования к обеспечению безопасности объекта при опасных природных процессах и явлениях и техногенных воздействиях',
                                   blank=True)
    inzh_zashita = models.TextField(max_length=300,
                                    verbose_name='Требования к инженерной защите территории объекта',
                                    blank=True)
    # Раздел 2 Пункты 24.1.1-24.1.11
    otoplenie = models.TextField(max_length=100,
                                 verbose_name='Отопление',
                                     blank=True)
    ventilyacia = models.TextField(max_length=100,
                                   verbose_name='Вентиляция',
                                     blank=True)
    vodoprovod = models.TextField(max_length=100,
                                  verbose_name='Водопровод',
                                     blank=True)
    kanalizacia = models.TextField(max_length=100,
                                   verbose_name='Канализация',
                                     blank=True)
    electrosnabzhenie = models.TextField(max_length=100,
                                         verbose_name='Электроснабжение',
                                     blank=True)
    telefonizacia = models.TextField(max_length=100,
                                     verbose_name='Телефонизация',
                                     blank=True)
    radiofikacia = models.TextField(max_length=100,
                                    verbose_name='Радиофикация',
                                     blank=True)
    inthernet = models.TextField(max_length=100,
                                 verbose_name='Информационно-телекоммуникационная сеть "Интернет"',
                                     blank=True)
    televidenie = models.TextField(max_length=100,
                                   verbose_name='Телевидение',
                                     blank=True)
    gazifikacia = models.TextField(max_length=100,
                                   verbose_name='Газификация',
                                     blank=True)
    avtomatizacia = models.TextField(max_length=100,
                                     verbose_name='Автоматизация и диспетчеризация',
                                     blank=True)
    # Раздел 2 Пункты 24.2.1-24.1.10
    vodosnabzhenie = models.TextField(max_length=100,
                                      verbose_name='Водоснабжение',
                                     blank=True)
    vodootvedenie = models.TextField(max_length=100,
                                     verbose_name='Водоотведение',
                                     blank=True)
    teplosnabzhenie = models.TextField(max_length=100,
                                       verbose_name='Теплоснабжение',
                                     blank=True)
    electrosnabzhenie_naruzh = models.TextField(max_length=100,
                                                verbose_name='Электроснабжение',
                                     blank=True)
    telefonizacia_naruzh = models.TextField(max_length=100,
                                            verbose_name='Телефонизация',
                                     blank=True)
    radiofikacia_naruzh = models.TextField(max_length=100,
                                           verbose_name='Радиофикация',
                                     blank=True)
    inthernet_naruzh = models.TextField(max_length=100,
                                        verbose_name='Информационно-телекоммуникационная сеть "Интернет"',
                                     blank=True)
    televidenie_naruzh = models.TextField(max_length=100,
                                          verbose_name='Телевидение',
                                     blank=True)
    gazosnabzhenie = models.TextField(max_length=100,
                                      verbose_name='Газоснабжение',
                                     blank=True)
    inoe_naruzh = models.TextField(max_length=100,
                                   verbose_name='Иные сети инженерно-технического обеспечения',
                                   blank=True)
    # Раздел 2 Пункты 25-37
    ohrana_okr_sredi = models.TextField(max_length=300,
                                        verbose_name='Требования к мероприятиям по охране окружающей среды',
                                        blank=True)
    obespeh_pozharn_bezop = models.TextField(max_length=300,
                                             verbose_name='Требования к мероприятиям по обеспечению пожарной безопасности',
                                             blank=True)
    energy_effekt = models.TextField(max_length=300,
                                     verbose_name='Требования к мероприятиям по обеспечению соблюдения требований энергетической эффективности и по оснащенности объекта приборами учета используемых энергетических ресурсов',
                                     blank=True)
    energy_effekt_klass = models.TextField(max_length=300,
                                             verbose_name='Класс энергетической эффективности',
                                     blank=True)
    energy_effekt_kharakteristika = models.TextField(max_length=300,
                                             verbose_name='Характеристика расхода тепловой энергии',
                                             blank=True)
    energy_effekt_rekviziti = models.TextField(max_length=300,
                                             verbose_name='Реквизиты энергетического паспорта(при наличии)',
                                             blank=True)
    invalidi = models.TextField(max_length=300,
                                verbose_name='Требования к мероприятиям по обеспечению доступа инвалидов к объекту',
                                blank=True)
    inzh_teh_ykreplenie = models.TextField(max_length=300,
                                           verbose_name='Требования к инженерно-техническому укреплению объекта в целях обеспечения его антитеррористической защищенности',
                                           blank=True)
    uslovia_prebivania = models.TextField(max_length=300,
                                          verbose_name='Требования к соблюдению безопасных для здоровья человека условий проживания и пребывания в объекте и требования к соблюдению безопасного уровня воздействия объекта на окружающую среду',
                                          blank=True)
    technich_ekspluatacia = models.TextField(max_length=300,
                                             verbose_name='Требования к технической эксплуатации и техническому обслуживанию объекта',
                                             blank=True)
    proekt_organizacii_str = models.TextField(max_length=300,
                                              verbose_name='Требования к проекту организации строительства объекта',
                                              blank=True)
    snos_sohranenie = models.TextField(max_length=300,
                                       verbose_name='Обоснование необходимости сноса или сохранения зданий, сооружений, зеленых насаждений, а также переноса инженерных сетей и коммуникаций, расположенных на земельном участке, на котором планируется размещение объекта',
                                       blank=True)
    blagoustroistvo = models.TextField(max_length=300,
                                       verbose_name='Требования к решениям по благоустройству прилегающей территории, к малым архитектурным формам и к планировочной организации земельного участка, на котором планируется размещение объекта',
                                       blank=True)
    vosstanovlenie = models.TextField(max_length=300,
                                      verbose_name='Требования к разработке проекта восстановления (рекультивации) нарушенных земель или плодородного слоя',
                                      blank=True)
    skladirovanie = models.TextField(max_length=300,
                                     verbose_name='Требования к местам складирования излишков грунта и (или) мусора при строительстве и протяженность маршрута их доставки',
                                     blank=True)
    nauchno_issled = models.TextField(max_length=300,
                                      verbose_name='Требования к выполнению научно-исследовательских и опытно- конструкторских работ в процессе проектирования и строительства объекта',
                                      blank=True)

    # Раздел 3 Пункты 38-45
    sostav_proektnoi_documentacii_spravochnik = MultiSelectField(
        choices=[('1', 'Раздел 1 "Пояснительная записка" '),
                 ('2', 'Раздел 2 "Схема планировочной организации земельного участка"'),
                 ('3', 'Раздел 3 "Архитектурные решения"'),
                 ('4', 'Раздел 4 "Конструктивные и объемно-планировочные решения"'),
                 ('5', 'Раздел 5 "Сведения об инженерном оборудовании, о сетях инженерно-технического обеспечения, перечень инженерно-технических мероприятий, содержание технологических решений"'),
                 ('6', 'Раздел 6 "Проект организации строительства"'),
                 ('7', 'Раздел 7 "Проект организации работ по сносу или демонтажу объектов капитального строительства"'),
                 ('8', 'Раздел 8 "Перечень мероприятий по охране окружающей среды"'),
                 ('9', 'Раздел 9 "Мероприятия по обеспечению пожарной безопасности"'),
                 ('10','Раздел 10 "Мероприятия по обеспечению доступа инвалидов"'),
                 ('11','Раздел 11 "Смета на строительство объектов капитального строительства"'),
                 ('12','Раздел 12 "Иная документация в случаях, предусмотренных федеральными законами"')],
        verbose_name='Выбор необходимых разделов проектной документации', blank=True)
    sostav_proektnoi_documentacii = models.TextField(max_length=300,
                                                     verbose_name='Иные требования к составу проектной документации, в том числе требования о разработке разделов проектной документации, наличие которых не является обязательным',
                                     blank=True)
    smetnaya_documentacia = models.TextField(max_length=300,
                                             verbose_name='Требования к подготовке сметной документации',
                                              blank=True)
    spec_tech_uslovia = models.TextField(max_length=300,
                                         verbose_name='Требования к разработке специальных технических условий',
                                              blank=True)
    standartizacia = models.TextField(max_length=300,
                                      verbose_name='Требования о применении при разработке проектной документации документов в области стандартизации, не включенных в перечень национальных стандартов и сводов правил',
                                      blank=True)
    demonstacii = models.TextField(max_length=300,
                                   verbose_name='Требования к выполнению демонстрационных материалов, макетов',
                                   blank=True)
    inform_modelirovanie = models.TextField(max_length=300,
                                            verbose_name='Требования о применении технологий информационного моделирования',
                                            blank=True)
    econom_effect_document = models.TextField(max_length=300,
                                              verbose_name='Требование о применении экономически эффективной проектной документации повторного использования',
                                              blank=True)
    prochee = models.TextField(max_length=300,
                               verbose_name='Прочие дополнительные требования и указания, конкретизирующие объем проектных работ',
                               blank=True)
    # Раздел 3 Пункты 46.1-46.7
    rekviziti_ogradostroy_plan = models.TextField(max_length=300, blank=True,
                                           verbose_name='Реквизиты документа "Градостроительный план земельного участка на котором планируется размещение объекта и (или) проект планировки территории  и проект межевания территории"')
    gradostroy_plan = models.FileField(
        verbose_name='',
        blank=True, upload_to='media/')
    rekviziti_res_engineers = models.TextField(max_length=300, blank=True,
                                                  verbose_name='Реквизиты документа "Результаты инженерных изысканий"')
    res_engineers = models.FileField(verbose_name='',
                                     blank=True, upload_to='media/')
    rekviziti_technich_condition = models.TextField(max_length=300, blank=True,
                                               verbose_name='Реквизиты документа "Технические условия на подключение объекта к сетям инженерно-технического обеспечения"')
    #technich_condition = models.FileField(
    #    verbose_name='',
    #    blank=True, upload_to='media/')
    rekviziti_materiali_proekta_planirovki = models.TextField(max_length=300, blank=True,
                                               verbose_name='Реквизиты документа "Имеющиеся материалы утвержденного проекта планировки участка строительства. Сведения о надземных и подземных инженерных сооружениях и коммуникациях"')
    materiali_proekta_planirovki = models.FileField(
        verbose_name='',
        blank=True, upload_to='media/')
    rekviziti_reshenie_o_soglasovanii = models.TextField(max_length=300, blank=True,
                                               verbose_name='Реквизиты документа "Решение о предварительном  согласовании  места размещения объекта"')
    reshenie_o_soglasovanii = models.FileField(
        verbose_name='',
        blank=True, upload_to='media/')
    rekviziti_doc_polnomochiya = models.TextField(max_length=300, blank=True,
                                               verbose_name='Реквизиты документа, подтверждающего полномочия лица, утверждающего задание на проектирование')
    doc_polnomochiya = models.FileField(
        verbose_name='',
        blank=True, upload_to='media/')
    rekviziti_other_documents = models.TextField(max_length=300, blank=True,
                                               verbose_name='Реквизиты иных документов и материалов, которые необходимо учесть в качестве исходных данных для проектирования')
    other_documents = models.FileField(
        verbose_name='',
        blank=True, upload_to='media/')

    def __str__(self):
        return self.title


class CitizenData(models.Model):
    citizen = models.ForeignKey(Citizen, on_delete=models.CASCADE)
    document = models.FileField(verbose_name='',
        blank=True, upload_to='media/')


class Industrial(models.Model):
  #Шапка
  objectname = models.TextField(max_length=500,
        verbose_name='Наименование объекта капитального строительства')
  objectaddress = models.TextField(max_length=500,
        verbose_name='Адрес объекта капитального строительства')
  #Общие данные Пункты 1-10
  osnovanie = models.CharField(choices=osnovanie_choices, max_length=300,
                                          verbose_name='Основание для проектирования')
  rekviziti_osnovanie = models.TextField(max_length=300,
                                 verbose_name='Реквизиты документа-основания')
  zastroichik = models.TextField(max_length=300,
                                 verbose_name='Застройщик(заказчик)')
  investor = models.TextField(max_length=300,
                              verbose_name='Инвестор', blank=True)
  projectorganization = models.TextField(max_length=300,
                                         verbose_name='Проектная организация')
  vidrabot = models.CharField(choices = [('Строительство','Строительство'),('Реконструкция','Реконструкция'),('Капитальный ремонт','Капитальный ремонт')], max_length=60,
                              verbose_name='Вид работ')
  finansirovanie = models.CharField(choices=[('ФБ', 'Федеральный бюджет'), ('РБ', 'Региональный бюджет'),
                                         ('МБ', 'Местный бюджет'), ('ВБ', 'Внебюджетные средства')], max_length=60,
                                verbose_name='Выбор источника финансирования строительства')
  finansirovanie_rekviziti = models.TextField(max_length=300,
                                      verbose_name='Источник финансирования строительства')
  techobespech = models.CharField(choices=[('Получение', 'Требуется разработка технических условий'), ('Продление', 'Требуется продление или актуализация технических условий'),
                                         ('Получены', 'Имеются актуальные технические условия')], max_length=60,
                                    verbose_name='Технические условия на подключение (присоединение) объекта к сетям инженерно-технического обеспечения (при наличии)')
  techobespech_spravochnik = MultiSelectField(choices = my_systems_firstwave, verbose_name='Перечень сетей инженерно-технического обеспечения')
  techobespech_spravochnik_drugoe = models.TextField(max_length=100, verbose_name='Другое', blank = True)
  etapistroitelsta = models.TextField(choices=[('Выделение не требуется', 'Выделение не требуется'), ('Проработать вопрос в ходе проектирования', 'Проработать вопрос в ходе проектирования'), ('Выделить этапы', 'Выделить этапы')],
                                    max_length=60,verbose_name='Требования к выделению этапов строительства объектов')
  videlenie_etapov = models.TextField(max_length=300,verbose_name='Выделение этапов', blank = True)
  start_date = models.TextField(max_length=300,verbose_name='Дата начала строительства объекта')
  end_date = models.TextField(max_length=300,verbose_name='Дата окончания строительства объекта')
  techeconompokazatel = models.TextField(max_length=300,
                                         verbose_name='Требования к основным технико-экономическим показателям объекта (площадь, объем, протяженность,  количество этажей, производственная мощность, пропускная способность, грузооборот, интенсивность движения и другие показатели)')
  #Общие данные Пункты 11.1-11.7
  naznachenie = models.CharField(max_length=100, verbose_name='Назначение')
  prinadlezhnost = models.CharField(choices = [('Да','Да'),('Нет','Нет')], max_length=3,
                                    verbose_name='Принадлежность к объектам транспортной инфраструктуры и к другим объектам, функционально-технологические особенности которых влияют на их безопасность')
  prinadlezhnost_text = models.TextField(max_length=300,verbose_name='Вид объекта строительства', blank = True)

  opasnieyavlenia = models.CharField(choices= [('Да', 'Да'), ('Нет', 'Нет')], max_length=3,
                                    verbose_name='Возможность возникновения опасных природных процессов и явлений и техногенных воздействий на территории, на которой будет осуществляться строительство объекта')
  klassopasnosti = models.CharField(choices=[('Нет', 'Нет'), ('I класс опасности', 'I класс опасности'), ('II класс опасности', 'II класс опасности'),('III класс опасности', 'III класс опасности'),('IV класс опасности', 'IV класс опасности')], max_length=30,
                                    verbose_name='Принадлежность к опасным производственным объектам')
  klassopasnosti_klass = models.TextField(max_length=100, verbose_name='Класс опасного объекта', blank = True)
  klassopasnosti_category = models.TextField(max_length=100, verbose_name='Категория опасного объекта', blank = True)
  categoryzdanii =  models.TextField(max_length=100, verbose_name='Категория зданий, сооружений, помещений по пожарной и взрывопожарной опасности')
  stepenognya =  models.TextField(max_length=100, verbose_name='Степень огнестойкости ')
  konstructive =  models.TextField(max_length=100, verbose_name='Класс конструктивной пожарной опасности ')
  functionalpozar =  models.TextField(max_length=100, verbose_name='Класс функциональной пожарной опасности')
  prebivanieludei = models.CharField(choices=[('Да', 'Да'), ('Нет', 'Нет')], max_length=3,
                                    verbose_name='Наличие помещений с постоянным пребыванием людей')
  urovenotvetstvennosti = models.CharField(choices=[('Повышенный', 'Повышенный'), ('Нормальный', 'Нормальный'), ('Пониженный', 'Пониженный')], max_length=60,
                                           verbose_name='Уровень ответственности')
  #Общие данные Пункты 12-16
  opasniobekt = models.TextField(max_length=300,
                                         verbose_name='Требования о необходимости соответствия проектной документации обоснованию безопасности опасного производственного объекта', blank=True)
  proektniireshenia = models.TextField(max_length=300,
                                         verbose_name='Требования к качеству, конкурентоспособности, экологичности и энергоэффективности проектных решений')
  inzhinerniziskania = models.TextField(max_length=300,
                                         verbose_name='Необходимость выполнения инженерных изысканий для подготовки проектной документации')
  predelnstoimost = models.TextField(max_length=300,
                                         verbose_name='Предполагаемая (предельная) стоимость строительства объекта')
  istochnikfinans = models.TextField(max_length=300,
                                         verbose_name='Сведения об источниках финансирования строительства объекта')
  #Раздел 2 Пункты 17 - 20
  shema_plan_org = models.TextField(max_length=300,
                                      verbose_name='Требования к схеме планировочной организации земельного участка',
                                      blank=True)
  shema_plan_org_RZO = models.CharField(
        choices=[('Пространство для пребывания людей', 'Пространство для пребывания людей'),
                 ('Пространство для ведения человеческой деятельности', 'Пространство для ведения человеческой деятельности'),
                 ('Пространство для хранения', 'Пространство для хранения'),
                 ('Пространство для технических систем', 'Пространство для технических систем'),
                 ('Пространство для связей между другими пространствами', 'Пространство для связей между другими пространствами'),
                 ('Пространство для движения транспорта', 'Пространство для движения транспорта'),
                 ('Пространство для физических процессов', 'Пространство для физических процессов'),
                 ('Пространство с неустановленным функциональным назначением', 'Пространство с неустановленным функциональным назначением'),
                 ('Территориальные зоны', 'Территориальные зоны')], max_length=60,
        verbose_name='Классификация земельного участка')
  arh_hud_reshenia = models.TextField(max_length=300,
                                 verbose_name='Требования к архитектурно-художественным решениям, включая требования к графическим материалам',
                                 blank=True)
  technologich_reshenia = models.TextField(max_length=300,
                                    verbose_name='Требования к технологическим решениям',
                                              blank=True)
  #Раздел 2 Пункты 21.1-21.17 Только для объектов производственного и непроизводственного назначения
  materiali = models.TextField(max_length=300,
                                 verbose_name='Порядок выбора и применения материалов, изделий, конструкций, оборудования и их согласования застройщиком',
                                 blank=True)
  stroitelnie_konstrukcii = models.TextField(max_length=300,
                                 verbose_name='Требования к строительным конструкциям',
                                 blank=True)
  fundament = models.TextField(max_length=300,
                                 verbose_name='Требования к фундаментам',
                                 blank=True)
  steni_podvali_cokol = models.TextField(max_length=300,
                               verbose_name='Требования к стенам, подвалам и цокольному этажу',
                               blank=True)
  steni_naruzhn = models.TextField(max_length=300,
                               verbose_name='Требования к наружным стенам',
                               blank=True)
  steni_vnutr = models.TextField(max_length=300,
                               verbose_name='Требования к внутренним стенам и перегородкам',
                               blank=True)
  perekritia = models.TextField(max_length=300,
                               verbose_name='Требования к перекрытиям',
                               blank=True)
  colonni = models.TextField(max_length=300,
                               verbose_name='Требования к колоннам, ригелям',
                               blank=True)
  lestnici = models.TextField(max_length=300,
                               verbose_name='Требования к лестницам',
                               blank=True)
  poli = models.TextField(max_length=300,
                               verbose_name='Требования к полам',
                               blank=True)
  krovlya = models.TextField(max_length=300,
                          verbose_name='Требования к кровле',
                          blank=True)
  vitrazhi = models.TextField(max_length=300,
                          verbose_name='Требования к витражам, окнам',
                          blank=True)
  dveri = models.TextField(max_length=300,
                          verbose_name='Требования к дверям',
                          blank=True)
  otdelka_vnutr = models.TextField(max_length=300,
                          verbose_name='Требования к внутренней отделке',
                          blank=True)
  otdelka_naruzhn = models.TextField(max_length=300,
                          verbose_name='Требования к наружной отделке',
                          blank=True)
  bezopasnost = models.TextField(max_length=300,
                          verbose_name='Требования к обеспечению безопасности объекта при опасных природных процессах и явлениях и техногенных воздействиях',
                          blank=True)
  inzh_zashita = models.TextField(max_length=300,
                          verbose_name='Требования к инженерной защите территории объекта',
                          blank=True)
  #Раздел 2 Пункты 24.1.1-24.1.11
  otoplenie = models.TextField(max_length=100,
                               verbose_name='Отопление',
                               blank=True)
  ventilyacia = models.TextField(max_length=100,
                                 verbose_name='Вентиляция',
                                 blank=True)
  vodoprovod = models.TextField(max_length=100,
                                verbose_name='Водопровод',
                                blank=True)
  kanalizacia = models.TextField(max_length=100,
                                 verbose_name='Канализация',
                                 blank=True)
  electrosnabzhenie = models.TextField(max_length=100,
                                       verbose_name='Электроснабжение',
                                       blank=True)
  telefonizacia = models.TextField(max_length=100,
                                   verbose_name='Телефонизация',
                                   blank=True)
  radiofikacia = models.TextField(max_length=100,
                                  verbose_name='Радиофикация',
                                  blank=True)
  inthernet = models.TextField(max_length=100,
                               verbose_name='Информационно-телекоммуникационная сеть "Интернет"',
                               blank=True)
  televidenie = models.TextField(max_length=100,
                                 verbose_name='Телевидение',
                                 blank=True)
  gazifikacia = models.TextField(max_length=100,
                                 verbose_name='Газификация',
                                 blank=True)
  avtomatizacia = models.TextField(max_length=100,
                                   verbose_name='Автоматизация и диспетчеризация',
                                   blank=True)
  # Раздел 2 Пункты 24.2.1-24.1.10
  vodosnabzhenie = models.TextField(max_length=100,
                                    verbose_name='Водоснабжение',
                                    blank=True)
  vodootvedenie = models.TextField(max_length=100,
                                   verbose_name='Водоотведение',
                                   blank=True)
  teplosnabzhenie = models.TextField(max_length=100,
                                     verbose_name='Теплоснабжение',
                                     blank=True)
  electrosnabzhenie_naruzh = models.TextField(max_length=100,
                                              verbose_name='Электроснабжение',
                                              blank=True)
  telefonizacia_naruzh = models.TextField(max_length=100,
                                          verbose_name='Телефонизация',
                                          blank=True)
  radiofikacia_naruzh = models.TextField(max_length=100,
                                         verbose_name='Радиофикация',
                                         blank=True)
  inthernet_naruzh = models.TextField(max_length=100,
                                      verbose_name='Информационно-телекоммуникационная сеть "Интернет"',
                                      blank=True)
  televidenie_naruzh = models.TextField(max_length=100,
                                        verbose_name='Телевидение',
                                        blank=True)
  gazosnabzhenie = models.TextField(max_length=100,
                                    verbose_name='Газоснабжение',
                                    blank=True)
  inoe_naruzh = models.TextField(max_length=100,
                                 verbose_name='Иные сети инженерно-технического обеспечения',
                                 blank=True)
  #Раздел 2 Пункты 25-37
  ohrana_okr_sredi = models.TextField(max_length=300,
                                      verbose_name='Требования к мероприятиям по охране окружающей среды',
                                      blank=True)
  obespeh_pozharn_bezop = models.TextField(max_length=300,
                                           verbose_name='Требования к мероприятиям по обеспечению пожарной безопасности',
                                           blank=True)
  energy_effekt = models.TextField(max_length=300,
                                   verbose_name='Требования к мероприятиям по обеспечению соблюдения требований энергетической эффективности и по оснащенности объекта приборами учета используемых энергетических ресурсов',
                                   blank=True)
  energy_effekt_klass = models.TextField(max_length=300,
                                             verbose_name='Класс энергетической эффективности',
                                     blank=True)
  energy_effekt_kharakteristika = models.TextField(max_length=300,
                                             verbose_name='Характеристика расхода тепловой энергии',
                                             blank=True)
  energy_effekt_rekviziti = models.TextField(max_length=300,
                                             verbose_name='Реквизиты энергетического паспорта(при наличии)',
                                             blank=True)
  invalidi = models.TextField(max_length=300,
                              verbose_name='Требования к мероприятиям по обеспечению доступа инвалидов к объекту',
                              blank=True)
  inzh_teh_ykreplenie = models.TextField(max_length=300,
                                         verbose_name='Требования к инженерно-техническому укреплению объекта в целях обеспечения его антитеррористической защищенности',
                                         blank=True)
  uslovia_prebivania = models.TextField(max_length=300,
                                        verbose_name='Требования к соблюдению безопасных для здоровья человека условий проживания и пребывания в объекте и требования к соблюдению безопасного уровня воздействия объекта на окружающую среду',
                                        blank=True)
  technich_ekspluatacia = models.TextField(max_length=300,
                                           verbose_name='Требования к технической эксплуатации и техническому обслуживанию объекта',
                                           blank=True)
  proekt_organizacii_str = models.TextField(max_length=300,
                                            verbose_name='Требования к проекту организации строительства объекта',
                                            blank=True)
  snos_sohranenie = models.TextField(max_length=300,
                                     verbose_name='Обоснование необходимости сноса или сохранения зданий, сооружений, зеленых насаждений, а также переноса инженерных сетей и коммуникаций, расположенных на земельном участке, на котором планируется размещение объекта',
                                     blank=True)
  blagoustroistvo = models.TextField(max_length=300,
                                     verbose_name='Требования к решениям по благоустройству прилегающей территории, к малым архитектурным формам и к планировочной организации земельного участка, на котором планируется размещение объекта',
                                     blank=True)
  vosstanovlenie = models.TextField(max_length=300,
                                    verbose_name='Требования к разработке проекта восстановления (рекультивации) нарушенных земель или плодородного слоя',
                                    blank=True)
  skladirovanie = models.TextField(max_length=300,
                                   verbose_name='Требования к местам складирования излишков грунта и (или) мусора при строительстве и протяженность маршрута их доставки',
                                   blank=True)
  nauchno_issled = models.TextField(max_length=300,
                                    verbose_name='Требования к выполнению научно-исследовательских и опытно- конструкторских работ в процессе проектирования и строительства объекта',
                                    blank=True)

  # Раздел 3 Пункты 38-45
  sostav_proektnoi_documentacii_spravochnik = MultiSelectField(
        choices=[('1', 'Раздел 1 "Пояснительная записка" '),
                 ('2', 'Раздел 2 "Схема планировочной организации земельного участка"'),
                 ('3', 'Раздел 3 "Архитектурные решения"'),
                 ('4', 'Раздел 4 "Конструктивные и объемно-планировочные решения"'),
                 ('5', 'Раздел 5 "Сведения об инженерном оборудовании, о сетях инженерно-технического обеспечения, перечень инженерно-технических мероприятий, содержание технологических решений"'),
                 ('6', 'Раздел 6 "Проект организации строительства"'),
                 ('7', 'Раздел 7 "Проект организации работ по сносу или демонтажу объектов капитального строительства"'),
                 ('8', 'Раздел 8 "Перечень мероприятий по охране окружающей среды"'),
                 ('9', 'Раздел 9 "Мероприятия по обеспечению пожарной безопасности"'),
                 ('10','Раздел 10 "Мероприятия по обеспечению доступа инвалидов"'),
                 ('11','Раздел 11 "Смета на строительство объектов капитального строительства"'),
                 ('12','Раздел 12 "Иная документация в случаях, предусмотренных федеральными законами"')],
        verbose_name='Выбор необходимых разделов проектной документации', blank=True)
  sostav_proektnoi_documentacii = models.TextField(max_length=300,
                                                     verbose_name='Иные требования к составу проектной документации, в том числе требования о разработке разделов проектной документации, наличие которых не является обязательным',
                                     blank=True)
  smetnaya_documentacia = models.TextField(max_length=300,
                                           verbose_name='Требования к подготовке сметной документации',
                                           blank=True)
  spec_tech_uslovia = models.TextField(max_length=300,
                                       verbose_name='Требования к разработке специальных технических условий',
                                       blank=True)
  standartizacia = models.TextField(max_length=300,
                                    verbose_name='Требования о применении при разработке проектной документации документов в области стандартизации, не включенных в перечень национальных стандартов и сводов правил',
                                    blank=True)
  demonstacii = models.TextField(max_length=300,
                                 verbose_name='Требования к выполнению демонстрационных материалов, макетов',
                                 blank=True)
  inform_modelirovanie = models.TextField(max_length=300,
                                          verbose_name='Требования о применении технологий информационного моделирования',
                                          blank=True)
  econom_effect_document = models.TextField(max_length=300,
                                            verbose_name='Требование о применении экономически эффективной проектной документации повторного использования',
                                            blank=True)
  prochee = models.TextField(max_length=300,
                             verbose_name='Прочие дополнительные требования и указания, конкретизирующие объем проектных работ',
                             blank=True)
  #Раздел 3 Пункты 46.1-46.7
  rekviziti_ogradostroy_plan = models.TextField(max_length=300, blank=True,
                                           verbose_name='Реквизиты документа "Градостроительный план земельного участка на котором планируется размещение объекта и (или) проект планировки территории  и проект межевания территории"')
  gradostroy_plan = models.FileField(
        verbose_name='',
        blank=True, upload_to='media/')
  rekviziti_res_engineers = models.TextField(max_length=300, blank=True,
                                                  verbose_name='Реквизиты документа "Результаты инженерных изысканий"')
  res_engineers = models.FileField(verbose_name='',
                                     blank=True, upload_to='media/')
  rekviziti_technich_condition = models.TextField(max_length=300, blank=True,
                                               verbose_name='Реквизиты документа "Технические условия на подключение объекта к сетям инженерно-технического обеспечения"')
  #technich_condition = models.FileField(
  #      verbose_name='',
  #      blank=True, upload_to='media/')
  rekviziti_materiali_proekta_planirovki = models.TextField(max_length=300, blank=True,
                                               verbose_name='Реквизиты документа "Имеющиеся материалы утвержденного проекта планировки участка строительства. Сведения о надземных и подземных инженерных сооружениях и коммуникациях"')
  materiali_proekta_planirovki = models.FileField(
        verbose_name='',
        blank=True, upload_to='media/')
  rekviziti_reshenie_o_soglasovanii = models.TextField(max_length=300, blank=True,
                                               verbose_name='Реквизиты документа "Решение о предварительном  согласовании  места размещения объекта"')
  reshenie_o_soglasovanii = models.FileField(
        verbose_name='',
        blank=True, upload_to='media/')
  rekviziti_doc_polnomochiya = models.TextField(max_length=300, blank=True,
                                               verbose_name='Реквизиты документа, подтверждающего полномочия лица, утверждающего задание на проектирование')
  doc_polnomochiya = models.FileField(
        verbose_name='',
        blank=True, upload_to='media/')
  rekviziti_other_documents = models.TextField(max_length=300, blank=True,
                                               verbose_name='Реквизиты иных документов и материалов, которые необходимо учесть в качестве исходных данных для проектирования')
  other_documents = models.FileField(
        verbose_name='',
        blank=True, upload_to='media/')

  def __str__(self):
    return self.title

class IndustrialData(models.Model):
    industrial = models.ForeignKey(Industrial, on_delete=models.CASCADE)
    document = models.FileField(verbose_name='',
        blank=True, upload_to='media/')