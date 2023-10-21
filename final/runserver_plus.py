from django.core.management.commands.runserver import Command as RunserverCommand
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import os
import sys


class Watcher:
    def __init__(self):
        self.paths = [
            ".",
        ]
        self.event_handler = FileSystemEventHandler()

    def run(self):
        observer = Observer()
        for path in self.paths:
            observer.schedule(self.event_handler, path, recursive=True)
        observer.start()
        try:
            while True:
                pass
        except KeyboardInterrupt:
            observer.stop()
        observer.join()


class RunserverPlusCommand(RunserverCommand):
    def inner_run(self, *args, **options):
        # Start the file watcher in a separate thread
        from threading import Thread

        t = Thread(target=Watcher().run)
        t.setDaemon(True)
        t.start()
        super().inner_run(*args, **options)


RunserverPlusCommand.default_addr = "[::]"
RunserverPlusCommand.default_port = "8000"
