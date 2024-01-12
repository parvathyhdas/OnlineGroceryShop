from django.urls import path
from GroceryApp import views

urlpatterns = [path('index/',views.index,name="index"),
                path('categoryPage/',views.categoryPage,name="categoryPage"),
                path('saveCategory/',views.saveCategory,name="saveCategory"),
                path('displayCategories/',views.displayCategories,name="displayCategories"),
                path('editcategory/<int:dataid>/',views.editcategory,name="editcategory"),
                path('updateCategory/<int:dataid>/',views.updateCategory,name="updateCategory"),
                path('deleteCategory/<int:dataid>/',views.deleteCategory,name="deleteCategory"),
                path('addProduct/',views.addProduct,name="addProduct"),
                path('saveProduct/',views.saveProduct,name="saveProduct"),
                path('displayproduct/',views.displayproduct,name="displayproduct"),
                path('editProduct/<int:dataid>/',views.editProduct,name="editProduct"),
                path('updateProduct/<int:dataid>/',views.updateProduct,name="updateProduct"),
                path('deleteProduct/<int:dataid>/',views.deleteProduct,name="deleteProduct"),
                path('adminlogin/',views.adminlogin,name="adminlogin"),
                path('adminLoginPage/',views.adminLoginPage,name="adminLoginPage"),
                path('admin_logout/',views.admin_logout,name="admin_logout"),
                path('displayContact/',views.displayContact,name="displayContact"),
                path('deleteContact/<int:dataid>/',views.deleteContact,name="deleteContact"),
               ]