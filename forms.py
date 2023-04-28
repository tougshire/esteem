from .models import Assignment, Customer, Estimator, Estirequest, EstirequestDocument, EstisheetDoor, EstisheetExteriorMillwork, EstisheetHardware, EstisheetICF, EstisheetInteriorMillwork, EstisheetMarvinDoor, EstisheetWindow, OptionDoorBrand, OptionWindowBrand, Proposal, ProposalDocument, Salesperson
from addable.forms import Addable, AddableMultiple
from datetime import date, timedelta
from django import forms
from django.contrib.contenttypes.forms import generic_inlineformset_factory
from django.forms import ModelForm, inlineformset_factory
from django.urls import reverse_lazy
import inspect

class SelectWithBrand(forms.Select):

    def __init__(self, attrs=None, choices=()):
        super().__init__(attrs, choices)
        if 'data-limitby' in attrs:
            self.limitby = attrs['data-limitby']

    def create_option(self, name, value, label, selected, index, subindex=None, attrs=None):

        option = super().create_option(name, value, label, selected, index, subindex, attrs)

        if value:
            option['attrs']['data-' + self.limitby ] = getattr(value.instance, self.limitby).pk

        return option

class AssignmentForm(ModelForm):
    class Meta:

        model=Assignment
        fields=[
            'estirequest',
            'salesperson',
        ]

class Assignment_EstirequestForm(ModelForm):
    class Meta:

        model=Assignment
        fields=[
            'salesperson',
        ]

class CustomerForm(ModelForm):
    class Meta:

        model=Customer
        fields=[
            'name',
            'email',
            'phone',
            'additional_contact',
            'is_type_commercialgc',
            'is_type_builder',
            'is_type_remodeler',
            'is_type_homeowner',
            'billing_address',
            'business_card',
            'archived',
            'custom_logo',
        ]
        widgets={
            'email':forms.TextInput,
        }

class EstirequestDocumentForm(ModelForm):
    class Meta:

        model=EstirequestDocument
        fields=[
            'estirequest',
            'title',
            'uploadedfile',
        ]

class EstirequestDocument_EstirequestForm(ModelForm):
    class Meta:

        model=EstirequestDocument
        fields=[
            'title',
            'uploadedfile',
        ]

class OptionDoorBrandForm(ModelForm):
    class Meta:

        model=OptionDoorBrand
        fields=[
            'name',
        ]

class EstisheetDoorForm(ModelForm):
    class Meta:

        model=EstisheetDoor
        fields=[
            'estirequest',
            'new_or_replacement',
            'optiondoorbrand',
            'comments',
            'optionexterior_color',
            'optionhardware_finish',
            'optionhardware_style',
            'optioninterior_finish',
            'optionlock_sensors',
            'model_number',
            'optionscreen',
            'optionshades',
            'size',
            'handing',
            'transom_height',
        ]
        widgets={
            'optionexterior_color':SelectWithBrand(attrs={'data-limitby':'optiondoorbrand','data-rawname':'optionexterior_color'}),
            'optionhardware_finish':SelectWithBrand(attrs={'data-limitby':'optiondoorbrand','data-rawname':'optionhardware_finish'}),
            'optionhardware_style':SelectWithBrand(attrs={'data-limitby':'optiondoorbrand','data-rawname':'optionhardware_style'}),
            'optioninterior_finish':SelectWithBrand(attrs={'data-limitby':'optiondoorbrand','data-rawname':'optioninterior_finish'}),
            'optionlock_sensors':SelectWithBrand(attrs={'data-limitby':'optiondoorbrand','data-rawname':'optionlock_sensors'}),
            'model_number':SelectWithBrand(attrs={'data-limitby':'optiondoorbrand','data-rawname':'model_number'}),
            'optionscreen':SelectWithBrand(attrs={'data-limitby':'optiondoorbrand','data-rawname':'optionscreen'}),
            'optionshades':SelectWithBrand(attrs={'data-limitby':'optiondoorbrand','data-rawname':'optionshades'}),
        }

class EstisheetDoor_EstirequestForm(ModelForm):
    class Meta:

        model=EstisheetDoor
        fields=[
            'optiondoorbrand',
            'new_or_replacement',
            'comments',
            'optionexterior_color',
            'optionhardware_finish',
            'optionhardware_style',
            'optioninterior_finish',
            'optionlock_sensors',
            'model_number',
            'optionscreen',
            'optionshades',
            'size',
            'handing',
            'transom_height',
        ]
        widgets={
            'optionexterior_color':SelectWithBrand(attrs={'data-limitby':'optiondoorbrand','data-rawname':'optionexterior_color'}),
            'optionhardware_finish':SelectWithBrand(attrs={'data-limitby':'optiondoorbrand','data-rawname':'optionhardware_finish'}),
            'optionhardware_style':SelectWithBrand(attrs={'data-limitby':'optiondoorbrand','data-rawname':'optionhardware_style'}),
            'optioninterior_finish':SelectWithBrand(attrs={'data-limitby':'optiondoorbrand','data-rawname':'optioninterior_finish'}),
            'optionlock_sensors':SelectWithBrand(attrs={'data-limitby':'optiondoorbrand','data-rawname':'optionlock_sensors'}),
            'model_number':SelectWithBrand(attrs={'data-limitby':'optiondoorbrand','data-rawname':'model_number'}),
            'optionscreen':SelectWithBrand(attrs={'data-limitby':'optiondoorbrand','data-rawname':'optionscreen'}),
            'optionshades':SelectWithBrand(attrs={'data-limitby':'optiondoorbrand','data-rawname':'optionshades'}),
        }

class EstisheetICFForm(ModelForm):
    class Meta:

        model=EstisheetICF
        fields=[
            'estirequest',
            'option0thickness',
            'option1thickness',
            'option2thickness',
            'option3thickness',
            'optionpargecoating',
            'optionbgmembrane',
            'optionslabinsulation',
            'optionfloor',
            'optionroof',
            'comments',
        ]

class EstisheetICF_EstirequestForm(ModelForm):
    class Meta:

        model=EstisheetICF
        fields=[
            'option0thickness',
            'option1thickness',
            'option2thickness',
            'option3thickness',
            'optionpargecoating',
            'optionbgmembrane',
            'optionslabinsulation',
            'optionfloor',
            'optionroof',
            'comments',
        ]

class EstisheetInteriorMillworkForm(ModelForm):
    class Meta:
        model = EstisheetInteriorMillwork
        fields=[
            'estirequest',
            'primaryspecies',
            'trim1baselength',
            'trim1basewidthsize',
            'trim1casinglength',
            'trim1casingwidthsize',
            'trim1crownlength',
            'trim1crownwidthsize',
            'trim1comments',
            'trim1commentswidthsize',
            'trim2baselength',
            'trim2basewidthsize',
            'trim2casinglength',
            'trim2casingwidthsize',
            'trim2crownlength',
            'trim2crownwidthsize',
            'trim2comments',
            'trim2commentswidthsize',
            'trim3baselength',
            'trim3basewidthsize',
            'trim3casinglength',
            'trim3casingwidthsize',
            'trim3crownlength',
            'trim3crownwidthsize',
            'trim3comments',
            'trim3commentswidthsize',
            'casingdetails',
            'windowstoolskirt',
            'pictureframe',
            'dwreturn',
            'interiorcolumns',
            'interiordoors',
            'doorstyle',
            'doorhanging',
            'jambthickness',
            'specialtydoors',
            'stair1treadspecies',
            'stair1riserspecies',
            'stair1handrail',
            'stair1picketnewel',
            'stair2treadspecies',
            'stair2riserspecies',
            'stair2handrail',
            'stair2picketnewel',
            'stair3treadspecies',
            'stair3riserspecies',
            'stair3handrail',
            'stair3picketnewel',
            'stairnotes',
            'wainscot',
            'cofferedceiling',
            'comments',
        ]

class EstisheetInteriorMillwork_EstirequestForm(ModelForm):
    class Meta:
        model = EstisheetInteriorMillwork
        fields=[
            'primaryspecies',
            'trim1baselength',
            'trim1basewidthsize',
            'trim1casinglength',
            'trim1casingwidthsize',
            'trim1crownlength',
            'trim1crownwidthsize',
            'trim1comments',
            'trim1commentswidthsize',
            'trim2baselength',
            'trim2basewidthsize',
            'trim2casinglength',
            'trim2casingwidthsize',
            'trim2crownlength',
            'trim2crownwidthsize',
            'trim2comments',
            'trim2commentswidthsize',
            'trim3baselength',
            'trim3basewidthsize',
            'trim3casinglength',
            'trim3casingwidthsize',
            'trim3crownlength',
            'trim3crownwidthsize',
            'trim3comments',
            'trim3commentswidthsize',
            'casingdetails',
            'windowstoolskirt',
            'pictureframe',
            'dwreturn',
            'interiorcolumns',
            'interiordoors',
            'doorstyle',
            'doorhanging',
            'jambthickness',
            'specialtydoors',
            'stair1treadspecies',
            'stair1riserspecies',
            'stair1handrail',
            'stair1picketnewel',
            'stair2treadspecies',
            'stair2riserspecies',
            'stair2handrail',
            'stair2picketnewel',
            'stair3treadspecies',
            'stair3riserspecies',
            'stair3handrail',
            'stair3picketnewel',
            'stairnotes',
            'wainscot',
            'cofferedceiling',
            'comments',
        ]

class EstisheetExteriorMillworkForm(ModelForm):
    class Meta:
        model = EstisheetExteriorMillwork
        fields = [
            'estirequest',
            'railingstyle',
            'railingstylecomments',
            'railinglevel',
            'railingstair',
            'takeoff',
            'railingnewelposts',
            'railingnewelbrackets',
            'railingnewelcovers',
            'columncomments',
            'optionexteriormillworkdeckingbrand',
            'optionexteriormillworkdeckingcollection',
            'deckingcolor',
            'deckinggrooves',
            'shutters',
        ]
        widgets={
            'optionexteriormillworkdeckingcollection':SelectWithBrand(attrs={'data-limitby':'optionexteriormillworkdeckingbrand','data-rawname':'optionexteriormillworkdeckingcollection'}),
            'deckingcolor':SelectWithBrand(attrs={'data-limitby':'optionexteriormillworkdeckingcollection','data-rawname':'deckingcolor'}),
        }

class EstisheetHardwareForm(ModelForm):
    class Meta:
        model = EstisheetHardware
        fields = [
            'estirequest',
            'entrysets',
            'entrysetscomments',
            'electroniclocks',
            'electroniclockscomments',
            'deadbolts',
            'deadboltscomments',
            'keyedknobs',
            'keyedknobscomments',
            'knobs',
            'knobscomments',
            'sideplatelocks',
            'sideplatelockscomments',
            'slidingdoorhardware',
            'slidingdoorhardwarecomments',
            'barndoorhardware',
            'barndoorhardwarecomments',
            'dooraccessories',
            'dooraccessoriescomments',
            'knobs',
            'knobscomments',

        ]

class EstisheetHardware_EstirequestForm(ModelForm):
    class Meta:
        model = EstisheetHardware
        fields = [
            'estirequest',
            'entrysets',
            'entrysetscomments',
            'electroniclocks',
            'electroniclockscomments',
            'deadbolts',
            'deadboltscomments',
            'keyedknobs',
            'keyedknobscomments',
            'knobs',
            'knobscomments',
            'sideplatelocks',
            'sideplatelockscomments',
            'slidingdoorhardware',
            'slidingdoorhardwarecomments',
            'barndoorhardware',
            'barndoorhardwarecomments',
            'dooraccessoriescomments',
            'knobs',
            'knobscomments',
        ]

class EstisheetExteriorMillwork_EstirequestForm(ModelForm):
    class Meta:
        model = EstisheetExteriorMillwork
        fields = [
            'estirequest',
            'railingstyle',
            'railingstylecomments',
            'railinglevel',
            'railingstair',
            'takeoff',
            'railingnewelbrackets',
            'railingnewelposts',
            'railingnewelcovers',
            'columncomments',
            'optionexteriormillworkdeckingbrand',
            'optionexteriormillworkdeckingcollection',
            'deckingcolor',
            'deckinggrooves',
            'shutters',
        ]
        widgets={
            'optionexteriormillworkdeckingcollection':SelectWithBrand(attrs={'data-limitby':'optionexteriormillworkdeckingbrand','data-rawname':'optionexteriormillworkdeckingcollection'}),
            'deckingcolor':SelectWithBrand(attrs={'data-limitby':'optionexteriormillworkdeckingcollection','data-rawname':'deckingcolor'}),
        }

class EstimatorForm(ModelForm):
    class Meta:

        model=Estimator
        fields=[
            'user',
            'name',
        ]

class EstisheetMarvinDoorForm(ModelForm):
    class Meta:

        model=EstisheetMarvinDoor
        fields=[
            'estirequest',
            'new_or_replacement',
            'optionmarvindoorbrand',
            'comments',
            'optionexterior_color',
            'optionhardware_finish',
            'optionhardware_style',
            'optioninterior_finish',
            'optionlock_sensors',
            'optionscreens',
            'optionshades',
        ]
        widgets={
            'optionexterior_color':SelectWithBrand(attrs={'data-limitby':'optionmarvindoorbrand','data-rawname':'optionexterior_color'}),
            'optionhardware_finish':SelectWithBrand(attrs={'data-limitby':'optionmarvindoorbrand','data-rawname':'optionhardware_finish'}),
            'optionhardware_style':SelectWithBrand(attrs={'data-limitby':'optionmarvindoorbrand','data-rawname':'optionhardware_style'}),
            'optioninterior_finish':SelectWithBrand(attrs={'data-limitby':'optionmarvindoorbrand','data-rawname':'optioninterior_finish'}),
            'optionlock_sensors':SelectWithBrand(attrs={'data-limitby':'optionmarvindoorbrand','data-rawname':'optionlock_sensors'}),
            'optionscreens':SelectWithBrand(attrs={'data-limitby':'optionmarvindoorbrand','data-rawname':'optionscreens'}),
            'optionshades':SelectWithBrand(attrs={'data-limitby':'optionmarvindoorbrand','data-rawname':'optionshades'}),
        }

class EstisheetMarvinDoor_EstirequestForm(ModelForm):
    class Meta:

        model=EstisheetMarvinDoor
        fields=[
            'optionmarvindoorbrand',
            'new_or_replacement',
            'comments',
            'optionexterior_color',
            'optionhardware_finish',
            'optionhardware_style',
            'optioninterior_finish',
            'optionlock_sensors',
            'optionscreens',
            'optionshades',
        ]
        widgets={
            'optionexterior_color':SelectWithBrand(attrs={'data-limitby':'optionmarvindoorbrand','data-rawname':'optionexterior_color'}),
            'optionhardware_finish':SelectWithBrand(attrs={'data-limitby':'optionmarvindoorbrand','data-rawname':'optionhardware_finish'}),
            'optionhardware_style':SelectWithBrand(attrs={'data-limitby':'optionmarvindoorbrand','data-rawname':'optionhardware_style'}),
            'optioninterior_finish':SelectWithBrand(attrs={'data-limitby':'optionmarvindoorbrand','data-rawname':'optioninterior_finish'}),
            'optionlock_sensors':SelectWithBrand(attrs={'data-limitby':'optionmarvindoorbrand','data-rawname':'optionlock_sensors'}),
            'optionscreens':SelectWithBrand(attrs={'data-limitby':'optionmarvindoorbrand','data-rawname':'optionscreens'}),
            'optionshades':SelectWithBrand(attrs={'data-limitby':'optionmarvindoorbrand','data-rawname':'optionshades'}),
        }

class EstirequestForm(ModelForm):
    class Meta:

        model=Estirequest
        fields=[
            'address',
            'citystzip',
            'requestnum',
            'comments',
            'customer',
            'new_or_remodel',
            'name',
            'create_date',
            'submit_date',
            'status',
            'has_windows',
            'has_doors',
            'has_marvindoors',
            'has_icfs',
            'has_interiormillworks',
            'has_exteriormillworks',
            'has_hardware',
        ]
        widgets = {
            'customer': Addable(attrs={'data-add_url':reverse_lazy('customer_popup'), 'data-secondaries':''}),
        }

class SalespersonForm(ModelForm):
    class Meta:

        model=Salesperson
        fields=[
            'user',
            'name',
        ]

class OptionWindowBrandForm(ModelForm):
    class Meta:

        model=OptionWindowBrand
        fields=[
            'name',
        ]

class EstisheetWindowForm(ModelForm):
    class Meta:

        model=EstisheetWindow
        fields=[
            'optionwindowbrand',
            'comments',
            'optionexterior_color',
            'optionhardware_finish',
            'optioninterior_finish',
            'optionlock_sensors',
            'new_or_replacement',
            'estirequest',
            'optionscreen',
            'optionshades',
        ]
        widgets={
            'optionexterior_color':SelectWithBrand(attrs={'data-limitby':'optionwindowbrand','data-rawname':'optionexterior_color'}),
            'optionhardware_finish':SelectWithBrand(attrs={'data-limitby':'optionwindowbrand','data-rawname':'optionhardware_finish'}),
            'optioninterior_finish':SelectWithBrand(attrs={'data-limitby':'optionwindowbrand','data-rawname':'optioninterior_finish'}),
            'optionlock_sensors':SelectWithBrand(attrs={'data-limitby':'optionwindowbrand','data-rawname':'optionlock_sensors'}),
            'optionscreen':SelectWithBrand(attrs={'data-limitby':'optionwindowbrand','data-rawname':'optionscreen'}),
            'optionshades':SelectWithBrand(attrs={'data-limitby':'optionwindowbrand','data-rawname':'optionshades'}),
        }

class EstisheetWindow_EstirequestForm(ModelForm):

    class Meta:

        model=EstisheetWindow
        fields=[
            'new_or_replacement',
            'optionwindowbrand',
            'comments',
            'optionexterior_color',
            'optionhardware_finish',
            'optioninterior_finish',
            'optionlock_sensors',
            'optionscreen',
            'optionshades',
        ]
        widgets={
            'optionexterior_color':SelectWithBrand(attrs={'data-limitby':'optionwindowbrand','data-rawname':'optionexterior_color'}),
            'optionhardware_finish':SelectWithBrand(attrs={'data-limitby':'optionwindowbrand','data-rawname':'optionhardware_finish'}),
            'optioninterior_finish':SelectWithBrand(attrs={'data-limitby':'optionwindowbrand','data-rawname':'optioninterior_finish'}),
            'optionlock_sensors':SelectWithBrand(attrs={'data-limitby':'optionwindowbrand','data-rawname':'optionlock_sensors'}),
            'optionscreen':SelectWithBrand(attrs={'data-limitby':'optionwindowbrand','data-rawname':'optionscreen'}),
            'optionshades':SelectWithBrand(attrs={'data-limitby':'optionwindowbrand','data-rawname':'optionshades'}),
        }

class ProposalForm(ModelForm):
    class Meta:

        model=Proposal
        fields=[
            'estirequest',
            'amount',
            'component',
            'estimator',
            'create_date',
            'uploadedfile',
        ]

class Proposal_EstirequestForm(ModelForm):
    class Meta:

        model=Proposal
        fields=[
            'amount',
            'estimator',
            'component',
            'create_date',
            'uploadedfile',
        ]

class ProposalDocumentForm(ModelForm):
    class Meta:

        model=ProposalDocument
        fields=[
            'proposal',
            'title',
            'uploadedfile',
        ]

class ProposalDocument_ProposalForm(ModelForm):
    class Meta:

        model=ProposalDocument
        fields=[
            'title',
            'uploadedfile',
        ]

Assignment_EstirequestFormset = inlineformset_factory(Estirequest, Assignment, form=Assignment_EstirequestForm, extra=0, min_num=1, can_delete=True)
Proposal_EstirequestFormset = inlineformset_factory(Estirequest, Proposal, form=Proposal_EstirequestForm, extra=1, can_delete=True)
EstirequestDocument_EstirequestFormset = inlineformset_factory(Estirequest, EstirequestDocument, form=EstirequestDocument_EstirequestForm, extra=1, can_delete=True)
EstisheetDoor_EstirequestFormset = inlineformset_factory(Estirequest, EstisheetDoor, form=EstisheetDoor_EstirequestForm, extra=0, min_num=1,  can_delete=True)
EstisheetICF_EstirequestFormset = inlineformset_factory(Estirequest, EstisheetICF, form=EstisheetICF_EstirequestForm, extra=0, min_num=1,  can_delete=True)
EstisheetInteriorMillwork_EstirequestFormset = inlineformset_factory(Estirequest, EstisheetInteriorMillwork, form=EstisheetInteriorMillwork_EstirequestForm, extra=0, min_num=1,  can_delete=True)
EstisheetExteriorMillwork_EstirequestFormset = inlineformset_factory(Estirequest, EstisheetExteriorMillwork, form=EstisheetExteriorMillwork_EstirequestForm, extra=0, min_num=1,  can_delete=True)
EstisheetHardware_EstirequestFormset = inlineformset_factory(Estirequest, EstisheetHardware, form=EstisheetHardware_EstirequestForm, extra=0, min_num=1,  can_delete=True)
EstisheetMarvinDoor_EstirequestFormset = inlineformset_factory(Estirequest, EstisheetMarvinDoor, form=EstisheetMarvinDoor_EstirequestForm, extra=0, min_num=1, can_delete=True)
EstisheetWindow_EstirequestFormset = inlineformset_factory(Estirequest, EstisheetWindow, form=EstisheetWindow_EstirequestForm, extra=0, min_num=1, can_delete=True)
ProposalDocument_ProposalFormset = inlineformset_factory(Proposal, ProposalDocument, form=ProposalDocument_ProposalForm, extra=1, can_delete=True)
