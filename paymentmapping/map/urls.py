from django.urls import path
from .views import upload_csv,get_column_names,get_mapping_data,post_mapping_data,edit_CompanyOnboardingPaymentDetail,edit_SubCompanyOnboardingPaymentDetail,edit_VendorOnboardingPaymentDetail,delete_CompanyOnboardingPaymentDetail,delete_SubCompanyOnboardingPaymentDetail,delete_VendorOnboardingPaymentDetail,get_company_onboarding_details,get_sub_company_onboarding_details,get_vendor_onboarding_details,edit_banOnboardingPaymentDetails,delete_banOnboardingPaymentDetails,get_ban_onboarding_payment_details
urlpatterns = [
    path('post_mapping_data', post_mapping_data.as_view()),
    path('view_mapping_data', get_mapping_data.as_view()),
    path('upload_csv', upload_csv),
    path('get_columns', get_column_names.as_view()),
    path('edit_company_data/<int:id>', edit_CompanyOnboardingPaymentDetail.as_view()),
    path('edit_sub_company_data/<int:id>', edit_SubCompanyOnboardingPaymentDetail.as_view()),
    path('edit_vendor_data/<int:id>', edit_VendorOnboardingPaymentDetail.as_view()),
    path('edit_ban_details/<int:id>',edit_banOnboardingPaymentDetails.as_view()),
    path('delete_company_data/<int:id>', delete_CompanyOnboardingPaymentDetail.as_view()),
    path('delete_sub_company_data/<int:id>', delete_SubCompanyOnboardingPaymentDetail.as_view()),
    path('delete_vendor_data/<int:id>', delete_VendorOnboardingPaymentDetail.as_view()),
    path('delete_ban_details/<int:id>',delete_banOnboardingPaymentDetails.as_view()),
    path('get_company_data', get_company_onboarding_details.as_view()),
    path('get_sub_company_data', get_sub_company_onboarding_details.as_view()),
    path('get_vendor_data', get_vendor_onboarding_details.as_view()),
    path('get_ban_details',delete_banOnboardingPaymentDetails.as_view())
]