## Track Debug Log
### Track Debug Log Step by Step
* Click ``HaoIDE`` > ``Debug`` > ``Track Debug Log``
* Choose the user that you want to track and press enter
* Check the progress in the status bar until succeed message appeared

### Track Self Debug Log Step by Step
* Click ``HaoIDE`` > ``Debug`` > ``Track Self Debug Log``
* Choose the user that you want to track and press enter
* Check the progress in the status bar until succeed message appeared

### Track All Debug Logs Step by Step
* Click ``HaoIDE`` > ``Debug`` > ``Track All Debug Logs``
* After confirmed, plugin will start to track debug logs for all users
* After track is finished, track result will be displayed in the output panel

## Fetch Debug Log
### Fetch Debug Log Step by Step
* Click ``HaoIDE`` > ``Debug`` > ``Fetch Debug Log``
* Choose the user that you want to fetch and press enter
* After fetch is finished, debug log list will appear in the output panel

### Fetch Self Debug Log Step by Step
* Click ``HaoIDE`` > ``Debug`` > ``Fetch Self Debug Log``
* Choose the user that you want to fetch and press enter
* After fetch is finished, debug log list will appear in the output panel

## View Debug Log Detail
- Put the focus in the LogId got by fetch command, press <kbd>alt</kbd> and click left button, the debug log detail will be retrieved and displayed in the new view.

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

## Run Test
* By Main Menu: click ``HaoIDE`` > ``Debug`` > ``Run Test``, choose the test class and press <kbd>enter</kbd>, check the progress in the status bar until succeed message appeared, and then a new view with the test result will be open.
* By Context Menu: in the context of opened class, click ``HaoIDE`` > ``Run Test Class``, check the progress in the status bar until succeed message appeared, and then a new view with the test result will be open.

## View Code Coverage
* This feature just works when api version is >= 29.0
* In the context menu of open class or trigger, click ``HaoIDE`` > ``View Code Coverage`` in the context menu, wait for the end of the progress on the status bar, you will see the code coverage percentage in the console and a new view with not covered highlight lines.
* Put the focus in the ApexClass Name, press ``alt`` and click left button for twice, the code coverage of specified class will be retrieved and displayed in the new view.