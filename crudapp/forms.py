
from django import forms
from . models import Tanishq

class TanishqForm(forms.ModelForm):
    class Meta:
        model=Tanishq
        fields='__all__'

        labels={
            "cid":'Customer ID',
            'name':'Customer Name',
            'choice':'Choice',
            'paymentMode':'Payment Method',
            'image':'Product Image',
            'date':'Purchase Date',
            'email':'Email ID',
        }

        widgets={
            'date':forms.DateInput(
                attrs={
                    'type':'date'
                }
            )
        }