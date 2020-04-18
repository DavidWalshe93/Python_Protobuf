"""
Author:         David Walshe
Date:           18/04/2020   
"""

import enums.enum_example_pb2 as enum_example_pb2


def create_enum_protobuf():
    """
    Creates a enum protobuf
    """
    enum_message = enum_example_pb2.EnumMessage()
    enum_message.id = 345
    enum_message.day_of_the_week = enum_example_pb2.THURSDAY

    print("*" * 20)
    print("Enums")
    print("*" * 20)
    print(enum_message)
    print(enum_message.day_of_the_week == enum_example_pb2.THURSDAY)