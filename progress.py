import glob
allProblems = 2050

fileNamesPy = glob.glob("*/*.py")
fileCountPy = len(fileNamesPy)

fileNamesJs = glob.glob("*/*.js")
fileCountJs = len(fileNamesJs)

progress = round(fileCountPy / allProblems * 100)

with open("README.md", "w") as file:
    file.write("# leetcode\n\n"
    "<p1>teaching myself dynamic programming</p1>\n\n"
    "<p1>challenges from [leetcode.com](leetcode.com)</p1>\n\n"
    f'{fileCountPy}/{allProblems} Python Solutions\n'
    f'{fileCountJs}/{allProblems} Javascript Solutions\n'
    "![" + str(progress) + "%](https://progress-bar.dev/" + str(progress) + "/?scale=500&title=solved&width=330)")
