
# QuickAdminPanel Codebase Saver

This is a quick python script that is used to save your project from QuickAdminPanel for free.




## Usage
- In QuickAdminPanel configure your project to your liking.
- Open Developer Tools to the network tab
- Click "View Code" to launch the code preview modal.
- In the network tab you should see the "files" request.
   - Right click the request and click "Copy response"
   - Create a new json file locally and paste in the contents of the response.
- Open the provided script and update the two lines with your desired local paths.
   - ```repo_path = "PROJECT PATH"```
   - ```file = open("PROJECT DIRECTORY JSON FILE")```
- Then execute the script and your codebase is built.
    - ```python {scriptname}.py```
