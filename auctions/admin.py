from django.contrib import admin

from .models import AuctionList, User, Category, Bid, Comment

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name",)

class ListingsAdmin(admin.ModelAdmin):
    list_display = ("title", "image", "owner", "starting_bid", "is_active", "category", "date_posted")
    list_filter = ("is_active", "category")
    search_fields = ("title", "description")

class BidsAdmin(admin.ModelAdmin):
    list_display = ("bidder", "listing", "bid_amount", "timestamp")
    list_filter = ("listing",)

class CommentsAdmin(admin.ModelAdmin):
    list_display = ("commenter", "comment_text", "listing")
    search_fields = ("comment_text",)

class UserAdmin(admin.ModelAdmin):
    list_display = ("username", "email", "is_staff", "is_superuser")

admin.site.register(User, UserAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(AuctionList, ListingsAdmin)
admin.site.register(Bid, BidsAdmin)
admin.site.register(Comment, CommentsAdmin)