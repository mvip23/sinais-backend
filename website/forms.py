from django import forms
from .models import Contato, Lead

class ContatoForm(forms.ModelForm):
    """Formulário de contato"""
    class Meta:
        model = Contato
        fields = ['nome', 'email', 'telefone', 'empresa', 'assunto', 'mensagem']
        widgets = {
            'nome': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Seu nome completo'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'seu@email.com'
            }),
            'telefone': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': '(11) 99999-9999'
            }),
            'empresa': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Nome da sua empresa'
            }),
            'assunto': forms.Select(attrs={
                'class': 'form-select'
            }),
            'mensagem': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 5,
                'placeholder': 'Digite sua mensagem...'
            }),
        }

class LeadForm(forms.ModelForm):
    """Formulário para captura de leads"""
    class Meta:
        model = Lead
        fields = ['email', 'nome', 'empresa', 'telefone']
        widgets = {
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Seu melhor email'
            }),
            'nome': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Seu nome'
            }),
            'empresa': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Nome da empresa'
            }),
            'telefone': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Telefone'
            }),
        }

class DemoForm(forms.Form):
    """Formulário para agendar demonstração"""
    nome = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Seu nome completo'
        })
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'seu@email.com'
        })
    )
    empresa = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Nome da empresa'
        })
    )
    telefone = forms.CharField(
        max_length=20,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': '(11) 99999-9999'
        })
    )
    funcionarios = forms.ChoiceField(
        choices=[
            ('1-10', '1-10 funcionários'),
            ('11-50', '11-50 funcionários'),
            ('51-200', '51-200 funcionários'),
            ('200+', 'Mais de 200 funcionários'),
        ],
        widget=forms.Select(attrs={
            'class': 'form-select'
        })
    )
    data_demo = forms.DateField(
        widget=forms.DateInput(attrs={
            'class': 'form-control',
            'type': 'date'
        })
    )
    horario = forms.ChoiceField(
        choices=[
            ('09:00', '09:00'),
            ('10:00', '10:00'),
            ('11:00', '11:00'),
            ('14:00', '14:00'),
            ('15:00', '15:00'),
            ('16:00', '16:00'),
        ],
        widget=forms.Select(attrs={
            'class': 'form-select'
        })
    )
    observacoes = forms.CharField(
        required=False,
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'rows': 3,
            'placeholder': 'Alguma observação ou necessidade específica?'
        })
    ) 