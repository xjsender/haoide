[1mdiff --git a/salesforce/soap.py b/salesforce/soap.py[m
[1mindex 03db9af..bbdf0ca 100644[m
[1m--- a/salesforce/soap.py[m
[1m+++ b/salesforce/soap.py[m
[36m@@ -54,7 +54,11 @@[m [mclass SOAP():[m
     def create_request(self, request_type, options={}):[m
         soap_body = getattr(self, "create_%s_request" % request_type)(options)[m
         if self.settings["debug_mode"]:[m
[31m-            print ("[Debug for %s]: \n%s" % (request_type, soap_body.decode("UTF-8")))[m
[32m+[m[32m            print ("[Debug for {request_type}]: \n{seprate}\n{content}\n{seprate}".format([m
[32m+[m[32m                seprate="~" * 100,[m
[32m+[m[32m                request_type=request_type,[m
[32m+[m[32m                content=soap_body.decode("UTF-8")[m
[32m+[m[32m            ))[m
         return soap_body[m
 [m
     ##############################################[m
[1mdiff --git a/util.py b/util.py[m
[1mindex 4377a80..8e06198 100644[m
[1m--- a/util.py[m
[1m+++ b/util.py[m
[36m@@ -1093,6 +1093,12 @@[m [mdef build_deploy_package(files):[m
     package_xml_content = build_package_xml(settings, package_dict)[m
     package_xml_content = format_xml(package_xml_content)[m
 [m
[32m+[m[32m    if settings["debug_mode"]:[m
[32m+[m[32m        print ("{seprate}\n[Package.xml for Deployment]: \n{seprate}\n{content}\n{seprate}".format([m
[32m+[m[32m            seprate="~" * 100,[m
[32m+[m[32m            content=package_xml_content.decode("UTF-8")[m
[32m+[m[32m        ))[m
[32m+[m
     # Write package content to .package path[m
     try:[m
         time_stamp = time.strftime("%Y%m%d%H%M", time.localtime(time.time()))[m
[36m@@ -1119,7 +1125,7 @@[m [mdef build_deploy_package(files):[m
     base64_package = base64_encode(zipfile_path)[m
 [m
     # Remove temporary `test.zip`[m
[31m-    os.remove(zipfile_path)[m
[32m+[m[32m    # os.remove(zipfile_path)[m
 [m
     return base64_package[m
 [m
