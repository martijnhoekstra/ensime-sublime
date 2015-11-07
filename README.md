# Sublime ENSIME

[![Join the chat at https://gitter.im/ensime/ensime-sublime](https://badges.gitter.im/Join%20Chat.svg)](https://gitter.im/ensime/ensime-sublime?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)

ENSIME-Sublime provides Scala support to the Sublime Text editor, it is a bit rough round the edges, but is being 
actively worked on - watch this space.

N.b. SublimeText 2 (ST2) support is deprecated as all of the development is currently happening for 
Sublime Text 3 (ST3).  If you are interest in ST2 support consider contributing to the [Sublime Text 2 Branch](https://github.com/ensime/ensime-sublime/tree/ST2)  

## Project status

The project is up and functional and supports a subset of the Ensime features:

* error highlighting
* code completion (hit . followed by ctrl-space or command-space should work)
* goto definition
* type hints
* extract local, extract method
* add import, organize imports
* supports Scala 2.10 and 2.11

This is a work in progress, please do submit issues to [our tracker](https://github.com/ensime/ensime-sublime/issues/new).

## Getting it going

Right now you need to jump through some hoops to get started - we are working on it.

### Setup 1 - All

1. Ensure you have a jdk installed and visible on your path
1. Ensure you have sbt installed and visible on your path
1. Install [Sublime Text 3](http://www.sublimetext.com/3) (if you do not have Sublime Text already installed).

### Setup 2a - plugin - Package Control

1. Install the ensime plugin from [Package Control](https://packagecontrol.io/packages/Ensime)

or
### Setup 2b - plugin - Manual

1. Clone this project (let's refer to it as `$PLUGIN`).
2. Manually install Ensime-Sublime
  2. for Sublime Text 3:  
  Symlink ```~/Library/Application Support/Sublime Text 3/Packages/Ensime``` (Mac) or ```/.config/sublime-text-3/Packages/Ensime``` (Linux) to `$PLUGIN`.

3. Restart Sublime Text.

### Prepare project
1. Checkout your project (referred to as `$PROJECT`).
3. Add the Ensime sbt plugin to your user sbt configuration (recommended) or directly to the sbt project itself 
(see [ensime-server wiki](https://github.com/ensime/ensime-emacs/wiki/Quick-Start-Guide#installing-the-ensime-sbt-plugin) for details 
- ignore the Emacs bits).
3. Run ```sbt gen-ensime``` to create a ```.ensime``` file.

### Configure Ensime-Sublime plugin

1. Open the Ensime plugin configuration at `Preference -> Package Settings -> Ensime -> Settings - User`.
2. Add the below entry to the file:
```
{
	"connect_to_external_server": false,
}
```

### Start server and link in Sublime

Note that Ensime Server requires `grealpath` utility (run e.g. `brew install coreutils` to install it). 

1. In Sublime Text create a [new project](http://sublimetext.userecho.com/topic/50034-project-menu-new-project/) with `$PROJECT`
as a root (to do so: open a new window (`Ctrl+Shift+N` for Windows/Linux and `Cmd+Shift+N` for Mac) and open `$PROJECT` as a root).

2. Open the Sublime command palette (typically bound to `Ctrl+Shift+P` on Windows/Linux and `Cmd+Shift+P` on Mac) and type `Ensime: Startup`.

With luck - if you open a Scala file in your project, you should have error highlighting (on save) and jump to definition working!

## Additional Sublime Configurations

* By default Ensime customizes mouse bindings. It makes
       `Ctrl+Click`/`Cmd+Click` invoke `Go to Definition` and `Alt+Click` stand for `Inspect Type at Point`.
       If you want to disable these bindings or change them bindings to something else,
       adjust the config at `Preferences > Package Settings > Mousemap - Default`.

* For Windows users, make sure the `Line Endings` setting is set to `Unix`.
       You may do this by going to `View > Line Endings` and selecting `Unix`.

## How to use?

Open the Sublime command palette (typically bound to `Ctrl+Shift+P` on Windows/Linux and `Cmd+Shift+P` on Mac) and type `Ensime: Startup`.

If you don't have an Ensime project, the plugin will guide you through creating it.

If you already have a project, an ENSIME server process will be started in the background,
and the server will initialize a resident instance of the Scala compiler.
After the server is ready, a message will appear in the left-hand corner of the status bar.
It will read either `ENSIME` if the currently opened file belongs to the active Ensime project
or `ensime` if it doesn't. Keep an eye on this message - it's an indicator of things going well.

## Troubleshooting

If you find that some features of Ensime are not working properly (i.e. Go To Definition or Error Highlighting), then check the `Line Endings`
setting in Sublime Text.  On Windows, the line endings is set to `Windows` by default. 
Simply change this setting to `Unix` by going to `View > Line Endings` and selecting `Unix`.

## Contacts

Submit issues on the [tracker](https://github.com/ensime/ensime-sublime/issues) or come find us on the 
[ensime-sublime Gitter channel](https://gitter.im/ensime/ensime-sublime).
