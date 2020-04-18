"""
Author:         David Walshe
Date:           17/04/2020   
"""

from simple.binary import run_simple_proto
from enums.enums import create_enum_protobuf
from complex.complex import create_complex_protobuf

if __name__ == '__main__':

    # Simple
    # ======
    run_simple_proto()

    # Enum
    # ====
    create_enum_protobuf()

    # Complex
    # =======
    create_complex_protobuf()