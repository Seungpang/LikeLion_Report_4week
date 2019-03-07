from django import forms 

class TodoForm(forms.Form):
    text = forms.CharField(max_length=40, 
        widget=forms.TextInput(
            attrs={'class' : 'form-control', 'placeholder' : 'todo 리스트를 적으세요', 'aria-label' : 'Todo', 'aria-describedby' : 'add-btn'}))