import asyncio
import contextlib
import os
import sys
import telethon
from telethon import events
import heroku3
import urllib3
from git import Repo
from git.exc import GitCommandError, InvalidGitRepositoryError, NoSuchPathError
from config import *
plugin_category = "tools"
#ENV = bool(os.environ.get("ENV", False))
# -- Constants -- #
Heroku = heroku3.from_key(HEROKU_API_KEY)
heroku_api = "https://api.heroku.com"
upstream_repo_url = 'https://github.com/perdark/per-sed'
upstream_repo_branch = 'https://github.com/perdark/per-sed'

REPO_REMOTE_NAME = "temponame"
IFFUCI_ACTIVE_BRANCH_NAME = "master"
NO_HEROKU_APP_CFGD = "no heroku application found, but a key given? 😕 "
HEROKU_GIT_REF_SPEC = "HEAD:refs/heads/master"
RESTARTING_APP = "re-starting heroku application"
IS_SELECTED_DIFFERENT_BRANCH = (
    "looks like a custom branch {branch_name} "
    "is being used:\n"
    "in this case, Updater is unable to identify the branch to be updated."
    "please check out to an official branch, and re-start the updater."
)


# -- Constants End -- #

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

requirements_path = os.path.join(
    os.path.dirname(os.path.dirname(
        os.path.dirname(__file__))), "requirements.txt"
)


async def gen_chlog(repo, diff):
    d_form = "%d/%m/%y"
    return "".join(
        f"  • {c.summary} ({c.committed_datetime.strftime(d_form)}) <{c.author}>\n"
        for c in repo.iter_commits(diff)
    )


async def print_changelogs(event, ac_br, changelog):
    changelog_str = (
        f"**New UPDATE available for [{ac_br}]:\n\nCHANGELOG:**\n`{changelog}`"
    )
    if len(changelog_str) > 4096:
        await event.edit("`Changelog is too big, view the file to see it.`")
        with open("output.txt", "w+") as file:
            file.write(changelog_str)
        await event.client.send_file(
            event.chat_id,
            "output.txt",
            reply_to=event.id,
        )
        os.remove("output.txt")
    else:
        await event.client.send_message(
            event.chat_id,
            changelog_str,
            reply_to=event.id,
        )
    return True


async def update_requirements():
    reqs = str(requirements_path)
    try:
        process = await asyncio.create_subprocess_shell(
            " ".join([sys.executable, "-m", "pip", "install", "-r", reqs]),
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE,
        )
        await process.communicate()
        return process.returncode
    except Exception as e:
        return repr(e)


async def update_bot(event, repo, ups_rem, ac_br):
    try:
        ups_rem.pull(ac_br)
    except GitCommandError:
        repo.git.reset("--hard", "FETCH_HEAD")
    await update_requirements()
    sandy = await event.edit(
        "`Successfully Updated!\n" "Bot is restarting... Wait for a minute!`"
    )
    await event.client.reload(sandy)


@sedthon.on(events.NewMessage(outgoing=True, pattern=r"\.تحديث"))
async def upstream(event):
    event = await event.edit("⌔∮ يتم البحث على التحديثات ام وجدت")
    off_repo = upstream_repo_url
    force_update = False
    txt = (
        "**⌔∮ عذرا لم يتم اكمال التحديث بسبب بعض الاخطاء "
        + "**اللوگ:**\n"
    )

    repo = Repo(upstream_repo_branch, search_parent_directories=True)
    origin = repo.create_remote("upstream", off_repo)
    origin.fetch()
    force_update = True
    repo.create_head("master", origin.refs.master)
    repo.heads.master.set_tracking_branch(origin.refs.master)
    repo.heads.master.checkout(True)
    ac_br = repo.active_branch.name
    with contextlib.suppress(BaseException):
        repo.create_remote("upstream", off_repo)
    ups_rem = repo.remote("upstream")
    ups_rem.fetch(ac_br)
    changelog = await gen_chlog(repo, f"HEAD..upstream/{ac_br}")
    #
    if changelog == "" and not force_update:
        await event.edit(
            "\n⌔∮ عزيز المستخدم انت تستخدم اخر اصدار من جمثون 🫂♥"
        )
        return repo.__del__()

    await event.edit("⌔∮ جارِ تحديث جمثون يرجى الأنتظار قليلا")
    await update_bot(event, repo, ups_rem, ac_br)
    return
