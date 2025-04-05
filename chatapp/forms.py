# from django import forms

# class ChatForm(forms.Form):
#     message = forms.CharField(label='', widget=forms.TextInput(attrs={
#         'placeholder': 'Ask something...',
#         'class': 'chat-input'
#     }))


from django import forms

class ChatForm(forms.Form):
    message = forms.CharField(
        label='',
        widget=forms.Textarea(attrs={
            'rows': 2,
            'placeholder': 'Type your message here...',
        })
    )
