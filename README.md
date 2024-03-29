# Auto File Organizer

Welcome to Auto File Organizer.

This is a simple script designed to take a folder of mixed file types, and organize them into subfolders and group them together based on their file types.

## How it works
The application takes a provided folder, and organizes the files on the root level into sub folders based on their file types.
There're two levels of organization. These being Generic and Specific.

### Generic
Generic will organize files into Subfolders based on their generic file types. Example, all "png", "jpg", "jpeg", "svg" files will be stored in a folder called "Images", whereas files with "docx", "txt", "md", "pdf", etc, will be stored in a file called "Documents".

### Specific
Specific will be similar to Generic, but will create one further level of sub folders within the Generic category, which will host documents of specific types.

For example, documents with the ".docx" extension, will be stored in "Documents/Word" subfolder, and ".xlsx" will be "Documents/Excel", etc.

## How To Use.

1. Visit the website (here)[https://example.com/]
2. Upload a folder with mixed file types
3. Select level of granularity (Generic, Specific)
4. Press "FIX IT!" and watch the magic happen
5. Download the organized files.

Note, your data is not stored for any longer than it needs to be, nor or the contents of the files read.

There's also a simpler local version you can run if you have python installed, that will operate on the folder directly without you having to upload and download.

## How to use local version

1. Clone the repository.
2. Ensure python 3.10 or greater is installed.
3. Run `python autoFileOrganize.py "folder_path_in_quotes" level`. Where level is either Generic or Specific. Generic by default.
4. Relax and Enjoy the fun of being able to watch it work live!

The local version doesn't have any extra dependencies, so no need to install the requirements.txt file. That's only for those wanting to run the actual web app themselves.

If you just want to test the `autoFileOrganize.py` file to see it actually working, run `python test_AutoFileOrganize.py` to create a folder filled with files. Then press "enter" and watch the demo play!

## Generic Option
### Folders
Below is a list of the Generic folder names
- Documents
- Images
- Videos
- Code
- Misc

### File types per folder:
| Folder Name | File Types |
|-------------|------------|
| Documents   | docx, txt, md, pdf, xlsx, pptx, odt, rtf, doc, xls, ppt, csv, json, xml, yaml, log, txt |
| Images      | png, jpg, jpeg, svg, gif, bmp, tiff, webp |
| Videos      | mp4, avi, mov, flv, mkv, webm, m4v, mpeg, wmv, rm, ogv |
| Code        | py, js, html, css, java, c, c++, c#, php, rb, go, swift, kt, ts, sql, pl, sh, bat, cmd, ps1, rtf, log, txt |
| Misc        | Various other file types not categorized |

## Specific Option
Pending development and thinking. Will most likely just apply to the Documents folder.