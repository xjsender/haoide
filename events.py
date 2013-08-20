import sublime
import sublime_plugin
import os
import time

try:
    from . import context
    from .salesforce import util
except:
    import context
    from salesforce import util

class BackupAfterSave(sublime_plugin.EventListener):
    """
    Every time when you save your ApexPage, ApexTrigger, ApexClass, ApexComponent, 
    this class will make a copy with the time_stamp in the history path of current project
    """

    def on_post_save(self, view):
        # Get current file name and Read file content
        file_name = view.file_name()
        try:
            body = open(file_name, encoding="utf-8").read()
        except:
            body = open(file_name, "rb").read()

        # Get component_name amd component_type
        component_name = util.get_component_name(file_name)
        component_type = util.get_component_type(file_name)

        # If this file is not ApexTrigger, ApexComponent, 
        # ApexPage or ApexClass, just return
        if component_type not in ["ApexClass", "ApexPage", "ApexComponent", "ApexTrigger", "StaticResource"]:
            return

        # Get toolingapi settings
        toolingapi_settings = context.get_toolingapi_settings()

        # Get component extension
        component_extension = toolingapi_settings[component_type]["extension"]

        # Get Workspace, if not exist, make it
        workspace = toolingapi_settings["workspace"] + "/history/" + component_type
        if not os.path.exists(workspace):
            os.makedirs(workspace)

        # Backup current file
        time_stamp = time.strftime("%Y-%m-%d-%H-%M", time.localtime())
        fp = open(workspace + "/" + component_name + "-" +\
            time_stamp + component_extension, "w")

        fp.write(body)
        fp.close()
