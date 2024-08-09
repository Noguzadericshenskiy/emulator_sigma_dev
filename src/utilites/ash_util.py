def indicate_send_b6(array_bytes: bytearray):
    new_msg = bytearray(b"\xB6\x49")
    for i_byte in array_bytes[2:]:
        if i_byte == 182:
            new_msg.append(i_byte)
            new_msg.append(0)
        else:
            new_msg.append(i_byte)
    return new_msg