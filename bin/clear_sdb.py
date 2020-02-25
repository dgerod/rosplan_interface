#! /usr/bin/env python
# -*- coding: utf-8 -*-

from rosplan_pytools.rosplan.controller import scene_database as sdb


def main():

    sdb.initialize()
    sdb.remove_elements()


if __name__ == "__main__":
    main()
