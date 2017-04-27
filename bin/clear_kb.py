#! /usr/bin/env python
# -*- coding: utf-8 -*-

from rosplan_interface import kb_interface as kbi

def main():
    kbi.init_kb()
    kbi.clear_all()

if __name__ == '__main__':
    main()
