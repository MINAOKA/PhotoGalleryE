from django.contrib import admin
# CustimUserをインポート
from .models import CustomUser
class CustomUserAdmin(admin.ModelAdmin):
    '''
    管理ページのレコード一覧に表示するカラムを設定するクラス
    
    '''
    # レコード一覧にidとusernameを表示
    list_display = ('id','username')
    # 表示するカラムにリンクを設定
    list_display_links = ('id','username')

# django管理サイトにCustomerUser、CustomUserAdminを登録する
admin.site.register(CustomUser, CustomUserAdmin)

# Register your models here.
