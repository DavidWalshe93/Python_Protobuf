"""
Author:         David Walshe
Date:           18/04/2020   
"""

import complex.complex_pb2 as complex_pb2


def create_complex_protobuf():
    """
    Creates a "complex" protobuf with hierarchical fields.
    """
    complex_message = complex_pb2.ComplexMessage()

    complex_message.one_dummy.id = 123
    complex_message.one_dummy.name = "I am a dummy message"

    # Verbose way to add values to a list.
    first_multiple_dummy = complex_message.multiple_dummy.add()
    first_multiple_dummy.id = 354
    first_multiple_dummy.name = "I am the first dummy element"

    # Concise way to add values to protobuf list.
    complex_message.multiple_dummy.add(id=567, name="Second Element")

    # If you use extend, be mindful that it does a copy of the instance added so
    # future changes after extend are not persisted.

    print("=" * 20)
    print("Complex")
    print("=" * 20)

    print(complex_message)


