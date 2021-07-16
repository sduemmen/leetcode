import glob

fileNames = glob.glob("*/*.py")
fileCount = len(fileNames)
progress = fileCount // 1923

with open("README.md", "w") as file:
    file.write("# leetcode\n\n<p1>teaching myself dynamic programming</p1>\n\n<p1>challenges from [leetcode.com](leetcode.com)</p1>\n\n![" + str(progress) + "%](https://progress-bar.dev/" + str(progress) + "/?scale=500&title=solved&width=330)")
