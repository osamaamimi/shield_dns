import struct

RCODE_SERVFAIL = 2
RCODE_NXDOMAIN = 3


def find_question_end(request):
    """Return the index where the first question ends (name + QTYPE + QCLASS)."""
    index = 12

    while True:
        if index >= len(request):
            raise ValueError("unexpected end of packet")

        length = request[index]
        if length == 0:
            index += 1          # skip the zero byte that ends the name
            break
        if length > 63:
            raise ValueError("invalid label length")

        index += 1 + length     # skip the length byte and the label itself

    end = index + 4             # QTYPE (2 bytes) + QCLASS (2 bytes)
    if end > len(request):
        raise ValueError("question truncated")

    return end


def build_error(request, rcode):
    """Build a DNS response that carries only an error code (rcode)."""
    if len(request) < 13:
        raise ValueError("packet too short")

    transaction_id = request[:2]

    question_end = find_question_end(request)
    question_section = request[12:question_end]

    # copy the RD bit from the client's request
    request_flags = struct.unpack(">H", request[2:4])[0]
    rd = str((request_flags >> 8) & 1)

    QR = '1'
    Opcode = '0000'
    AA = '0'
    TC = '0'
    RD = rd
    RA = '1'
    Z = '000'
    Rcode = format(rcode, "04b")

    flags_combination = QR + Opcode + AA + TC + RD + RA + Z + Rcode
    flags = struct.pack(">H", int(flags_combination, 2))

    QDcount = struct.pack(">H", 1)
    ANcount = struct.pack(">H", 0)
    NScount = struct.pack(">H", 0)
    ARcount = struct.pack(">H", 0)

    return (transaction_id + flags + QDcount + ANcount
            + NScount + ARcount + question_section)


def build_nxdomin(request):
    return build_error(request, RCODE_NXDOMAIN)


def build_servfail(request):
    return build_error(request, RCODE_SERVFAIL)
