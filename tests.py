from django.test import TestCase

from django.conf import settings
from django.contrib.auth import get_user_model
from ervin.models import ErvinGroup
from django.contrib.auth.models import Group

from django.contrib.auth.models import Permission

from esteem.models import Estimator, Salesperson

class SalespersonTestCase(TestCase):
    def setUp(self):

        group_estimators=ErvinGroup.objects.create(
            name="Esteem_Estimators",
        )
        for permname in ['add_assignment', 'change_assignment', 'delete_assignment', 'view_assignment', 'view_customer', 'view_estimator', 'view_estirequest', 'view_estirequestdocument', 'view_estisheetdoor', 'view_estisheetexteriormillwork', 'view_estisheeticf', 'view_estisheetinteriormillwork', 'view_estisheetmarvindoor', 'view_estisheetwindow', 'view_optiondoorbrand', 'view_optiondoorexteriorcolor', 'view_optiondoorhardwarefinish', 'view_optiondoorinteriorfinish', 'view_optiondoorlocksensor', 'view_optiondoorscreen', 'view_optiondoorshade', 'view_optionexteriormillworkdeckingbrand', 'view_optionexteriormillworkdeckingcollection', 'view_optionexteriormillworkdeckingcolor', 'view_optionexteriormillworkdeckinggrooves', 'view_optionexteriormillworkrailingstyle', 'view_optionicfwallthickness', 'view_optioninteriormillworkprimaryspecies', 'view_optioninteriormillworkriserspecies', 'view_optioninteriormillworktreadspecies', 'view_optionmarvindoorbrand', 'view_optionmarvindoorexteriorcolor', 'view_optionmarvindoorhardwarefinish', 'view_optionmarvindoorhardwarestyle', 'view_optionmarvindoorinteriorfinish', 'view_optionmarvindoorinteriorspecies', 'view_optionmarvindoorlocksensor', 'view_optionmarvindoorscreen', 'view_optionmarvindoorshade', 'view_optionwindowbrand', 'view_optionwindowexteriorcolor', 'view_optionwindowhardwarefinish', 'view_optionwindowinteriorfinish', 'view_optionwindowinteriorspecies', 'view_optionwindowlocksensor', 'view_optionwindowscreen', 'view_optionwindowshade', 'add_proposal', 'change_proposal', 'delete_proposal', 'list_proposals', 'view_proposal', 'add_proposaldocument', 'change_proposaldocument', 'delete_proposaldocument', 'view_proposaldocument', 'add_salesperson', 'change_salesperson', 'delete_salesperson', 'view_salesperson']:
            group_estimators.permissions.add(Permission.objects.get(codename=permname))

        group_salespeople=ErvinGroup.objects.create(
            name="Esteem_Salespeople",
        )
        for permname in ['add_assignment', 'change_assignment', 'delete_assignment', 'view_assignment', 'add_customer', 'change_customer', 'delete_customer', 'view_customer', 'view_estimator', 'add_estirequest', 'change_estirequest', 'delete_estirequest', 'view_estirequest', 'add_estirequestdocument', 'change_estirequestdocument', 'delete_estirequestdocument', 'view_estirequestdocument', 'add_estisheetdoor', 'change_estisheetdoor', 'delete_estisheetdoor', 'view_estisheetdoor', 'add_estisheetexteriormillwork', 'change_estisheetexteriormillwork', 'delete_estisheetexteriormillwork', 'view_estisheetexteriormillwork', 'add_estisheeticf', 'change_estisheeticf', 'delete_estisheeticf', 'view_estisheeticf', 'add_estisheetinteriormillwork', 'change_estisheetinteriormillwork', 'delete_estisheetinteriormillwork', 'view_estisheetinteriormillwork', 'add_estisheetmarvindoor', 'change_estisheetmarvindoor', 'delete_estisheetmarvindoor', 'view_estisheetmarvindoor', 'add_estisheetwindow', 'change_estisheetwindow', 'delete_estisheetwindow', 'view_estisheetwindow', 'view_optiondoorbrand', 'add_optiondoorexteriorcolor', 'change_optiondoorexteriorcolor', 'delete_optiondoorexteriorcolor', 'view_optiondoorexteriorcolor', 'view_optiondoorhardwarefinish', 'view_optiondoorinteriorfinish', 'view_optiondoorlocksensor', 'view_optiondoorscreen', 'view_optiondoorshade', 'view_optionexteriormillworkdeckingbrand', 'view_optionexteriormillworkdeckingcollection', 'view_optionexteriormillworkdeckingcolor', 'view_optionexteriormillworkdeckinggrooves', 'view_optionexteriormillworkrailingstyle', 'view_optionicfwallthickness', 'view_optioninteriormillworkprimaryspecies', 'view_optioninteriormillworkriserspecies', 'view_optioninteriormillworktreadspecies', 'view_optionmarvindoorbrand', 'view_optionmarvindoorexteriorcolor', 'view_optionmarvindoorhardwarefinish', 'view_optionmarvindoorhardwarestyle', 'view_optionmarvindoorinteriorfinish', 'view_optionmarvindoorinteriorspecies', 'view_optionmarvindoorlocksensor', 'view_optionmarvindoorscreen', 'view_optionmarvindoorshade', 'view_optionwindowbrand', 'view_optionwindowexteriorcolor', 'view_optionwindowhardwarefinish', 'view_optionwindowinteriorfinish', 'view_optionwindowinteriorspecies', 'view_optionwindowlocksensor', 'view_optionwindowscreen', 'view_optionwindowshade', 'view_proposal', 'view_proposaldocument', 'delete_salesperson']:
            group_salespeople.permissions.add(Permission.objects.get(codename=permname))

        self.sales_user=get_user_model().objects.create(
            username="salesuser",
            email="salesuser@ervinarchproducts.com",
            first_name="sales",
            last_name="user",
        )
        self.estimator_user=get_user_model().objects.create(
            username="estimatoruser",
            email="estimatoruser@tougshire.com",
            first_name="estimator",
            last_name="user",
        )

    def test_salespermissions_added(self):

        salesperson=Salesperson.objects.create(
            user=self.sales_user,
        )
        self.assertIn(Group.objects.get(name='Esteem_Salespeople'), salesperson.user.groups.all())

        estimator=Estimator.objects.create(
            user=self.sales_user,
        )
        self.assertIn(Group.objects.get(name='Esteem_Estimators'), estimator.user.groups.all())
