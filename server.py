
# Utilities around server initialisation (e.g. starting up classpath file etc.)
import subprocess
import re
import _thread
import os


def strip_margin(text):
    """
    Similar to scala stripMargin function, remove blank text and the margin character '|' making it easier
    to embed blocks of text into a function.
    (borrowed from https://gist.github.com/sekimura/2678967)
    :param text: The body of text
    :return: text with lhs margin stripped
    """
    return re.sub('\n[ \t]*\|', '\n', text)


def write_classpath_sbt_script(build_file, scala_version, ensime_version, classpath_file):
    with open(build_file, "w") as f:
        f.write(strip_margin("""
            |import sbt._
            |import IO._
            |import java.io._
            |scalaVersion := """ + '"' + scala_version + '"' + """
            |ivyScala := ivyScala.value map { _.copy(overrideScalaVersion = true) }
            |// allows local builds of scala
            |resolvers += Resolver.mavenLocal
            |resolvers += Resolver.sonatypeRepo("snapshots")
            |resolvers += "Typesafe repository" at "http://repo.typesafe.com/typesafe/releases/"
            |resolvers += "Akka Repo" at "http://repo.akka.io/repository"
            |libraryDependencies ++= Seq(
            |   "org.ensime" %% "ensime" % """ + '"' + ensime_version + '"' + """,
            |   "org.scala-lang" % "scala-compiler" % scalaVersion.value force(),
            |   "org.scala-lang" % "scala-reflect" % scalaVersion.value force(),
            |   "org.scala-lang" % "scalap" % scalaVersion.value force()
            |)
            |val saveClasspathTask = TaskKey[Unit]("saveClasspath", "Save the classpath to a file")
            |saveClasspathTask := {
            |   val managed = (managedClasspath in Runtime).value.map(_.data.getAbsolutePath)
            |   val unmanaged = (unmanagedClasspath in Runtime).value.map(_.data.getAbsolutePath)
            |   val out = file(""" + '"' + classpath_file + '"' + """)
            |   write(out, (unmanaged ++ managed).mkString(File.pathSeparator))
            |}
            |"""))


def write_build_props_file(build_props_file):
    with open(build_props_file, "w") as f:
        f.write("""sbt.version=0.13.8\n""")


def exec_save_classpath(logger, sbt_cmd, working_dir, classpath_file, callback_fn):
    """
    Run the sbt saveClasspath task (for starting the ensimeProcess) in a seperate thread calling back
    with the result.
    :param sbt_cmd: The command for running sbt
    :param working_dir: The working directory to run in
    :param classpath_file: Where to write the classpath file to
    :param callback_fn: The function to call with the classpath (as a string)
    :return: Nothing
    """
    def worker():
        logger.info("Save classpath task running")
        cmd = sbt_cmd + ["saveClasspath"]
        output_file_path = os.path.join(working_dir, "saveClasspath.log")
        with open(output_file_path, "w") as output_file:
            res = subprocess.call(cmd, cwd=working_dir, stdout=output_file, stderr=subprocess.STDOUT)
            if res == 0:
                with open(classpath_file, "r") as f:
                    read_classpath = f.read().replace('\n', '')
                logger.info("Save classpath task completed successfully")
                callback_fn(read_classpath)
            else:
                logger.info("Save classpath task failed with error " + str(res) + " check " + str(output_file_path))
                callback_fn(None)

    _thread.start_new_thread(worker, ())
