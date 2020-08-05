from django.db import models
from django.db import models
from django.contrib.auth.models import User
from buy.models import Plan, Request

class Notification(models.Model):
    unusual_activity = models.BooleanField(blank=True, default=True)
    new_browser = models.BooleanField(blank=True, default=True)

    sales_and_latest_news = models.BooleanField(blank=True, default=True)
    features_and_updates = models.BooleanField(blank=True, default=True)
    tips = models.BooleanField(blank=True, default=True)

class WebSite(models.Model):
    INDASTRY = (
        ('eCommerce','eCommerce'),
        ('Business','Business'),
        ('Entertainment','Entertainment'),
        ('Portfolio','Portfolio'),
        ('Media','Media'),
        ('Brochure','Brochure'),
        ('Nonprofit','Nonprofit'),
        ('Educational','Educational'),
        ('Infopreneur','Infopreneur'),
        ('Personal','Personal'),
        ('Web Portal','Web Portal'),
        ('Wiki or Community Forum','Wiki or Community Forum'),
        
    )
    name = models.CharField(max_length=100, default='')
    type = models.CharField(max_length=100, choices=INDASTRY)
    domain = models.URLField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='website_user', default='')

    def __str__(self):
        return self.name

class Address(models.Model):
    COUNTRY = (
    ('AX','Åland Islands'),
    ('AF','Afghanistan'),
    ('AL','Albania'),
    ('DZ','Algeria'),
    ('AD','Andorra'),
    ('AO','Angola'),
    ('AI','Anguilla'),
    ('AQ','Antarctica'),
    ('AG','Antigua and Barbuda'),
    ('AR','Argentina'),
    ('AM','Armenia'),
    ('AW','Aruba'),
    ('AUD','Australia'),
    ('AT','Austria'),
    ('AZ','Azerbaijan'),
    ('BS','Bahamas'),
    ('BH','Bahrain'),
    ('BD','Bangladesh'),
    ('BB','Barbados'),
    ('BY','Belarus'),
    ('PW','Belau'),
    ('BE','Belgium'),
    ('BZ','Belize'),
    ('BJ','Benin'),
    ('BM','Bermuda'),
    ('BT','Bhutan'),
    ('BO','Bolivia'),
    ('BQ','Bonaire, Saint Eustatius and Saba'),
    ('BA','Bosnia and Herzegovina'),
    ('BW','Botswana'),
    ('BV','Bouvet Island'),
    ('BR','Brazil'),
    ('IO','British Indian Ocean Territory'),
    ('VG','British Virgin Islands'),
    ('BN','Brunei'),
    ('BG','Bulgaria'),
    ('BF','Burkina Faso'),
    ('BI','Burundi'),
    ('KH','Cambodia'),
    ('CM','Cameroon'),
    ('CAD','Canada'),
    ('CV','Cape Verde'),
    ('KY','Cayman Islands'),
    ('CF','Central African Republic'),
    ('TD','Chad'),
    ('CL','Chile'),
    ('CN','China'),
    ('CX','Christmas Island'),
    ('CC','Cocos (Keeling) Islands'),
    ('CO','Colombia'),
    ('KM','Comoros'),
    ('CG','Congo (Brazzaville)'),
    ('CD','Congo (Kinshasa)'),
    ('CK','Cook Islands'),
    ('CR','Costa Rica'),
    ('HR','Croatia'),
    ('CU','Cuba'),
    ('CW','CuraÇao'),
    ('CY','Cyprus'),
    ('CZ','Czech Republic'),
    ('DK','Denmark'),
    ('DJ','Djibouti'),
    ('DM','Dominica'),
    ('DO','Dominican Republic'),
    ('EC','Ecuador'),
    ('EG','Egypt'),
    ('SV','El Salvador'),
    ('GQ','Equatorial Guinea'),
    ('ER','Eritrea'),
    ('EE','Estonia'),
    ('ET','Ethiopia'),
    ('FK','Falkland Islands'),
    ('FO','Faroe Islands'),
    ('FJ','Fiji'),
    ('FI','Finland'),
    ('FR','France'),
    ('GF','French Guiana'),
    ('PF','French Polynesia'),
    ('TF','French Southern Territories'),
    ('GA','Gabon'),
    ('GM','Gambia'),
    ('GE','Georgia'),
    ('DE','Germany'),
    ('GH','Ghana'),
    ('GI','Gibraltar'),
    ('GR','Greece'),
    ('GL','Greenland'),
    ('GD','Grenada'),
    ('GP','Guadeloupe'),
    ('GT','Guatemala'),
    ('GG','Guernsey'),
    ('GN','Guinea'),
    ('GW','Guinea-Bissau'),
    ('GY','Guyana'),
    ('HT','Haiti'),
    ('HM','Heard Island and McDonald Islands'),
    ('HN','Honduras'),
    ('HK','Hong Kong'),
    ('HU','Hungary'),
    ('IS','Iceland'),
    ('IN','India'),
    ('ID','Indonesia'),
    ('IR','Iran'),
    ('IQ','Iraq'),
    ('IM','Isle of Man'),
    ('IL','Israel'),
    ('IT','Italy'),
    ('CI','Ivory Coast'),
    ('JM','Jamaica'),
    ('JPY','Japan'),
    ('JE','Jersey'),
    ('JO','Jordan'),
    ('KZ','Kazakhstan'),
    ('KE','Kenya'),
    ('KI','Kiribati'),
    ('KW','Kuwait'),
    ('KG','Kyrgyzstan'),
    ('LA','Laos'),
    ('LV','Latvia'),
    ('LB','Lebanon'),
    ('LS','Lesotho'),
    ('LR','Liberia'),
    ('LY','Libya'),
    ('LI','Liechtenstein'),
    ('LT','Lithuania'),
    ('LU','Luxembourg'),
    ('MO','Macao S.A.R., China'),
    ('MK','Macedonia'),
    ('MG','Madagascar'),
    ('MW','Malawi'),
    ('MY','Malaysia'),
    ('MV','Maldives'),
    ('ML','Mali'),
    ('MT','Malta'),
    ('MH','Marshall Islands'),
    ('MQ','Martinique'),
    ('MR','Mauritania'),
    ('MU','Mauritius'),
    ('YT','Mayotte'),
    ('MX','Mexico'),
    ('FM','Micronesia'),
    ('MD','Moldova'),
    ('MC','Monaco'),
    ('MN','Mongolia'),
    ('ME','Montenegro'),
    ('MS','Montserrat'),
    ('MA','Morocco'),
    ('MZ','Mozambique'),
    ('MM','Myanmar'),
    ('NA','Namibia'),
    ('NR','Nauru'),
    ('NP','Nepal'),
    ('NL','Netherlands'),
    ('AN','Netherlands Antilles'),
    ('NC','New Caledonia'),
    ('NZ','New Zealand'),
    ('NI','Nicaragua'),
    ('NE','Niger'),
    ('NG','Nigeria'),
    ('NU','Niue'),
    ('NF','Norfolk Island'),
    ('KP','North Korea'),
    ('NO','Norway'),
    ('OM','Oman'),
    ('PK','Pakistan'),
    ('PS','Palestinian Territory'),
    ('PA','Panama'),
    ('PG','Papua New Guinea'),
    ('PY','Paraguay'),
    ('PE','Peru'),
    ('PH','Philippines'),
    ('PN','Pitcairn'),
    ('PL','Poland'),
    ('PT','Portugal'),
    ('QA','Qatar'),
    ('IE','Republic of Ireland'),
    ('RE','Reunion'),
    ('RO','Romania'),
    ('RU','Russia'),
    ('RW','Rwanda'),
    ('ST','São Tomé and Príncipe'),
    ('BL','Saint Barthélemy'),
    ('SH','Saint Helena'),
    ('KN','Saint Kitts and Nevis'),
    ('LC','Saint Lucia'),
    ('SX','Saint Martin (Dutch part)'),
    ('MF','Saint Martin (French part)'),
    ('PM','Saint Pierre and Miquelon'),
    ('VC','Saint Vincent and the Grenadines'),
    ('SM','San Marino'),
    ('SA','Saudi Arabia'),
    ('SN','Senegal'),
    ('RS','Serbia'),
    ('SC','Seychelles'),
    ('SL','Sierra Leone'),
    ('SG','Singapore'),
    ('SK','Slovakia'),
    ('SI','Slovenia'),
    ('SB','Solomon Islands'),
    ('SO','Somalia'),
    ('ZAR','South Africa'),
    ('GS','South Georgia/Sandwich Islands'),
    ('KR','South Korea'),
    ('SS','South Sudan'),
    ('ES','Spain'),
    ('LK','Sri Lanka'),
    ('SD','Sudan'),
    ('SR','Suriname'),
    ('SJ','Svalbard and Jan Mayen'),
    ('SZ','Swaziland'),
    ('SE','Sweden'),
    ('CH','Switzerland'),
    ('SY','Syria'),
    ('TW','Taiwan'),
    ('TJ','Tajikistan'),
    ('TZ','Tanzania'),
    ('TH','Thailand'),
    ('TL','Timor-Leste'),
    ('TG','Togo'),
    ('TK','Tokelau'),
    ('TO','Tonga'),
    ('TT','Trinidad and Tobago'),
    ('TN','Tunisia'),
    ('TR','Turkey'),
    ('TM','Turkmenistan'),
    ('TC','Turks and Caicos Islands'),
    ('TV','Tuvalu'),
    ('UG','Uganda'),
    ('UA','Ukraine'),
    ('AE','United Arab Emirates'),
    ('GBP','United Kingdom (UK)'),
    ('USA','United States (US)'),
    ('UY','Uruguay'),
    ('UZ','Uzbekistan'),
    ('VU','Vanuatu'),
    ('VA','Vatican'),
    ('VE','Venezuela'),
    ('VN','Vietnam'),
    ('WF','Wallis and Futuna'),
    ('EH','Western Sahara'),
    ('WS','Western Samoa'),
    ('YE','Yemen'),
    ('ZM','Zambia'),
    ('ZW','Zimbabwe'),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='address')
    addres_line_1 = models.CharField(max_length=200)
    addres_line_2 = models.CharField(max_length=200)
    province = models.CharField(max_length=200)
    country = models.CharField(max_length=200, choices=COUNTRY)
        
class Profile(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    my_websites = models.ForeignKey(WebSite, on_delete=models.CASCADE, default='', null=True, blank=True)
    


    def __str__(self):
        return f'{self.user.username} Profile'
