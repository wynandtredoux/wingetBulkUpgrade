# wingetBulkUpgrade
A small python script to upgrade a list of winget packages provided by the user. Written for Windows 10 in python 3.10

## Usage
`winBulk.py [-h] packages`

Update multiple winget packages

positional arguments:
<br>&nbsp;&nbsp;&nbsp;packages&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;A list of package names, comma delimited, no spaces between commas

options:
<br>&nbsp;&nbsp;&nbsp;-h, --help&nbsp;&nbsp;&nbsp;&nbsp;show this help message and exit 

## Example
`python wunBulk.py "7-zip,Bulk Rename Utility,Git,Notepad++"`

Will upgrade 7-zip, Bulk Rename Utility, Git, and Notepad++ with the newest version that the winget package manager can find
