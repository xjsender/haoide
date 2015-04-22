# Deploy
There has a setting ``switch_back_after_migration`` to control whether switch back to original project after deploy is finished, default value is ``true``

* Deploy Package Zip, [demo](https://raw.githubusercontent.com/xjsender/SublimeApexScreenshot/master/DeployZip.gif) is here
    - Click ```HaoIDE``` > ```Metadata Migration``` > ```Deploy Package.zip``` in the main menu
    - Input your zip file path and click <kbd>Enter</kbd>
    - Waiting and checking the progress message in the output panel
    - After operation is finished, you will see the deploy result

* Deploy Files to Server
    - Choose the file to deploy
    - Click ```HaoIDE``` > ```Deploy File to Server``` in the context menu
    - Waiting and checking the progress message in the output panel
    - After operation is finished, you will see the deploy result

* Deploy Open Files
    - Sometimes, when you want to deploy class, page or somethings else, however, you didn't want to choose them in the sidebar when there are huge number of code files, you can open the files that you want to deploy to server and Click ```HaoIDE``` > ```Metadata Migration``` > ```Deploy Open Files``` in the main menu to deploy multiply files to target server. 

    - Actually, you can even open code files in different orgs and deploy them to the same org, for example, there have three classes to be deployed, A and B are in UAT environment and they are newly developed feature, C in UAT environment is completely different with production environment and there is urgent bug needed to be fixed in production, so at this moment, you can open A and B classes in UAT and the fixed version of C class in production and click ```Deploy Open Files``` to deploy the three class from different orgs to production environment.

    - This command is just enabled when any one of open files is salesforce code files.

* Deploy Package Folder, [demo](https://raw.githubusercontent.com/xjsender/SublimeApexScreenshot/master/DeployPackageFolder.gif) is here
    - Choose a valid package folder, for example, ``src`` folder or ``Project/src``, plugin will check whether ``src`` folder contains ``package.xml`` file, if yes, you will ``Deploy To Server`` command in the sidebar menu, otherwise, ``Deploy To Server`` will be hidden
    - Click the ```Deploy To Server`` command
    - Waiting and checking the progress message in the output panel
    - After operation is finished, you will see the deploy result