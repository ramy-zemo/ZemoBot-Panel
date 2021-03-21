from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from commands.forms import AddCommand, AddAdminCommand, DeleteCommand, DeleteAdminCommand
from django.contrib import messages
from sql.commands import create_command, delete_command
from sql.admin_commands import create_admin_command, delete_admin_command


# Create your views here.
@login_required(login_url='/login', redirect_field_name="")
def commands_view(request, *args, **kwargs):
    ctx = {'form_add_command': AddCommand(),
           'form_add_admin_command': AddAdminCommand(),
           'form_delete_command': DeleteCommand(),
           'form_delete_admin_command': DeleteAdminCommand()}

    return render(request, "commands.html", ctx)


def add_command_view(request, *args, **kwargs):
    if request.method == 'POST':
        form = AddCommand(request.POST)
        if form.is_valid():
            messages.success(request, "Command added successfully.", extra_tags="add_command")
            command_creation = create_command(form.cleaned_data["category"], form.cleaned_data["command"], form.cleaned_data["parameters"], form.cleaned_data["description"])

            if command_creation:
                messages.error(message=command_creation, extra_tags="add_command")
        else:
            messages.error(message="Invalid Input.", extra_tags="add_command")
    else:
        return redirect("/400")

    return redirect("/commands")


def delete_command_view(request, *args, **kwargs):
    if request.method == 'POST':
        form = DeleteCommand(request.POST)
        if form.is_valid():
            messages.success(request, "Command deleted successfully.", extra_tags="delete_command")
            command_creation = delete_command(form.cleaned_data["select_command"])
            if command_creation:
                messages.error(request=request, message=command_creation, extra_tags="delete_command")
        else:
            messages.error(request=request, message="Invalid Input.", extra_tags="delete_command")

    else:
        return redirect("/400")

    return redirect("/commands")


def add_admin_command_view(request, *args, **kwargs):
    if request.method == 'POST':
        form = AddAdminCommand(request.POST)
        if form.is_valid():
            messages.success(request, "Admin command added successfully.", extra_tags="add_admin_command")
            command_creation = create_admin_command(form.cleaned_data["command"], form.cleaned_data["parameters"], form.cleaned_data["description"])

            if command_creation:
                messages.error(request=request, message=command_creation, extra_tags="add_admin_command")
        else:
            messages.error(request=request, message="Invalid Input.", extra_tags="add_admin_command")
    else:
        return redirect("/400")

    return redirect("/commands")


def delete_admin_command_view(request, *args, **kwargs):
    if request.method == 'POST':
        form = DeleteAdminCommand(request.POST)
        if form.is_valid():
            messages.success(request, "Command deleted successfully.", extra_tags="delete_admin_command")
            command_creation = delete_admin_command(form.cleaned_data["command"])

            if command_creation:
                messages.error(request, message=command_creation, extra_tags="delete_admin_command")
        else:
            messages.error(request, message="Invalid Input.", extra_tags="delete_admin_command")

    else:
        return redirect("/400")

    return redirect("/commands")
