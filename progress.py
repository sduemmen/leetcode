import glob

fileNames = glob.glob("*/*.py")

fileCount = len(fileNames)

progress = fileCount / 1923

with open("README.md", "w") as file:
    file.write("# leetcode\n\n<p1>a collection of [leetcode.com](leetcode.com) challenges and solutions</p1>\n\n![" + str(progress) + "%](https://progress-bar.dev/" + str(progress) + ")")
