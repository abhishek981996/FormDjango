# make sure this is at the top if it isn't already
from django import forms
from Djangoproject.settings import DATE_INPUT_FORMATS

# our new form
class ContactForm(forms.Form):
    contact_name = forms.CharField(required=True)
    contact_email = forms.EmailField(required=True)
    content = forms.CharField(
        required=True,
        widget=forms.Textarea
    )
    date_of_birth = forms.DateField(input_formats=DATE_INPUT_FORMATS,required=True)

    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        self.fields['contact_name'].label = "Your name:"
        self.fields['contact_email'].label = "Your email:"
        self.fields['content'].label ="What do you want to say?"
        self.fields['date_of_birth'].label= 'Whats your birth day?'