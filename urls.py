from django.urls import path
from .views import AssignmentCreate, AssignmentDelete, AssignmentDetail, AssignmentList, AssignmentUpdate, CustomerCreate, CustomerDelete, CustomerDetail, CustomerList, CustomerUpdate, CustomerPopup, CustomerPopupSuccess, OptionDoorBrandCreate, OptionDoorBrandDelete, OptionDoorBrandDetail, OptionDoorBrandList, OptionDoorBrandUpdate, EstisheetDoorCreate, EstisheetDoorDelete, EstisheetDoorDetail, EstisheetDoorList, EstisheetDoorUpdate, ProposalCreate, ProposalDelete, ProposalDetail, ProposalList, ProposalEstirequestCreate, ProposalUpdate, EstimatorCreate, EstimatorDelete, EstimatorDetail, EstimatorList, EstimatorUpdate, EstisheetMarvinDoorCreate, EstisheetMarvinDoorDelete, EstisheetMarvinDoorDetail, EstisheetMarvinDoorList, EstisheetMarvinDoorUpdate, EstirequestCreate, EstirequestDelete, EstirequestDetail, EstirequestDocumentCreate, EstirequestDocumentDelete, EstirequestDocumentDetail, EstirequestDocumentList, EstirequestDocumentUpdate, EstirequestList, EstirequestUpdate, SalespersonCreate, SalespersonDelete, SalespersonDetail, SalespersonList, SalespersonUpdate, OptionWindowBrandCreate, OptionWindowBrandDelete, OptionWindowBrandDetail, OptionWindowBrandList, OptionWindowBrandUpdate, EstisheetWindowCreate, EstisheetWindowDelete, EstisheetWindowDetail, EstisheetWindowList, EstisheetWindowUpdate, EstisheetICFCreate, EstisheetICFDelete, EstisheetICFDetail, EstisheetICFList, EstisheetICFUpdate 

urlpatterns = [
    path ('', EstirequestList.as_view(), name='esteem'),

    path ('assignment/create/', AssignmentCreate.as_view(), name='assignment_create'),
    path ('assignment/update/<int:pk>/', AssignmentUpdate.as_view(), name='assignment_update'),
    path ('assignment/detail/<int:pk>/', AssignmentDetail.as_view(), name='assignment_detail'),
    path ('assignment/delete/<int:pk>/', AssignmentDelete.as_view(), name='assignment_delete'),
    path ('assignment/list/', AssignmentList.as_view(), name='assignment_list'),

    path ('customer/create/', CustomerCreate.as_view(), name='customer_create'),
    path ('customer/update/<int:pk>/', CustomerUpdate.as_view(), name='customer_update'),
    path ('customer/detail/<int:pk>/', CustomerDetail.as_view(), name='customer_detail'),
    path ('customer/delete/<int:pk>/', CustomerDelete.as_view(), name='customer_delete'),
    path ('customer/list/', CustomerList.as_view(), name='customer_list'),
    path ('customer/popup/', CustomerPopup.as_view(), name='customer_popup'),
    path ('customer/popup/<int:pk>?refresh=<str:refresh>/', CustomerPopupSuccess.as_view(), name='customer_popupsuccess'),

    path ('proposal/create/', ProposalCreate.as_view(), name='proposal_create'),
    path ('proposal/create/estirequest/<int:estirequest_pk>', ProposalCreate.as_view(), name='proposal_create'),
    path ('proposal/create/estirequest/<int:estirequest_pk>/<component>', ProposalCreate.as_view(), name='proposal_create'),
    path ('proposal/update/<int:pk>/', ProposalUpdate.as_view(), name='proposal_update'),
    path ('proposal/detail/<int:pk>/', ProposalDetail.as_view(), name='proposal_detail'),
    path ('proposal/delete/<int:pk>/', ProposalDelete.as_view(), name='proposal_delete'),
    path ('proposal/list/', ProposalList.as_view(), name='proposal_list'),

    path ('proposal_estirequest/<int:estirequest>/', ProposalCreate.as_view(), name='proposal_estirequest_estirequest'),

    path ('estirequestdocument/create/', EstirequestDocumentCreate.as_view(), name='estirequestdocument_create'),
    path ('estirequestdocument/update/<int:pk>/', EstirequestDocumentUpdate.as_view(), name='estirequestdocument_update'),
    path ('estirequestdocument/detail/<int:pk>/', EstirequestDocumentDetail.as_view(), name='estirequestdocument_detail'),
    path ('estirequestdocument/delete/<int:pk>/', EstirequestDocumentDelete.as_view(), name='estirequestdocument_delete'),
    path ('estirequestdocument/list/', EstirequestDocumentList.as_view(), name='estirequestdocument_list'),

    path ('optiondoorbrand/create/', OptionDoorBrandCreate.as_view(), name='optiondoorbrand_create'),
    path ('optiondoorbrand/update/<int:pk>/', OptionDoorBrandUpdate.as_view(), name='optiondoorbrand_update'),
    path ('optiondoorbrand/detail/<int:pk>/', OptionDoorBrandDetail.as_view(), name='optiondoorbrand_detail'),
    path ('optiondoorbrand/delete/<int:pk>/', OptionDoorBrandDelete.as_view(), name='optiondoorbrand_delete'),
    path ('optiondoorbrand/list/', OptionDoorBrandList.as_view(), name='optiondoorbrand_list'),

    path ('estisheetdoor/create/', EstisheetDoorCreate.as_view(), name='estisheetdoor_create'),
    path ('estisheetdoor/update/<int:pk>/', EstisheetDoorUpdate.as_view(), name='estisheetdoor_update'),
    path ('estisheetdoor/detail/<int:pk>/', EstisheetDoorDetail.as_view(), name='estisheetdoor_detail'),
    path ('estisheetdoor/delete/<int:pk>/', EstisheetDoorDelete.as_view(), name='estisheetdoor_delete'),
    path ('estisheetdoor/list/', EstisheetDoorList.as_view(), name='estisheetdoor_list'),


    path ('estisheeticf/create/', EstisheetICFCreate.as_view(), name='estisheeticf_create'),
    path ('estisheeticf/update/<int:pk>/', EstisheetICFUpdate.as_view(), name='estisheeticf_update'),
    path ('estisheeticf/detail/<int:pk>/', EstisheetICFDetail.as_view(), name='estisheeticf_detail'),
    path ('estisheeticf/delete/<int:pk>/', EstisheetICFDelete.as_view(), name='estisheeticf_delete'),
    path ('estisheeticf/list/', EstisheetICFList.as_view(), name='estisheeticf_list'),

    path ('estimator/create/', EstimatorCreate.as_view(), name='estimator_create'),
    path ('estimator/update/<int:pk>/', EstimatorUpdate.as_view(), name='estimator_update'),
    path ('estimator/detail/<int:pk>/', EstimatorDetail.as_view(), name='estimator_detail'),
    path ('estimator/delete/<int:pk>/', EstimatorDelete.as_view(), name='estimator_delete'),
    path ('estimator/list/', EstimatorList.as_view(), name='estimator_list'),
    path ('estisheetmarvindoor/create/', EstisheetMarvinDoorCreate.as_view(), name='estisheetmarvindoor_create'),
    path ('estisheetmarvindoor/update/<int:pk>/', EstisheetMarvinDoorUpdate.as_view(), name='estisheetmarvindoor_update'),
    path ('estisheetmarvindoor/detail/<int:pk>/', EstisheetMarvinDoorDetail.as_view(), name='estisheetmarvindoor_detail'),
    path ('estisheetmarvindoor/delete/<int:pk>/', EstisheetMarvinDoorDelete.as_view(), name='estisheetmarvindoor_delete'),
    path ('estisheetmarvindoor/list/', EstisheetMarvinDoorList.as_view(), name='estisheetmarvindoor_list'),
    path ('estirequest/create/', EstirequestCreate.as_view(), name='estirequest_create'),
    path ('estirequest/update/<int:pk>/', EstirequestUpdate.as_view(), name='estirequest_update'),
    path ('estirequest/update/<int:pk>/page/<str:at_page>/', EstirequestUpdate.as_view(), name='estirequest_update' ),
    path ('estirequest/detail/<int:pk>/', EstirequestDetail.as_view(), name='estirequest_detail'),
    path ('estirequest/delete/<int:pk>/', EstirequestDelete.as_view(), name='estirequest_delete'),
    path ('estirequest/list/', EstirequestList.as_view(), name='estirequest_list'),
    path ('salesperson/create/', SalespersonCreate.as_view(), name='salesperson_create'),
    path ('salesperson/update/<int:pk>/', SalespersonUpdate.as_view(), name='salesperson_update'),
    path ('salesperson/detail/<int:pk>/', SalespersonDetail.as_view(), name='salesperson_detail'),
    path ('salesperson/delete/<int:pk>/', SalespersonDelete.as_view(), name='salesperson_delete'),
    path ('salesperson/list/', SalespersonList.as_view(), name='salesperson_list'),
    path ('optionwindowbrand/create/', OptionWindowBrandCreate.as_view(), name='optionwindowbrand_create'),
    path ('optionwindowbrand/update/<int:pk>/', OptionWindowBrandUpdate.as_view(), name='optionwindowbrand_update'),
    path ('optionwindowbrand/detail/<int:pk>/', OptionWindowBrandDetail.as_view(), name='optionwindowbrand_detail'),
    path ('optionwindowbrand/delete/<int:pk>/', OptionWindowBrandDelete.as_view(), name='optionwindowbrand_delete'),
    path ('optionwindowbrand/list/', OptionWindowBrandList.as_view(), name='optionwindowbrand_list'),
    path ('estisheetwindow/create/', EstisheetWindowCreate.as_view(), name='estisheetwindow_create'),
    path ('estisheetwindow/update/<int:pk>/', EstisheetWindowUpdate.as_view(), name='estisheetwindow_update'),
    path ('estisheetwindow/detail/<int:pk>/', EstisheetWindowDetail.as_view(), name='estisheetwindow_detail'),
    path ('estisheetwindow/delete/<int:pk>/', EstisheetWindowDelete.as_view(), name='estisheetwindow_delete'),
    path ('estisheetwindow/list/', EstisheetWindowList.as_view(), name='estisheetwindow_list'),
]
