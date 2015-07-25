## Execute Anonymous
Choose any apex code snippet, press <kbd>Ctrl</kbd>+<kbd>Alt</kbd>+<kbd>E</kbd> or click ```HaoIDE``` > ```Execute Anonymous``` in the context menu, you will see the result, you should be aware, if anonymous code compile is failed, message will be shown in output panel, just after compile succeed, the executed result will be shown in the new view.

There has a ```log_levels``` setting in the default settings to control the anonymous log level , If you want to change anonymous log levels, you can override it in your user settings.

## Track Debug Log
### Track Debug Log Step by Step
* Click ``HaoIDE`` > ``Debug`` > ``Track One``
* Choose the user that you want to track and press enter
* Check the progress in the status bar until succeed message appeared

### Track Self Debug Log Step by Step
* Click ``HaoIDE`` > ``Debug`` > ``Track Self``
* Choose the user that you want to track and press enter
* Check the progress in the status bar until succeed message appeared

### Track All Debug Logs Step by Step
* Click ``HaoIDE`` > ``Debug`` > ``Track All``
* After confirmed, plugin will start to track debug logs for all users
* After track is finished, track result will be displayed in the output panel

## Fetch Debug Log
### Fetch Debug Log Step by Step
* Click ``HaoIDE`` > ``Debug`` > ``Fetch One``
* Choose the user that you want to fetch and press enter
* After fetch is finished, debug log list will appear in the output panel

### Fetch Self Debug Log Step by Step
* Click ``HaoIDE`` > ``Debug`` > ``Fetch Self``
* Choose the user that you want to fetch and press enter
* After fetch is finished, debug log list will appear in the output panel

## Settings related to Debug Log
<table>
  <thead>
    <th>Setting Name</th>
    <th>Default Value</th>
    <th>Description</th>
  </thead>

  <tbody>
    <tr>
      <td>trace_flag</td>
      <td>
        <pre><code>
{
    "ApexCode" : "Debug",
    "ApexProfiling" : "Finest",
    "Callout" : "Info",
    "Database" : "Finest",
    "System" : "Debug",
    "Validation" : "Info",
    "Visualforce" : "Info",
    "Workflow" : "Info"
}
        </code></pre>
      </td>
      <td>Used to define the debug log level</td>
    </tr>
    <tr>
      <td>last_n_logs</td>
      <td>20</td>
      <td>Log number returned by fetching</td>
    </tr>
  </tbody>
</table>

## View Debug Log Detail
- Put the focus in the LogId got by fetch command, press <kbd>alt</kbd> and click left button, the debug log detail will be retrieved and displayed in the new view.

## Run Test
* This feature will be deprecated in the release v3.1.5, because this feature is executed in async way, it's very slow.

## Run Sync Test
* Click ``HaoIDE > Run Sync Test`` in the context menu or press <kbd>alt/command + shift + u</kbd>, you can get the test run result and related coverage report
* The coverage information will be kept in ``.config/coverages.json`` cache file, when you execute ``view_code_coverage`` command next time, plugin will read code coverage information from here

## View Code Coverage
* This feature just works when api version is >= 29.0
* In the context menu of open class or trigger, click ``HaoIDE`` > ``View Code Coverage`` in the context menu, wait for the end of the progress on the status bar, you will see the code coverage percentage in the console and a new view with not covered highlight lines.
* Put the focus in the ApexClass Name, press ``alt`` and click left button for twice, the code coverage of specified class will be retrieved and displayed in the new view.
