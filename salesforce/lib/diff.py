import sublime, sublime_plugin
import difflib
import time
import datetime
import codecs
import os

def diff_changes(file_name, result):
    try:
        if "Body" in result:
            server = result["Body"].splitlines()
        elif "Markup" in result:
            server = result["Markup"].splitlines()

        local = codecs.open(file_name, "r", "utf-8").read().splitlines()
    except UnicodeDecodeError:
        show_diff_panel("Diff only works with UTF-8 files")
        return

    time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))
    bdate_literal = result["LastModifiedDate"].split(".")[0]
    server_date = datetime.datetime.strptime(bdate_literal, "%Y-%m-%dT%H:%M:%S")
    local_date = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))

    diff = difflib.unified_diff(server, local, "Server", "Local ", server_date, local_date, lineterm='')
    difftxt = u"\n".join(line for line in diff)

    if difftxt == "":
        show_diff_panel("There is no difference between %s and server" % os.path.basename(file_name))
        return

    show_diff_panel(difftxt)

def show_diff_panel(difftxt):
    win = sublime.active_window()
    v = win.create_output_panel('diff_with_server')
    v.assign_syntax('Packages/Diff/Diff.tmLanguage')

    v.run_command('append', {'characters': difftxt})
    win.run_command("show_panel", {"panel": "output.diff_with_server"})
