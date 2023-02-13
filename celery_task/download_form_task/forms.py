from django import forms

class DownloadForm(forms.Form):
    options = [
        ('AWS', 'AWS'),
        ('GCP', 'GCP'),
        ('AZURE', 'AZURE'),
    ]

    drop_down = forms.ChoiceField(choices=options)
    url = forms.URLField(help_text="Enter a link...")
    