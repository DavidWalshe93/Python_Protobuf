"""
Author:         David Walshe
Date:           18/04/2020   
"""

import simple.simple_pb2 as simple_pb2


def create_simple_protobuf() -> simple_pb2.SimpleMessage:
    """
    Creates a simple protobuf with content filled.

    :return: A newly create simple_pb2 Protobuf.
    """
    simple_message = simple_pb2.SimpleMessage()
    simple_message.id = 123
    simple_message.is_simple = True
    simple_message.name = "This is a simple Message"
    sample_list = simple_message.sample_list
    sample_list.append(3)
    sample_list.append(4)
    sample_list.append(5)
    sample_list.append(6)

    return simple_message


def write_proto_to_binary(simple_message: simple_pb2.SimpleMessage):
    """
    Writes a protobuf to a binary file.

    :param simple_message: The protobuf object to write.
    """
    with open("simple.bin", "wb") as fh:
        bytes_as_string = simple_message.SerializeToString()
        fh.write(bytes_as_string)


def read_proto_from_binary():
    """
    Reads a binary file and converts i
    :return:
    """
    with open("simple.bin", "rb") as fh:
        simple_message_read = simple_pb2.SimpleMessage().FromString(fh.read())

    return simple_message_read


def run_simple_proto():
    """
    Helper method to show binary read and write of protobufs
    """
    sb = create_simple_protobuf()
    print("Original Protobuf")
    print("=" * 20)
    print(sb)
    print("*" * 20)

    write_proto_to_binary(sb)

    sb2 = read_proto_from_binary()
    print("From Binary File")
    print("=" * 20)
    print(sb2)
    print("*" * 20)

    print(f"Is simple?: {sb2.is_simple}")
