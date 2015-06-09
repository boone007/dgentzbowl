from django import forms

from.models import Player, BowlGame


class BowlGameForm(forms.ModelForm):
    class Meta:
        model = BowlGame
        fields = ['bowl', 'fav', 'dog', 'spread', 'hilo']



class PlayerForm(forms.ModelForm):
    class Meta:
        model = Player
        fields = ['name', 'username', 'email']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        return email


