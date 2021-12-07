#  iPyClip

This folder contains lots of examples to help you get started with Pythonista, and to give you some ideas of what you can do with it.

## New Examples in 3.3

Tap on the links to open the new examples directly.

* [CoreML Image Recognition](pythonista3://Examples/ObjC/CoreML%20Image%20Recognition.py?action=open)
* [Notification Quiz](pythonista3://Examples/Misc/Notification%20Quiz.py?action=open)
* [Satellite Image](pythonista3://Examples/Misc/Satellite%20Image.py?action=open)
* [Reverse Clock](pythonista3://Examples/Animation/Reverse%20Clock.py?action=open)

## Animation

These are little experiments and toys, created using the `scene` module -- have a look at the *Games* section for more examples of this sort.

## Extension

The scripts in this folder are intended to be run from the Pythonista app *extension*, not the app itself. You can show the extension from the share sheet within other apps, e.g. Safari, Photos, Maps, and many third-party apps. If you don't see the "Run Pythonista Script" activity in the sheet, tap "More" first, and then enable it in the list of activities.

Using the `appex` module, you can access the data that was passed to the share sheet by the other app, e.g. text in Notes, web URLs in Safari, or images in Photos.

## Game Tutorial

This is a tutorial for making a simple game using the `scene` module. Unlike the other examples, the scripts here are all the same game, built in multiple steps that are easier to follow than looking at the full source code of a completed game.

## Games

These are some examples of relatively simple, but complete games that were created using the `scene` module.

## Keyboard

These scripts are meant to be run in Pythonista's custom keyboard app extension. You can enable this in the Settings app (Keyboard > Keyboards > Add New Keyboard). Some examples require that you additionally enable 'Full Access', but it's not a requirement to use the keyboard at all.

## Misc

Most of the scripts in this folder are pretty short, and demonstrate a single concept or module. There are demos of accessing your address book, Twitter data, reminders, creating animated GIFs, and writing/playing MIDI files.

## ObjC

The examples in this folder use the `objc_util` module to "bridge" native iOS APIs. This is a fairly advanced topic, but most of the examples here are quite simple.

## Plotting

This folder contains a number of sample scripts from the matplotlib documentation to create various types of charts.

The *Motion Plot* example is specific to Pythonista -- it uses the `motion` module to gather data from your device's accelerometer, and then plots it in a simple line chart.

**Tip:** You can save a plot that is shown in the console to your camera roll by tapping and holding the image.

## User Interface

This folder contains a couple of examples using the `ui` module for native user interfaces on iOS. The *Calculator* and *Color Mixer* examples consist of two files each -- the `.pyui` file contains the visual layout of the user interface, while the actual code lives in the `.py` file. To run these examples, you need to open the `.py` file.

## Widget

These scripts are meant for the (somewhat experimental) Pythonista "Today" widget that you can use on your home/lock screen. Please note that a widget's resources are extremely limited, so the examples are kept very minimal for a reason.

I hope you enjoy coding in Pythonista! 💚
