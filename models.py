from django.db import models
from datetime import date
from django.utils import timezone
from datetime import datetime
import inspect
from django.conf import settings
from django.urls import reverse, reverse_lazy

YESNO=(
    ('Y','yes'),
    ('N','no'),
)

class Estimator(models.Model):
    name = models.CharField('name', blank=True, help_text='What is the name of the estimator', max_length=200 )
    user = models.ForeignKey(settings.AUTH_USER_MODEL, blank=True, help_text='Who is the user associated with this estimator?', null=True, on_delete=models.PROTECT)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('estimator_detail', args=[str(self.id)])

    class Meta:
        ordering = ('name',)
        verbose_name = 'estimator'

class Customer(models.Model):
    name = models.CharField('name', blank=True, help_text='What is the customer\'s name?', max_length=200)
    email = models.EmailField('email', blank=True, help_text='What is the customer\'s primary email address?', max_length=300)
    phone = models.CharField('phone', blank=True, help_text='What is the customer\'s primary phone number?', max_length=200)
    additional_contact = models.TextField('additional contact information', blank=True, help_text='What is the contact information other than primary email and primary phone?')
    is_type_commercialgc = models.BooleanField('Commercial GC', blank=True, default=False, help_text='Is this customer a general contractor?')
    is_type_builder = models.BooleanField('builder', blank=True, default=False, help_text='Is this customer a builder?')
    is_type_remodeler = models.BooleanField('remodeler', blank=True, default=False, help_text='Is this customer a remodeler?')
    is_type_homeowner = models.BooleanField('homeowner', blank=True, default=False, help_text='Is this customer a homeowner?')
    billing_address = models.TextField('billing address', blank=True, help_text='What is the customer\'s billing address?')
    archived=models.CharField('archived', choices=YESNO, default='N', help_text='Should this customer be removed from the list of active customers?', max_length=1)
    business_card=models.FileField('business card', blank=True, help_text='What is this customer\'s business card?', null=True)
    custom_logo = models.FileField('logo', blank=True, help_text='For salespeople who work for this customer, what logo will be displayed?', null=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)
        verbose_name = 'customer'

    def can_change(self, user):
        can = False
        if user is not None:
            if user.is_superuser:
                return True
            if user.groups.filter(name="Esteem_Managers").exists():
                return True
            if user.groups.filter(name="Esteem_Salespeople").exists():
                return True
            if user.groups.filter(name="Esteem_SalespersonAssociates").exists():
                for salesperson in user.salesperson_set.all():
                    if salesperson.associated_customer.pk == self.pk:
                        return True

    def can_view_in_list(self, user):
        can = False
        if user is not None:
            if user.is_superuser:
                return True
            if user.groups.filter(name="Esteem_Managers").exists():
                return True
            if user.groups.filter(name="Esteem_Estimators").exists():
                return True
            if user.groups.filter(name="Esteem_Salespeople").exists():
                return True
            if user.groups.filter(name="Esteem_SalespersonAssociates").exists():
                for salesperson in user.salesperson_set.all():
                    if salesperson.associated_customer.pk == self.pk:
                        return True

    def can_view(self, user):
        can = False
        if user is not None:
            if user.is_superuser:
                return True
            if user.groups.filter(name="Esteem_Managers").exists():
                return True
            if user.groups.filter(name="Esteem_Estimators").exists():
                return True
            if user.groups.filter(name="Esteem_Salespeople").exists():
                return True
            if user.groups.filter(name="Esteem_SalespersonAssociates").exists():
                for salesperson in user.salesperson_set.all():
                    if salesperson.associated_customer.pk == self.pk:
                        return True


class Salesperson(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, blank=True, help_text='Who is the user associated with this sales person?', null=True, on_delete=models.PROTECT)
    name = models.CharField('name', max_length=200, blank=True, help_text='What is he name of the salesperson')
    associated_customer = models.ForeignKey(Customer, blank=True, help_text='If this salesperson works for a customer, who is this sales person\'s associated customer?', null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('salesperson_detail', args=[str(self.id)])

    class Meta:
        ordering = ('name',)
        verbose_name = 'sales person'
        verbose_name_plural = 'sales people'

class Estirequest(models.Model):
    STATUS_DRAFT='DR'
    STATUS_SUBMITTED='SU'
    STATUS_ESTIMATED='ES'
    STATUS_WON='WN'
    STATUS_LOST='LS'
    STATUS_CHOICES=(
        (STATUS_DRAFT, 'Draft'),
        (STATUS_SUBMITTED, 'Submitted for Estimate'),
        (STATUS_ESTIMATED, 'Estimate Submitted'),
        (STATUS_WON, 'Won'),
        (STATUS_LOST, 'Lost'),
    )
    NR_NEW='N'
    NR_RE='R'
    NR_CHOICES=(
        (NR_NEW, 'New Construction'),
        (NR_RE, 'Remodel'),
    )

    name = models.CharField('project name', max_length=200, blank=True, help_text='What is the project\'s name?')
    requestnum = models.CharField('est.req#', blank=True, help_text='What is the estimate request number?', max_length=20, unique=True)
    new_or_remodel = models.CharField('new/remodel', max_length=2, choices=NR_CHOICES, default=NR_NEW, help_text='Is this a new construction or a remodel?')
    customer = models.ForeignKey(Customer, blank=True, help_text='Who is the customer for this project?', null=True, on_delete=models.PROTECT)
    address = models.CharField('address/lot', max_length=200, blank=True, help_text='What is the project\'s street address or lot number?')
    citystzip = models.CharField('city, state, zip', max_length=200, blank=True, help_text='What is the project\'s city, state and zip?')
    create_date = models.DateField('date', blank=True, default=date.today, help_text='What is the date that this request was created?')
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='created by', null=True, on_delete=models.PROTECT, help_text="The user who submitted the request")
    submit_date = models.DateField('date', blank=True, help_text='What is the date that this request was submitted for estimate?', null=True)
    status = models.CharField('status', max_length=2, choices=STATUS_CHOICES, default=STATUS_DRAFT, help_text='What is the status of this request')
    comments = models.TextField('comments for estimator', blank=True, help_text='What are comments for this request?')
    has_windows = models.BooleanField('windows', default=False, help_text='Does this project have windows?')
    has_doors = models.BooleanField('non-Marvin doors', default=False, help_text='Does this project have doors?')
    has_marvindoors = models.BooleanField('marvin doors', default=False, help_text='Does this project have Marvin doors?')
    has_icfs = models.BooleanField('icf', default=False, help_text='Does this project have ICF?')
    has_interiormillworks = models.BooleanField('interior millwork', default=False, help_text='Does this project have Interior Millwork?')
    has_exteriormillworks = models.BooleanField('exterior millwork', default=False, help_text='Does this project have Exterior Millwork?')

    class Meta:
        ordering = ('-create_date', '-submit_date', 'name',)
        verbose_name = 'estimate requested'
        verbose_name_plural = 'estimates requested'
        permissions = [
            ('list_estirequests', 'Can list estirequests')
        ]

    def __str__(self):
        str = self.name
        if not str > '':
            str = self.requestnum
        return str

    def get_absolute_url(self):
        return reverse('estirequest_detail', args=[str(self.id)])

    def get_latest_proposal(self):
        return self.proposal_set.all().first()

    def can_change(self, user):
        can = False
        if user is not None:
            if user.is_superuser:
                return True
            if user.groups.filter(name="Esteem_Managers").exists():
                return True
            if user.groups.filter(name="Esteem_Salespeople").exists():
                for assignment in self.assignment_set.all():
                    if user == assignment.salesperson.user:
                        return True
            if user.groups.filter(name="Esteem_SalespersonAssociates").exists():
                for assignment in self.assignment_set.all():
                    if user == assignment.salesperson.user:
                        return True

    def can_view_in_list(self, user):
        can = False
        if user is not None:
            if user.is_superuser:
                return True
            if user.groups.filter(name="Esteem_Managers").exists():
                return True
            if user.groups.filter(name="Esteem_Estimators").exists():
                if self.status == self.STATUS_SUBMITTED:
                    return True
                if self.status == self.STATUS_ESTIMATED:
                    for proposal in self.proposal_set.all():
                        if proposal.estimator:
                            if user==proposal.estimator.user:
                                return True
            if user.groups.filter(name="Esteem_Salespeople").exists():
                for assignment in self.assignment_set.all():
                    if user == assignment.salesperson.user:
                        return True
            if user.groups.filter(name="Esteem_SalespersonAssociates").exists():
                for assignment in self.assignment_set.all():
                    if user == assignment.salesperson.user:
                        return True

    def can_view(self, user):
        can = False
        if user is not None:
            if user.is_superuser:
                return True
            if user.groups.filter(name="Esteem_Managers").exists():
                return True
            if user.groups.filter(name="Esteem_Estimators").exists():
                if self.status == self.STATUS_SUBMITTED:
                    return True
                if self.status == self.STATUS_ESTIMATED:
                    return True
            if user.groups.filter(name="Esteem_Salespeople").exists():
                for assignment in self.assignment_set.all():
                    if user == assignment.salesperson.user:
                        return True
            if user.groups.filter(name="Esteem_SalespersonAssociates").exists():
                for assignment in self.assignment_set.all():
                    if user == assignment.salesperson.user:
                        return True







class EstirequestDocument(models.Model):
    estirequest = models.ForeignKey(Estirequest, on_delete=models.CASCADE, help_text='What is the request to which this document is attached?')
    title = models.CharField('title', max_length = 200, blank=True, help_text='What is this documents title?')
    uploadedfile = models.FileField(upload_to='documents/', blank=True, null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('estirequestdocument_detail', args=[str(self.id)])

    class Meta:
        ordering = ('title',)
        verbose_name = 'estimate request document'

class OptionDoorBrand(models.Model):
    name = models.CharField('name', max_length=200, blank=True, help_text='What is the name of this brand?')

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)
        verbose_name = 'option door brand'


class OptionDoorExteriorColor(models.Model):
    optiondoorbrand = models.ForeignKey(OptionDoorBrand, blank=True, help_text='What is the brand to which this options applies?', null=True, on_delete=models.PROTECT)
    name = models.CharField('name', max_length=200, blank=True, help_text='What is the name of this color?')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'option door exterior color'
        ordering = ('optiondoorbrand', 'name',)

class OptionDoorInteriorFinish(models.Model):
    optiondoorbrand = models.ForeignKey(OptionDoorBrand, blank=True, help_text='What is the brand to which this options applies?', null=True, on_delete=models.PROTECT)
    name = models.CharField('name', max_length=200, blank=True, help_text='What is the name of this finish?')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'option door interior finish'
        ordering = ('optiondoorbrand','name',)

class OptionDoorHardwareFinish(models.Model):
    optiondoorbrand = models.ForeignKey(OptionDoorBrand, blank=True, help_text='What is the brand to which this options applies?', null=True, on_delete=models.PROTECT)
    name = models.CharField('name', max_length=200, blank=True, help_text='What is the name of this finish?')

    def __str__(self):
        return self.name


    class Meta:
        ordering = ('optiondoorbrand','name',)
        verbose_name = 'option door hardware finish'

class OptionDoorScreen(models.Model):
    optiondoorbrand = models.ForeignKey(OptionDoorBrand, blank=True, help_text='What is the brand to which this options applies?', null=True, on_delete=models.PROTECT)
    name = models.CharField('name', max_length=200, blank=True, help_text='What is the name of this type of screen?')

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('optiondoorbrand','name',)
        verbose_name = 'option door screen'

class OptionDoorShade(models.Model):
    optiondoorbrand = models.ForeignKey(OptionDoorBrand, blank=True, help_text='What is the brand to which this options applies?', null=True, on_delete=models.PROTECT)
    name = models.CharField('name', max_length=200, blank=True, help_text='What is the name of this type of shade?')

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('optiondoorbrand','name',)
        verbose_name = 'option door shade'

class OptionDoorLockSensor(models.Model):
    optiondoorbrand = models.ForeignKey(OptionDoorBrand, blank=True, help_text='What is the brand to which this options applies?', null=True, on_delete=models.PROTECT)
    name = models.CharField('name', max_length=200, blank=True, help_text='What is the name of this type of sensor?')

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('optiondoorbrand','name',)
        verbose_name = 'option door lock sensor'

class OptionMarvinDoorBrand(models.Model):
    name = models.CharField('name', max_length=200, blank=True, help_text='What is the name of this brand?')

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)
        verbose_name = 'option marvin door brand'

class OptionMarvinDoorExteriorColor(models.Model):
    optionmarvindoorbrand = models.ForeignKey(OptionMarvinDoorBrand, blank=True, help_text='What is the brand to which this options applies?', null=True, on_delete=models.PROTECT)
    name = models.CharField('name', max_length=200, blank=True, help_text='What is the name of this color?')

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('optionmarvindoorbrand','name',)
        verbose_name = 'option marvin door exterior color'

class OptionMarvinDoorInteriorSpecies(models.Model):
    optionmarvindoorbrand = models.ForeignKey(OptionMarvinDoorBrand, blank=True, help_text='What is the brand to which this options applies?', null=True, on_delete=models.PROTECT)
    name = models.CharField('name', max_length=200, blank=True, help_text='What is the name of this species?')

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('optionmarvindoorbrand','name',)
        verbose_name = 'option marvin door interior species'

class OptionMarvinDoorInteriorFinish(models.Model):
    optionmarvindoorbrand = models.ForeignKey(OptionMarvinDoorBrand, blank=True, help_text='What is the brand to which this options applies?', null=True, on_delete=models.PROTECT)
    name = models.CharField('name', max_length=200, blank=True, help_text='What is the name of this finish?')

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('optionmarvindoorbrand','name',)
        verbose_name = 'option marvin door interior finish'

class OptionMarvinDoorHardwareFinish(models.Model):
    optionmarvindoorbrand = models.ForeignKey(OptionMarvinDoorBrand, blank=True, help_text='What is the brand to which this options applies?', null=True, on_delete=models.PROTECT)
    name = models.CharField('name', max_length=200, blank=True, help_text='What is the name of this finish?')

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('optionmarvindoorbrand','name',)
        verbose_name = 'option marvin door hardware finish'

class OptionMarvinDoorHardwareStyle(models.Model):
    optionmarvindoorbrand = models.ForeignKey(OptionMarvinDoorBrand, blank=True, help_text='What is the brand to which this options applies?', null=True, on_delete=models.PROTECT)
    name = models.CharField('name', max_length=200, blank=True, help_text='What is the name of this style?')

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('optionmarvindoorbrand','name',)
        verbose_name = 'option marvin door hardware style'

class OptionMarvinDoorScreen(models.Model):
    optionmarvindoorbrand = models.ForeignKey(OptionMarvinDoorBrand, blank=True, help_text='What is the brand to which this options applies?', null=True, on_delete=models.PROTECT)
    name = models.CharField('name', max_length=200, blank=True, help_text='What is the name of this type of screen?')

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('optionmarvindoorbrand','name',)
        verbose_name = 'option marvin door screen'

class OptionMarvinDoorShade(models.Model):
    optionmarvindoorbrand = models.ForeignKey(OptionMarvinDoorBrand, blank=True, help_text='What is the brand to which this options applies?', null=True, on_delete=models.PROTECT)
    name = models.CharField('name', max_length=200, blank=True, help_text='What is the name of this type of shade?')

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('optionmarvindoorbrand','name',)
        verbose_name = 'option marvin door shade'

class OptionMarvinDoorLockSensor(models.Model):
    optionmarvindoorbrand = models.ForeignKey(OptionMarvinDoorBrand, blank=True, help_text='What is the brand to which this options applies?', null=True, on_delete=models.PROTECT)
    name = models.CharField('name', max_length=200, blank=True, help_text='What is the name of this type of sensor?')

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('optionmarvindoorbrand','name',)
        verbose_name = 'option marvin door lock sensor'

class OptionWindowBrand(models.Model):
    name = models.CharField('name', max_length=200, blank=True, help_text='What is the name of this brand?')

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)
        verbose_name = 'option window brand'

class OptionWindowExteriorColor(models.Model):
    optionwindowbrand = models.ForeignKey(OptionWindowBrand, blank=True, help_text='What is the brand to which this options applies?', null=True, on_delete=models.PROTECT)
    name = models.CharField('name', max_length=200, blank=True, help_text='What is the name of this color?')

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('optionwindowbrand','name',)
        verbose_name = 'option window exterior color'

class OptionWindowInteriorFinish(models.Model):
    optionwindowbrand = models.ForeignKey(OptionWindowBrand, blank=True, help_text='What is the brand to which this options applies?', null=True, on_delete=models.PROTECT)
    name = models.CharField('name', max_length=200, blank=True, help_text='What is the name of this finish?')

    def __str__(self):
        return self.name


    class Meta:
        ordering = ('optionwindowbrand','name',)
        verbose_name = 'option window interior finish'

class OptionWindowInteriorSpecies(models.Model):
    optionwindowbrand = models.ForeignKey(OptionWindowBrand, blank=True, help_text='What is the brand to which this options applies?', null=True, on_delete=models.PROTECT)
    name = models.CharField('name', max_length=200, blank=True, help_text='What is the name of this finish?')

    def __str__(self):
        return self.name


    class Meta:
        ordering = ('optionwindowbrand','name',)
        verbose_name = 'option window interior species'

class OptionWindowHardwareFinish(models.Model):
    optionwindowbrand = models.ForeignKey(OptionWindowBrand, blank=True, help_text='What is the brand to which this options applies?', null=True, on_delete=models.PROTECT)
    name = models.CharField('name', max_length=200, blank=True, help_text='What is the name of this finish?')

    def __str__(self):
        return self.name


    class Meta:
        ordering = ('optionwindowbrand','name',)
        verbose_name = 'option window hardware finish'

class OptionWindowScreen(models.Model):
    optionwindowbrand = models.ForeignKey(OptionWindowBrand, blank=True, help_text='What is the brand to which this options applies?', null=True, on_delete=models.PROTECT)
    name = models.CharField('name', max_length=200, blank=True, help_text='What is the name of this type of screen?')

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('optionwindowbrand','name',)
        verbose_name = 'option window screen'

class OptionWindowShade(models.Model):
    optionwindowbrand = models.ForeignKey(OptionWindowBrand, blank=True, help_text='What is the brand to which this options applies?', null=True, on_delete=models.PROTECT)
    name = models.CharField('name', max_length=200, blank=True, help_text='What is the name of this type of shade?')

    def __str__(self):
        return self.name


    class Meta:
        ordering = ('optionwindowbrand','name',)
        verbose_name = 'option window shade'

class OptionWindowLockSensor(models.Model):
    optionwindowbrand = models.ForeignKey(OptionWindowBrand, blank=True, help_text='What is the brand to which this options applies?', null=True, on_delete=models.PROTECT)
    name = models.CharField('name', max_length=200, blank=True, help_text='What is the name of this type of sensor?')

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('optionwindowbrand','name',)
        verbose_name = 'option window lock sensor'

class OptionICFWallThickness(models.Model):
    name = models.CharField('label', max_length=10, blank=True, help_text='What is the label to describe this thickness?')
    inches = models.IntegerField('inches', default=0, help_text='What is the thickness in inches?')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'option icf wall thickness'
        ordering = ['inches',]

class OptionInteriorMillworkPrimarySpecies(models.Model):
    name = models.CharField('name', max_length=200, blank=True, help_text='What is the name of this species?')

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)
        verbose_name = 'option interior millwork primary species'

class OptionInteriorMillworkTreadSpecies(models.Model):
    name = models.CharField('name', max_length=200, blank=True, help_text='What is the name of this species?')

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)
        verbose_name = 'option interior millwork tread species'


class OptionInteriorMillworkRiserSpecies(models.Model):
    name = models.CharField('name', max_length=200, blank=True, help_text='What is the name of this species?')

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)
        verbose_name = 'option interior millwork riser species'

class OptionExteriorMillworkRailingStyle(models.Model):
    name = models.CharField('name', max_length=200, blank=True, help_text='What is the name of this style?')

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)
        verbose_name = 'option exterior millwork railing style'

class OptionExteriorMillworkDeckingBrand(models.Model):
    name = models.CharField('name', max_length=200, blank=True, help_text='What is the name of this material?')

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)
        verbose_name = 'option exterior millwork decking brand'


class OptionExteriorMillworkDeckingGrooves(models.Model):
    name = models.CharField('name', max_length=200, blank=True, help_text='What is the name of this groove option?')

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)
        verbose_name = 'option exterior millwork decking grooves'

class OptionExteriorMillworkDeckingCollection(models.Model):
    optionexteriormillworkdeckingbrand = models.ForeignKey(OptionExteriorMillworkDeckingBrand, blank=True, help_text='What is the brand to which this options applies?', null=True, on_delete=models.PROTECT)
    name = models.CharField('name', max_length=200, blank=True, help_text='What is the name of this collection?')

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)
        verbose_name = 'option exterior millwork decking collection'

class OptionExteriorMillworkDeckingColor(models.Model):
    name = models.CharField('name', max_length=200, blank=True, help_text='What is the name of this color?')
    optionexteriormillworkdeckingcollection = models.ForeignKey(OptionExteriorMillworkDeckingCollection, blank=True, help_text='What is the decking collection for which this color is an option?', null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)
        verbose_name = 'option exterior millwork decking color'

class EstisheetDoor(models.Model):

    NR_NEW='N'
    NR_RE='R'
    NR_CHOICES=(
        (NR_NEW, 'New Construction'),
        (NR_RE, 'Replacement'),
    )
    estirequest = models.ForeignKey(Estirequest, on_delete=models.CASCADE, help_text='For which request is this sheet?')
    new_or_replacement = models.CharField('new/replacement', max_length=2, blank=True, choices=NR_CHOICES, help_text='Is this door a new installation or a replacement?', null=True)
    optiondoorbrand = models.ForeignKey(OptionDoorBrand, null=True, blank=True, help_text='What is the brand of these doors?', on_delete=models.PROTECT)
    model_number = models.CharField('model number', max_length=200, blank=True, help_text='What is the model number of this door?')
    size = models.CharField('size', max_length=20, blank=True, help_text='What is the size of door?')
    handing = models.CharField('handing', max_length=200, blank=True, help_text='What are the handing and other considerations for this door?')
    transom_height = models.CharField('transom height', max_length=200, blank=True, help_text='What is the height of the transom?' )
    optionexterior_color = models.ForeignKey(OptionDoorExteriorColor, verbose_name='exterior color', blank=True, help_text='what is the exterior color of these doors?', null=True, on_delete=models.PROTECT)
    optioninterior_finish = models.ForeignKey(OptionDoorInteriorFinish, verbose_name='interior finish', blank=True, help_text='what is the interior finish of these doors?', null=True, on_delete=models.PROTECT)
    optionhardware_finish = models.ForeignKey(OptionDoorHardwareFinish, verbose_name='hardware finish', blank=True, help_text='what is the hardware finish of these doors?', null=True, on_delete=models.PROTECT)
    optionhardware_style = models.CharField('hardware style', max_length=50, blank=True, help_text='What is the hardware style of these doors?')
    optionscreen = models.ForeignKey(OptionDoorScreen, null=True, blank=True, help_text='What screens are included with these doors?', on_delete=models.PROTECT, verbose_name='screens')
    optionshades = models.ForeignKey(OptionDoorShade, verbose_name='shades', blank=True, help_text='what shades are included with these doors?', null=True, on_delete=models.PROTECT)
    optionlock_sensors = models.BooleanField('lock sensors', default=False, help_text='Do these doors have lock sensors?')
    comments = models.TextField('comments', blank=True, help_text='What are comments for this estimate?')

    def __str__(self):
        return 'Non-Marvin Doors for ' + self.estirequest

    class Meta:
        ordering = ('estirequest',)
        verbose_name = 'estimate sheet for non-marvin door'

class EstisheetMarvinDoor(models.Model):

    NR_NEW='N'
    NR_RE='R'
    NR_CHOICES=(
        (NR_NEW, 'New Construction'),
        (NR_RE, 'Replacement'),
    )
    estirequest = models.ForeignKey(Estirequest, on_delete=models.CASCADE, help_text='For what request is this sheet?')
    new_or_replacement = models.CharField('new/replacement', max_length=2, blank=True, choices=NR_CHOICES, help_text='Is this door a new installation or a replacement?', null=True)
    optionexterior_color = models.ForeignKey(OptionMarvinDoorExteriorColor, verbose_name='exterior color', blank=True, help_text='what is the exterior color of these doors?', null=True, on_delete=models.PROTECT)
    optionmarvindoorbrand = models.ForeignKey(OptionMarvinDoorBrand, null=True, blank=True, help_text='What is the brand of these doors?', on_delete=models.PROTECT)
    optioninterior_finish = models.ForeignKey(OptionMarvinDoorInteriorFinish, verbose_name='interior finish', blank=True, help_text='what is the interior finish of these doors?', null=True, on_delete=models.PROTECT)
    optionhardware_style = models.ForeignKey(OptionMarvinDoorHardwareStyle, verbose_name='hardware style', blank=True, help_text='what is the hardware style of these doors?', null=True, on_delete=models.PROTECT)
    optionhardware_finish = models.ForeignKey(OptionMarvinDoorHardwareFinish, verbose_name='hardware finish', blank=True, help_text='what is the hardware finish of these doors?', null=True, on_delete=models.PROTECT)
    optionscreens = models.ForeignKey(OptionMarvinDoorScreen, null=True, blank=True, help_text='What screens are included with these doors?', on_delete=models.PROTECT, verbose_name='screens')
    optionshades = models.ForeignKey(OptionMarvinDoorShade, verbose_name='shades', blank=True, help_text='what shades are included with these doors?', null=True, on_delete=models.PROTECT)
    optionlock_sensors = models.BooleanField('lock sensors', default=False, help_text='Do these doors have lock sensors?')
    comments = models.TextField('comments', blank=True, help_text='What are comments for this estimate?')

    def __str__(self):
        return 'Marvin-Doors for ' + self.estirequest

    class Meta:
        verbose_name = 'estimate sheet for marvin door'
        ordering = ('estirequest',)

class EstisheetWindow(models.Model):

    NR_NEW='N'
    NR_RE='R'
    NR_CHOICES=(
        (NR_NEW, 'New Construction'),
        (NR_RE, 'Replacement'),
    )
    estirequest = models.ForeignKey(Estirequest, on_delete=models.CASCADE, help_text='For what request is this sheet?')
    new_or_replacement = models.CharField('new/replacement', max_length=2, blank=True, choices=NR_CHOICES, help_text='Is this window a new installation or a replacement?', null=True)
    optionwindowbrand = models.ForeignKey(OptionWindowBrand, null=True, blank=True, help_text='What is the brand of these windows?', on_delete=models.PROTECT)
    optionexterior_color = models.ForeignKey(OptionWindowExteriorColor, verbose_name='exterior color', blank=True, help_text='what is the exterior color of these windows?', null=True, on_delete=models.PROTECT)
    optioninterior_finish = models.ForeignKey(OptionWindowInteriorFinish, verbose_name='interior finish', blank=True, help_text='what is the interior finish of these windows?', null=True, on_delete=models.PROTECT)
    optionhardware_finish = models.ForeignKey(OptionWindowHardwareFinish, verbose_name='hardware finish', blank=True, help_text='what is the hardware finish of these windows?', null=True, on_delete=models.PROTECT)
    optionscreen = models.ForeignKey(OptionWindowScreen, null=True, blank=True, help_text='What screens are included with these windows?', on_delete=models.PROTECT, verbose_name='screens')
    optionshades = models.ForeignKey(OptionWindowShade, verbose_name='shades', blank=True, help_text='what shades are included with these windows?', null=True, on_delete=models.PROTECT)
    optionlock_sensors = models.BooleanField('lock sensors', default=False, help_text='Do these windows have lock sensors?')
    comments = models.TextField('comments', blank=True, help_text='What are comments for this estimate?')

    def __str__(self):
        return 'Windows for ' + self.estirequest

    class Meta:
        ordering = ('estirequest',)
        verbose_name = 'estimate sheet for windows'

class EstisheetICF(models.Model):

    NR_NEW='N'
    NR_RE='R'
    NR_CHOICES=(
        (NR_NEW, 'New Construction'),
        (NR_RE, 'Replacement'),
    )
    estirequest = models.ForeignKey(Estirequest, on_delete=models.CASCADE, help_text='For what request is this sheet?')
    optionbthickness = models.ForeignKey(OptionICFWallThickness, verbose_name='basement wall thickness', blank=True, help_text='what is the basement wall thickness?', null=True, on_delete=models.PROTECT, related_name='icfbwall0')
    option0thickness = models.ForeignKey(OptionICFWallThickness, verbose_name='foundation wall thickness', blank=True, help_text='what is the foundation wall thickness?', null=True, on_delete=models.PROTECT, related_name='icf0wall0')
    option1thickness = models.ForeignKey(OptionICFWallThickness, verbose_name='1st floor wall thickness', blank=True, help_text='what is the first floor wall thickness?', null=True, on_delete=models.PROTECT, related_name='icfwall1')
    option2thickness = models.ForeignKey(OptionICFWallThickness, verbose_name='2nd floor wall thickness', blank=True, help_text='what is the second floor wall thickness?', null=True, on_delete=models.PROTECT, related_name='icfwall2')
    option3thickness = models.ForeignKey(OptionICFWallThickness, verbose_name='3rd floor wall thickness', blank=True, help_text='what is the third floor wall thickness?', null=True, on_delete=models.PROTECT, related_name='icfwall3')
    optionpargecoating = models.CharField('foundation parge coating', max_length=1, choices=YESNO, default='N', help_text='Does this estimate include foundation parge coating?', null=True)
    optionbgmembrane = models.CharField('below grade membrane', max_length=1, choices=YESNO, default='N', help_text='Does this estimate include below grade membrane?', null=True)
    optionslabinsulation = models.CharField('slab on grade insullation', max_length=1, choices=YESNO, default='N', help_text='Does this estimate include slab on grade insullation?', null=True)
    optionfloor = models.CharField('ICF floor system', max_length=1, choices=YESNO, default='N', help_text='Does this estimate include an ICF floor system?', null=True)
    optionroof = models.CharField('ICF roof system', max_length=1, choices=YESNO, default='N', help_text='Does this estimate include an ICF roof system?', null=True)
    comments = models.TextField('comments', blank=True, help_text='What are comments for this estimate?')

    def __str__(self):
        return 'ICF For ' + self.estirequest

    class Meta:
        ordering = ('estirequest',)
        verbose_name = 'estimate sheet for icf'

class EstisheetInteriorMillwork(models.Model):

    estirequest = models.ForeignKey(Estirequest, help_text='For what request is this sheet?', on_delete=models.CASCADE)
    primaryspecies = models.ForeignKey(OptionInteriorMillworkPrimarySpecies, null=True, blank=True, help_text='What is the primary species for this millwork?', on_delete=models.SET_NULL)
    trim1baselength  = models.CharField('trim type 1 base length', blank=True, max_length=10)
    trim1basewidthsize  = models.CharField('trim type 1 base width/size', blank=True, max_length=10)
    trim1casinglength  = models.CharField('trim type 1 casing length', blank=True, max_length=10)
    trim1casingwidthsize  = models.CharField('trim type 1 casing width/size', blank=True, max_length=10)
    trim1crownlength  = models.CharField('trim type 1 crown length', blank=True, max_length=10)
    trim1crownwidthsize  = models.CharField('trim type 1 crown width/size', blank=True, max_length=10)
    trim1comments  = models.CharField('trim type 1 comments length', blank=True, max_length=100)
    trim1commentswidthsize  = models.CharField('trim type 1 comments width/size', blank=True, max_length=100)
    trim2baselength  = models.CharField('trim type 2 base length', blank=True, max_length=10)
    trim2basewidthsize  = models.CharField('trim type 2 base width/size', blank=True, max_length=10)
    trim2casinglength  = models.CharField('trim type 2 casing length', blank=True, max_length=10)
    trim2casingwidthsize  = models.CharField('trim type 2 casing width/size', blank=True, max_length=10)
    trim2crownlength  = models.CharField('trim type 2 crown length', blank=True, max_length=10)
    trim2crownwidthsize  = models.CharField('trim type 2 crown width/size', blank=True, max_length=10)
    trim2comments  = models.CharField('trim type 2 comments length', blank=True, max_length=100)
    trim2commentswidthsize  = models.CharField('trim type 2 comments width/size', blank=True, max_length=100)
    trim3baselength  = models.CharField('trim type 3 base length', blank=True, max_length=10)
    trim3basewidthsize  = models.CharField('trim type 3 base width/size', blank=True, max_length=10)
    trim3casinglength  = models.CharField('trim type 3 casing length', blank=True, max_length=10)
    trim3casingwidthsize  = models.CharField('trim type 3 casing width/size', blank=True, max_length=10)
    trim3crownlength  = models.CharField('trim type 3 crown length', blank=True, max_length=10)
    trim3crownwidthsize  = models.CharField('trim type 3 crown width/size', blank=True, max_length=10)
    trim3comments  = models.CharField('trim type 3 comments length', blank=True, max_length=100)
    trim3commentswidthsize  = models.CharField('trim type 3 comments width/size', blank=True, max_length=100)
    casingdetails = models.CharField('casing details', blank=True, max_length=20)
    windowstoolskirt = models.BooleanField('window stool with skirt', blank=True, default=False)
    pictureframe = models.CharField('picture frame', choices=YESNO, default='N', max_length=1)
    casingdetails = models.CharField('casing details', blank=True, max_length=30)
    dwreturn = models.BooleanField('dwreturn', blank=True, default=False)
    interiorcolumns = models.CharField('interiordoors', blank=True, max_length=30)
    interiordoors = models.CharField('interiordoors', blank=True, max_length=30)
    doorstyle = models.CharField('doorstyle', blank=True, max_length=30)
    doorhanging = models.CharField('hanging', blank=True, max_length=30)
    jambthickness = models.CharField('jambthickness', blank=True, max_length=30)
    specialtydoors = models.CharField('specialtydoors', blank=True, max_length=80)
    stair1treadspecies = models.ForeignKey(OptionInteriorMillworkTreadSpecies, null=True, blank=True, help_text='What is the species for this tread?', on_delete=models.SET_NULL, related_name='stair1tread')
    stair1riserspecies = models.ForeignKey(OptionInteriorMillworkRiserSpecies, null=True, blank=True, help_text='What is the species for this riser?', on_delete=models.SET_NULL, related_name='stair1riser')
    stair1handrail = models.CharField('stair1handrail', blank=True, max_length=30)
    stair1picketnewel = models.CharField('stair1picketnewel', blank=True, max_length=100)
    stair2treadspecies = models.ForeignKey(OptionInteriorMillworkTreadSpecies, null=True, blank=True, help_text='What is the species for this tread?', on_delete=models.SET_NULL, related_name='stair2tread')
    stair2riserspecies = models.ForeignKey(OptionInteriorMillworkRiserSpecies, null=True, blank=True, help_text='What is the species for this riser?', on_delete=models.SET_NULL, related_name='stair2riser')
    stair2handrail = models.CharField('stair2handrail', blank=True, max_length=30)
    stair2picketnewel = models.CharField('stair2picketnewel', blank=True, max_length=30)
    stair3treadspecies = models.ForeignKey(OptionInteriorMillworkTreadSpecies, null=True, blank=True, help_text='What is the species for this tread?', on_delete=models.SET_NULL, related_name='stair3tread')
    stair3riserspecies = models.ForeignKey(OptionInteriorMillworkRiserSpecies, null=True, blank=True, help_text='What is the species for this riser?', on_delete=models.SET_NULL, related_name='stair3riser')
    stair3handrail = models.CharField('stair3handrail', blank=True, max_length=30)
    stair3picketnewel = models.CharField('stair3picketnewel', blank=True, max_length=30)
    stairnotes  = models.CharField('stairnotes ', blank=True, max_length=30)
    wainscot = models.CharField('wainscot', blank=True, max_length=80)
    cofferedceiling = models.CharField('coffered ceiling', blank=True, max_length=80)
    comments = models.TextField('comments', blank=True, help_text='What are comments for this estimate?')

    def __str__(self):
        return 'Interior Millwork for ' + self.estirequest

    class Meta:
        ordering = ('estirequest',)
        verbose_name = 'estimate sheet for interior millwork'

class EstisheetExteriorMillwork(models.Model):

    estirequest = models.ForeignKey(Estirequest, help_text='For what request is this sheet?', on_delete=models.CASCADE)
    railingstyle  = models.ForeignKey(OptionExteriorMillworkRailingStyle, blank=True, help_text='What is the railing style?', null=True, on_delete=models.SET_NULL)
    railingstylecomments  = models.CharField('railing style comments', blank=True, help_text='What is the railing style?', max_length=255)
    railinglevel  = models.CharField('level rail sections', blank=True, help_text='What is the quantity of level rail?', max_length=25)
    railingstair  = models.CharField('stair rail sections', blank=True, help_text='What is the quantity of stair rail?', max_length=25)
    takeoff  = models.FileField('take off', upload_to='documents/', blank=True, help_text='What is the take off?', max_length=25, null=True)
    railingnewelposts = models.CharField('structural newel posts', blank=True, default=0, help_text='How many newel posts  are to be installed', max_length=6)
    railingnewelbrackets = models.CharField('install newel brackets', blank=True, default=0, help_text='How many newel brackets are to be installed', max_length=6)
    railingnewelcovers = models.CharField('install newel covers', blank=True, default=0, help_text='How many newel covers are to be installed', max_length=6)
    columncomments = models.CharField('column comments', blank=True, help_text='What are any comments about columns?', max_length=255)
    optionexteriormillworkdeckingbrand = models.ForeignKey(OptionExteriorMillworkDeckingBrand, blank=True, help_text='What is the decking material?', null=True, on_delete=models.SET_NULL)
    deckinggrooves = models.ForeignKey(OptionExteriorMillworkDeckingGrooves, blank=True, help_text='What kind of grooving does this decking have?', null=True, on_delete=models.SET_NULL)
    optionexteriormillworkdeckingcollection = models.ForeignKey(OptionExteriorMillworkDeckingCollection, blank=True, help_text='What is the decking collection?', null=True, on_delete=models.SET_NULL)
    deckingcolor = models.ForeignKey(OptionExteriorMillworkDeckingColor, blank=True, help_text='What is the decking color?', null=True, on_delete=models.SET_NULL)
    shutters = models.CharField('shutter comments', blank=True, help_text='What are any notes about shutters?', max_length=255)

    def __str__(self):
        return 'Exterior Millwork for ' + self.estirequest


    class Meta:
        ordering = ('estirequest',)
        verbose_name = 'estimate sheet for exterior millwork'

class Assignment(models.Model):
    salesperson = models.ForeignKey(Salesperson, on_delete=models.SET_NULL, blank=True, help_text='Who is the salesperson of this project', null=True)
    estirequest = models.ForeignKey(Estirequest, on_delete=models.CASCADE, help_text='For which project is this assigment?')

    def __str__(self):
        return '{} assigned to {}'.format(self.salesperson, self.estirequest)

    class Meta:
        ordering = ('salesperson',)
        verbose_name = 'assignment'

class Proposal(models.Model):
    STATUS_DRAFT='DR'
    STATUS_SUBMITTED='SU'
    STATUS_ACCEPTED='AC'
    STATUS_CHOICES=(
        (STATUS_DRAFT, 'Draft'),
        (STATUS_SUBMITTED, 'Submitted'),
        (STATUS_ACCEPTED, 'Accepted'),
    )
    estirequest = models.ForeignKey(Estirequest, on_delete=models.CASCADE, help_text='For which request is this sheet?')
    component = models.CharField('Component', blank=True, max_length=100, help_text='For what component is this estimate')
    amount = models.DecimalField('Amount',  decimal_places=2, blank=True, help_text='What is the amount of the proposal?', max_digits=10, null=True)
    estimator = models.ForeignKey(Estimator, blank=True, help_text='Who submitted this proposal?', null=True, on_delete=models.PROTECT)
    create_date = models.DateField('date', blank=True, default=date.today, help_text='When was this proposal created?')
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='created by', null=True, on_delete=models.PROTECT, help_text="The user who submitted the proposal")
    update_date = models.DateField('updated', blank=True, auto_now=True, help_text='When was this proposal created?')
    uploadedfile = models.FileField('file', upload_to='documents/', blank=True, null=True)
    comments = models.TextField('comments', blank=True, help_text='What are comments for this proposal?')

    def can_view_in_list(self, user):
        can = False
        if user is not None:
            if user.is_superuser:
                return True
            if user.groups.filter(name="Esteem_Managers").exists():
                return True
            if user.groups.filter(name="Esteem_Estimators").exists():
                if self.estimator:
                    if user==self.estimator.user:
                        return True

    def can_view(self, user):
        can = False
        if user is not None:
            if user.is_superuser:
                return True
            if user.groups.filter(name="Esteem_Managers").exists():
                return True
            if user.groups.filter(name="Esteem_Estimators").exists():
                if self.estirequest.status == self.STATUS_SUBMITTED:
                    return True
                if self.estirequest.status == self.STATUS_ESTIMATED:
                    return True
            if user.groups.filter(name="Esteem_Salespeople").exists():
                for assignment in self.estirequest.assignment_set.all():
                    if user == assignment.salesperson.user:
                        return True

    def can_change(self, user):
        can = False
        if user is not None:
            if user.is_superuser:
                return True
            if user.groups.filter(name="Esteem_Managers").exists():
                return True
            if user.groups.filter(name="Esteem_Estimators").exists():
                if self.estimator is not None:
                    if self.estimator.user is not None:
                        if user == self.estimator.user:
                            return True

    def __str__(self):
        return '{} {}'.format(self.estirequest, self.component)

    class Meta:
        ordering = ('-create_date',)
        verbose_name = 'proposal'
        permissions = [
            ('list_proposals', 'Can list proposals')
        ]

class ProposalDocument(models.Model):
    proposal = models.ForeignKey(Proposal, on_delete=models.CASCADE, help_text='What is the proposal to which this document is attached?')
    title = models.CharField('title', max_length = 200, blank=True, help_text='What is this documents title?')
    uploadedfile = models.FileField(upload_to='documents/', blank=True, null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('proposaldocument_detail', args=[str(self.id)])

    class Meta:
        ordering = ('title',)
        verbose_name = 'proposal document'

class QueryEstirequest(models.Model):
    user = models.ForeignKey( settings.AUTH_USER_MODEL, verbose_name='user', on_delete=models.SET_NULL, help_text='who is the user associated with the setting', null=True, blank=True, related_name='estirequest_query', )
    query_name = models.CharField( 'query name', max_length=50,  blank=True, help_text='The name of this query')
    latest_use = models.DateTimeField('last used', auto_now=True, help_text='The most recent use of this query')

    name_value = models.CharField( 'name', max_length=30, blank=True, )
    name_use = models.BooleanField('use name', default=False)
    name_operator = models.CharField('name operator', max_length=100, default='name__icontains', choices=(('name__iexact', 'equals'),('name__icontains', 'contains')) )

    address_value = models.CharField( 'address', max_length=30, blank=True, )
    address_use = models.BooleanField('use address', default=False)
    address_operator = models.CharField('address operator', max_length=100, default='address__icontains', choices=(('address__iexact', 'equals'),('address__icontains', 'contains')) )

    ORDERBY_CHOICES = [
        ('name', 'Name'),
    ]

    orderby1 = models.CharField('order by',  max_length=20, choices=ORDERBY_CHOICES, default='makemodel')
    orderby2 = models.CharField('order by',  max_length=20, choices=ORDERBY_CHOICES, default='inventory')
    orderby3 = models.CharField('order by',  max_length=20, choices=ORDERBY_CHOICES, default='condition')

    paginate_by = models.IntegerField('paginate by', default=10)

    def query_display(self):
        fieldnames = [
            'name',
        ]

        display_string = ''
        for fieldname in fieldnames:

            if getattr(self, fieldname + '_use'):

                if display_string > '':
                    display_string =display_string + ', '

                field = self._meta.get_field(fieldname + '_value')
                print(inspect.currentframe().f_lineno)
                print(type(field).__name__)
                if type(field).__name__=="ManyToManyField":
                    valuestring=''
                    for value in getattr(self, fieldname + '_value').all():
                        if valuestring > '':
                            valuestring = valuestring + ', '

                        valuestring = valuestring = valuestring + str(value)
                else:
                    valuestring = getattr(self, fieldname + '_value')

                display_string = display_string + ' {} {} {}'.format( field.verbose_name, getattr(self, 'get_' + fieldname + '_operator_display' )(), valuestring )

        return display_string

    class Meta:
        unique_together = [['query_name', 'user']]
        ordering = ['-latest_use']
