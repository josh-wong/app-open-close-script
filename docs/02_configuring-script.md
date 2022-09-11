# How to configure the app-open-close script

This document describes how to set up the **app-open-close** script and provides a reference for using Task Scheduler in Windows to automate this script.

## Configure the app-open-close script

On your computer, create a text file. 

Copy the contents of **[app-open-close.py](https://github.com/josh-wong/app-open-close-script/blob/main/app-open-close.py)** and paste the contents into the text file you created. 

Save the file with the extension ".py" so that the file changes from being a text file to a Python file.

In the script:

- Replace `<INSERT APP URI>` as specified in the script.

!!! note

    An app URI starts with `<APP NAME>:` and might include a scheme that opens a specific part of the app. For details about URIs and schemes, see [Launch the default app for a URI | Microsoft](https://docs.microsoft.com/en-us/windows/uwp/launch-resume/launch-default-app).

- Replace `<XX>` as specified in the script.
- Replace `<INSERT APP NAME>` as specified in the script.

!!! note

    The "APP NAME" should match the name of the app that was called in the "APP URI," minus any scheme that was added to the end of the URI.

- Replace `<INSERT DETAILED MESSAGE ABOUT WHY THIS APP WAS OPENED AND CLOSED>` as specified in the script. 

Then, save your changes.

## Automate this script

To automate the **app-open-close** script, you can add a task for the script in Task Scheduler in Windows. However, because most Windows environments are set up differently, this tutorial does not describe setting up tasks in Task Scheduler.

For details on using Task Scheduler, please see [Task Scheduler for developers](https://docs.microsoft.com/en-us/windows/win32/taskschd/task-scheduler-start-page).
