# Sublime ENSIME

This project provides integration with ENSIME and Sublime Text Editor 2.
It has recently moved to the Ensime project and is in the process of being re-enlivened - so watch this space.
## Project status

```
19.06.2015: It lives 

We now have a version that starts and works (at least for some bits) - you need to follow the 'getting it going' steps below carefully, all other startup options will fail right now.

Have fun, come and join the party and hack on Ensime-Sublime

11.06.2015: Project moved to Ensime organisation.

With the kind permission of the original authors this project has been moved under the Ensime umbrella.
It is currently in a non-working state.  Please ignore the below instructions - we are working on bringing 
it up to date and into a workable state as soon as possible - watch this space!

```

This is a beta version.  It has been hacked to get it working against an up to date Ensime, but many things are likely to be broken.  Jump to source and error hightlight have been seen to work at least once ;)
Please submit issues to our tracker: https://github.com/ensime/ensime-sublime/issues/new

## Getting it going
As mentioned above we are in the process of bringing this project back to life - it works (well we think it does) but you have to jump through a bunch of hoops to get it working.

### Setup plugin
1. Install Sublime Text 2 (work need ) 
2. Clone this project (lets return to this as $PLUGIN) 
3. Symlink ```~/Library/Application Support/Sublime Text 2/Packages/Ensime``` (Mac) or ```/.config/sublime-text-2/Packages/Ensime``` (linux) to $PLUGIN
4. Restart Sublime

Later the plugin will be deployed using Package Control, but thats on the todo list.

### Prepare project
1. Checkout your project into $PROJECT
1. Add the Ensime sbt plugin to the project or to your user sbt configuration (see https://github.com/ensime/ensime-server/wiki/Quick-Start-Guide) for details of installing the plugin - ignore the Emacs bits.
2. run ```sbt gen-ensime``` to create a ```.ensime``` file

### Configure Ensime-Sublime plugin

1. ``` Preference -> Package Settings -> Ensime -> Settings User ->
2. Add the below entires to the file (replacing $PROJECT with the path)

```
  "connect_to_external_server": true,
  "error_highlight": true,
  "external_server_port_file": "$PROJECT/.ensime_cache/port",
```

### Start server and link in Sublime
1. Run $PLUGIN/serverStart.sh $PROJECt/.ensime (works with linux and mac) - starts an ensime instance for your project
2. In Sublime  - create a new window and within it do ```Project -> New Project``` and select $PROJECT as the root.
3. Open the Sublime command palette (typically bound to `Ctrl+Shift+P` on Windows/Linux and `Cmd+Shift+P` on Mac) and type `Ensime: Startup`.

With luck - if you open a scala file in your project, you should hav error highlighting (on save) and jump to definition working!

## Features

* Supports scala 2.9-2.11

* Creates and understands `.ensime` projects (maximum one project per Sublime window,
  if you have a project with multiple subprojects only a single subproject will be available at a time).

* Integrates with SBT to generate Ensime projects from SBT projects and provides
  a command, which runs SBT compilation for the current Ensime project.

* Once your Ensime project is configured (we have a helper for that) and Ensime is run,
  Scala files in that Ensime project benefit from a number of semantic services:

    * On-the-fly typechecking and error highlighting on save. Error messages are displayed
      in the status bar when you click highlighted regions (unfortunately, Sublime Text 2 doesn't
      support programmable tooltips). Moreover, errors can be viewed in a dynamically updated buffer
      displayed with `Tools > Ensime > Commands > Show notes`.

    * Type-aware completions for identifiers (integrates into the built-in mechanism of completions
      in Sublime Text 2, depending on your configuration it might be bound to `Ctrl+Space`/`Cmd+Space` or `Tab`).

    * Type-aware go to definition (implemented by `ensime_go_to_definition` command: bind it yourself
      to your favorite hotkey or use the default `Ctrl+Click` binding on Windows/Linux or `Cmd+Click` on Mac).

* Implements experimental support for debugging. At the moment you can set breakpoints, create launch
  configurations, step through programs in the debugger, inspect program output, navigate stack traces
  and watch values of local variables. Things are far from smooth, but it might be worth a try.

## How to install?

1. Install the package itself:

    a. If you use [Package Control](http://wbond.net/sublime_packages/package_control), install package Ensime.
    (`Preferences > Package Control > Install Package > Ensime`).

    b. Otherwise install manually.
       In your Sublime Text `Packages` directory, invoke:

    ```
    git clone git://github.com/sublimescala/sublime-ensime.git Ensime
    ```

    You can find the `Packages` directory by opening Sublime, selecting `View > Show Console`
    and then running the `sublime.packages_path()` command.
    Make sure you're using the right directory, or the plugin won't work.

2. Install the ENSIME server:

    Download Ensime from http://download.sublimescala.org.
    The archive will contain a directory with an Ensime version.
    
    Make sure to download the build which matches your Scala version.
    The primary development platform of Ensime is 2.10.x, but 2.9.x is supported as well
    (though availability of builds of 2.9.x might lag behind). Every once in a while,
    the plugin might undergo updates which will require fresh Ensime builds. If there's
    no 2.9.x build of required version, please [ping us](https://github.com/sublimescala/sublime-ensime/issues/68)
    or compile Ensime from sources (it's as easy as running `sbt ++2.9.2 package`).

    Extract the contents of this directory into the `server` subdirectory
    of just created `Ensime` directory. If you do everything correctly,
    `Ensime/server/bin` will contain Ensime startup scripts and
    `Ensime/server/lib` will contain Ensime binaries.

3. (Re)start Sublime Text editor.

4. Configure Ensime.

    a. Use `Preferences > Package Settings > Ensime` (Windows/Linux) or
       `Sublime Text 2 > Preferences > Package Settings > Ensime` (Mac)
       to configure different aspects of this plugin.

    b. By default Ensime customizes mouse bindings. It makes
       `Ctrl+Click`/`Cmd+Click` invoke `Go to Definition` and `Alt+Click` stand for `Inspect Type at Point`.
       If you want to disable these bindings or change them bindings to something else,
       adjust the config at `Preferences > Package Settings > Mousemap - Default`.

    c. For Windows users, make sure the `Line Endings` setting is set to `Unix`.
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

If you find that some features of Ensime are not working properly (i.e. Go To Definition or Error Highlighting), then check the `Line Endings` setting in Sublime Text 2.  On Windows, the line endings is set to `Windows` by default.  Simply change this setting to `Unix` by going to `View > Line Endings` and selecting `Unix`.

## Contacts

Submit issues on the tracker https://github.com/ensime/ensime-sublime/issues or come find us on the https://gitter.im/ensime/ensime-server Gitter channel
