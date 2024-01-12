from django.urls import path
from Frontend import views

urlpatterns = [path('homePage/',views.homePage,name="homePage"),
               path('productsPage/',views.productsPage,name="productsPage"),
               path('single_product/<int:proid>/',views.single_product,name="single_product"),
               path('productFiltered/<cat_name>/',views.productFiltered,name="productFiltered"),
               path('aboutPage/',views.aboutPage,name="aboutPage"),
               path('contactPage/',views.contactPage,name="contactPage"),
               path('servicePage/',views.servicePage,name="servicePage"),
               path('saveContactPage/',views.saveContactPage,name="saveContactPage"),
               path('signUpPage/',views.signUpPage,name="signUpPage"),
               path('saveSignup/',views.saveSignup,name="saveSignup"),
               path("",views.UserLogin,name="UserLogin"),
               path('UserLogout/',views.UserLogout,name="UserLogout"),
               path('cartPage/',views.cartPage,name="cartPage"),
               path('saveCartPage/',views.saveCartPage,name="saveCartPage"),
               path('removeItem/<int:dataid>/',views.removeItem,name="removeItem"),
               path('checkout/',views.checkout,name="checkout"),
               path('saveOrder/',views.saveOrder,name="saveOrder"),
               ]