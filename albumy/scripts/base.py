# -*- coding: utf-8 -*-


from flask_script import Command


class BaseCommand(Command):
    """
    命令类 基类
    """
    def run(self):
        raise NotImplementedError

    name = None

    @classmethod
    def get_name(cls):
        return cls.name
