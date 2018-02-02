'''
author: huangxy
homepage: http://salesforcexytools.com
linence: 
'''
import base64
import sublime
import os
import sys
import threading
from .. import util
from .. import context
import time
from .cherrypy import wsgiserver
from . import bottle
# bottle.debug(True)
from .bottle import Bottle, ServerAdapter
from .bottle import static_file, request, template
# Create a new app stack
app = Bottle()

close_window_script = """
    function close_window() {
        var userAgent = navigator.userAgent;
        if (userAgent.indexOf("Firefox") != -1
                || userAgent.indexOf("Chrome") != -1) {
            window.location.href = "about:blank";
        } else {
            window.opener = null;
            window.open("", "_self");
            window.close();
        }
    }
    window.setTimeout(close_window, 5000);
"""

@app.route('/auth/callback', method=['GET', 'POST'])
def do_callback():
    html = '''
        <html>
            <head>
                <title>haoide OAuth2</title>
            </head>
            <body>
                <script type="text/javascript">
                    var url = window.location.href;
                    var arg=url.split("#");
                    if (arg[1] === "undefined") {
                    } else {
                          var reUrl = "/auth/finish?" +arg[1];
                          window.location.href=reUrl;  
                    }
                </script>
            </body>
        </html>
      '''
    query = request.query_string
    params = {}
    if 'error' in query:
        params['error'] = request.query['error']
        params['error_description'] = ''
        if 'error_description' in query:
            params['error_description'] = request.query['error_description']
        err_page = '''
            <html>
                <head>
                    <title>haoide OAuth2</title>
                </head>
                <body>
                    <span style="background-color:#ff0000;">Login Error!!</span><br/>
                    <span style="background-color:#ff0000;">{error_description}</span>
                </body>
            </html>
        '''
        return err_page.format(error_description=params['error_description'])

    return html

@app.route('/auth/finish', method=['GET', 'POST'])
def do_finish():
    query = request.query_string
    params = {}
    if 'access_token' in query:
        params['access_token'] = request.query['access_token']

        result = {}
        for item in request.params:
           result[item]=request.params.get(item)

        settings = context.get_settings()
        instance_url = result["instance_url"]
        result["project name"] = settings["default_project"]["project_name"]
        result["session_id"] = result["access_token"]
        result["metadata_url"] = instance_url + "/services/Soap/m/%s.0" % settings["api_version"]
        result["rest_url"] = instance_url + "/services/data/v%s.0" % settings["api_version"]
        result["apex_url"] = instance_url + "/services/Soap/s/%s.0" % settings["api_version"]
        result["partner_url"] = instance_url + "/services/Soap/u/%s.0" % settings["api_version"]
        result["instance_url"] = instance_url
        result["time_stamp"] = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))
        result["user_id"] = result["id"][-18:]
        result["headers"] = {
            "Authorization": "OAuth " + result["access_token"],
            "Content-Type": "application/json; charset=UTF-8",
            "Accept": "application/json"
        }
        result["success"] = True
        util.add_config_history('session', result, settings)

        # If not describe metadata, just execute it
        described_metadata = util.get_described_metadata(settings)
        if not described_metadata:
            sublime.active_window().run_command("describe_metadata")

        html = '''
            <html>
                <head>
                    <title>haoide OAuth2</title>
                    <script>{script}</script>
                </head>
                <body>
                    <center>
                        <h3 style="color: #a6e22e">Login Success</h2>
                        <span>you can find the session cache in the [workspace]/[default project]/.config/session.json</span><br/>
                        <span style="">Window will be closed in five minutes later</span><br/>
                    </center>
                </body>
            </html>
        '''.format(script=close_window_script)
    else:
        html = '''
            <html>
                <head>
                    <title>haoide OAuth2</title>
                    <script>{script}</script>
                </head>
                <body>
                    <span style="background-color:#ff0000;">Login Error!!</span><br/>
                    <h3 style="font: #ff0000">Login Failed!!</h2>
                    <span style="">Window will be closed in five minutes later</span><br/>
                </body>
            </html>
        '''.format(script=close_window_script)
    return html


class StoppableCherryPyServer(ServerAdapter):
    """HACK for making a stoppable server"""

    def __int__(self, *args, **kwargs):
        super(ServerAdapter, self).__init__(*args, **kwargs)
        self.srv = None

    def run(self, handler):
        self.srv = wsgiserver.CherryPyWSGIServer(
            (self.host, self.port), handler, numthreads=2, timeout=2, shutdown_timeout=2
        )
        self.srv.start()

    def shutdown(self):
        try:
            if self.srv is not None:
                self.srv.stop()
        except:
            raise Exception('Error on shutting down cherrypy server')
        self.srv = None

def bottle_run(server):
    try:
        print("Bottle v%s server starting up..." % (bottle.__version__))
        print("Listening on http://%s:%d/" % (server.host, server.port))
        server.run(app)
    except:
        raise

class Server(object):
    class ServerThread(threading.Thread):
        def __init__(self, server):
            threading.Thread.__init__(self)
            self.server = server

        def run(self):
            bottle_run(server=self.server)

    def __init__(self, host='127.0.0.1', port='56889'):
        self.server = StoppableCherryPyServer(host=host, port=port)
        self.runner = Server.ServerThread(self.server)
        self.runner.daemon = True
        self.runner.start()

    def stop(self):
        print('Bottle server shuting down...')
        self.server.shutdown()
        self.runner.join()