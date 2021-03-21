from django import forms
from django.forms import ModelChoiceField
from sql.commands import get_all_commands_with_id


class AddCommand(forms.Form):
    command = forms.CharField(label="Command", max_length=20, widget=forms.TextInput(attrs={"placeholder": "Command", "class": "form-control"}))
    parameters = forms.CharField(label="Parameters", max_length=40, widget=forms.TextInput(attrs={"placeholder": "(*required) (parameter)", "class": "form-control"}))
    description = forms.CharField(label="Description", max_length=250, widget=forms.TextInput(attrs={"placeholder": "Info about the command", "class": "form-control"}))
    category = forms.CharField(label="Category", max_length=20, widget=forms.TextInput(attrs={"placeholder": "Enter category or category id", "class": "form-control"}))


class AddAdminCommand(forms.Form):
    command = forms.CharField(label="Command", max_length=20, widget=forms.TextInput(attrs={"placeholder": "Command", "class": "form-control"}))
    parameters = forms.CharField(label="Parameters", max_length=40, widget=forms.TextInput(attrs={"placeholder": "(*required) (parameter)", "class": "form-control"}))
    description = forms.CharField(label="Description", max_length=250, widget=forms.TextInput(attrs={"placeholder": "Info about the command", "class": "form-control"}))


class DeleteCommand(forms.Form):
    # command = forms.CharField(label="Command", max_length=20, widget=forms.TextInput(attrs={"placeholder": "Command", "class": "form-control"}))
    Commands = get_all_commands_with_id()
    select_command = forms.ChoiceField(choices=Commands, label="Command", widget=forms.Select(attrs={"class": "form-control"}))


class DeleteAdminCommand(forms.Form):
    command = forms.CharField(label="Command", max_length=20, widget=forms.TextInput(attrs={"placeholder": "Command", "class": "form-control"}))
