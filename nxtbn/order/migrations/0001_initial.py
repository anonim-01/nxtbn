# Generated by Django 4.2.11 on 2024-09-23 03:52

from decimal import Decimal
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import nxtbn.core.mixin
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('street_address', models.CharField(max_length=255)),
                ('city', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=100)),
                ('postal_code', models.CharField(max_length=20)),
                ('country', models.CharField(max_length=100)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('phone_number', models.CharField(blank=True, max_length=15, null=True)),
                ('email_address', models.EmailField(blank=True, max_length=254, null=True)),
                ('is_default_delivery_address', models.BooleanField(default=False)),
            ],
            options={
                'ordering': ('-is_default_delivery_address', 'last_name', 'first_name'),
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('alias', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('currency', models.CharField(choices=[('USD', 'United States Dollar'), ('EUR', 'Euro'), ('GBP', 'British Pound Sterling'), ('JPY', 'Japanese Yen'), ('AUD', 'Australian Dollar'), ('CAD', 'Canadian Dollar'), ('CHF', 'Swiss Franc'), ('CNY', 'Chinese Yuan'), ('SEK', 'Swedish Krona'), ('NZD', 'New Zealand Dollar'), ('INR', 'Indian Rupee'), ('BRL', 'Brazilian Real'), ('RUB', 'Russian Ruble'), ('ZAR', 'South African Rand'), ('AED', 'United Arab Emirates Dirham'), ('AFN', 'Afghan Afghani'), ('ALL', 'Albanian Lek'), ('AMD', 'Armenian Dram'), ('ANG', 'Netherlands Antillean Guilder'), ('AOA', 'Angolan Kwanza'), ('ARS', 'Argentine Peso'), ('AWG', 'Aruban Florin'), ('AZN', 'Azerbaijani Manat'), ('BAM', 'Bosnia and Herzegovina Convertible Mark'), ('BBD', 'Barbadian Dollar'), ('BDT', 'Bangladeshi Taka'), ('BGN', 'Bulgarian Lev'), ('BHD', 'Bahraini Dinar'), ('BIF', 'Burundian Franc'), ('BMD', 'Bermudian Dollar'), ('BND', 'Brunei Dollar'), ('BOB', 'Bolivian Boliviano'), ('BSD', 'Bahamian Dollar'), ('BTN', 'Bhutanese Ngultrum'), ('BWP', 'Botswana Pula'), ('BYN', 'Belarusian Ruble'), ('BZD', 'Belize Dollar'), ('CDF', 'Congolese Franc'), ('CLP', 'Chilean Peso'), ('COP', 'Colombian Peso'), ('CRC', 'Costa Rican Colón'), ('CUP', 'Cuban Peso'), ('CVE', 'Cape Verdean Escudo'), ('CZK', 'Czech Koruna'), ('DJF', 'Djiboutian Franc'), ('DKK', 'Danish Krone'), ('DOP', 'Dominican Peso'), ('DZD', 'Algerian Dinar'), ('EGP', 'Egyptian Pound'), ('ERN', 'Eritrean Nakfa'), ('ETB', 'Ethiopian Birr'), ('FJD', 'Fijian Dollar'), ('FKP', 'Falkland Islands Pound'), ('FOK', 'Faroese Króna'), ('GEL', 'Georgian Lari'), ('GGP', 'Guernsey Pound'), ('GHS', 'Ghanaian Cedi'), ('GIP', 'Gibraltar Pound'), ('GMD', 'Gambian Dalasi'), ('GNF', 'Guinean Franc'), ('GTQ', 'Guatemalan Quetzal'), ('GYD', 'Guyanese Dollar'), ('HKD', 'Hong Kong Dollar'), ('HNL', 'Honduran Lempira'), ('HRK', 'Croatian Kuna'), ('HTG', 'Haitian Gourde'), ('HUF', 'Hungarian Forint'), ('IDR', 'Indonesian Rupiah'), ('ILS', 'Israeli New Shekel'), ('IMP', 'Isle of Man Pound'), ('IQD', 'Iraqi Dinar'), ('IRR', 'Iranian Rial'), ('ISK', 'Icelandic Króna'), ('JMD', 'Jamaican Dollar'), ('JOD', 'Jordanian Dinar'), ('KES', 'Kenyan Shilling'), ('KGS', 'Kyrgyzstani Som'), ('KHR', 'Cambodian Riel'), ('KID', 'Kiribati Dollar'), ('KMF', 'Comorian Franc'), ('KRW', 'South Korean Won'), ('KWD', 'Kuwaiti Dinar'), ('KYD', 'Cayman Islands Dollar'), ('KZT', 'Kazakhstani Tenge'), ('LAK', 'Lao Kip'), ('LBP', 'Lebanese Pound'), ('LKR', 'Sri Lankan Rupee'), ('LRD', 'Liberian Dollar'), ('LSL', 'Lesotho Loti'), ('LYD', 'Libyan Dinar'), ('MAD', 'Moroccan Dirham'), ('MDL', 'Moldovan Leu'), ('MGA', 'Malagasy Ariary'), ('MKD', 'Macedonian Denar'), ('MMK', 'Burmese Kyat'), ('MNT', 'Mongolian Tögrög'), ('MOP', 'Macanese Pataca'), ('MRU', 'Mauritanian Ouguiya'), ('MUR', 'Mauritian Rupee'), ('MVR', 'Maldivian Rufiyaa'), ('MWK', 'Malawian Kwacha'), ('MXN', 'Mexican Peso'), ('MYR', 'Malaysian Ringgit'), ('MZN', 'Mozambican Metical'), ('NAD', 'Namibian Dollar'), ('NGN', 'Nigerian Naira'), ('NIO', 'Nicaraguan Córdoba'), ('NOK', 'Norwegian Krone'), ('NPR', 'Nepalese Rupee'), ('OMR', 'Omani Rial'), ('PAB', 'Panamanian Balboa'), ('PEN', 'Peruvian Sol'), ('PGK', 'Papua New Guinean Kina'), ('PHP', 'Philippine Peso'), ('PKR', 'Pakistani Rupee'), ('PLN', 'Polish Złoty'), ('PYG', 'Paraguayan Guaraní'), ('QAR', 'Qatari Riyal'), ('RON', 'Romanian Leu'), ('RSD', 'Serbian Dinar'), ('RWF', 'Rwandan Franc'), ('SAR', 'Saudi Riyal'), ('SBD', 'Solomon Islands Dollar'), ('SCR', 'Seychellois Rupee'), ('SDG', 'Sudanese Pound'), ('SGD', 'Singapore Dollar'), ('SHP', 'Saint Helena Pound'), ('SLL', 'Sierra Leonean Leone'), ('SOS', 'Somali Shilling'), ('SRD', 'Surinamese Dollar'), ('SSP', 'South Sudanese Pound'), ('STN', 'São Tomé and Príncipe Dobra'), ('SYP', 'Syrian Pound'), ('SZL', 'Eswatini Lilangeni'), ('THB', 'Thai Baht'), ('TJS', 'Tajikistani Somoni'), ('TMT', 'Turkmenistani Manat'), ('TND', 'Tunisian Dinar'), ('TOP', 'Tongan Paʻanga'), ('TRY', 'Turkish Lira'), ('TTD', 'Trinidad and Tobago Dollar'), ('TVD', 'Tuvaluan Dollar'), ('TWD', 'New Taiwan Dollar'), ('TZS', 'Tanzanian Shilling'), ('UAH', 'Ukrainian Hryvnia'), ('UGX', 'Ugandan Shilling'), ('UYU', 'Uruguayan Peso'), ('UZS', 'Uzbekistani Som'), ('VES', 'Venezuelan Bolívar Soberano'), ('VND', 'Vietnamese Đồng'), ('VUV', 'Vanuatu Vatu'), ('WST', 'Samoan Tālā'), ('XAF', 'Central African CFA Franc'), ('XCD', 'East Caribbean Dollar'), ('XOF', 'West African CFA Franc'), ('XPF', 'CFP Franc'), ('YER', 'Yemeni Rial'), ('ZMW', 'Zambian Kwacha'), ('ZWL', 'Zimbabwean Dollar')], default='USD', help_text="ISO currency code for the order. This is the base currency in which the total amount will be stored after converting from the customer's currency to the base currency. For example, 'USD' for US Dollars. The base currency is defined in the settings.", max_length=3)),
                ('total_price', models.BigIntegerField(blank=True, help_text="Total amount of the order in cents, converted from the original currency (customer's currency) to the base currency. For example, if the base currency is USD and the customer_currency is different (e.g., AUD), the total amount will be converted to USD. This converted amount is stored in cents.", null=True, validators=[django.core.validators.MinValueValidator(1)])),
                ('customer_currency', models.CharField(choices=[('USD', 'United States Dollar'), ('EUR', 'Euro'), ('GBP', 'British Pound Sterling'), ('JPY', 'Japanese Yen'), ('AUD', 'Australian Dollar'), ('CAD', 'Canadian Dollar'), ('CHF', 'Swiss Franc'), ('CNY', 'Chinese Yuan'), ('SEK', 'Swedish Krona'), ('NZD', 'New Zealand Dollar'), ('INR', 'Indian Rupee'), ('BRL', 'Brazilian Real'), ('RUB', 'Russian Ruble'), ('ZAR', 'South African Rand'), ('AED', 'United Arab Emirates Dirham'), ('AFN', 'Afghan Afghani'), ('ALL', 'Albanian Lek'), ('AMD', 'Armenian Dram'), ('ANG', 'Netherlands Antillean Guilder'), ('AOA', 'Angolan Kwanza'), ('ARS', 'Argentine Peso'), ('AWG', 'Aruban Florin'), ('AZN', 'Azerbaijani Manat'), ('BAM', 'Bosnia and Herzegovina Convertible Mark'), ('BBD', 'Barbadian Dollar'), ('BDT', 'Bangladeshi Taka'), ('BGN', 'Bulgarian Lev'), ('BHD', 'Bahraini Dinar'), ('BIF', 'Burundian Franc'), ('BMD', 'Bermudian Dollar'), ('BND', 'Brunei Dollar'), ('BOB', 'Bolivian Boliviano'), ('BSD', 'Bahamian Dollar'), ('BTN', 'Bhutanese Ngultrum'), ('BWP', 'Botswana Pula'), ('BYN', 'Belarusian Ruble'), ('BZD', 'Belize Dollar'), ('CDF', 'Congolese Franc'), ('CLP', 'Chilean Peso'), ('COP', 'Colombian Peso'), ('CRC', 'Costa Rican Colón'), ('CUP', 'Cuban Peso'), ('CVE', 'Cape Verdean Escudo'), ('CZK', 'Czech Koruna'), ('DJF', 'Djiboutian Franc'), ('DKK', 'Danish Krone'), ('DOP', 'Dominican Peso'), ('DZD', 'Algerian Dinar'), ('EGP', 'Egyptian Pound'), ('ERN', 'Eritrean Nakfa'), ('ETB', 'Ethiopian Birr'), ('FJD', 'Fijian Dollar'), ('FKP', 'Falkland Islands Pound'), ('FOK', 'Faroese Króna'), ('GEL', 'Georgian Lari'), ('GGP', 'Guernsey Pound'), ('GHS', 'Ghanaian Cedi'), ('GIP', 'Gibraltar Pound'), ('GMD', 'Gambian Dalasi'), ('GNF', 'Guinean Franc'), ('GTQ', 'Guatemalan Quetzal'), ('GYD', 'Guyanese Dollar'), ('HKD', 'Hong Kong Dollar'), ('HNL', 'Honduran Lempira'), ('HRK', 'Croatian Kuna'), ('HTG', 'Haitian Gourde'), ('HUF', 'Hungarian Forint'), ('IDR', 'Indonesian Rupiah'), ('ILS', 'Israeli New Shekel'), ('IMP', 'Isle of Man Pound'), ('IQD', 'Iraqi Dinar'), ('IRR', 'Iranian Rial'), ('ISK', 'Icelandic Króna'), ('JMD', 'Jamaican Dollar'), ('JOD', 'Jordanian Dinar'), ('KES', 'Kenyan Shilling'), ('KGS', 'Kyrgyzstani Som'), ('KHR', 'Cambodian Riel'), ('KID', 'Kiribati Dollar'), ('KMF', 'Comorian Franc'), ('KRW', 'South Korean Won'), ('KWD', 'Kuwaiti Dinar'), ('KYD', 'Cayman Islands Dollar'), ('KZT', 'Kazakhstani Tenge'), ('LAK', 'Lao Kip'), ('LBP', 'Lebanese Pound'), ('LKR', 'Sri Lankan Rupee'), ('LRD', 'Liberian Dollar'), ('LSL', 'Lesotho Loti'), ('LYD', 'Libyan Dinar'), ('MAD', 'Moroccan Dirham'), ('MDL', 'Moldovan Leu'), ('MGA', 'Malagasy Ariary'), ('MKD', 'Macedonian Denar'), ('MMK', 'Burmese Kyat'), ('MNT', 'Mongolian Tögrög'), ('MOP', 'Macanese Pataca'), ('MRU', 'Mauritanian Ouguiya'), ('MUR', 'Mauritian Rupee'), ('MVR', 'Maldivian Rufiyaa'), ('MWK', 'Malawian Kwacha'), ('MXN', 'Mexican Peso'), ('MYR', 'Malaysian Ringgit'), ('MZN', 'Mozambican Metical'), ('NAD', 'Namibian Dollar'), ('NGN', 'Nigerian Naira'), ('NIO', 'Nicaraguan Córdoba'), ('NOK', 'Norwegian Krone'), ('NPR', 'Nepalese Rupee'), ('OMR', 'Omani Rial'), ('PAB', 'Panamanian Balboa'), ('PEN', 'Peruvian Sol'), ('PGK', 'Papua New Guinean Kina'), ('PHP', 'Philippine Peso'), ('PKR', 'Pakistani Rupee'), ('PLN', 'Polish Złoty'), ('PYG', 'Paraguayan Guaraní'), ('QAR', 'Qatari Riyal'), ('RON', 'Romanian Leu'), ('RSD', 'Serbian Dinar'), ('RWF', 'Rwandan Franc'), ('SAR', 'Saudi Riyal'), ('SBD', 'Solomon Islands Dollar'), ('SCR', 'Seychellois Rupee'), ('SDG', 'Sudanese Pound'), ('SGD', 'Singapore Dollar'), ('SHP', 'Saint Helena Pound'), ('SLL', 'Sierra Leonean Leone'), ('SOS', 'Somali Shilling'), ('SRD', 'Surinamese Dollar'), ('SSP', 'South Sudanese Pound'), ('STN', 'São Tomé and Príncipe Dobra'), ('SYP', 'Syrian Pound'), ('SZL', 'Eswatini Lilangeni'), ('THB', 'Thai Baht'), ('TJS', 'Tajikistani Somoni'), ('TMT', 'Turkmenistani Manat'), ('TND', 'Tunisian Dinar'), ('TOP', 'Tongan Paʻanga'), ('TRY', 'Turkish Lira'), ('TTD', 'Trinidad and Tobago Dollar'), ('TVD', 'Tuvaluan Dollar'), ('TWD', 'New Taiwan Dollar'), ('TZS', 'Tanzanian Shilling'), ('UAH', 'Ukrainian Hryvnia'), ('UGX', 'Ugandan Shilling'), ('UYU', 'Uruguayan Peso'), ('UZS', 'Uzbekistani Som'), ('VES', 'Venezuelan Bolívar Soberano'), ('VND', 'Vietnamese Đồng'), ('VUV', 'Vanuatu Vatu'), ('WST', 'Samoan Tālā'), ('XAF', 'Central African CFA Franc'), ('XCD', 'East Caribbean Dollar'), ('XOF', 'West African CFA Franc'), ('XPF', 'CFP Franc'), ('YER', 'Yemeni Rial'), ('ZMW', 'Zambian Kwacha'), ('ZWL', 'Zimbabwean Dollar')], help_text="ISO currency code of the original amount paid by the customer. For example, 'AUD' for Australian Dollars.", max_length=3)),
                ('total_price_in_customer_currency', models.DecimalField(blank=True, decimal_places=4, help_text="Original amount paid by the customer in the customer's currency, stored in cents. ", max_digits=12, null=True)),
                ('status', models.CharField(choices=[('PENDING', 'Pending'), ('PROCESSING', 'Processing'), ('SHIPPED', 'Shipped'), ('DELIVERED', 'Delivered'), ('CANCELLED', 'Cancelled'), ('RETURNED', 'Returned')], default='PENDING', help_text='Represents the current stage of the order within its lifecycle.', max_length=20, verbose_name='Order Status')),
                ('authorize_status', models.CharField(choices=[('NONE', 'No funds are authorized'), ('PARTIAL', "Partially authorized; funds don't fully cover the order's total"), ('FULL', "Fully authorized; funds cover the order's total")], default='NONE', help_text='Represents the authorization status of the order based on fund coverage.', max_length=32, verbose_name='Authorization Status')),
                ('charge_status', models.CharField(choices=[('DUE', 'Due'), ('PARTIAL', 'Partially charged'), ('FULL', 'Fully charged'), ('OVERCHARGED', 'Overcharged')], default='DUE', help_text='Represents the charge status of the order based on transaction charges.', max_length=32, verbose_name='Charge Status')),
                ('payment_terms', models.CharField(choices=[('DUE_ON_RECEIPT', 'Due on receipt'), ('DUE_ON_FULFILLMENT', 'Due on fulfillment'), ('DUE_ON_INSTALLMENT', 'Due on installment'), ('FIXED_DATE', 'Fixed date')], default='DUE_ON_RECEIPT', help_text='Represents the payment terms for the order.', max_length=32)),
                ('due_date', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'ordering': ('-created_at',),
            },
            bases=(nxtbn.core.mixin.MonetaryMixin, models.Model),
        ),
        migrations.CreateModel(
            name='OrderLineItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(1)])),
                ('price_per_unit', models.DecimalField(decimal_places=3, max_digits=12, validators=[django.core.validators.MinValueValidator(Decimal('0.01'))])),
                ('currency', models.CharField(choices=[('USD', 'United States Dollar'), ('EUR', 'Euro'), ('GBP', 'British Pound Sterling'), ('JPY', 'Japanese Yen'), ('AUD', 'Australian Dollar'), ('CAD', 'Canadian Dollar'), ('CHF', 'Swiss Franc'), ('CNY', 'Chinese Yuan'), ('SEK', 'Swedish Krona'), ('NZD', 'New Zealand Dollar'), ('INR', 'Indian Rupee'), ('BRL', 'Brazilian Real'), ('RUB', 'Russian Ruble'), ('ZAR', 'South African Rand'), ('AED', 'United Arab Emirates Dirham'), ('AFN', 'Afghan Afghani'), ('ALL', 'Albanian Lek'), ('AMD', 'Armenian Dram'), ('ANG', 'Netherlands Antillean Guilder'), ('AOA', 'Angolan Kwanza'), ('ARS', 'Argentine Peso'), ('AWG', 'Aruban Florin'), ('AZN', 'Azerbaijani Manat'), ('BAM', 'Bosnia and Herzegovina Convertible Mark'), ('BBD', 'Barbadian Dollar'), ('BDT', 'Bangladeshi Taka'), ('BGN', 'Bulgarian Lev'), ('BHD', 'Bahraini Dinar'), ('BIF', 'Burundian Franc'), ('BMD', 'Bermudian Dollar'), ('BND', 'Brunei Dollar'), ('BOB', 'Bolivian Boliviano'), ('BSD', 'Bahamian Dollar'), ('BTN', 'Bhutanese Ngultrum'), ('BWP', 'Botswana Pula'), ('BYN', 'Belarusian Ruble'), ('BZD', 'Belize Dollar'), ('CDF', 'Congolese Franc'), ('CLP', 'Chilean Peso'), ('COP', 'Colombian Peso'), ('CRC', 'Costa Rican Colón'), ('CUP', 'Cuban Peso'), ('CVE', 'Cape Verdean Escudo'), ('CZK', 'Czech Koruna'), ('DJF', 'Djiboutian Franc'), ('DKK', 'Danish Krone'), ('DOP', 'Dominican Peso'), ('DZD', 'Algerian Dinar'), ('EGP', 'Egyptian Pound'), ('ERN', 'Eritrean Nakfa'), ('ETB', 'Ethiopian Birr'), ('FJD', 'Fijian Dollar'), ('FKP', 'Falkland Islands Pound'), ('FOK', 'Faroese Króna'), ('GEL', 'Georgian Lari'), ('GGP', 'Guernsey Pound'), ('GHS', 'Ghanaian Cedi'), ('GIP', 'Gibraltar Pound'), ('GMD', 'Gambian Dalasi'), ('GNF', 'Guinean Franc'), ('GTQ', 'Guatemalan Quetzal'), ('GYD', 'Guyanese Dollar'), ('HKD', 'Hong Kong Dollar'), ('HNL', 'Honduran Lempira'), ('HRK', 'Croatian Kuna'), ('HTG', 'Haitian Gourde'), ('HUF', 'Hungarian Forint'), ('IDR', 'Indonesian Rupiah'), ('ILS', 'Israeli New Shekel'), ('IMP', 'Isle of Man Pound'), ('IQD', 'Iraqi Dinar'), ('IRR', 'Iranian Rial'), ('ISK', 'Icelandic Króna'), ('JMD', 'Jamaican Dollar'), ('JOD', 'Jordanian Dinar'), ('KES', 'Kenyan Shilling'), ('KGS', 'Kyrgyzstani Som'), ('KHR', 'Cambodian Riel'), ('KID', 'Kiribati Dollar'), ('KMF', 'Comorian Franc'), ('KRW', 'South Korean Won'), ('KWD', 'Kuwaiti Dinar'), ('KYD', 'Cayman Islands Dollar'), ('KZT', 'Kazakhstani Tenge'), ('LAK', 'Lao Kip'), ('LBP', 'Lebanese Pound'), ('LKR', 'Sri Lankan Rupee'), ('LRD', 'Liberian Dollar'), ('LSL', 'Lesotho Loti'), ('LYD', 'Libyan Dinar'), ('MAD', 'Moroccan Dirham'), ('MDL', 'Moldovan Leu'), ('MGA', 'Malagasy Ariary'), ('MKD', 'Macedonian Denar'), ('MMK', 'Burmese Kyat'), ('MNT', 'Mongolian Tögrög'), ('MOP', 'Macanese Pataca'), ('MRU', 'Mauritanian Ouguiya'), ('MUR', 'Mauritian Rupee'), ('MVR', 'Maldivian Rufiyaa'), ('MWK', 'Malawian Kwacha'), ('MXN', 'Mexican Peso'), ('MYR', 'Malaysian Ringgit'), ('MZN', 'Mozambican Metical'), ('NAD', 'Namibian Dollar'), ('NGN', 'Nigerian Naira'), ('NIO', 'Nicaraguan Córdoba'), ('NOK', 'Norwegian Krone'), ('NPR', 'Nepalese Rupee'), ('OMR', 'Omani Rial'), ('PAB', 'Panamanian Balboa'), ('PEN', 'Peruvian Sol'), ('PGK', 'Papua New Guinean Kina'), ('PHP', 'Philippine Peso'), ('PKR', 'Pakistani Rupee'), ('PLN', 'Polish Złoty'), ('PYG', 'Paraguayan Guaraní'), ('QAR', 'Qatari Riyal'), ('RON', 'Romanian Leu'), ('RSD', 'Serbian Dinar'), ('RWF', 'Rwandan Franc'), ('SAR', 'Saudi Riyal'), ('SBD', 'Solomon Islands Dollar'), ('SCR', 'Seychellois Rupee'), ('SDG', 'Sudanese Pound'), ('SGD', 'Singapore Dollar'), ('SHP', 'Saint Helena Pound'), ('SLL', 'Sierra Leonean Leone'), ('SOS', 'Somali Shilling'), ('SRD', 'Surinamese Dollar'), ('SSP', 'South Sudanese Pound'), ('STN', 'São Tomé and Príncipe Dobra'), ('SYP', 'Syrian Pound'), ('SZL', 'Eswatini Lilangeni'), ('THB', 'Thai Baht'), ('TJS', 'Tajikistani Somoni'), ('TMT', 'Turkmenistani Manat'), ('TND', 'Tunisian Dinar'), ('TOP', 'Tongan Paʻanga'), ('TRY', 'Turkish Lira'), ('TTD', 'Trinidad and Tobago Dollar'), ('TVD', 'Tuvaluan Dollar'), ('TWD', 'New Taiwan Dollar'), ('TZS', 'Tanzanian Shilling'), ('UAH', 'Ukrainian Hryvnia'), ('UGX', 'Ugandan Shilling'), ('UYU', 'Uruguayan Peso'), ('UZS', 'Uzbekistani Som'), ('VES', 'Venezuelan Bolívar Soberano'), ('VND', 'Vietnamese Đồng'), ('VUV', 'Vanuatu Vatu'), ('WST', 'Samoan Tālā'), ('XAF', 'Central African CFA Franc'), ('XCD', 'East Caribbean Dollar'), ('XOF', 'West African CFA Franc'), ('XPF', 'CFP Franc'), ('YER', 'Yemeni Rial'), ('ZMW', 'Zambian Kwacha'), ('ZWL', 'Zimbabwean Dollar')], default='USD', max_length=3)),
                ('total_price', models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(1)])),
                ('customer_currency', models.CharField(choices=[('USD', 'United States Dollar'), ('EUR', 'Euro'), ('GBP', 'British Pound Sterling'), ('JPY', 'Japanese Yen'), ('AUD', 'Australian Dollar'), ('CAD', 'Canadian Dollar'), ('CHF', 'Swiss Franc'), ('CNY', 'Chinese Yuan'), ('SEK', 'Swedish Krona'), ('NZD', 'New Zealand Dollar'), ('INR', 'Indian Rupee'), ('BRL', 'Brazilian Real'), ('RUB', 'Russian Ruble'), ('ZAR', 'South African Rand'), ('AED', 'United Arab Emirates Dirham'), ('AFN', 'Afghan Afghani'), ('ALL', 'Albanian Lek'), ('AMD', 'Armenian Dram'), ('ANG', 'Netherlands Antillean Guilder'), ('AOA', 'Angolan Kwanza'), ('ARS', 'Argentine Peso'), ('AWG', 'Aruban Florin'), ('AZN', 'Azerbaijani Manat'), ('BAM', 'Bosnia and Herzegovina Convertible Mark'), ('BBD', 'Barbadian Dollar'), ('BDT', 'Bangladeshi Taka'), ('BGN', 'Bulgarian Lev'), ('BHD', 'Bahraini Dinar'), ('BIF', 'Burundian Franc'), ('BMD', 'Bermudian Dollar'), ('BND', 'Brunei Dollar'), ('BOB', 'Bolivian Boliviano'), ('BSD', 'Bahamian Dollar'), ('BTN', 'Bhutanese Ngultrum'), ('BWP', 'Botswana Pula'), ('BYN', 'Belarusian Ruble'), ('BZD', 'Belize Dollar'), ('CDF', 'Congolese Franc'), ('CLP', 'Chilean Peso'), ('COP', 'Colombian Peso'), ('CRC', 'Costa Rican Colón'), ('CUP', 'Cuban Peso'), ('CVE', 'Cape Verdean Escudo'), ('CZK', 'Czech Koruna'), ('DJF', 'Djiboutian Franc'), ('DKK', 'Danish Krone'), ('DOP', 'Dominican Peso'), ('DZD', 'Algerian Dinar'), ('EGP', 'Egyptian Pound'), ('ERN', 'Eritrean Nakfa'), ('ETB', 'Ethiopian Birr'), ('FJD', 'Fijian Dollar'), ('FKP', 'Falkland Islands Pound'), ('FOK', 'Faroese Króna'), ('GEL', 'Georgian Lari'), ('GGP', 'Guernsey Pound'), ('GHS', 'Ghanaian Cedi'), ('GIP', 'Gibraltar Pound'), ('GMD', 'Gambian Dalasi'), ('GNF', 'Guinean Franc'), ('GTQ', 'Guatemalan Quetzal'), ('GYD', 'Guyanese Dollar'), ('HKD', 'Hong Kong Dollar'), ('HNL', 'Honduran Lempira'), ('HRK', 'Croatian Kuna'), ('HTG', 'Haitian Gourde'), ('HUF', 'Hungarian Forint'), ('IDR', 'Indonesian Rupiah'), ('ILS', 'Israeli New Shekel'), ('IMP', 'Isle of Man Pound'), ('IQD', 'Iraqi Dinar'), ('IRR', 'Iranian Rial'), ('ISK', 'Icelandic Króna'), ('JMD', 'Jamaican Dollar'), ('JOD', 'Jordanian Dinar'), ('KES', 'Kenyan Shilling'), ('KGS', 'Kyrgyzstani Som'), ('KHR', 'Cambodian Riel'), ('KID', 'Kiribati Dollar'), ('KMF', 'Comorian Franc'), ('KRW', 'South Korean Won'), ('KWD', 'Kuwaiti Dinar'), ('KYD', 'Cayman Islands Dollar'), ('KZT', 'Kazakhstani Tenge'), ('LAK', 'Lao Kip'), ('LBP', 'Lebanese Pound'), ('LKR', 'Sri Lankan Rupee'), ('LRD', 'Liberian Dollar'), ('LSL', 'Lesotho Loti'), ('LYD', 'Libyan Dinar'), ('MAD', 'Moroccan Dirham'), ('MDL', 'Moldovan Leu'), ('MGA', 'Malagasy Ariary'), ('MKD', 'Macedonian Denar'), ('MMK', 'Burmese Kyat'), ('MNT', 'Mongolian Tögrög'), ('MOP', 'Macanese Pataca'), ('MRU', 'Mauritanian Ouguiya'), ('MUR', 'Mauritian Rupee'), ('MVR', 'Maldivian Rufiyaa'), ('MWK', 'Malawian Kwacha'), ('MXN', 'Mexican Peso'), ('MYR', 'Malaysian Ringgit'), ('MZN', 'Mozambican Metical'), ('NAD', 'Namibian Dollar'), ('NGN', 'Nigerian Naira'), ('NIO', 'Nicaraguan Córdoba'), ('NOK', 'Norwegian Krone'), ('NPR', 'Nepalese Rupee'), ('OMR', 'Omani Rial'), ('PAB', 'Panamanian Balboa'), ('PEN', 'Peruvian Sol'), ('PGK', 'Papua New Guinean Kina'), ('PHP', 'Philippine Peso'), ('PKR', 'Pakistani Rupee'), ('PLN', 'Polish Złoty'), ('PYG', 'Paraguayan Guaraní'), ('QAR', 'Qatari Riyal'), ('RON', 'Romanian Leu'), ('RSD', 'Serbian Dinar'), ('RWF', 'Rwandan Franc'), ('SAR', 'Saudi Riyal'), ('SBD', 'Solomon Islands Dollar'), ('SCR', 'Seychellois Rupee'), ('SDG', 'Sudanese Pound'), ('SGD', 'Singapore Dollar'), ('SHP', 'Saint Helena Pound'), ('SLL', 'Sierra Leonean Leone'), ('SOS', 'Somali Shilling'), ('SRD', 'Surinamese Dollar'), ('SSP', 'South Sudanese Pound'), ('STN', 'São Tomé and Príncipe Dobra'), ('SYP', 'Syrian Pound'), ('SZL', 'Eswatini Lilangeni'), ('THB', 'Thai Baht'), ('TJS', 'Tajikistani Somoni'), ('TMT', 'Turkmenistani Manat'), ('TND', 'Tunisian Dinar'), ('TOP', 'Tongan Paʻanga'), ('TRY', 'Turkish Lira'), ('TTD', 'Trinidad and Tobago Dollar'), ('TVD', 'Tuvaluan Dollar'), ('TWD', 'New Taiwan Dollar'), ('TZS', 'Tanzanian Shilling'), ('UAH', 'Ukrainian Hryvnia'), ('UGX', 'Ugandan Shilling'), ('UYU', 'Uruguayan Peso'), ('UZS', 'Uzbekistani Som'), ('VES', 'Venezuelan Bolívar Soberano'), ('VND', 'Vietnamese Đồng'), ('VUV', 'Vanuatu Vatu'), ('WST', 'Samoan Tālā'), ('XAF', 'Central African CFA Franc'), ('XCD', 'East Caribbean Dollar'), ('XOF', 'West African CFA Franc'), ('XPF', 'CFP Franc'), ('YER', 'Yemeni Rial'), ('ZMW', 'Zambian Kwacha'), ('ZWL', 'Zimbabwean Dollar')], default='USD', max_length=3)),
                ('total_price_in_customer_currency', models.DecimalField(blank=True, decimal_places=4, max_digits=12, null=True)),
                ('tax_rate', models.DecimalField(blank=True, decimal_places=2, help_text='Tax rate at the time of the order', max_digits=5, null=True)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='line_items', to='order.order')),
            ],
            bases=(nxtbn.core.mixin.MonetaryMixin, models.Model),
        ),
    ]
