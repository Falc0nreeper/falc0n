from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import Category, Genre, Movie, MovieShots, Actor, Rating, RatingStar, Reviews
# Register your models here.
from django.contrib.gis import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget



class MovieAdminForm(forms.ModelForm):
    description = forms.CharField(label='Tavfsifi', widget=CKEditorUploadingWidget())
    class Meta:
        model = Movie
        fields = '__all__'


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "url")
    list_display_links = ("name", "id")

class ReviewInline(admin.TabularInline):
	model = Reviews
	extra = 1
	readonly_fields = ("name" , "email")

class MovieShotsInline(admin.TabularInline):
	model = MovieShots
	extra = 1

	readonly_fields = ("get_image",)

	def get_image(self, obj):
		return mark_safe(f'<img src={obj.image.url} width="100" height="60"')

	get_image.short_description = "Rasm"

@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
	list_display = ("title", "category", "url", "draft")
	list_filter = ("category", "years")
	search_fields = ("title", "category__name")
	inlines = [MovieShotsInline, ReviewInline]
	save_on_top = True
	save_as = True
	list_editable = ("draft",)
	actions = ["publish", "unpublish"]
	form = MovieAdminForm
	readonly_fields = ("get_image",)
	fieldsets = (
		(None, {
			"fields": (("title", "tagline"), )
		}),

		(None, {
			"fields": (("description", ("poster", "get_image"),))
		}),

		(None, {
			"fields": (("years", "world_premiere", "country"), )
		}),

		("Aktyorlar", {
			"classes": ("collapse",),
			"fields": (("actors", "directors", "genres", "category"), )
		}),

		(None, {
			"fields": (("budget", "fees_in_usa", "fees_in_world"), )
		}),
		("Optsiyalar", {
			"fields": (("url", "draft"), )
		}),
	)

	def get_image(self, obj):
		return mark_safe(f'<img src={obj.poster.url} width="100" height="100"')


	def unpublish(self, request, queryset):
		"""Publikatsiyadan olib tashlash"""
		row_update = queryset.update(draft=True)
		if row_update == 1:
			message_bit = "1 Yangilandi"
		else:
			message_bit = f"{row_update} Postlar Yangilandi"
		self.message_user(request, f"{message_bit}")


	def publish(self, request, queryset):
		"""Publikatsiya qilish"""
		row_update = queryset.update(draft=False)
		if row_update == 1:
			message_bit = "1 Yangilandi"
		else:
			message_bit = f"{row_update} Postlar Yangilandi"
		self.message_user(request, f"{message_bit}")

	publish.short_description = "Publikatsiya qilish"
	publish.allowed_permissions = ('change', )

	unpublish.short_description = "Publikatsiya olib tashlash"
	unpublish.allowed_permissions = ('change', )




	get_image.short_description = "Rasm"

@admin.register(Reviews)
class ReviewAdmin(admin.ModelAdmin):
	list_display = ("name", "email", "parent", "movie", "id")
	readonly_fields = ("name", "email")


@admin.register(Genre)
class GengreAdmin(admin.ModelAdmin):
	list_display = ("name", "url")


@admin.register(Actor)
class ActorAdmin(admin.ModelAdmin):

	list_display = ("name", "age", "get_image")
	readonly_fields = ("get_image",)

	def get_image(self, obj):
		return mark_safe(f'<img src={obj.image.url} width="60" height="60"')

	get_image.short_description = "Rasm"




@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):

	list_display = ("name", "ip")


@admin.register(MovieShots)
class MovieShotsAdmin(admin.ModelAdmin):

	list_display = ("title", "movie", "get_image")
	readonly_fields = ("get_image",)

	def get_image(self, obj):
		return mark_safe(f'<img src={obj.image.url} width="130" height="80"')

	get_image.short_description = "Rasm"

admin.site.register(RatingStar)

admin.site.site_title = "CreateXup Movies"
admin.site.site_header = "CreateXup Movies"