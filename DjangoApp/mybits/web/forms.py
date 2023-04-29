from django import ModelForm, Textarea, TextInput
from .models import Restaurant

class RestaurantForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        visible = self.visible_fields()
        for form in visible:
            form.field.widget.attrs['class'] = 'form-control'
            form.field.widget.attrs['autocomplete'] = 'off'
    class Meta:
        model = Restaurant
        fields = ['name', 'id_restaurant', 'phone', 'email', 'website', 'menu_pdf', 'id_localization']
