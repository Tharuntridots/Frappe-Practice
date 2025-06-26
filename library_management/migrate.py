
import frappe

def before_migrate():
    print('running before migrate')

def after_migrate():
    print('running after migrate')


def before_tests():
    print("test part running")