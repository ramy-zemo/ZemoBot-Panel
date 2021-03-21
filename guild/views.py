from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from sql.guild import get_all_guild_ids, get_active_guild_ids
from sql.commands import get_all_commands, get_categories_with_command_count
from sql.level import get_top_user_ranking


# Create your views here.
@login_required(login_url='/login', redirect_field_name="")
def guild_view(request, *args, **kwargs):
    ctx = {"user_ranking": [(1, 2, 3), (2, 3, 4)]}
    return render(request, "guild.html", ctx)


@login_required(login_url='/login', redirect_field_name="")
def home_view(request, *args, **kwargs):
    context_object_name = "context"

    ctx = {"all_servers": len(get_all_guild_ids()),
           "active_servers": len(get_active_guild_ids()),
           "commands": len(get_all_commands()),
           "user_ranking": get_top_user_ranking()}

    category_data = get_categories_with_command_count()
    ranking_data = get_top_user_ranking()

    ctx["ranking_data"] = ranking_data
    for category in category_data:
        ctx[category] = category_data[category]

    return render(request, "home.html", ctx)
