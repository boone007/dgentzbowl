from django.contrib import admin

# Register your models here.
from .models import BowlGame, Player
from .forms import PlayerForm


class PlayerAdmin(admin.ModelAdmin):
    list_display = ["__unicode__", "timestamp"]
    form = PlayerForm
    #class Meta:
    #    model = Player

admin.site.register(BowlGame)
admin.site.register(Player, PlayerAdmin)